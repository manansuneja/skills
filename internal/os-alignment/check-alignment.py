#!/usr/bin/env python3
"""Validate shared Workspace OS family behaviors without coupling published skills at runtime."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]

VARIANTS = {
    "workspace-os-setup": {
        "root": ROOT / "skills/business/workspace-os-setup",
        "asset": "assets/workspace-os-workspace",
        "practices": "workspace-best-practices",
        "docs": "workspace-hub-docs",
        "apply": "apply-workspace-struct.md",
    },
    "pm-os-setup": {
        "root": ROOT / "skills/product-management/pm-os-setup",
        "asset": "assets/pm-os-workspace",
        "practices": "product-practices",
        "docs": "product-docs",
        "apply": "apply-pmos-struct.md",
    },
}

ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"Missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8-sig")


def require_terms(label: str, text: str, terms: list[str]) -> None:
    lowered = text.lower()
    for term in terms:
        if term.lower() not in lowered:
            fail(f"{label} is missing alignment term: {term!r}")


def validate_links(asset_root: Path) -> None:
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for source in asset_root.rglob("*.md"):
        for raw_target in link_pattern.findall(read(source)):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")) or "{{" in target:
                continue
            resolved = (source.parent / unquote(target)).resolve()
            if not resolved.exists():
                fail(
                    f"Broken Markdown link in {source.relative_to(ROOT)}: {raw_target}"
                )


def validate_audience_labels(asset_root: Path, practices: Path, docs: Path) -> None:
    agent_files = [asset_root / "AGENTS.md", asset_root / "CLAUDE.md"]
    agent_files.extend((asset_root / "agents").rglob("*.md"))
    agent_files.extend((asset_root / "_workspace_setup_docs").rglob("*.md"))
    for path in agent_files:
        if path.name == "README.md" and path.parent.name == "personalization":
            continue
        if path.is_file() and "Agent-facing" not in read(path):
            fail(f"Missing agent-facing label: {path.relative_to(ROOT)}")

    for path in practices.rglob("*.md"):
        text = read(path)
        if "For you" not in text and "Shared template" not in text:
            fail(f"Missing shared customization label: {path.relative_to(ROOT)}")

    for path in docs.rglob("*.md"):
        text = read(path)
        if not any(label in text for label in ("Your primary", "Your workspace", "Your product")):
            fail(f"Missing user-content label: {path.relative_to(ROOT)}")

    if "For you" not in read(asset_root / "START_HERE.md"):
        fail(f"Missing user-facing label: {(asset_root / 'START_HERE.md').relative_to(ROOT)}")


def validate_variant(name: str, config: dict[str, object]) -> None:
    skill_root = config["root"]
    assert isinstance(skill_root, Path)
    asset_root = skill_root / str(config["asset"])
    practices = asset_root / str(config["practices"])
    docs = asset_root / str(config["docs"])

    required_paths = [
        skill_root / "SKILL.md",
        asset_root / "AGENTS.md",
        asset_root / "START_HERE.md",
        asset_root / "INDEX.md",
        asset_root / "_workspace_setup_docs/personalization/AGENTS.md",
        asset_root / f"_workspace_setup_docs/skills/{config['apply']}",
        asset_root / "_workspace_setup_docs/skills/manage-workspace-skills.md",
        practices / "INDEX.md",
        practices / "skills/INDEX.md",
        practices / "templates/INDEX.md",
        practices / "references/INDEX.md",
        docs / "INDEX.md",
    ]
    for path in required_paths:
        if not path.is_file():
            fail(f"{name} is missing required aligned path: {path.relative_to(ROOT)}")

    skill = read(skill_root / "SKILL.md")
    agents = read(asset_root / "AGENTS.md")
    personalization = read(asset_root / "_workspace_setup_docs/personalization/AGENTS.md")
    apply_struct = read(asset_root / f"_workspace_setup_docs/skills/{config['apply']}")
    manage = read(asset_root / "_workspace_setup_docs/skills/manage-workspace-skills.md")
    start_here = read(asset_root / "START_HERE.md")

    require_terms(
        f"{name}/SKILL.md",
        skill,
        [
            "current directory",
            "reconcile",
            "generated-empty",
            "root-folder renaming",
            "structural reconciliation",
            "default library minimal",
            "Never overwrite raw input",
        ],
    )
    require_terms(
        f"{name}/AGENTS.md",
        agents,
        [
            "Agent-facing",
            "Automatic structural reconciliation",
            "user-created",
            "Keep skills and routes synchronized",
            "Never overwrite raw input",
        ],
    )
    require_terms(
        f"{name}/personalization/AGENTS.md",
        personalization,
        [
            "**Keep:**",
            "**Add:**",
            "**Remove:**",
            "**Ask:**",
            "generated-empty",
            "user-authored",
            "Rename the root last",
            "final filesystem operation",
        ],
    )
    require_terms(
        f"{name}/{config['apply']}",
        apply_struct,
        [
            "Focused folder lifecycle",
            "Automatic structural reconciliation",
            "Audience labels",
            "Never overwrite raw input",
        ],
    )
    require_terms(
        f"{name}/manage-workspace-skills.md",
        manage,
        ["skills/", "templates/", "references/", "Less is more"],
    )
    require_terms(
        f"{name}/START_HERE.md",
        start_here,
        ["folder", "manually", "automatically"],
    )

    validate_audience_labels(asset_root, practices, docs)
    validate_links(asset_root)


for variant_name, variant_config in VARIANTS.items():
    validate_variant(variant_name, variant_config)

pm_asset = VARIANTS["pm-os-setup"]["root"] / VARIANTS["pm-os-setup"]["asset"]
assert isinstance(pm_asset, Path)
if (pm_asset / "product-skills").exists():
    fail("PM OS must keep skills under product-practices/skills/, not a top-level product-skills/.")

optional_pm_defaults = [
    "product-docs/design",
    "product-docs/data-insights",
    "product-docs/roadmaps",
    "product-docs/stakeholder-comms",
    "agents/sub-agents/design-partner.md",
    "agents/sub-agents/data-insights-analyst.md",
    "agents/sub-agents/roadmap-planner.md",
    "agents/sub-agents/stakeholder-communicator.md",
]
for relative in optional_pm_defaults:
    if (pm_asset / relative).exists():
        fail(f"PM OS optional profile-driven area is still in the minimal scaffold: {relative}")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)

print("Workspace OS family alignment passed for workspace-os-setup and pm-os-setup.")
