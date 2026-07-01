# Setup Agent Guide — Personalize This Workspace OS

> **Agent-facing:** This is the one-time apply guide for the agent. The user should answer the intake,
> then stay focused on `{{DOCS_ROOT}}/` rather than editing this file.

Turn this generic Workspace OS into a focused workspace that feels native to the owner's category and
requirements. The operating machinery remains reusable; the content structure, terminology,
trackers, skills, and routes should fit the actual work. This is a context intake and structure
reconciliation, not a filesystem tour.

Use the machinery vs content-layer boundary in [../../AGENTS.md](../../AGENTS.md). Workspace OS
machinery stays in the background; content files describe the user's real business, studio, project,
research, knowledge, or other work.

When setup is complete, delete `_workspace_setup_docs/personalization/` as the final content cleanup.
Its absence tells future sessions that personalization is complete. Durable behavior belongs in
`AGENTS.md`, `agents/`, `_workspace_setup_docs/`, `workspace-best-practices/`, and `{{DOCS_ROOT}}/`.

## Setup goals

By the end, the workspace should have:

- A concise `{{DOCS_ROOT}}/workspace-profile.md` grounded in the user's real work.
- A category-appropriate information architecture using the owner's vocabulary.
- A small, relevant set of top-level folders plus useful subfolders and trackers under
  `{{DOCS_ROOT}}/`.
- No clearly irrelevant generated-empty content folders.
- A customized Workspace Chief and only useful specialist routes.
- A minimal `workspace-best-practices/` library whose skills and templates match the kept content
  areas, recurring workflows, and stated output preferences.
- Current `INDEX.md` files and healthy links.
- A root-folder rename to match the workspace name, completed safely by default.
- No unnecessary tool-adapter clutter.

## Step 1 — Ask one lightweight intake

Ask these four questions in one friendly message. Rough notes, links, file paths, or “skip for now”
are all fine.

1. What should this workspace be called? I'll rename the root folder to match at the very end (give
   an exact folder name if you want one; otherwise I'll use `<workspace-slug>-workspace`)—say so now
   if you'd rather keep the current folder name. Mention that the editor may need to reopen the
   renamed folder.
2. What category or kind of work is this, who is it for, and what should the workspace keep in mind?
3. What three to five kinds of work should be easiest right now? What core things, stages, or status
   should it track—for example clients, projects, rooms, sources, campaigns, drafts, approvals,
   budgets, or deliverables? Is there anything the owner explicitly does not want represented?
4. What is the next useful outcome, and what existing files, links, decisions, examples, constraints,
   formats, or writing style should be used?

Do not ask separately about every artifact type. Preferences can emerge from real examples and become
skills over time. Detect the host tool when possible; ask only if tool-specific wiring is requested.
If the answers are thin, ask at most one follow-up round.

## Step 2 — Build a reconciliation plan

Work from the workspace root. Read the root and docs-root indexes, then inspect the actual folders
under `{{DOCS_ROOT}}/`. First build a compact domain model:

- Core entities and relationships.
- Lifecycle stages or recurring sequences.
- Repeated artifacts and decisions.
- Status, dates, owners, costs, evidence, dependencies, or next actions worth tracking.
- The owner's natural terminology.

Translate that model into folders, subfolders, structured trackers, templates, skills, and agent
routes. Before placing anything, decide which layer it belongs in: `{{DOCS_ROOT}}/` holds the work
itself—notes, planning, research, and current state; `workspace-best-practices/` holds anything
reusable across many future pieces of work, such as a voice/tone guide, brand examples, or a recurring
format. A folder name that shows up in a profile's candidate list (for example a voice-and-style
folder for a content/marketing workspace) does not automatically belong in `{{DOCS_ROOT}}/`—if it will
be referenced repeatedly rather than updated as new work happens, it belongs in
`workspace-best-practices/references/` instead. Build three synchronized plans: content structure,
best practices, and agents. For each use the same four sets:

- **Keep:** supports an explicit current/near-term use, contains user-authored material, or is a
  necessary cross-cutting area.
- **Add:** needed now or soon and has a purpose distinct from existing folders.
- **Remove:** clearly irrelevant generated folders containing no artifact beyond their unchanged
  starter `INDEX.md`.
- **Ask:** relevance is uncertain, or the folder contains user-authored files, raw input, custom
  links/index content, or nested artifacts.

Use the installed `workspace-os-setup/references/workspace-profiles.md` reference when the host makes
it available. Requirements decide immediate scope; category knowledge supplies appropriate domain
structure, terminology, and high-confidence missing pieces. Aim for a close fit, not a generic
lowest-common-denominator tree, but do not union every industry suggestion. An interior-design studio
focused on knowledge, brainstorming, and writing does not need `vendors/` merely because vendors are
common in interior design.

