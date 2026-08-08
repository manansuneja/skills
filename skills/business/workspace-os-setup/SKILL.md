---
name: workspace-os-setup
description: "Builds and personalizes a plain-file workspace that gives an agent lasting context about a business, studio, team, practice, or client project. It adds a Workspace Chief, organized documents, indexes, and reusable ways of working, then adapts the structure to the user's needs. Use for a Workspace OS, business or studio workspace, project memory, knowledge base, or requests to run workspace-os-setup. Not for application code or unrelated scaffolding."
---

# Workspace OS Setup

## Overview

Set up a **Workspace OS**: a plain-Markdown workspace where context compounds instead of disappearing
into chat. The user talks to one **Workspace Chief** that routes work to workspace practices and
compatible installed capabilities. The root `INDEX.md` is a living, human-first dashboard;
meaningful content areas use local indexes so durable context stays easy for people and future
agents to find.

The operating machinery stays generic, but the working surface should become specific to the user's
category and requirements. Personalization models the domain's entities, lifecycle, recurring work,
terminology, and things to track; then it keeps what matters, adds what is missing, and removes
generated clutter.

## Workspace Shapes

Choose one content root:

- **Workspace hub:** `workspace-hub-docs/` for an ongoing studio, business, team, personal knowledge
  system, research practice, or other standing workspace.
- **Client project:** `project-docs/` for one engagement or bounded initiative that should live
  separately from a broader hub.

For a tailored setup, read [references/workspace-profiles.md](references/workspace-profiles.md). Use
category knowledge to get close to how the work actually operates, while using stated requirements to
decide what belongs now. Prefer domain language and useful nested structure over a lowest-common-
denominator folder tree.

## What Gets Created

```text
INDEX.md                         agents/workspace-chief.md
START_HERE.md                    agents/sub-agents/...
AGENTS.md                        _workspace_setup_docs/skills/apply-workspace-struct.md
CLAUDE.md                        _workspace_setup_docs/skills/manage-workspace-skills.md
.cursor/rules/workspace-os.mdc   _workspace_setup_docs/personalization/...
workspace-best-practices/
  skills/                        summarize-notes.md brainstorm.md ...
  templates/                     meeting-summary.md outcome.md decision.md
  references/
workspace-hub-docs/ or project-docs/
  workspace-profile.md           meetings/ outcomes/ decisions/
```

The root and each meaningful content domain get an `INDEX.md`. Tiny leaf folders can be represented
by their nearest parent index instead of carrying duplicate maps.

## Operating Modes

- **Workspace mode:** When the agent has a user-selected writable workspace root, follow the full
  setup workflow below and create the durable Markdown workspace.
- **Conversation mode:** When the client has no writable workspace root, including many mobile or
  web conversations, say so before setup. Workspace OS can still guide the work and maintain a
  compact Markdown `Workspace OS Index` in the conversation, but it must not claim that it created
  a persistent folder tree, a ChatGPT Project, or files that the client cannot actually access.
  Keep the index to current work, waiting items, recent decisions, and links or names for artifacts
  created in the conversation. Default artifacts to Markdown. Offer to provide supported
  downloadable Markdown files or a starter pack, or to continue the full setup later in a
  file-capable environment.

Conversation mode is a useful working surface, not a silent substitute for the durable workspace.
If a compatible installed capability can save an artifact to a destination the user already
controls, use it only when requested or clearly appropriate and confirm the destination when it is
ambiguous. Do not install, connect, or imply access to another capability automatically.

## Setup Workflow

1. **Ask one short intake.** Collect the workspace name, hub or project shape, category/context,
   objective, primary uses, and whether the current folder should become the workspace (the default)
   or a new folder should be created instead.

2. **Choose the workspace root.** Default to the current directory and rename it in place later (step
   9) rather than nesting a new folder inside it. This matters most when an editor (Cursor, Claude
   Code, VS Code, or similar) already has the current directory open as its project root: a nested
   `<workspace-slug>-workspace/` subfolder sits outside what the editor is showing, so the user has to
   manually close and reopen the new folder before anything looks right. A folder that is merely not
   perfectly empty—containing a `.git/`, a `README.md`, or a couple of starter files—is still safe to
   use directly. Only create `<workspace-slug>-workspace/` when the current directory is genuinely
   unsafe to use directly: a home folder, Downloads, Desktop, a collection of unrelated repositories,
   or a folder that already holds unrelated project files that should not mix with the workspace.

3. **Guard against clobbering.** Never overwrite an existing workspace or unrelated project files.
   Treat `AGENTS.md`, `INDEX.md`, `agents/`, `_workspace_setup_docs/`,
   `workspace-best-practices/`, `workspace-hub-docs/`, and `project-docs/` as current markers. Also
   recognize legacy top-level `workspace-skills/` and `business-*` folders. If markers exist, ask
   read `_workspace_setup_docs/workspace-state.json` when present and ask whether the user wants an
   update or migration instead of scaffolding over them. A newer setup skill never silently migrates
   an existing workspace.

