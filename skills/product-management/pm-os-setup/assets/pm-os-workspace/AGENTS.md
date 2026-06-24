# AGENTS.md - {{PROJECT_NAME}} workspace

Operating guide for any AI agent working in this workspace. Read this, then [INDEX.md](INDEX.md).
This is a PM operating system: a workspace with memory, where context compounds over time.

## First: is this workspace personalized yet?

**If the `_setup/` folder still exists, this workspace has not been personalized.** It is still the
generic scaffold. Before doing substantial PM work, offer to run setup:

> Read `_setup/AGENTS.md` and interview me to personalize this PM OS.

Run that intake - product context, Chief PM style, key preferences. When the interview is complete and
the user confirms their answers:

1. Apply the answers across `AGENTS.md`, `product-docs/product-vision.md`, `agents/pm-chief.md`, and any
   skills the user gave preferences for (full steps in `_setup/AGENTS.md`).
2. Confirm the core questions are answered: product, users, problem, stage/goal, and PM style.
3. Delete the entire `_setup/` folder. Keep everything else, including this workspace's `README.md`
   (the user's guide).

The presence of `_setup/` is the "not personalized yet" flag; its absence means setup is done - do not
recreate it. If the user wants to start work immediately, you may proceed, but personalize at the first
natural opportunity so the Chief PM and product docs stop sounding generic.

## Workspace guide vs agent profiles

This file is the workspace operating guide. It is not a duplicate agent profile.

For PM work, enter through the **Chief PM**: [agents/pm-chief.md](agents/pm-chief.md). The Chief PM
coordinates the work and delegates to specialists. In Claude Code, Cursor, and Codex the PM usually
just talks in the workspace and this guide points the chat to the Chief. In GitHub Copilot they can
also select the Chief or a specialist from the agent picker.

## Operating layer vs product layer

This is the global boundary rule for the workspace. Individual agents and skills may add a short
reminder, but this section is the source of truth.

Keep these separate:

- **Operating layer:** this PM OS itself - `AGENTS.md`, `agents/`, `skills/`, indexes, and structure
  automation. The Chief PM and specialists live here.
- **Product layer:** the actual product or project the PM is building - `product-docs/`, PRDs,
  decisions, meetings, customer context, roadmap, and strategy.

Do not let operating-layer concepts leak into product artifacts. A PRD, product vision, or decision
should not treat the Chief PM, PM OS, or workspace sub-agents as the user's product unless the PM
explicitly says they are building a PM OS. If the product includes AI agents, robots, copilots, or
automation, define those as product-specific actors from the product context, not from this workspace
agent system.

## Always do these

- **Orient first.** Read [INDEX.md](INDEX.md) - at the root and in every folder - to find which file
  matters and which to skip. Don't load the whole workspace into context to find one thing.
- **Route, don't solo.** Match the request to a specialist in
  [agents/sub-agents/](agents/sub-agents/INDEX.md) and apply its skill, rather than doing everything
  yourself in one voice.
- **Ground in the vision.** [product-docs/product-vision.md](product-docs/product-vision.md) is the
  source of truth for what {{PROJECT_NAME}} is and why. Tie work back to it.
- **Keep the layers separate.** Use workspace agents and skills to do the work; write product docs
  about the user's actual product.
- **Enforce structure.** Whatever gets produced follows the conventions below.
- **Keep documentation alive.** If product context changes, update
  [product-docs/product-vision.md](product-docs/product-vision.md). If another product doc should
  change, ask the PM and route the update through the documentation-steward.
- **Let agents adapt.** The Chief and specialists should shape their behavior from the product
  vision, recent product docs, and the nature of this project. When those change, update the relevant
  agent or skill file instead of relying on memory.

## Conventions (full version: [skills/apply-pmos-struct.md](skills/apply-pmos-struct.md))

- `lower-kebab-case` names, no spaces. Markdown for text; a table/JSON/sheet when it becomes data.
- An `INDEX.md` in **every** PM OS content folder, kept current - every new artifact or meaningful
  change updates the nearest index in the same change.
- New artifact -> right folder (a subfolder if it earns one), good name, indexed.
- New top-level area -> also update the root `INDEX.md`.
- **Never overwrite raw input.** Raw notes stay raw; summaries and artifacts are new files.

## Structure

```
agents/        Chief PM + sub-agents (meeting-summarizer, brainstorm-partner, prd-writer, documentation-steward, skill-librarian)
skills/        how work gets done (summarize-notes, brainstorm, to-prd, document-product-context, manage-workspace-skills, apply-pmos-struct)
product-docs/  the work: product-vision.md, meetings/, prds/, decisions/
```

## Extending this OS

Want to tailor it - your PRD format, meeting style, writing voice, extra sub-agents? See
[_setup/README.md](_setup/README.md). (It's the one-time setup helper; the whole
`_setup/` folder is safe to delete once you're set up.)
