#!/usr/bin/env python3
"""Static checks for generated workflow skill families (flat layout).

A family is installed flat under the skills root and bound by a shared naming
prefix. The coordinator skill is named ``<prefix>-workflow`` and holds the
single ``linkages.md`` registry plus ``README.md``. Generated/adopted children
are flat siblings named ``<prefix>-<phase>``. Connected standalone skills are
validated as unchanged external dependencies and may keep any valid skill name.

Usage:
    validate_workflow_family.py <coordinator-skill-dir> --skills-root <skills-root>
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
VALID_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def clean_cell(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    return value.strip()


CONFLICT_RE = re.compile(r"^(?:<{7}|={7}|>{7})(?:\s|$)", re.MULTILINE)

try:
    import yaml  # type: ignore
except ImportError:  # PyYAML is optional; fall back to a block-aware line parser.
    yaml = None


def _read_text(skill_md: Path) -> str:
    try:
        return skill_md.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return skill_md.read_text()


def _has_utf8_bom(path: Path) -> bool:
    try:
        return path.read_bytes().startswith(b"\xef\xbb\xbf")
    except OSError:
        return False


def _fallback_parse(block: str) -> dict[str, str]:
    """Block-scalar-aware line parser used when PyYAML is unavailable."""
    fields: dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line or line[:1] in (" ", "\t"):
            i += 1
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value in (">", ">-", "|", "|-", ">+", "|+"):
            # Folded/literal block scalar: gather indented continuation lines.
            collected: list[str] = []
            i += 1
            while i < len(lines) and (lines[i][:1] in (" ", "\t") or lines[i] == ""):
                collected.append(lines[i].strip())
                i += 1
            fields[key] = " ".join(c for c in collected if c)
            continue
        fields[key] = value.strip("\"'")
        i += 1
    return fields


def read_frontmatter(skill_md: Path) -> dict[str, str]:
    content = _read_text(skill_md)
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}
    block = match.group(1)
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
            if isinstance(data, dict):
                return {str(k): ("" if v is None else str(v)) for k, v in data.items()}
        except yaml.YAMLError:
            return {}
    return _fallback_parse(block)


def validate_frontmatter_yaml(skill_md: Path, label: str) -> list[str]:
    """Catch the breakage that makes the harness silently skip a skill."""
    errors: list[str] = []
    if not skill_md.exists():
        return [f"Missing SKILL.md in {label}: {skill_md}"]
    if _has_utf8_bom(skill_md):
        errors.append(
            f"SKILL.md has a UTF-8 BOM before frontmatter in {label}: {skill_md}. "
            "Rewrite as UTF-8 without BOM so installers see line 1 as literal '---'."
        )
    content = _read_text(skill_md)
    if CONFLICT_RE.search(content):
        errors.append(f"Merge-conflict markers present in {label}: {skill_md}")
    if not content.startswith("---"):
        errors.append(f"SKILL.md must start with YAML frontmatter (---) in {label}: {skill_md}")
        return errors
    match = FRONTMATTER_RE.match(content)
    if not match:
        errors.append(f"Unterminated frontmatter (missing closing ---) in {label}: {skill_md}")
        return errors
    if yaml is not None:
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            detail = str(exc).splitlines()[0]
            errors.append(f"Invalid YAML frontmatter in {label}: {detail} (quote/fold values containing ':' )")
            return errors
        if not isinstance(data, dict):
            errors.append(f"Frontmatter is not a mapping in {label}: {skill_md}")
        return errors
    # No PyYAML: heuristically catch the most common breakage — an unquoted
    # colon-space inside a plain scalar value (YAML reads it as a nested mapping).
    for raw in match.group(1).splitlines():
        if ":" not in raw or raw[:1] in (" ", "\t"):
            continue
        key, value = raw.split(":", 1)
        value = value.strip()
        if value in (">", ">-", "|", "|-", ">+", "|+"):
            continue  # block scalar — colons on following lines are literal
        if value[:1] in ("\"", "'"):
            continue  # quoted scalar
        if ": " in value or value.endswith(":"):
            errors.append(
                f"Likely invalid YAML in {label}: value of '{key.strip()}' contains an "
                f"unquoted ':' — use a folded block scalar (>-) or quotes."
            )
    return errors


def read_frontmatter_name(skill_md: Path) -> str | None:
    return read_frontmatter(skill_md).get("name")


def validate_skill_metadata(skill_dir: Path, expected_name: str | None, label: str) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    yaml_errors = validate_frontmatter_yaml(skill_md, label)
    if yaml_errors:
        # Hard YAML failures make every downstream field unreliable; report and stop here.
        return yaml_errors
    frontmatter = read_frontmatter(skill_md)
    name = frontmatter.get("name")
    description = frontmatter.get("description", "")

    if not name:
        errors.append(f"Missing frontmatter name in {label}: {skill_md}")
    elif not VALID_NAME_RE.match(name):
        # Agent Skills spec: lowercase a-z/0-9/hyphen, no leading/trailing or consecutive hyphens.
        errors.append(f"Invalid skill name in {label}: {name!r}")
    elif len(name) > 64:
        # Agent Skills spec: name must be 1-64 characters.
        errors.append(f"Skill name exceeds 64 characters in {label}: {name!r} ({len(name)})")
    elif "claude" in name or "anthropic" in name:
        errors.append(f"Reserved word in skill name for {label}: {name!r}")

    if expected_name and name != expected_name:
        errors.append(f"Frontmatter mismatch for {label}: expected {expected_name!r}, got {name!r}")

    if skill_dir.name != name:
        errors.append(f"Folder/name mismatch for {label}: folder {skill_dir.name!r}, name {name!r}")

    if not description:
        errors.append(f"Missing description in {label}: {skill_md}")
    else:
        if len(description) > 1024:
            errors.append(f"Description too long in {label}: {len(description)} characters")
        if "<" in description or ">" in description:
            errors.append(f"Description contains XML angle brackets in {label}")
        if "use when" not in description.lower():
            errors.append(f"Description should include trigger conditions in {label}")

    # README/linkages belong only in the coordinator folder; never decorative docs in children.
    for extra_name in ("CHANGELOG.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md", "index.md"):
        if (skill_dir / extra_name).exists():
            errors.append(f"Unexpected doc inside {label}: {skill_dir / extra_name}")

    return errors


def validate_external_skill(skill_dir: Path, expected_name: str, label: str) -> list[str]:
    """Validate only the open-format contract; never impose family-owned conventions."""
    errors = validate_frontmatter_yaml(skill_dir / "SKILL.md", label)
    if errors:
        return errors
    frontmatter = read_frontmatter(skill_dir / "SKILL.md")
    name = frontmatter.get("name")
    description = frontmatter.get("description", "")
    if name != expected_name:
        errors.append(f"Frontmatter mismatch for {label}: expected {expected_name!r}, got {name!r}")
    if name and not VALID_NAME_RE.match(name):
        errors.append(f"Invalid external skill name in {label}: {name!r}")
    if skill_dir.name != name:
        errors.append(f"Folder/name mismatch for {label}: folder {skill_dir.name!r}, name {name!r}")
    if not description:
        errors.append(f"Missing description in {label}: {skill_dir / 'SKILL.md'}")
    elif len(description) > 1024:
        errors.append(f"Description too long in {label}: {len(description)} characters")
    return errors


def read_generator_signature(skill_md: Path) -> str | None:
    """Return the Workflow Creator signature value, reading the *nested*
    ``metadata.generator`` field (the documented, canonical location).

    ``read_frontmatter`` flattens nested mappings to ``str(dict)``, so it cannot
    see ``metadata.generator``; this reads the metadata block directly. A
    top-level ``generator`` is tolerated for backward compatibility.
    """
    content = _read_text(skill_md)
    match = FRONTMATTER_RE.match(content)
    if not match:
        return None
    block = match.group(1)
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            return None
        if isinstance(data, dict):
            meta = data.get("metadata")
            if isinstance(meta, dict) and meta.get("generator"):
                return str(meta["generator"])
            if data.get("generator"):
                return str(data["generator"])
        return None
    # No PyYAML: scan for a 'generator:' line (indentation stripped, so a
    # nested metadata.generator and a top-level one both match).
    for raw in block.splitlines():
        stripped = raw.strip()
        if stripped.startswith("generator:"):
            return stripped.split(":", 1)[1].strip().strip("\"'")
    return None


def check_watermark(skill_dir: Path, label: str) -> list[str]:
    """Warn (non-fatal) when a generated skill is missing the Workflow Creator signature.

    The canonical marker is the frontmatter field ``metadata.generator: workflow-create``.
    Returned strings are warnings, not errors: families created before the watermark
    convention stay valid, but new ones should carry it.
    """
    warnings: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return warnings
    if read_generator_signature(skill_md) != "workflow-create":
        warnings.append(
            f"Missing Workflow Creator signature in {label}: "
            f"add 'metadata.generator: workflow-create' to {skill_md}"
        )
    return warnings


def derive_prefix(coordinator_name: str | None, coordinator_dir: Path) -> str | None:
    name = coordinator_name or coordinator_dir.name
    if name.endswith("-workflow"):
        return name[: -len("-workflow")]
    return None


def expand_path_tokens(path_text: str, coordinator_dir: Path, skills_root: Path | None) -> str:
    token_values = {
        "${USER_ROOT}": Path.home(),
        "${PARENT_SKILL_DIR}": coordinator_dir,
        "${SKILLS_ROOT}": skills_root or coordinator_dir.parent,
        "${WORKFLOW_ROOT}": coordinator_dir.parent,
    }
    expanded = path_text
    for token, value in token_values.items():
        expanded = expanded.replace(token, str(value))
    return expanded


def resolve_skill_path(path_text: str, coordinator_dir: Path, skills_root: Path | None) -> Path:
    path_text = expand_path_tokens(path_text, coordinator_dir, skills_root).strip()
    candidate = Path(path_text)
    if candidate.is_absolute():
        return candidate
    # Flat layout: members are siblings under the skills root.
    root = skills_root or coordinator_dir.parent
    rooted = root / path_text
    if rooted.exists():
        return rooted
    sibling = coordinator_dir.parent / Path(path_text).name
    if sibling.exists():
        return sibling
    return root / path_text


def parse_linkage_rows(linkages_md: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw_line in linkages_md.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or "---" in line:
            continue
        cells = [clean_cell(cell) for cell in line.strip("|").split("|")]
        if len(cells) not in (7, 8) or cells[0].lower() == "order":
            continue
        rows.append(
            {
                "order": cells[0],
                "skill": cells[1].lstrip("/"),
                "path": cells[2],
                "expected_name": cells[3],
                "previous": cells[4],
                "next": cells[5],
                "status": cells[6],
                "kind": cells[7].lower() if len(cells) == 8 else "family",
            }
        )
    return rows


def parse_external_dependency_rows(linkages_md: Path) -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    for raw_line in linkages_md.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or "---" in line:
            continue
        cells = [clean_cell(cell) for cell in line.strip("|").split("|")]
        if len(cells) != 6 or cells[0].lower() == "skill":
            continue
        skill = cells[0].lstrip("/")
        records[skill] = {
            "source": cells[1],
            "install": cells[2],
            "path": cells[3],
            "hash": cells[4].lower(),
            "verified": cells[5],
        }
    return records


def validate(coordinator_dir: Path, skills_root: Path | None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    coordinator_dir = coordinator_dir.resolve()
    if skills_root:
        skills_root = skills_root.resolve()
    else:
        skills_root = coordinator_dir.parent

    coordinator_md = coordinator_dir / "SKILL.md"
    linkages_md = coordinator_dir / "linkages.md"
    readme_md = coordinator_dir / "README.md"

    if not coordinator_md.exists():
        errors.append(f"Missing coordinator SKILL.md: {coordinator_md}")
        return errors, warnings
    if not linkages_md.exists():
        errors.append(f"Missing coordinator linkages.md: {linkages_md}")
        return errors, warnings
    if not readme_md.exists():
        errors.append(f"Missing coordinator README.md: {readme_md}")

    coordinator_content = coordinator_md.read_text(encoding="utf-8-sig")
    coordinator_name = read_frontmatter_name(coordinator_md)
    errors.extend(validate_skill_metadata(coordinator_dir, coordinator_name, "coordinator"))
    warnings.extend(check_watermark(coordinator_dir, "coordinator"))

    prefix = derive_prefix(coordinator_name, coordinator_dir)
    if not prefix:
        errors.append(
            f"Coordinator skill name must end with '-workflow': {coordinator_name!r}"
        )

    if "linkages.md" not in coordinator_content:
        errors.append("Coordinator SKILL.md must reference linkages.md")
    if "runStatus.md" not in coordinator_content:
        errors.append("Coordinator SKILL.md must reference runStatus.md")

    rows = parse_linkage_rows(linkages_md)
    external_records = parse_external_dependency_rows(linkages_md)
    child_rows = [r for r in rows if r["expected_name"] != coordinator_name]
    if not child_rows:
        errors.append(f"No child rows found in linkage table: {linkages_md}")

    ledger_names: set[str] = {coordinator_name} if coordinator_name else set()

    for row in child_rows:
        ledger_names.add(row["expected_name"])
        if row["kind"] not in {"family", "generated", "adopted", "external"}:
            errors.append(f"Unknown linkage kind for /{row['skill']}: {row['kind']!r}")
            continue
        child_path = resolve_skill_path(row["path"], coordinator_dir, skills_root)
        skill_md = child_path / "SKILL.md"
        if not child_path.exists():
            errors.append(f"Missing child path for /{row['skill']}: {child_path}")
            continue
        if not skill_md.exists():
            errors.append(f"Missing child SKILL.md for /{row['skill']}: {skill_md}")
            continue

        if row["kind"] == "external":
            errors.extend(validate_external_skill(child_path, row["expected_name"], f"/{row['skill']}"))
            record = external_records.get(row["expected_name"])
            if not record:
                errors.append(
                    f"Missing ## External Dependencies record for /{row['skill']}"
                )
                continue
            if not record["source"] or not record["install"]:
                errors.append(f"External dependency lacks source/install command: /{row['skill']}")
            expected_hash = record["hash"]
            if not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
                errors.append(f"Invalid SKILL.md SHA-256 for /{row['skill']}: {expected_hash!r}")
            else:
                actual_hash = hashlib.sha256(skill_md.read_bytes()).hexdigest()
                if actual_hash != expected_hash:
                    errors.append(
                        f"External dependency drift for /{row['skill']}: "
                        f"expected {expected_hash}, got {actual_hash}"
                    )
            continue

        actual_name = read_frontmatter_name(skill_md)
        errors.extend(validate_skill_metadata(child_path, row["expected_name"], f"/{row['skill']}"))
        warnings.extend(check_watermark(child_path, f"/{row['skill']}"))

        if prefix and actual_name and not actual_name.startswith(f"{prefix}-"):
            errors.append(
                f"Child skill name should start with prefix {prefix!r}: {actual_name!r}"
            )
        if actual_name == coordinator_name:
            errors.append(f"Child cannot reuse the coordinator name: {actual_name!r}")
        if actual_name and actual_name.endswith("-workflow"):
            errors.append(
                f"Only the coordinator may end with '-workflow': {actual_name!r}"
            )

        child_content = skill_md.read_text(encoding="utf-8-sig")
        if "## Orchestration Linkage" not in child_content:
            errors.append(f"Missing orchestration note in /{row['skill']}")
        if coordinator_name and f"Parent: `/{coordinator_name}`" not in child_content:
            errors.append(f"Missing parent linkage to /{coordinator_name} in /{row['skill']}")
        if "standalone" not in child_content.lower():
            errors.append(f"Missing standalone-mode instruction in /{row['skill']}")

    # Orphan check: a prefixed skill on disk that is not in the ledger.
    if prefix:
        for child_dir in sorted(skills_root.glob(f"{prefix}-*")):
            if not child_dir.is_dir() or not (child_dir / "SKILL.md").exists():
                continue
            disk_name = read_frontmatter_name(child_dir / "SKILL.md") or child_dir.name
            if disk_name not in ledger_names:
                errors.append(
                    f"Orphan skill not in linkages.md (ask user if it belongs): {child_dir}"
                )

    # Exactly one -workflow skill in the family.
    if prefix:
        workflow_skills = [
            d for d in skills_root.glob(f"{prefix}-*")
            if d.is_dir() and d.name.endswith("-workflow")
        ]
        if len(workflow_skills) > 1:
            names = ", ".join(d.name for d in workflow_skills)
            errors.append(f"More than one '-workflow' coordinator for prefix {prefix!r}: {names}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a generated workflow skill family (flat layout).")
    parser.add_argument("coordinator_skill_dir", type=Path)
    parser.add_argument("--skills-root", type=Path, default=None)
    args = parser.parse_args()

    errors, warnings = validate(args.coordinator_skill_dir, args.skills_root)
    if warnings:
        print("Workflow family validation warnings:")
        for warning in warnings:
            print(f"- {warning}")
    if errors:
        print("Workflow family validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Workflow family validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
