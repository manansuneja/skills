#!/usr/bin/env python3
"""Cross-platform release and scaffold smoke tests for plugin packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import re
from pathlib import Path

from build_plugins import DEFAULT_CATALOG, DEFAULT_OUTPUT, REPO_ROOT, build


REQUIRED_PM_PATHS = (
    "AGENTS.md",
    "INDEX.md",
    "START_HERE.md",
    "agents/pm-chief.md",
    "product-docs/product-vision.md",
    "product-docs/projects/INDEX.md",
    "product-practices/skills/INDEX.md",
    "product-practices/skills/run-projects.md",
    "product-practices/skills/to-build-brief.md",
    "product-practices/templates/project-brief.md",
    "product-practices/templates/project-status.md",
    "product-practices/templates/build-brief.md",
    "agents/sub-agents/program-manager.md",
    "agents/sub-agents/builder.md",
    "_workspace_setup_docs/personalization/README.md",
    "_workspace_setup_docs/workspace-state.json",
)
REQUIRED_WORKSPACE_PATHS = (
    "AGENTS.md",
    "INDEX.md",
    "START_HERE.md",
    "agents/workspace-chief.md",
    "workspace-best-practices/skills/INDEX.md",
    "_workspace_setup_docs/personalization/README.md",
    "_workspace_setup_docs/workspace-state.json",
)
TOKEN_RE = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")


class TestFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise TestFailure(message)


def tree_snapshot(root: Path) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    if not root.exists():
        return snapshot
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        snapshot[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return snapshot


def run_scaffold(script: Path, target: Path, project_name: str, mode: str, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    if os.name == "nt":
        executable = shutil.which("pwsh") or shutil.which("powershell")
        require(bool(executable), "PowerShell is required for the Windows scaffold smoke test")
        command = [
            str(executable),
            "-NoProfile",
            "-File",
            str(script.with_suffix(".ps1")),
            "-ProjectName",
            project_name,
            "-TargetPath",
            str(target),
            "-UseCurrentFolder" if mode == "current" else "-CreateFolder",
        ]
    else:
        command = [
            "bash",
            str(script.with_suffix(".sh")),
            "--project-name",
            project_name,
            "--target-path",
            str(target),
            "--use-current-folder" if mode == "current" else "--create-folder",
        ]
    result = subprocess.run(command, cwd=target, capture_output=True, text=True, check=False)
    if expect_success and result.returncode != 0:
        raise TestFailure(f"Scaffold failed ({' '.join(command)}):\n{result.stdout}\n{result.stderr}")
    if not expect_success and result.returncode == 0:
        raise TestFailure(f"Scaffold unexpectedly succeeded ({' '.join(command)})")
    return result


def assert_required_workspace(root: Path) -> None:
    for relative in REQUIRED_PM_PATHS:
        require((root / relative).exists(), f"Scaffold is missing required path: {root / relative}")
    state = json.loads((root / "_workspace_setup_docs/workspace-state.json").read_text(encoding="utf-8"))
    require(state.get("system") == "pm-os", "PM OS state has the wrong system identifier")
    require(state.get("setupVersion") == "1.3.0", "PM OS state has the wrong setup version")
    require(state.get("workspaceSchemaVersion") == 2, "PM OS state has the wrong workspace schema")
    require(not (root / "product-docs/prds").exists(), "PM OS scaffold still ships the flat prds/ folder")
    index_text = (root / "INDEX.md").read_text(encoding="utf-8")
    require("## Now" in index_text and "## Waiting on" in index_text, "PM OS root index is not a living workboard")
    agents_text = (root / "AGENTS.md").read_text(encoding="utf-8")
    require("Markdown" in agents_text and "installed capability" in agents_text, "PM OS capability routing contract is missing")
    require("pm-builder" in agents_text and "File by scope" in agents_text, "PM OS profile or filing-by-scope contract is missing")


def assert_no_unresolved_tokens(root: Path) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or "_workspace_setup_docs/personalization" in path.relative_to(root).as_posix():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        require(TOKEN_RE.search(text) is None, f"Unresolved PM OS token in {path}")


def run_workspace_scaffold(script: Path, target: Path, name: str, kind: str, mode: str, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    if os.name == "nt":
        executable = shutil.which("pwsh") or shutil.which("powershell")
        require(bool(executable), "PowerShell is required for the Windows scaffold smoke test")
        command = [
            str(executable), "-NoProfile", "-File", str(script.with_suffix(".ps1")),
            "-WorkspaceName", name,
            "-WorkspaceKind", kind,
            "-WorkspaceCategory", "consulting",
            "-Objective", "Deliver clear client outcomes",
            "-PrimaryUse", "weekly operations",
            "-TargetPath", str(target),
            "-UseCurrentFolder" if mode == "current" else "-CreateFolder",
        ]
    else:
        command = [
            "bash", str(script.with_suffix(".sh")),
            "--workspace-name", name,
            "--workspace-kind", kind,
            "--workspace-category", "consulting",
            "--objective", "Deliver clear client outcomes",
            "--primary-use", "weekly operations",
            "--target-path", str(target),
            "--use-current-folder" if mode == "current" else "--create-folder",
        ]
    result = subprocess.run(command, cwd=target, capture_output=True, text=True, check=False)
    if expect_success and result.returncode != 0:
        raise TestFailure(f"Workspace scaffold failed ({' '.join(command)}):\n{result.stdout}\n{result.stderr}")
    if not expect_success and result.returncode == 0:
        raise TestFailure(f"Workspace scaffold unexpectedly succeeded ({' '.join(command)})")
    return result


def assert_workspace_output(root: Path, docs_root: str) -> None:
    for relative in REQUIRED_WORKSPACE_PATHS:
        require((root / relative).exists(), f"Workspace scaffold is missing required path: {root / relative}")
    require((root / docs_root / "workspace-profile.md").is_file(), f"Workspace scaffold is missing {docs_root}/workspace-profile.md")
    wrong_docs = "project-docs" if docs_root == "workspace-hub-docs" else "workspace-hub-docs"
    require(not (root / wrong_docs).exists(), f"Workspace scaffold retained the wrong docs root: {wrong_docs}")
    state = json.loads((root / "_workspace_setup_docs/workspace-state.json").read_text(encoding="utf-8"))
    require(state.get("system") == "workspace-os", "Workspace OS state has the wrong system identifier")
    require(state.get("setupVersion") == "1.2.1", "Workspace OS state has the wrong setup version")
    require(state.get("workspaceSchemaVersion") == 1, "Workspace OS state has the wrong workspace schema")
    index_text = (root / "INDEX.md").read_text(encoding="utf-8")
    require("## Now" in index_text and "## Waiting on" in index_text, "Workspace OS root index is not a living workboard")
    agents_text = (root / "AGENTS.md").read_text(encoding="utf-8")
    require("Markdown" in agents_text and "installed capability" in agents_text, "Workspace OS capability routing contract is missing")
    for path in root.rglob("*"):
        if not path.is_file() or "_workspace_setup_docs/personalization" in path.relative_to(root).as_posix():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        require(TOKEN_RE.search(text) is None, f"Unresolved workspace token in {path}")


def test_workspace_scaffold(output_root: Path) -> int:
    skill_root = output_root / "openai" / "workspace-os-setup" / "skills" / "workspace-os-setup"
    script_base = skill_root / "scripts" / "scaffold-workspace-os"
    require((script_base.with_suffix(".ps1") if os.name == "nt" else script_base.with_suffix(".sh")).is_file(), "Missing packaged Workspace OS scaffold script")
    checks = 0
    skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    require("Conversation mode" in skill_text and "must not claim" in skill_text, "Workspace OS conversation-mode disclosure is missing")
    checks += 1

    with tempfile.TemporaryDirectory(prefix="workspace-os-plugin-smoke-") as temp:
        sandbox = Path(temp).resolve()
        sentinel = sandbox / "outside-sentinel.txt"
        sentinel.write_text("do not modify\n", encoding="utf-8")

        hub_root = sandbox / "hub-mode"
        hub_root.mkdir()
        before_hub = tree_snapshot(sandbox)
        run_workspace_scaffold(script_base, hub_root, "Northstar Studio", "hub", "current")
        assert_workspace_output(hub_root, "workspace-hub-docs")
        new_hub_paths = set(tree_snapshot(sandbox)) - set(before_hub)
        require(all(path.startswith("hub-mode/") for path in new_hub_paths), f"Hub mode wrote outside its root: {sorted(new_hub_paths)}")
        require(sentinel.read_text(encoding="utf-8") == "do not modify\n", "Hub mode changed an outside file")
        checks += 4

        project_base = sandbox / "project-mode"
        project_base.mkdir()
        before_project = tree_snapshot(sandbox)
        run_workspace_scaffold(script_base, project_base, "Acme Launch", "project", "create")
        project_root = project_base / "acme-launch-workspace"
        assert_workspace_output(project_root, "project-docs")
        new_project_paths = set(tree_snapshot(sandbox)) - set(before_project)
        require(all(path.startswith("project-mode/acme-launch-workspace/") for path in new_project_paths), f"Project mode wrote outside its root: {sorted(new_project_paths)}")
        checks += 3

        marker_root = sandbox / "existing-marker"
        marker_root.mkdir()
        marker = marker_root / "AGENTS.md"
        marker.write_text("existing workspace marker\n", encoding="utf-8")
        before_marker = tree_snapshot(marker_root)
        run_workspace_scaffold(script_base, marker_root, "Existing Workspace", "hub", "current", expect_success=False)
        require(tree_snapshot(marker_root) == before_marker, "Existing Workspace OS marker was overwritten or partially modified")
        checks += 2

        conflict_root = sandbox / "existing-file"
        conflict_root.mkdir()
        conflict = conflict_root / "START_HERE.md"
        conflict.write_text("user-owned start file\n", encoding="utf-8")
        before_conflict = tree_snapshot(conflict_root)
        run_workspace_scaffold(script_base, conflict_root, "Conflict Workspace", "hub", "current", expect_success=False)
        require(tree_snapshot(conflict_root) == before_conflict, "Workspace collision preflight overwrote or partially modified files")
        checks += 2

    return checks


def test_pm_scaffold(output_root: Path) -> int:
    skill_root = output_root / "openai" / "pm-os-setup" / "skills" / "pm-os-setup"
    script_base = skill_root / "scripts" / "scaffold-pm-os"
    require((script_base.with_suffix(".ps1") if os.name == "nt" else script_base.with_suffix(".sh")).is_file(), "Missing packaged PM OS scaffold script")
    checks = 0
    skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    require("Conversation mode" in skill_text and "must not claim" in skill_text, "PM OS conversation-mode disclosure is missing")
    checks += 1

    with tempfile.TemporaryDirectory(prefix="pm-os-plugin-smoke-") as temp:
        sandbox = Path(temp).resolve()
        outside_sentinel = sandbox / "outside-sentinel.txt"
        outside_sentinel.write_text("do not modify\n", encoding="utf-8")

        current_root = sandbox / "current-mode"
        current_root.mkdir()
        before_current = tree_snapshot(sandbox)
        run_scaffold(script_base, current_root, "Atlas SaaS", "current")
        assert_required_workspace(current_root)
        assert_no_unresolved_tokens(current_root)
        require(outside_sentinel.read_text(encoding="utf-8") == "do not modify\n", "Scaffold wrote outside the chosen workspace")
        created_outside = set(tree_snapshot(sandbox)) - set(before_current) - {
            f"current-mode/{path.relative_to(current_root).as_posix()}" for path in current_root.rglob("*") if path.is_file()
        }
        require(not created_outside, f"Current-folder mode wrote outside its root: {sorted(created_outside)}")
        checks += 4

        create_base = sandbox / "create-mode"
        create_base.mkdir()
        before_create = tree_snapshot(sandbox)
        run_scaffold(script_base, create_base, "Product Discovery", "create")
        created_root = create_base / "product-discovery-workspace"
        assert_required_workspace(created_root)
        assert_no_unresolved_tokens(created_root)
        new_paths = set(tree_snapshot(sandbox)) - set(before_create)
        require(
            all(path.startswith("create-mode/product-discovery-workspace/") for path in new_paths),
            f"Create-folder mode wrote outside its root: {sorted(new_paths)}",
        )
        checks += 3

        marker_root = sandbox / "existing-marker"
        marker_root.mkdir()
        marker = marker_root / "AGENTS.md"
        marker.write_text("existing workspace marker\n", encoding="utf-8")
        before_marker = tree_snapshot(marker_root)
        run_scaffold(script_base, marker_root, "Existing Product", "current", expect_success=False)
        require(tree_snapshot(marker_root) == before_marker, "Existing PM OS marker was overwritten or the workspace was partially modified")
        checks += 2

        conflict_root = sandbox / "existing-file"
        conflict_root.mkdir()
        conflict = conflict_root / "START_HERE.md"
        conflict.write_text("user-owned start file\n", encoding="utf-8")
        run_scaffold(script_base, conflict_root, "Conflict Product", "current", expect_success=False)
        require(conflict.read_text(encoding="utf-8") == "user-owned start file\n", "Existing file was overwritten")
        checks += 2

    return checks


def test_reproducible_build(catalog_path: Path, plugin: str) -> int:
    dist_root = REPO_ROOT / "dist"
    dist_root.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="plugin-repro-", dir=dist_root) as temp:
        temp_root = Path(temp)
        first = temp_root / "first"
        second = temp_root / "second"
        build(catalog_path, first, [plugin], refresh_digests=False, archives=True)
        build(catalog_path, second, [plugin], refresh_digests=False, archives=True)
        first_snapshot = tree_snapshot(first)
        second_snapshot = tree_snapshot(second)
        require(first_snapshot == second_snapshot, "Repeated plugin builds produced different file lists or digests")
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin", default="pm-os-setup", choices=["pm-os-setup", "workspace-os-setup"])
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        checks = test_reproducible_build(args.catalog.resolve(), args.plugin)
        if args.plugin == "pm-os-setup":
            checks += test_pm_scaffold(args.output.resolve())
        elif args.plugin == "workspace-os-setup":
            checks += test_workspace_scaffold(args.output.resolve())
    except TestFailure as exc:
        print(f"Plugin smoke tests FAILED: {exc}", file=sys.stderr)
        return 1
    print(f"Plugin smoke tests passed ({checks} scenario checks on {sys.platform}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
