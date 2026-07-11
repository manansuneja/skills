---
name: pm-os-setup
description: "Builds and personalizes a PM workspace that gives an agent lasting product context. It organizes vision, users, meetings, decisions, outcomes, and PRDs as indexed files; adds a Chief PM and reusable product practices; and grows with the product. Use when a PM asks for a PM OS, product workspace, product memory system, or invokes pm-os-setup. Not for application code or unrelated scaffolding."
---

# PM OS Setup

## Overview

Set up a **Product Management operating system**: a plain-Markdown workspace where product context
compounds instead of disappearing into chat. The PM talks to one **Chief PM** that routes work to
specialists. Every content folder has an `INDEX.md`, and durable decisions, evidence, requirements,
and outcomes remain easy for people and future agents to find.

Keep the operating machinery reusable, but fit the working surface to the product's stage, the PM's
scope, current priorities, users, decision cadence, and recurring outputs. Personalization models
the product lifecycle and PM responsibilities, then keeps what matters, adds what is missing, and
removes generated clutter.

For tailored setup, read [references/product-profiles.md](references/product-profiles.md). Treat its
profiles as suggestion pools, not folder bundles. Explicit requirements decide immediate scope;
product and PM context provide vocabulary and high-confidence additions.

## What Gets Created

```text
INDEX.md                         agents/pm-chief.md
START_HERE.md                    agents/sub-agents/...
AGENTS.md                        _workspace_setup_docs/skills/apply-pmos-struct.md
CLAUDE.md                        _workspace_setup_docs/skills/manage-workspace-skills.md
.cursor/rules/pm-os.mdc          _workspace_setup_docs/personalization/...
product-practices/
  skills/                        summarize-notes.md brainstorm.md ...
  templates/                     meeting-summary.md outcome.md decision.md PRD templates ...
  references/
product-docs/
  product-vision.md              meetings/ outcomes/ decisions/ prds/
```

Every PM OS content folder also gets an `INDEX.md`.

## Setup Workflow

1. **Ask one short intake.** Collect the product/project and workspace name, what is being built and
   for whom, current product stage and near-term outcome, the PM's active responsibilities and
   recurring work, existing context or preferences, and whether the current folder should become the
   workspace (the default) or a new folder should be created.

2. **Choose the workspace root.** Default to the current directory and rename it in place later
   rather than nesting a new folder inside it. A folder containing `.git/`, `README.md`, or a few
   starter files can still be intentional. Create `<project-slug>-workspace/` only when the current
   directory is genuinely broad or unsafe, such as a home folder, Downloads, Desktop, a repository
   collection, or a folder with unrelated project material.

3. **Guard against clobbering.** Never overwrite an existing workspace or unrelated project files.
   Treat `AGENTS.md`, `INDEX.md`, `agents/`, `_workspace_setup_docs/`, `product-practices/`, and
   `product-docs/` as current markers. Also recognize legacy top-level `product-skills/`. If markers
   exist, ask whether the user wants an update or migration instead of scaffolding over them.

4. **Run the scaffold helper.** Prefer the bundled script over writing files manually.

   macOS/Linux:

   ```bash
   "<skill-root>/scripts/scaffold-pm-os.sh" --project-name "<project name>" --target-path "." --use-current-folder
   "<skill-root>/scripts/scaffold-pm-os.sh" --project-name "<project name>" --target-path "." --create-folder
   ```

   Windows PowerShell:

   ```powershell
   & "<skill-root>\scripts\scaffold-pm-os.ps1" -ProjectName "<project name>" -TargetPath "." -UseCurrentFolder
   & "<skill-root>\scripts\scaffold-pm-os.ps1" -ProjectName "<project name>" -TargetPath "." -CreateFolder
   ```

   Do not repeatedly try unavailable shells. On macOS/Linux, call `pwsh` only when the shell helper
   is unavailable and `command -v pwsh` succeeds.

