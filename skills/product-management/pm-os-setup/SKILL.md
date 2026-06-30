---
name: pm-os-setup
description: Scaffold a Product Management operating system - a Markdown workspace with memory that compounds over time. Creates or fills a workspace root with a Chief PM coordinator agent, specialized sub-agents for meetings, outcomes, brainstorming, PRDs, design, data insights, roadmaps, stakeholder communication, documentation, and skills, starter workflow skills for those PM jobs, shared skill templates/references folders, an INDEX.md map in every PM OS content folder, a product-docs tree (vision, meetings, outcomes, prds, decisions, design, data-insights, roadmaps, stakeholder-comms), plus START_HERE.md, AGENTS.md, CLAUDE.md, a Cursor rule, and a _setup/ subfolder for onboarding/personalization. Use when a PM or anyone wants to set up a PM OS, "PM operating system", PM workspace, agent workspace with memory, or asks to run pm-os-setup / PM-OS-Setup. After scaffolding, offers a "Customize my workspace" handoff so the user's own agent can personalize it. Not for building application code or generic unrelated file scaffolds.
---

# PM OS Setup

## Overview

This skill sets up a base **Product Management operating system**: a plain-Markdown workspace where
context compounds instead of leaking. The PM talks to one **Chief PM** agent that delegates to
specialized sub-agents, every PM OS content folder has an `INDEX.md` map, and conventions keep the workspace
findable for both the human and future agents.

The base is intentionally **generic**. This skill scaffolds it; the workspace's own `_setup/`
guide then drives the deeper, conversational personalization (real vision, the PM's PRD format, extra agents).

The durable root files are **the user's own** - don't put setup instructions in them:
- `START_HERE.md` - the **human welcome guide** for how to start talking to the agent.
- `AGENTS.md` - the **operating guide** agents auto-read for this workspace (front door, conventions).
- `CLAUDE.md` - a tiny compatibility pointer to `AGENTS.md` for Claude Code and any tool that
  expects that filename.

All setup/personalization material lives in the **`_setup/` subfolder** (its own `README.md` for
the human, `AGENTS.md` for the agent). It's transient - the user deletes the whole folder once set up.

## What gets created

A PM OS workspace root. Usually this is the current folder. If the user is in a broad/root directory,
create a new `{projectName}-workspace/` folder there instead.

```
INDEX.md            agents/pm-chief.md          skills/summarize-notes.md
START_HERE.md       agents/sub-agents/...       skills/START_HERE.md
AGENTS.md           CLAUDE.md                   skills/brainstorm.md
.cursor/rules/      skills/synthesize-outcomes.md skills/to-prd.md
_setup/             skills/data-insights.md     skills/roadmap-planning.md
                    skills/stakeholder-comms.md skills/document-product-context.md
                    skills/manage-workspace-skills.md   skills/apply-pmos-struct.md
                    skills/templates/           skills/references/
                    product-docs/product-vision.md
  README.md         product-docs/meetings/ , outcomes/ , prds/ , decisions/
  AGENTS.md         product-docs/design/ , data-insights/ , roadmaps/ , stakeholder-comms/
```

Plus an `INDEX.md` in every PM OS content folder and a tiny Cursor project rule.

## Setup workflow

Follow these steps in order.

Think of this like starting a new Next.js or other dev project:

- If the user already opened or created the project/workspace folder, set up the PM OS directly in
  the current folder.
- If the user is in a broad parent location and asks for a new workspace, create a clean
  `<project-slug>-workspace/` folder there.

1. **Ask two quick things** (one short message, don't over-interview - deeper questions come later
   via the `_setup/` guide):
   - What's the product/project name? (Used to fill `{{PROJECT_NAME}}` and to name the workspace
     folder if one needs to be created. If they skip it, use `pm-os-workspace` for a new folder and
     leave placeholders.)
   - Are we setting this up in the current folder, or should I create a new workspace folder here?

2. **Choose the workspace root.** Prefer the current directory when it looks intentionally chosen:
   empty, nearly empty, or already named like the product/project. This is the best UX in Claude Code,
   Cursor, and similar tools where the user opened a project folder first.

   Create a new `<project-slug>-workspace/` folder only when the current directory looks broad or
   unsafe to write into directly, such as a home folder, drive root, downloads folder, repo collection,
   desktop, or a directory with many unrelated files. In that case, tell the user the exact folder
   you will create before writing.

3. **Guard against clobbering.** Never overwrite an existing workspace or unrelated project files.
   If the chosen workspace root is non-empty, inspect only the top-level names and decide:

   - If it already contains PM OS files (`AGENTS.md`, `INDEX.md`, `agents/`, `skills/`, or
     `product-docs/`), stop and ask whether to update the existing PM OS instead of scaffolding.
   - If it is a normal project folder with a few existing files, explain the PM OS files that will be
     added and ask before writing.
   - If it is broad/root-like or cluttered, create `<project-slug>-workspace/` inside it instead.

   The final workspace root must be the folder the user opens. It should contain `INDEX.md`,
   `START_HERE.md`, `AGENTS.md`, `CLAUDE.md`, `.cursor/`, `_setup/`, `agents/`, `skills/`, and
   `product-docs/` directly.

