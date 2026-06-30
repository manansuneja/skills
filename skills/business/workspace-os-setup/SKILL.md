---
name: workspace-os-setup
description: "Scaffold a Workspace OS for a small business, solo business owner, agency, studio, service business, or client project: a Markdown workspace with durable memory, a Workspace Chief coordinator, specialist sub-agents, business-skills, business-practices, protected setup docs, automatic INDEX.md maps, and either a business-hub-docs tree or project-docs tree. Use when someone wants to set up a business workspace, business operating system, small-business agent workspace, client/project workspace, interior design workspace, operations workspace, client-management workspace, knowledge workspace, or asks to run workspace-os-setup / Workspace OS Setup. Not for building application code or unrelated file scaffolds."
---

# Workspace OS Setup

## Overview

Set up a **Workspace OS**: a plain-Markdown operating system for a business or client project where
context compounds instead of disappearing into chat. The user talks to one **Workspace Chief** agent
that routes work to specialists, every content folder has an `INDEX.md`, and the workspace keeps
business context, client work, decisions, notes, offers, operations, and reusable working style easy
for future agents to find.

The base scaffold is intentionally generic. The setup skill asks a few business-oriented questions,
runs the deterministic scaffold helper, then offers a personalization handoff through
`_workspace_setup_docs/personalization/`.

## Workspace Shapes

Choose one docs root:

- **Business hub:** `business-hub-docs/` for a standing business workspace, such as an interior design
  studio, consulting practice, ecommerce shop, local service business, or agency.
- **Client project:** `project-docs/` for one client engagement, business initiative, or bounded
  project that should live separately from the broader business hub.

When the user wants a tailored setup, read [references/workspace-profiles.md](references/workspace-profiles.md)
and use only the relevant profile guidance. Keep `SKILL.md` lean; the reference explains how to bias
folders, skills, and specialists for client management, brainstorming/offers, knowledge/study,
operations, project delivery, and general business use.

## What Gets Created

```
INDEX.md                         agents/workspace-chief.md
START_HERE.md                    agents/sub-agents/...
AGENTS.md                        _workspace_setup_docs/skills/apply-workspace-struct.md
CLAUDE.md                        _workspace_setup_docs/skills/manage-workspace-skills.md
.cursor/rules/workspace-os.mdc   _workspace_setup_docs/personalization/...
business-skills/START_HERE.md    business-skills/summarize-notes.md
business-skills/brainstorm.md    business-skills/offer-brief.md
business-skills/metrics-review.md business-skills/business-planning.md
business-practices/templates/    business-practices/references/
business-hub-docs/ or project-docs/
  business-profile.md            meetings/ outcomes/ offers/ decisions/
  brand-and-delivery/ metrics/ plans/ client-comms/
```

Plus an `INDEX.md` in every Workspace OS content folder.

## Setup Workflow

1. **Ask a short intake.** Keep this to one message; deeper personalization happens later.
   - Business, client, or project name.
   - Workspace kind: business hub or client project.
   - Business category and objective, if not already clear.
   - Primary use: client management, brainstorming/offers, knowledge/study, operations, project
     delivery, or general.
   - Current folder or new workspace folder.

2. **Choose the workspace root.** Prefer the current directory when it looks intentionally chosen:
   empty, nearly empty, or already named like the business/project. Create a new
   `<business-slug>-workspace/` folder when the current directory is broad or unsafe, such as a home
   folder, downloads folder, desktop, repo collection, or cluttered parent directory.

3. **Guard against clobbering.** Never overwrite an existing workspace or unrelated project files.
   If the target already contains `AGENTS.md`, `INDEX.md`, `agents/`, `_workspace_setup_docs/`,
   `business-skills/`, `business-hub-docs/`, or `project-docs/`, stop and ask whether to update the
   existing Workspace OS instead.

4. **Run the scaffold helper.** Prefer the bundled script over writing files manually.

   macOS/Linux:

   ```bash
   "<skill-root>/scripts/scaffold-workspace-os.sh" \
     --business-name "<business or project name>" \
     --workspace-kind business \
     --business-category "<category>" \
     --objective "<objective>" \
     --primary-use "<primary use>" \
     --target-path "." \
     --use-current-folder
   ```

   Use `--workspace-kind project` for a client-project workspace, and `--create-folder` when creating
   a new folder. `--project-name` is accepted as an alias for `--business-name`.

   Windows PowerShell:

   ```powershell
   & "<skill-root>\scripts\scaffold-workspace-os.ps1" `
     -BusinessName "<business or project name>" `
     -WorkspaceKind business `
     -BusinessCategory "<category>" `
     -Objective "<objective>" `
     -PrimaryUse "<primary use>" `
     -TargetPath "." `
     -UseCurrentFolder
   ```

5. **Manual fallback only if scripts are unavailable.** Copy the contents of
   `assets/workspace-os-workspace/` into the chosen workspace root, not the template folder itself.
   For a client-project workspace, rename `business-hub-docs/` to `project-docs/`. Fill these tokens
   in text files:
   - `{{BUSINESS_NAME}}`
   - `{{WORKSPACE_KIND}}`
   - `{{DOCS_ROOT}}`
   - `{{BUSINESS_CATEGORY}}`
   - `{{OBJECTIVE}}`
   - `{{PRIMARY_USE}}`
   - `{{DATE}}`

6. **Apply light profile tailoring when useful.** If the user gave a primary use, read
   `references/workspace-profiles.md` and make small first-pass changes: create any obviously needed
   folders with `INDEX.md`, add starter skills only when the profile calls for them, and update
   `agents/workspace-chief.md`, `agents/sub-agents/INDEX.md`, `business-skills/INDEX.md`, and the root
   `INDEX.md`. Keep this modest; personalization can deepen it later.

7. **Show the result.** Print the created tree and point the user to:
   - `INDEX.md` - the map.
   - `START_HERE.md` - the human welcome guide.
   - `AGENTS.md` - the operating guide agents read.
   - `business-hub-docs/` or `project-docs/` - the durable business/project memory.
   - `_workspace_setup_docs/personalization/` - the one-time guide to personalize further.

8. **Offer the handoff.** Tell them the base is ready and ask whether to personalize it now. If yes,
   read the newly created `_workspace_setup_docs/personalization/AGENTS.md` and follow its quick-start
   + apply steps. If not, they can later say: *"Customize my workspace."*

## Conventions To Preserve

- One front door: the user talks to the Workspace Chief; it delegates.
- Every content folder has an `INDEX.md`, kept current after meaningful changes.
- Use `lower-kebab-case` names. Markdown for narrative work; tables/CSV/JSON when the work becomes data.
- Synthesis, recommendations, prioritization, and next-step plans go in `outcomes/`, not only chat.
- Reusable ways of working live in `business-skills/`; examples and templates live in
  `business-practices/`.
- Never overwrite raw input. Preserve raw notes under an artifact-local `raw/` folder and write clean
  summaries/artifacts separately.

## Notes

- This skill scaffolds and optionally personalizes a workspace. It does not build app code.
- Tool wiring is minimal by default. `CLAUDE.md` points to `AGENTS.md`, and Cursor gets one always-on
  rule. Only generate `.claude/agents/` or `.github/agents/*.agent.md` if the user asks to wire those
  tools.
