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
```

`scripts/validate-catalog.ps1` is the required metadata gate and must pass before publishing. CI
runs it for every pull request and push that changes catalog files.

The public catalog should currently expose `workflow-create`, `pm-os-setup`, and
`workspace-os-setup`.
