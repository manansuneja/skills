#!/usr/bin/env python3
"""Validate plugin metadata, generated packages, and release invariants."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - exercised by a clean developer machine
    Draft202012Validator = None

from build_plugins import (
    DEFAULT_CATALOG,
    DEFAULT_OUTPUT,
    PORTABLE_SCHEMA,
    REPO_ROOT,
    SEMVER_RE,
    disk_tree_digest,
    digest_files,
    load_json,
    tracked_files,
)


PLUGIN_NAME_RE = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
LOCAL_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_PLACEHOLDERS = re.compile(r"TO_BE_COMPUTED|CHANGEME|REPLACE_ME|YOUR_[A-Z0-9_]+")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "OpenAI-style API key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
}
REQUIRED_OPENAI_INTERFACE = {
    "displayName",
    "shortDescription",
    "longDescription",
    "developerName",
    "category",
    "capabilities",
}
ALLOWED_OPENAI_TOP_LEVEL = {
    "name",
    "version",
    "description",
    "author",
    "repository",
    "license",
    "keywords",
    "skills",
    "interface",
    "mcpServers",
    "apps",
}


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.checks = 0

    def require(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    values: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def is_reparse_point(path: Path) -> bool:
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
    except OSError:
        return True
    return bool(attributes & 0x400)


def validate_package_tree(validation: Validation, root: Path, name: str, max_bytes: int) -> None:
    validation.require(root.is_dir(), f"Missing generated package: {root}")
    if not root.is_dir():
        return
    total = 0
    for path in root.rglob("*"):
        validation.require(not path.is_symlink(), f"Symlink is forbidden in {name}: {path}")
        validation.require(not is_reparse_point(path), f"Junction/reparse point is forbidden in {name}: {path}")
        if path.is_file():
            total += path.stat().st_size
            if path.stat().st_size <= 2_000_000:
                try:
                    text = path.read_text(encoding="utf-8")
                except (UnicodeDecodeError, OSError):
                    continue
                validation.require(
                    FORBIDDEN_PLACEHOLDERS.search(text) is None,
                    f"Release placeholder found in {path}",
                )
                for label, pattern in SECRET_PATTERNS.items():
                    validation.require(pattern.search(text) is None, f"Possible {label} found in {path}")
    validation.require(total <= max_bytes, f"{name} package is {total} bytes; limit is {max_bytes}")


def validate_skill_links(validation: Validation, skill_root: Path) -> None:
    skill_md = skill_root / "SKILL.md"
    if not skill_md.exists():
        return
    for match in LOCAL_LINK_RE.finditer(skill_md.read_text(encoding="utf-8")):
        raw = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
            continue
        decoded = unquote(raw.split("#", 1)[0])
        candidate = (skill_root / decoded).resolve()
        validation.require(
            skill_root.resolve() == candidate or skill_root.resolve() in candidate.parents,
            f"Skill link escapes package root: {skill_md} -> {raw}",
        )
        validation.require(candidate.exists(), f"Missing local skill reference: {skill_md} -> {raw}")


def validate_portable_manifest(validation: Validation, manifest_path: Path, schema: dict) -> None:
    validation.require(manifest_path.is_file(), f"Missing portable manifest: {manifest_path}")
    if not manifest_path.is_file():
        return
    manifest = load_json(manifest_path)
    if Draft202012Validator is None:
        validation.errors.append(
            "jsonschema is required; run: python -m pip install -r scripts/requirements-plugins.txt"
        )
        return
    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        validation.errors.append(f"Portable schema error at {manifest_path}:{location}: {error.message}")
    validation.require(manifest.get("$schema") == PORTABLE_SCHEMA, f"Wrong portable schema in {manifest_path}")


def validate_https(validation: Validation, value: object, label: str) -> None:
    parsed = urlparse(str(value))
    validation.require(parsed.scheme == "https" and bool(parsed.netloc), f"{label} must be an absolute https URL")


def validate_openai_manifest(validation: Validation, root: Path, entry: dict, listing: dict) -> None:
    manifest_path = root / ".codex-plugin" / "plugin.json"
    validation.require(manifest_path.is_file(), f"Missing OpenAI manifest: {manifest_path}")
    if not manifest_path.is_file():
        return
    manifest = load_json(manifest_path)
    extra = set(manifest) - ALLOWED_OPENAI_TOP_LEVEL
    validation.require(not extra, f"Unsupported OpenAI manifest fields in {manifest_path}: {sorted(extra)}")
    validation.require(manifest.get("name") == entry["name"], f"OpenAI manifest name mismatch for {entry['name']}")
    validation.require(manifest.get("version") == entry["version"], f"OpenAI manifest version mismatch for {entry['name']}")
    validation.require(bool(SEMVER_RE.fullmatch(str(manifest.get("version", "")))), f"Invalid OpenAI semver for {entry['name']}")
    validation.require(manifest.get("skills") == "./skills/", f"OpenAI skills path must be ./skills/ for {entry['name']}")
    validation.require("apps" not in manifest and "mcpServers" not in manifest, f"{entry['name']} v1 must remain skills-only")

    interface = manifest.get("interface", {})
    missing = REQUIRED_OPENAI_INTERFACE - set(interface)
    validation.require(not missing, f"Missing OpenAI interface fields for {entry['name']}: {sorted(missing)}")
    validation.require(interface.get("category") == entry["category"], f"Category mismatch for {entry['name']}")
    prompts = interface.get("defaultPrompt", [])
    validation.require(isinstance(prompts, list) and 1 <= len(prompts) <= 3, f"{entry['name']} needs 1-3 starter prompts")
    for prompt in prompts if isinstance(prompts, list) else []:
        validation.require(isinstance(prompt, str) and 0 < len(prompt) <= 128, f"Invalid starter prompt for {entry['name']}")
    for key in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        if key in interface:
            validate_https(validation, interface[key], f"{entry['name']} interface.{key}")
    for key in ("composerIcon", "logo", "logoDark"):
        if key not in interface:
            continue
        relative = PurePosixPath(str(interface[key]))
        validation.require(not relative.is_absolute() and ".." not in relative.parts, f"Unsafe {key} path for {entry['name']}")
        asset = (root / Path(relative.as_posix())).resolve()
        validation.require(root.resolve() in asset.parents, f"{key} escapes {entry['name']} package")
        validation.require(asset.is_file(), f"Missing {key} for {entry['name']}: {asset}")
    validation.require(interface.get("displayName") == listing["displayName"], f"Generated listing drift for {entry['name']}")


def validate_evals(validation: Validation, entry: dict) -> None:
    path = REPO_ROOT / entry["evals"]
    validation.require(path.is_file(), f"Missing evals file for {entry['name']}: {path}")
    if not path.is_file():
        return
    evals = load_json(path)
    validation.require(evals.get("plugin") == entry["name"], f"Eval plugin mismatch for {entry['name']}")
    validation.require(evals.get("version") == entry["version"], f"Eval version mismatch for {entry['name']}")
    cases = evals.get("cases", [])
    positives = [case for case in cases if case.get("polarity") == "positive"]
    negatives = [case for case in cases if case.get("polarity") == "negative"]
    validation.require(len(positives) == 5, f"{entry['name']} must have exactly five positive eval cases")
    validation.require(len(negatives) == 3, f"{entry['name']} must have exactly three negative eval cases")
    ids = [case.get("id") for case in cases]
    validation.require(len(ids) == len(set(ids)) and all(ids), f"Eval IDs must be unique and non-empty for {entry['name']}")
    for case in cases:
        validation.require(bool(case.get("prompt")), f"Eval {case.get('id')} has no prompt")
        validation.require(bool(case.get("expect", {}).get("behavior")), f"Eval {case.get('id')} has no expected behavior")


def validate_release_evidence(validation: Validation, entry: dict, output_root: Path) -> None:
    relative = entry.get("releaseEvidence")
    if not relative:
        validation.require(entry.get("status") != "pilot", f"Pilot {entry['name']} needs release evidence")
        return
    path = REPO_ROOT / relative
    validation.require(path.is_file(), f"Missing release evidence for {entry['name']}: {path}")
    if not path.is_file():
        return
    evidence = load_json(path)
    validation.require(evidence.get("plugin") == entry["name"], f"Release evidence plugin mismatch for {entry['name']}")
    validation.require(evidence.get("version") == entry["version"], f"Release evidence version mismatch for {entry['name']}")
    validation.require(evidence.get("payloadDigest") == entry["sourceDigest"], f"Release evidence payload digest drift for {entry['name']}")
    archive = evidence.get("submissionArchive", {})
    archive_path = REPO_ROOT / str(archive.get("path", ""))
    validation.require(archive_path.is_file(), f"Missing submission archive for {entry['name']}: {archive_path}")
    if archive_path.is_file():
        import hashlib

        digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
        validation.require(digest == archive.get("sha256"), f"Submission archive digest drift for {entry['name']}")
    validation.require(
        evidence.get("automatedChecks", {}).get("windowsLocal", {}).get("status") == "passed",
        f"Pilot {entry['name']} has no recorded local automated test pass",
    )


def validate_marketplace(validation: Validation, output_root: Path) -> None:
    path = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
    validation.require(path.is_file(), f"Missing marketplace manifest: {path}")
    if not path.is_file():
        return
    marketplace = load_json(path)
    validation.require(marketplace.get("name") == "manan-skills", "Marketplace name must be manan-skills")
    entries = marketplace.get("plugins", [])
    validation.require(len(entries) == 1, "Pilot marketplace must list only PM OS")
    if entries:
        entry = entries[0]
        validation.require(entry.get("name") == "pm-os-setup", "Pilot marketplace entry must be pm-os-setup")
        expected = "./dist/plugins/openai/pm-os-setup"
        validation.require(entry.get("source", {}).get("path") == expected, f"Marketplace source must be {expected}")
        validation.require(entry.get("policy", {}).get("installation") == "AVAILABLE", "Marketplace installation policy must be AVAILABLE")
        validation.require(entry.get("policy", {}).get("authentication") == "ON_INSTALL", "Marketplace authentication policy must be ON_INSTALL")
        validation.require("products" not in entry.get("policy", {}), "Marketplace must not use product gating")
        validation.require(entry.get("category") == "Productivity", "Marketplace category must be Productivity")
        validation.require((output_root / "openai" / "pm-os-setup").is_dir(), "Marketplace package target has not been built")


def validate_version_bumps(validation: Validation, catalog: dict, base_ref: str | None) -> None:
    """Require a version bump whenever a prior catalog digest changes."""
    if not base_ref or not base_ref.strip("0"):
        return
    result = subprocess.run(
        ["git", "show", f"{base_ref}:plugins/catalog.json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        # The first plugin rollout has no prior catalog to compare.
        return
    try:
        previous = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        validation.errors.append(f"Cannot parse base catalog at {base_ref}: {exc}")
        return
    previous_by_name = {entry.get("name"): entry for entry in previous.get("plugins", [])}
    for entry in catalog.get("plugins", []):
        old = previous_by_name.get(entry.get("name"))
        if not old or old.get("sourceDigest") == entry.get("sourceDigest"):
            continue
        def release_tuple(value: object) -> tuple[int, int, int]:
            core = str(value).split("-", 1)[0].split("+", 1)[0]
            try:
                major, minor, patch = core.split(".")
                return int(major), int(minor), int(patch)
            except (TypeError, ValueError):
                return (-1, -1, -1)

        validation.require(
            release_tuple(entry.get("version")) > release_tuple(old.get("version")),
            f"{entry.get('name')} source digest changed without a plugin version bump "
            f"({old.get('version')} -> {entry.get('version')})",
        )


def validate_all(catalog_path: Path, output_root: Path, base_ref: str | None = None) -> Validation:
    validation = Validation()
    catalog = load_json(catalog_path)
    schema_path = REPO_ROOT / "scripts" / "schemas" / "agent-plugins" / "1.0.0" / "plugin.schema.json"
    schema = load_json(schema_path)
    if Draft202012Validator is not None:
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # jsonschema exposes multiple schema exception types
            validation.errors.append(f"Pinned portable schema is invalid: {exc}")

    entries = catalog.get("plugins", [])
    names = [entry.get("name") for entry in entries]
    validation.require(len(entries) == 3, "Catalog must contain the three planned single-skill plugins")
    validation.require(len(names) == len(set(names)), "Catalog plugin names must be unique")
    validation.require(catalog.get("publisher", {}).get("name") == "Manan Suneja", "Publisher identity mismatch")
    max_bytes = int(catalog.get("maxPackageBytes", 1_048_576))
    validate_version_bumps(validation, catalog, base_ref)

    for entry in entries:
        name = str(entry.get("name", ""))
        validation.require(bool(PLUGIN_NAME_RE.fullmatch(name)), f"Invalid plugin name: {name}")
        validation.require(bool(SEMVER_RE.fullmatch(str(entry.get("version", "")))), f"Invalid semver for {name}")
        source_root = REPO_ROOT / entry["source"]
        validation.require(source_root.name == name, f"Canonical skill folder/name mismatch for {name}")
        validation.require(source_root.is_dir(), f"Missing canonical source for {name}: {source_root}")
        frontmatter = read_frontmatter(source_root / "SKILL.md") if source_root.is_dir() else {}
        validation.require(frontmatter.get("name") == name, f"SKILL.md frontmatter name mismatch for {name}")
        validation.require(bool(frontmatter.get("description")), f"SKILL.md needs a description for {name}")
        source_plugin_manifest = source_root / ".claude-plugin" / "plugin.json"
        if source_plugin_manifest.is_file():
            source_plugin = load_json(source_plugin_manifest)
            validation.require(source_plugin.get("name") == name, f"Canonical plugin identity mismatch for {name}")
            validation.require(
                source_plugin.get("version") == entry["version"],
                f"Catalog version for {name} must match its existing canonical manifest",
            )
        source_digest = digest_files(tracked_files(entry["source"]))
        validation.require(entry.get("sourceDigest") == source_digest, f"Catalog source digest is stale for {name}")

        if name in {"pm-os-setup", "workspace-os-setup"}:
            template_dir = "pm-os-workspace" if name == "pm-os-setup" else "workspace-os-workspace"
            state_path = source_root / "assets" / template_dir / "_workspace_setup_docs" / "workspace-state.json"
            validation.require(state_path.is_file(), f"Missing workspace state template for {name}")
            if state_path.is_file():
                state = load_json(state_path)
                expected_system = "pm-os" if name == "pm-os-setup" else "workspace-os"
                validation.require(state.get("system") == expected_system, f"Workspace state system mismatch for {name}")
                validation.require(state.get("setupVersion") == entry["version"], f"Workspace state setup version mismatch for {name}")
                validation.require(isinstance(state.get("workspaceSchemaVersion"), int), f"Workspace schema version must be an integer for {name}")

        listing_path = REPO_ROOT / entry["listing"]
        validation.require(listing_path.is_file(), f"Missing listing metadata for {name}")
        if not listing_path.is_file():
            continue
        listing = load_json(listing_path)
        validation.require(listing.get("developerName") == "Manan Suneja", f"Listing publisher mismatch for {name}")
        validation.require(listing.get("category") == entry["category"], f"Listing category mismatch for {name}")
        validate_https(validation, listing.get("supportURL"), f"{name} supportURL")
        validate_evals(validation, entry)
        if entry.get("status") == "pilot" or entry.get("releaseEvidence"):
            validate_release_evidence(validation, entry, output_root)

        portable_root = output_root / "portable" / name
        openai_root = output_root / "openai" / name
        validate_package_tree(validation, portable_root, f"portable/{name}", max_bytes)
        validate_package_tree(validation, openai_root, f"openai/{name}", max_bytes)
        validate_portable_manifest(validation, portable_root / "plugin.json", schema)
        validate_openai_manifest(validation, openai_root, entry, listing)
        portable_skill = portable_root / "skills" / name
        openai_skill = openai_root / "skills" / name
        validation.require(portable_skill.is_dir(), f"Missing portable skill payload for {name}")
        validation.require(openai_skill.is_dir(), f"Missing OpenAI skill payload for {name}")
        if portable_skill.is_dir() and openai_skill.is_dir():
            portable_digest = disk_tree_digest(portable_skill)
            openai_digest = disk_tree_digest(openai_skill)
            validation.require(portable_digest == openai_digest == source_digest, f"Skill payload digest mismatch for {name}")
            validate_skill_links(validation, portable_skill)

    validate_marketplace(validation, output_root)
    return validation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--base-ref",
        default=os.environ.get("PLUGIN_BASE_REF"),
        help="Git ref whose catalog is used to enforce version bumps when source digests change.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validation = validate_all(args.catalog.resolve(), args.output.resolve(), args.base_ref)
    if validation.errors:
        print(f"Plugin validation FAILED ({len(validation.errors)} errors, {validation.checks} checks):", file=sys.stderr)
        for error in validation.errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Plugin validation passed ({validation.checks} checks).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