4. **Run the scaffold helper for the active OS/shell.** Prefer the bundled script over manually
   writing files. This keeps Claude Code, Cursor, and other agents from spending minutes emitting
   every Markdown file one by one.

   Detect the active environment from the running agent and shell. On macOS/Linux in Bash, zsh, or
   sh, use the shell helper:

   ```bash
   "<skill-root>/scripts/scaffold-pm-os.sh" --project-name "<project name>" --target-path "." --use-current-folder
   "<skill-root>/scripts/scaffold-pm-os.sh" --project-name "<project name>" --target-path "." --create-folder
   ```

   On Windows PowerShell, use the PowerShell helper:

   ```powershell
   & "<skill-root>\scripts\scaffold-pm-os.ps1" -ProjectName "<project name>" -TargetPath "." -UseCurrentFolder
   & "<skill-root>\scripts\scaffold-pm-os.ps1" -ProjectName "<project name>" -TargetPath "." -CreateFolder
   ```

   Do not repeatedly try unavailable shells. Only call `pwsh` on macOS/Linux if the shell helper is
   unavailable and `command -v pwsh` already succeeds. If no helper can run, use the manual copy
   fallback below.

5. **Manual fallback only if the script is unavailable.** Recursively copy the contents of the
   bundled `assets/pm-os-workspace/` directory into the chosen workspace root. Keep the structure and
   filenames exactly.

   Copy the template contents, not the template folder. Do not create any of these wrong bases:
   - `<project-slug>-workspace/pm-os-workspace/...`
   - `<project-slug>-workspace/pm-os-setup/...`
   - `pm-os-setup-workspace/...`

6. **Fill placeholders** across the copied files - **except the `_setup/` folder**, which
   intentionally keeps the literal tokens so its guide stays usable later:
   - `{{PROJECT_NAME}}` -> the name from step 1 (or leave as-is everywhere if they skipped it).
   - `{{DATE}}` -> today's date in `MMM-DD-YYYY` (only appears in templates that need it).

   The scaffold helper already does this. Only do this manually when using the fallback path.

7. **Show the result.** Print the created tree and point the user to the orientation files:
   - `INDEX.md` - the map (always read first).
   - `START_HERE.md` - the user-facing welcome guide: just talk to the agent, paste notes, ask for
     outcomes, PRDs, design, data, roadmaps, comms, or skill updates.
   - `AGENTS.md` - the durable operating guide agents read to work in this workspace.
   - `CLAUDE.md` - a compatibility pointer to `AGENTS.md`; keep it small.
   - `_setup/` - the one-time guide to personalize further (deletable once done).

8. **Offer the handoff.** Tell them the base is generic and ask if they'd like to personalize it now.
   If yes, read the newly created `_setup/AGENTS.md` in the workspace and follow its quick-start
   + apply steps. If not, they can do it anytime by telling their agent: *"Customize my workspace."*

## Conventions to preserve

When copying and (optionally) personalizing, keep what makes the system work - the canonical rules
live in the workspace's `skills/apply-pmos-struct.md`:

- One front door (talk to the Chief PM; it delegates).
- An `INDEX.md` in every PM OS content folder, kept current - every artifact or meaningful change
  updates the nearest index.
- `lower-kebab-case` names, no spaces; Markdown for text, a table/JSON when work becomes data.
- Synthesis, recommendations, prioritization, MVP cuts, and next-step plans go in
  `product-docs/outcomes/`, not just chat.
- Design considerations, data insights, roadmaps, and stakeholder communications have their own
  first-class folders under `product-docs/`.
- Skill changes keep the whole operating layer synchronized: `skills/START_HERE.md`,
  `skills/INDEX.md`, the matching sub-agent, `agents/sub-agents/INDEX.md`, and Chief PM routing.
- Reusable output formats live in `skills/templates/`; PM-provided examples and style/context
  samples live in `skills/references/`. Individual skills should link there instead of carrying every
  possible template inline.
- Never overwrite raw input - keep it under an artifact-local `raw/` archive folder; summaries and
  artifacts are always new files in the main artifact folder.

## Notes

- This skill only **scaffolds and optionally personalizes** a workspace. It does not build
  application code.
- The `agents/` and `skills/` files are plain Markdown instructions; the user talks naturally and the
  generated `START_HERE.md` explains the simple workflow.
- **The Chief PM is the workspace's default persona, not a selectable app.** In Claude Code, Cursor,
  and Codex the user just talks and `AGENTS.md` makes the chat the Chief; only GitHub Copilot has an
  agent picker. Sub-agents are personas that point to skills.
- **Tool wiring is minimal by default.** The canonical `agents/`/`skills/` are tool-agnostic;
  `CLAUDE.md` is pre-shipped only as a pointer to `AGENTS.md`, and `.cursor/rules/pm-os.mdc` is
  pre-shipped as an always-on Cursor bridge. During personalization, only generate `.claude/agents/`
  specialists or flat `.github/agents/*.agent.md` files if the PM explicitly asks to wire that tool.
  Do not generate a legacy `.agents/` folder.
