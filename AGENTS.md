# Agent Guide

This repo is the public `manansuneja/skills` catalog.

## Catalog Rules

- Public skills live under `skills/<category>/<skill-name>/`.
- Every public skill must have a `SKILL.md` whose frontmatter `name` exactly matches the folder name.
- Every public skill's frontmatter `description` must be non-empty, explain what the skill does and
  when to use it, and contain no more than 1,024 characters (the Agent Skills specification limit).
- Every public skill must be listed in:
  - the root `README.md`
  - its category `README.md`
  - `.claude-plugin/plugin.json`
  - `skills.sh.json`
- Every public skill README must include the exact install command and a bottom section named `What This Skill Does And How To Use It`.
- Keep local plans, tests, announcements, screenshots, and unpublished skills outside the public commit.
- Do not add `.out-of-scope` until public issue traffic creates repeat rejected requests worth documenting.

## Plugin Release Rules

- `skills/` is the only canonical runtime source. Never hand-edit or commit a copied skill under
  `plugins/` or `dist/`.
- `plugins/catalog.json` is the release source of truth for plugin versions, status, canonical source
  paths, and source digests. A canonical skill change requires an intentional plugin version bump and
  refreshed digest.
- `plugins/<name>/` contains only store listing metadata, evaluation cases, release notes, and assets.
- `dist/plugins/` is generated, ignored, disposable output. It contains the self-contained copies
  required by plugin clients and release archives.
- Keep v1 packages skills-only. Do not add apps, MCP servers, hooks, authentication, or telemetry
  without a separately reviewed product and privacy change.
- Only `pm-os-setup` is listed in the local marketplace during the pilot. Follow-on plugin metadata
  does not imply public availability.

## Current Categories

- `skills/agent-workflows/` for workflow and meta-skill tooling.
- `skills/product-management/` for PM operating systems, product memory, and product-builder workflows.
- `skills/business/` for focused workspaces, studios, small businesses, knowledge systems,
  client-project memory, operations, and reusable owner workflows.

## Verification

From the repo root, run:

```bash
npx skills@latest add ./ --list
powershell -ExecutionPolicy Bypass -File scripts/list-skills.ps1
powershell -ExecutionPolicy Bypass -File scripts/validate-catalog.ps1
python scripts/build_plugins.py
python scripts/validate_plugins.py
python scripts/test_plugins.py --plugin pm-os-setup
python scripts/test_plugins.py --plugin workspace-os-setup
```

`scripts/validate-catalog.ps1` is the required metadata gate and must pass before publishing. CI
runs it for every pull request and push that changes catalog files.

Plugin CI runs the build, manifest/package validation, reproducibility check, and PM OS scaffold smoke
tests on Windows and Ubuntu. Use `python scripts/build_plugins.py --refresh-digests` only after a
canonical change and version bump; commit the reviewed catalog digest, never `dist/`.

The public catalog should currently expose `workflow-create`, `pm-os-setup`, and
`workspace-os-setup`.

## OS Family Alignment

`workspace-os-setup` and `pm-os-setup` are separate, standalone public skills, but they share a
behavioral contract. Before changing either one, read
[`internal/os-alignment/ALIGNMENT.md`](internal/os-alignment/ALIGNMENT.md). Apply shared behavior
changes to both skills in the same change unless the contract records an intentional domain
difference.

Run the alignment gate before publishing:

```bash
python3 internal/os-alignment/check-alignment.py
```

Do not introduce runtime links or dependencies between the two skill folders. Each skill must remain
independently installable from GitHub.
