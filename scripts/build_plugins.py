#!/usr/bin/env python3
"""Build self-contained Agent Plugins packages from canonical tracked skills."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = REPO_ROOT / "plugins" / "catalog.json"
DEFAULT_OUTPUT = REPO_ROOT / "dist" / "plugins"
PORTABLE_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
EXCLUDED_TOP_LEVEL = {
    ".claude-plugin",
    ".gitignore",
    "README.md",
    "LICENSE",
    "announcements",
    "visualize-this-outputs",
    "testing",
}


class BuildError(RuntimeError):
    pass


@dataclass(frozen=True)
class TrackedFile:
    repo_path: str
    relative_path: str
    mode: str
    content: bytes


def run_git(*args: str, text: bool = True) -> str | bytes:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=text,
    )
    if result.returncode != 0:
        stderr = result.stderr if text else result.stderr.decode("utf-8", "replace")
        raise BuildError(f"git {' '.join(args)} failed: {stderr.strip()}")
    return result.stdout


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BuildError(f"Cannot read JSON {path}: {exc}") from exc


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def assert_safe_output(output_root: Path) -> Path:
    resolved = output_root.resolve()
    repo = REPO_ROOT.resolve()
    if resolved == repo or repo not in resolved.parents:
        raise BuildError(f"Refusing to use output outside the repository: {resolved}")
    if resolved == repo / "dist":
        raise BuildError("Output must be a dedicated directory below dist, not dist itself.")
    return resolved


def tracked_files(source: str) -> list[TrackedFile]:
    unstaged = subprocess.run(
        ["git", "diff", "--quiet", "--", source],
        cwd=REPO_ROOT,
        check=False,
    )
    if unstaged.returncode == 1:
        raise BuildError(
            f"Canonical source has unstaged tracked changes: {source}. "
            "Review and stage them before computing a release digest."
        )
    if unstaged.returncode not in {0, 1}:
        raise BuildError(f"Could not inspect canonical source state: {source}")
    source_path = PurePosixPath(source)
    raw = run_git("ls-files", "-s", "--", source)
    files: list[TrackedFile] = []
    for line in str(raw).splitlines():
        if not line:
            continue
        metadata, repo_path = line.split("\t", 1)
        mode, _blob, stage = metadata.split()
        if stage != "0":
            raise BuildError(f"Unmerged canonical file cannot be packaged: {repo_path}")
        rel = PurePosixPath(repo_path).relative_to(source_path)
        if not rel.parts or rel.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        content = run_git("show", f":{repo_path}", text=False)
        files.append(TrackedFile(repo_path, rel.as_posix(), mode, bytes(content)))

    files.sort(key=lambda item: item.relative_path)
    if not files:
        raise BuildError(f"No tracked runtime files found under {source}")
    if not any(item.relative_path == "SKILL.md" for item in files):
        raise BuildError(f"Canonical skill has no tracked SKILL.md: {source}")
    return files


def digest_files(files: Iterable[TrackedFile]) -> str:
    digest = hashlib.sha256()
    for item in sorted(files, key=lambda value: value.relative_path):
        digest.update(item.relative_path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(item.content)
        digest.update(b"\0")
    return digest.hexdigest()


def disk_tree_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=lambda item: item.relative_to(root).as_posix()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def write_tracked_files(files: Iterable[TrackedFile], destination: Path) -> None:
    for item in files:
        target = destination / Path(item.relative_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(item.content)
        target.chmod(0o755 if item.mode == "100755" else 0o644)


def copy_overlay_assets(overlay_root: Path, destination: Path, listing: dict) -> None:
    assets = overlay_root / "assets"
    if not assets.exists():
        return
    references = {str(listing[key]) for key in ("composerIcon", "logo", "logoDark") if listing.get(key)}
    for reference in sorted(references):
        relative = PurePosixPath(reference)
        if relative.is_absolute() or ".." in relative.parts or not relative.parts or relative.parts[0] != "assets":
            raise BuildError(f"Unsafe overlay asset path: {reference}")
        path = (overlay_root / Path(*relative.parts)).resolve()
        if assets.resolve() not in path.parents or not path.is_file() or path.is_symlink():
            raise BuildError(f"Missing or unsafe overlay asset: {reference}")
        target = destination / Path(*relative.parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)


def generated_readme(entry: dict, listing: dict) -> str:
    source_url = f"https://github.com/manansuneja/skills/tree/main/{entry['source']}"
    return (
        f"# {listing['displayName']}\n\n"
        f"{listing['longDescription']}\n\n"
        "This release package is generated from the canonical skill source. "
        "Do not edit the packaged copy directly.\n\n"
        f"Source: {source_url}\n"
    )


def portable_manifest(catalog: dict, entry: dict, listing: dict) -> dict:
    return {
        "$schema": PORTABLE_SCHEMA,
        "name": entry["name"],
        "version": entry["version"],
        "description": listing["longDescription"],
        "author": catalog["publisher"],
        "homepage": catalog["homepage"],
        "repository": f"{catalog['repository']}/tree/main/{entry['source']}",
        "license": catalog["license"],
        "keywords": listing["keywords"],
    }


def openai_manifest(catalog: dict, entry: dict, listing: dict) -> dict:
    interface_keys = (
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "capabilities",
        "websiteURL",
        "privacyPolicyURL",
        "termsOfServiceURL",
        "defaultPrompt",
        "brandColor",
        "composerIcon",
        "logo",
        "logoDark",
        "screenshots",
    )
    interface = {key: listing[key] for key in interface_keys if key in listing}
    return {
        "name": entry["name"],
        "version": entry["version"],
        "description": listing["longDescription"],
        "author": catalog["publisher"],
        "repository": f"{catalog['repository']}/tree/main/{entry['source']}",
        "license": catalog["license"],
        "keywords": listing["keywords"],
        "skills": "./skills/",
        "interface": interface,
    }


def write_common_package_files(root: Path, entry: dict, listing: dict, files: list[TrackedFile], license_bytes: bytes) -> None:
    write_tracked_files(files, root / "skills" / entry["name"])
    (root / "LICENSE").write_bytes(license_bytes)
    (root / "README.md").write_text(generated_readme(entry, listing), encoding="utf-8", newline="\n")


def source_license(source: str) -> bytes:
    license_path = f"{source}/LICENSE"
    tracked = str(run_git("ls-files", "--", license_path)).strip()
    if tracked != license_path:
        return (REPO_ROOT / "LICENSE").read_bytes()
    return bytes(run_git("show", f":{license_path}", text=False))


def zip_directory(source: Path, target: Path, prefix: str = "") -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted((item for item in source.rglob("*") if item.is_file()), key=lambda item: item.relative_to(source).as_posix()):
            relative = path.relative_to(source).as_posix()
            name = f"{prefix.rstrip('/')}/{relative}" if prefix else relative
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            # Windows does not preserve POSIX executable bits. Derive archive
            # permissions from the packaged file role so ZIP bytes stay stable
            # across the Windows/Linux CI matrix.
            executable = path.suffix.lower() in {".sh", ".ps1", ".py"}
            info.external_attr = ((0o100755 if executable else 0o100644) & 0xFFFF) << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def select_entries(catalog: dict, names: list[str] | None) -> list[dict]:
    entries = catalog.get("plugins", [])
    if not names:
        return entries
    requested = set(names)
    selected = [entry for entry in entries if entry.get("name") in requested]
    missing = requested - {entry["name"] for entry in selected}
    if missing:
        raise BuildError(f"Unknown plugin(s): {', '.join(sorted(missing))}")
    return selected


def refresh_catalog_digests(catalog_path: Path, catalog: dict, entries: list[dict]) -> None:
    by_name = {entry["name"]: entry for entry in catalog["plugins"]}
    for entry in entries:
        by_name[entry["name"]]["sourceDigest"] = digest_files(tracked_files(entry["source"]))
    write_json(catalog_path, catalog)


def build(catalog_path: Path, output_root: Path, names: list[str] | None, refresh_digests: bool, archives: bool) -> dict:
    catalog_path = catalog_path.resolve()
    output_root = assert_safe_output(output_root)
    catalog = load_json(catalog_path)
    entries = select_entries(catalog, names)

    if refresh_digests:
        refresh_catalog_digests(catalog_path, catalog, entries)
        catalog = load_json(catalog_path)
        entries = select_entries(catalog, names)

    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    evidence: dict[str, object] = {
        "schemaVersion": 1,
        "catalog": catalog_path.relative_to(REPO_ROOT).as_posix(),
        "plugins": [],
    }

    for entry in entries:
        name = entry["name"]
        version = entry["version"]
        if not SEMVER_RE.fullmatch(version):
            raise BuildError(f"Invalid semver for {name}: {version}")
        listing = load_json(REPO_ROOT / entry["listing"])
        files = tracked_files(entry["source"])
        source_digest = digest_files(files)
        if source_digest != entry.get("sourceDigest"):
            raise BuildError(
                f"Source digest mismatch for {name}. Bump its version and run "
                "scripts/build_plugins.py --refresh-digests."
            )

        portable_root = output_root / "portable" / name
        openai_root = output_root / "openai" / name
        portable_root.mkdir(parents=True)
        (openai_root / ".codex-plugin").mkdir(parents=True)
        license_bytes = source_license(entry["source"])

        write_common_package_files(portable_root, entry, listing, files, license_bytes)
        write_common_package_files(openai_root, entry, listing, files, license_bytes)
        write_json(portable_root / "plugin.json", portable_manifest(catalog, entry, listing))
        write_json(openai_root / ".codex-plugin" / "plugin.json", openai_manifest(catalog, entry, listing))
        copy_overlay_assets((REPO_ROOT / entry["listing"]).parent, openai_root, listing)

        portable_payload_digest = disk_tree_digest(portable_root / "skills" / name)
        openai_payload_digest = disk_tree_digest(openai_root / "skills" / name)
        if portable_payload_digest != openai_payload_digest or portable_payload_digest != source_digest:
            raise BuildError(f"Generated skill payload mismatch for {name}")

        release_files: dict[str, dict[str, object]] = {}
        if archives:
            release_root = output_root / "releases"
            archive_specs = {
                "portable": (portable_root, release_root / f"{name}-{version}-portable.zip", ""),
                "openai": (openai_root, release_root / f"{name}-{version}-openai.zip", ""),
                "skillBundle": (
                    openai_root / "skills" / name,
                    release_root / f"{name}-{version}-skill-bundle.zip",
                    name,
                ),
            }
            for kind, (source, target, prefix) in archive_specs.items():
                zip_directory(source, target, prefix)
                release_files[kind] = {
                    "path": target.relative_to(output_root).as_posix(),
                    "sha256": sha256_file(target),
                    "bytes": target.stat().st_size,
                }

        plugin_evidence = {
            "name": name,
            "version": version,
            "status": entry["status"],
            "source": entry["source"],
            "sourceDigest": source_digest,
            "payloadDigest": portable_payload_digest,
            "portablePackageDigest": disk_tree_digest(portable_root),
            "openaiPackageDigest": disk_tree_digest(openai_root),
            "portableBytes": sum(path.stat().st_size for path in portable_root.rglob("*") if path.is_file()),
            "openaiBytes": sum(path.stat().st_size for path in openai_root.rglob("*") if path.is_file()),
            "releaseFiles": release_files,
        }
        evidence["plugins"].append(plugin_evidence)

    write_json(output_root / "build-manifest.json", evidence)
    return evidence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--plugin", action="append", dest="plugins", help="Build only this plugin (repeatable).")
    parser.add_argument(
        "--refresh-digests",
        action="store_true",
        help="Refresh catalog digests after an intentional versioned canonical change.",
    )
    parser.add_argument("--no-archives", action="store_true", help="Skip deterministic release ZIP generation.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        evidence = build(args.catalog, args.output, args.plugins, args.refresh_digests, not args.no_archives)
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    for item in evidence["plugins"]:
        print(
            f"Built {item['name']} {item['version']} "
            f"(source {item['sourceDigest'][:12]}, portable {item['portableBytes']} B, "
            f"openai {item['openaiBytes']} B)"
        )
    print(f"Build evidence: {args.output.resolve() / 'build-manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
