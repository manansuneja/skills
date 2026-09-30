---
name: pm-os-setup
description: "Builds and personalizes a PM workspace that gives an agent lasting product context. It organizes vision, projects, meetings, decisions, outcomes, PRDs, and build briefs as indexed files; adds a Chief PM, specialists for project status and build handoff, and reusable product practices; serves PMs and PM-builders who work with coding agents; and grows with the product. Use when a PM asks for a PM OS, product workspace, product memory system, or invokes pm-os-setup. Not for application code or unrelated scaffolding."
---

# PM OS

## Overview

Set up a **Product Management operating system**: a plain-Markdown workspace where product context
compounds instead of disappearing into chat. The PM talks to one **Chief PM** that routes work to
workspace practices and compatible installed capabilities. The root `INDEX.md` is a living,
human-first dashboard; meaningful content areas use local indexes so durable decisions, evidence,
requirements, and outcomes remain easy for people and future agents to find.

The workspace is **hybrid**: active work lives in one folder per initiative under
`product-docs/projects/`, each with a brief, a status log, requirements, and a build brief, while
product-wide knowledge (vision, shared meetings, outcomes, and the decisions log) stays in global
folders. It serves two kinds of PM: one who hands specs to an engineering team, and a **PM-builder**
who also builds prototypes and features with coding agents. The PM profile in `AGENTS.md` records
which; application code always stays in the PM's own repository.

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
  product-vision.md              meetings/ outcomes/ decisions/
  projects/                      INDEX.md (portfolio) and <project>/ brief, status, prd, build-brief
```

The root and each meaningful content domain get an `INDEX.md`. Tiny leaf folders can be represented
by their nearest parent index instead of carrying duplicate maps.

## Operating Modes

- **Workspace mode:** When the agent has a user-selected writable workspace root, follow the full
  setup workflow below and create the durable Markdown workspace.
- **Conversation mode:** When the client has no writable workspace root, including many mobile or
  web conversations, say so before setup. PM OS can still guide product work and maintain a compact
  Markdown `PM OS Index` in the conversation, but it must not claim that it created a persistent
  folder tree, a ChatGPT Project, or files that the client cannot actually access. Keep the index to
  current work, waiting items, recent decisions, and links or names for artifacts created in the
  conversation. Default artifacts to Markdown. Offer to provide supported downloadable Markdown
  files or a starter pack, or to continue the full setup later in a file-capable environment.

Conversation mode is a useful working surface, not a silent substitute for the durable workspace.
If a compatible installed capability can save an artifact to a destination the user already
controls, use it only when requested or clearly appropriate and confirm the destination when it is
ambiguous. Do not install, connect, or imply access to another capability automatically.

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
   exist, read `_workspace_setup_docs/workspace-state.json` when present and ask whether the user
   wants an update or migration instead of scaffolding over them. A newer setup skill never silently
   migrates an existing workspace. Schema-1 workspaces keep a flat `product-docs/prds/` and continue
   to work; adopting `projects/` is an explicit, separate migration the PM asks for.

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
   subfolders, trackers, templates, skills, and specialists. Begin with product vision, projects,
   meetings, outcomes, decisions, and the small PM skill core—summarizing, brainstorming,
   synthesizing outcomes, documenting product context, running projects, writing PRDs, and writing
   build briefs. Add, adapt, or remove the rest in lockstep with actual scope. Less is more. Update indexes and Chief PM routing.

   Keep ordinary PM artifacts Markdown-first. A request such as “create a PRD” produces `.md` by
   default. Use an available document, presentation, spreadsheet, design, research, or other
   installed capability only when the user explicitly asks for that format/capability or the context
   clearly requires it. If the format choice would materially change usability and intent remains
   unclear, ask one concise question. Do not install or connect another capability automatically.

7. **Show the result with a human-first map.** Point the user to:

   - `START_HERE.md` — the human welcome guide.
   - `product-docs/` — the primary product working surface, with `projects/` for active work.
   - `product-practices/` — skills, templates, and references controlling how work is done.
   - `INDEX.md` — the living workboard and high-level map.
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
- Mark agent-facing files clearly near the top; keep content indexes human-readable.
- Keep the root `INDEX.md` as a concise workboard plus navigation. Use local indexes for meaningful
  content domains, substantial subdomains, and multi-file artifacts—not automatically for every tiny
  leaf folder.
- Whenever an agent reads `AGENTS.md`, perform lightweight structural reconciliation: preserve and
  integrate unindexed user-created folders, subfolders, and files; add missing maps and clear
  routing; ask only when meaning or placement is genuinely ambiguous.
- Fit the product stage and PM scope. Do not scaffold every possible PM lane.
- Put synthesis, recommendations, prioritization, MVP cuts, and next steps in
  `product-docs/outcomes/` (or the project's `outcomes/` folder when they concern one project), not
  only chat.
- File by scope. Work that belongs to one initiative lives inside its project; product-wide work
  stays in the global folders; every decision also gets a row in the global decisions log.
- Record each project's stage and health in its `status.md` and mirror them in the portfolio table.
  Stage is a fact, not a gate. The Chief leads with Think (discover, define) or Build (build, launch,
  learn) from that stage.
- Ask how the PM works during personalization and set the PM profile in `AGENTS.md` to `pm` or
  `pm-builder`. Application code never lives in the workspace; link the repository from `brief.md`.
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
- Route specialized work through compatible installed skills or tools when useful, while keeping PM
  OS as the organizer. Default narrative work to Markdown; create heavier or binary formats only on
  explicit request or clear contextual need. Store generated deliverables with their source/context
  in the appropriate product area and update the nearest index.

## Notes

- This skill scaffolds and optionally personalizes a PM workspace. It does not build application
  code. The Builder specialist prepares briefs and prompts and checks results for coding agents;
  the code itself lives in the PM's repository.
- The Chief PM is the default workspace persona. In most tools, the PM simply talks in the workspace.
- Tool wiring stays minimal. `CLAUDE.md` points to `AGENTS.md`, and Cursor gets one always-on rule.
  Generate `.claude/agents/` or `.github/agents/*.agent.md` only when the PM asks.
- `_workspace_setup_docs/workspace-state.json` records the setup version and workspace schema. Treat
  plugin/skill updates and workspace migrations as separate operations.