Remove clearly irrelevant generated-empty folders without a second question and report them later.
For all **Ask** items, send one consolidated confirmation listing the exact proposed action. Never
delete or relocate user-authored content from inference alone. If the owner does not answer, keep it.

If a removed content area has generated skills, specialists, routes, templates, or index rows that
serve only that area, include those in the same reconciliation. Do not leave orphaned routes.

Begin with the common skill core: summarize notes, brainstorm, synthesize outcomes, and document
context. Remove even a common skill/sub-agent when it clearly does not fit the scope. Determine
semantically whether guidance is durable, then add a category-specific skill for a reusable
preference or recurring workflow; add a specialist only when a distinct recurring route is valuable.

## Step 3 — Apply the context and structure

1. If this is a legacy scaffold, normalize in place: rename `business-hub-docs/` to
   `workspace-hub-docs/` and `business-practices/` to `workspace-best-practices/`; then move a legacy
   `business-skills/` or top-level `workspace-skills/` directory to
   `workspace-best-practices/skills/`. Rename `business-profile.md` to `workspace-profile.md`.
   Preserve contents, update links, and never create a replacement root and copy files into it.
2. Replace any unresolved workspace-name, workspace-category, objective, and primary-use template
   tokens outside this personalization folder when answers are known.
3. Apply the keep/add/remove/confirmed-ask plan. Use category language and useful nested structure.
   Give each new content folder an `INDEX.md` with a clear purpose. Use a table, CSV, JSON, or sheet
   when the user needs to track repeated fields or status. Remove stale index rows and links.
4. Update `START_HERE.md` with a short workspace-specific introduction if useful.
5. Update `{{DOCS_ROOT}}/workspace-profile.md` with the purpose, category, audience, focus, domain
   model, things to track, current outcome, and known constraints. Do not describe the Workspace
   Chief as the user's work.
6. Customize `agents/workspace-chief.md`. Adjust its persona, routing emphasis, standing rules, and
   context-gathering behavior around the owner and the kept content areas.
7. Apply the best-practice and agent plans with the content plan. Create or update skills/templates
   when outputs need repeatable judgment, structure, or format. Remove unused generic skills and
   specialists. Add a specialist only for a distinct recurring role. Keep routes, indexes, and files
   synchronized.
8. Apply `_workspace_setup_docs/skills/apply-workspace-struct.md`: verify folder names, audience
   labels, indexes, links, and profile references.

Do not create `.claude/agents/` or `.github/agents/` during basic setup unless the owner explicitly
asks. Cursor is already wired through `.cursor/rules/workspace-os.mdc`.

## Step 4 — Validate, summarize, and clean up

Check that the workspace name, purpose/audience, active focus areas, next outcome, and requested source
material are captured. Search for stale paths, missing targets, orphaned routes, and unresolved
template tokens.

Prepare a concise handoff covering:

- The updated workspace profile and focus areas.
- How the folder/subfolder structure and trackers fit the category and requirements.
- Folders kept, added, removed, or deliberately retained.
- Skills, templates, references, or agents changed—and which outputs they now control.
- The final root path, or why it stayed unchanged.

If personalization is complete, delete `_workspace_setup_docs/personalization/` and remove its row
from `_workspace_setup_docs/INDEX.md`. Keep the root `START_HERE.md`. If required context is missing,
leave personalization in place and ask only the smallest necessary follow-up.

## Step 5 — Rename the root last

Do this by default as the final step of personalization—no separate confirmation question is needed.
Skip it only if the owner said during intake (or later) that they want to keep the current folder
name.

1. Compute the exact sibling destination. Use the owner's exact folder name when supplied; otherwise
   use `<workspace-slug>-workspace` in `lower-kebab-case`.
2. Confirm the destination does not exist, the parent is writable, and this root is the intended
   Workspace OS root rather than a broad folder containing unrelated projects. If unrelated material
   exists, ask before renaming the root.
3. Finish every content edit, validation, personalization-folder deletion, and summary preparation
   before the rename.
4. Rename the directory itself from its parent as one move (`mv -- old new` on macOS/Linux or
   `Move-Item -LiteralPath old -Destination new` on PowerShell). **Do not** `mkdir` a new root and move
   or copy the contents into it.
5. Make the rename the final filesystem operation. Report both old and new absolute paths and tell
   the owner their editor may need to reopen the new folder.

If any safety check fails, leave the root unchanged and report the exact blocker. Content
personalization may still be complete.