4. **Run the scaffold helper.** Prefer the bundled script over writing files manually.

   macOS/Linux:

   ```bash
   "<skill-root>/scripts/scaffold-workspace-os.sh" \
     --workspace-name "<workspace or project name>" \
     --workspace-kind hub \
     --workspace-category "<category or context>" \
     --objective "<objective>" \
     --primary-use "<primary uses>" \
     --target-path "." \
     --use-current-folder
   ```

   Use `--workspace-kind project` for a client-project workspace and `--create-folder` when creating
   a new root. Legacy `--business-name`, `--project-name`, and `--business-category` flags remain
   accepted as aliases.

   Windows PowerShell:

   ```powershell
   & "<skill-root>\scripts\scaffold-workspace-os.ps1" `
     -WorkspaceName "<workspace or project name>" `
     -WorkspaceKind hub `
     -WorkspaceCategory "<category or context>" `
     -Objective "<objective>" `
     -PrimaryUse "<primary uses>" `
     -TargetPath "." `
     -UseCurrentFolder
   ```

5. **Use a manual fallback only when scripts are unavailable.** Copy the contents of
   `assets/workspace-os-workspace/` into the chosen root. For a client project, map
   `workspace-hub-docs/` to `project-docs/`. Fill `{{WORKSPACE_NAME}}`, `{{WORKSPACE_KIND}}`,
   `{{DOCS_ROOT}}`, `{{WORKSPACE_CATEGORY}}`, `{{OBJECTIVE}}`, `{{PRIMARY_USE}}`, and `{{DATE}}`.

6. **Apply category-and-requirement tailoring.** Follow `references/workspace-profiles.md`. Model the
   category's core entities, lifecycle stages, recurring artifacts, relationships, terminology, and
   tracking needs. Turn that model into a focused mix of folders, subfolders, trackers, templates,
   skills, and specialists. Start from the common skill core—summarizing notes, brainstorming,
   synthesizing outcomes, and documenting context—then add, adapt, or remove skills and sub-agents in
   lockstep with the content structure. Less is more. Update indexes and routing.

   Keep ordinary workspace artifacts Markdown-first. Use an available document, presentation,
   spreadsheet, design, research, or other installed capability only when the user explicitly asks
   for that format/capability or the context clearly requires it. If the format choice would
   materially change usability and intent remains unclear, ask one concise question. Do not install
   or connect another capability automatically.

7. **Show the result with a human-first map.** Point the user to:

   - `START_HERE.md` — the human welcome guide.
   - `workspace-hub-docs/` or `project-docs/` — their primary working surface.
   - `workspace-best-practices/` — skills, templates, and references that control how work is done.
   - `INDEX.md` — the living workboard and high-level map.
   - `_workspace_setup_docs/personalization/` — agent-managed one-time setup.

   Explain that `agents/`, `_workspace_setup_docs/`, `AGENTS.md`, `CLAUDE.md`, and `.cursor/` are
   agent-facing machinery. `workspace-best-practices/` is a user-accessible customization center;
   the user supplies intention/examples and asks the agent to manage its files.
   Tell the user they can ask the agent to add any folder, subfolder, tracker, or workflow later. If
   they create one manually, the next agent should detect and integrate it automatically.

8. **Offer personalization.** If the user says yes, read the generated
   `_workspace_setup_docs/personalization/AGENTS.md` and follow it. Personalization must reconcile the
   structure, not merely add to it. It may remove clearly irrelevant generated-empty folders; it
   must ask once before deleting or relocating any folder containing user-authored content.

9. **Handle root-folder renaming safely.** During personalization, rename the root folder to match the
   chosen workspace name by default—this does not need a separate yes/no question. Perform one
   same-parent directory rename as the final filesystem operation after all content edits and checks.
   Do not create a destination folder and move files into it. Skip the rename and ask first only if
   the destination already exists or the root contains unrelated material. Report the old and new
   paths and note that the editor may need to reopen the folder.

## Conventions To Preserve

- One front door: the user talks to the Workspace Chief; it delegates.
- Keep the human surface small and obvious: `START_HERE.md`, the docs root, and optionally
  `workspace-best-practices/`.
- Mark agent-facing files clearly near the top; keep content indexes human-readable.
- Keep the root `INDEX.md` as a concise workboard plus navigation. Use local indexes for meaningful
  content domains, substantial subdomains, and multi-file artifacts—not automatically for every tiny
  leaf folder.
- Whenever an agent reads `AGENTS.md`, perform a lightweight structural reconciliation: detect
  unindexed user-created folders, subfolders, and files in user-owned areas; preserve them, infer
  their purpose, add missing indexes/maps, and connect relevant routing. Ask only when placement or
  meaning is genuinely ambiguous.
- Use `lower-kebab-case` names. Use Markdown for narrative work and structured formats when work
  becomes data.
- Put synthesis, recommendations, prioritization, and next steps in `outcomes/`, not only chat.
- Keep reusable instructions, exact formats, and examples together under `workspace-best-practices/`
  as `skills/`, `templates/`, and `references/`.
- Determine whether guidance is task-local or a durable operating preference from its meaning and
  scope, not trigger phrases. When a request contains both work to produce and a reusable
  convention, complete the work and update the relevant existing skill/template/reference in the
  same task.
- Keep the default library minimal. Add or update a skill for a durable preference or recurring
  workflow; add a sub-agent only when a distinct recurring role is useful. Synchronize them whenever
  content folders or requirements change.
- Never overwrite raw input. Preserve it under an artifact-local `raw/` folder and write clean
  summaries separately.
- Route specialized work through compatible installed skills or tools when useful, while keeping
  Workspace OS as the organizer. Default narrative work to Markdown; create heavier or binary
  formats only on explicit request or clear contextual need. Store generated deliverables with their
  source/context in the appropriate content area and update the nearest index.

## Notes

- This skill scaffolds and optionally personalizes a workspace. It does not build app code.
- Tool wiring stays minimal. `CLAUDE.md` points to `AGENTS.md`, and Cursor gets one always-on rule.
  Only generate `.claude/agents/` or `.github/agents/*.agent.md` when the user asks.
- `_workspace_setup_docs/workspace-state.json` records the setup version and workspace schema. Treat
  plugin/skill updates and workspace migrations as separate operations.