5. **Use a manual fallback only when scripts are unavailable.** Copy the contents of
   `assets/pm-os-workspace/` into the chosen root, not the template folder itself. Fill
   `{{PROJECT_NAME}}` and `{{DATE}}` outside `_workspace_setup_docs/personalization/`; keep tokens in
   that one-time guide so it remains reusable.

6. **Apply product-context tailoring.** Follow `references/product-profiles.md`. Model the users,
   product surfaces, lifecycle/stage, active bets, evidence, decisions, recurring artifacts,
   stakeholders, and things worth tracking. Turn that model into a focused mix of folders,
   subfolders, trackers, templates, skills, and specialists. Begin with product vision, meetings,
   outcomes, decisions, PRDs, and the small PM skill core—summarizing, brainstorming, synthesizing
   outcomes, documenting product context, and writing PRDs. Add, adapt, or remove the rest in
   lockstep with actual scope. Less is more. Update indexes and Chief PM routing.

7. **Show the result with a human-first map.** Point the user to:

   - `START_HERE.md` — the human welcome guide.
   - `product-docs/` — the primary product working surface.
   - `product-practices/` — skills, templates, and references controlling how work is done.
   - `INDEX.md` — the complete map.
   - `_workspace_setup_docs/personalization/` — agent-managed one-time setup.

   Explain that `agents/`, `_workspace_setup_docs/`, `AGENTS.md`, `CLAUDE.md`, and `.cursor/` are
   agent-facing machinery. Tell the PM they can ask the agent to add a folder, subfolder, tracker,
   workflow, output format, or specialist later. If they add one manually, the next agent should
   integrate it automatically.

8. **Offer personalization.** If the user says yes, read
   `_workspace_setup_docs/personalization/AGENTS.md`. Personalization must reconcile the structure,
   not merely add to it. It may remove clearly irrelevant generated-empty folders, skills,
   templates, specialists, and routes. It must ask once before deleting or relocating user-authored
   content.

9. **Handle root-folder renaming safely.** During personalization, rename the root folder to match
   the workspace name by default. Perform one same-parent rename as the final filesystem operation
   after all content edits and checks. Never create a destination root and move files into it. Skip
   the rename and ask first only if the destination exists or the root contains unrelated material.
   Report the old and new paths and note that the editor may need to reopen the folder.

## Conventions To Preserve

- One front door: the user talks to the Chief PM; it delegates.
- Keep the human surface small: `START_HERE.md`, `product-docs/`, and optionally
  `product-practices/`.
- Mark agent-facing files and indexes clearly near the top.
- Keep a current `INDEX.md` in every PM OS content folder.
- Whenever an agent reads `AGENTS.md`, perform lightweight structural reconciliation: preserve and
  integrate unindexed user-created folders, subfolders, and files; add missing maps and clear
  routing; ask only when meaning or placement is genuinely ambiguous.
- Fit the product stage and PM scope. Do not scaffold every possible PM lane.
- Put synthesis, recommendations, prioritization, MVP cuts, and next steps in
  `product-docs/outcomes/`, not only chat.
- Keep reusable instructions, formats, and examples together under `product-practices/` as
  `skills/`, `templates/`, and `references/`.
- Determine whether guidance is task-local or a durable operating preference from its meaning and
  scope, not trigger phrases. When a request contains both work to produce and a reusable
  convention, complete the work and update the relevant existing skill/template/reference in the
  same task.
- Keep the default library minimal. Add or update a skill for a durable preference or recurring
  workflow; add a specialist only when a distinct recurring role is useful. Synchronize them with
  content areas and Chief PM routing.
- Never overwrite raw input. Preserve it under an artifact-local `raw/` folder and create clean
  summaries and artifacts separately.

## Notes

- This skill scaffolds and optionally personalizes a PM workspace. It does not build application
  code.
- The Chief PM is the default workspace persona. In most tools, the PM simply talks in the workspace.
- Tool wiring stays minimal. `CLAUDE.md` points to `AGENTS.md`, and Cursor gets one always-on rule.
  Generate `.claude/agents/` or `.github/agents/*.agent.md` only when the PM asks.
