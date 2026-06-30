# AGENTS.md - {{BUSINESS_NAME}} workspace

Operating guide for any AI agent working in this workspace. Read this, then [INDEX.md](INDEX.md).
This is a Workspace OS for a business or client project: a workspace with memory, where context compounds over time.

## First: is this workspace personalized yet?

**If the `_workspace_setup_docs/personalization/` folder still exists, this workspace has not been personalized.** It is still the
generic scaffold. Before doing substantial business work, offer to run setup:

> Customize my workspace.

When the user asks to customize the workspace, read `_workspace_setup_docs/personalization/AGENTS.md` and run that intake - business
context, Workspace Chief style, key preferences. When the intake has enough context and the personalization
edits are applied:

1. Apply the answers across `AGENTS.md`, `{{DOCS_ROOT}}/business-profile.md`, `agents/workspace-chief.md`, and any
   skills the user gave preferences for (full steps in `_workspace_setup_docs/personalization/AGENTS.md`).
2. Check the core context is answered: workspace name, business/users, problem/opportunity, stage or
   near-term goal, and any existing files or examples the owner wanted used.
3. Delete the entire `_workspace_setup_docs/personalization/` folder as the final cleanup step. Keep everything else, including
   this workspace's `START_HERE.md` (the user's guide).

The presence of `_workspace_setup_docs/personalization/` is the "not personalized yet" flag; its absence means setup is done - do not
recreate it. If the user wants to start work immediately, you may proceed, but personalize at the first
natural opportunity so the Workspace Chief and business docs stop sounding generic.

## Workspace guide vs agent profiles

This file is the workspace operating guide. It is not a duplicate agent profile.

For business work, enter through the **Workspace Chief**: [agents/workspace-chief.md](agents/workspace-chief.md). The Workspace Chief
coordinates the work and delegates to specialists. In Claude Code, Cursor, and Codex the owner usually
just talks in the workspace and this guide points the chat to the Chief. In GitHub Copilot they can
also select the Chief or a specialist from the agent picker.

## Updating the installed Workspace OS skill

If the owner asks how to update the installed `workspace-os-setup` skill after new changes land in GitHub, give
them this command:

```bash
npx skills@latest update workspace-os-setup -g
```

This updates the globally installed skill. Do not run it silently unless the owner explicitly asks you
to update the installed skill.

## Operating layer vs business layer

This is the global boundary rule for the workspace. Individual agents and skills may add a short
reminder, but this section is the source of truth.

Keep these separate:

- **Workspace setup layer:** this Workspace OS itself - `AGENTS.md`, `agents/`, `_workspace_setup_docs/`,
  indexes, and structure automation. The Workspace Chief, specialists, and protected setup playbooks live
  here.
- **Business practice layer:** user-shaped business preferences in `business-skills/` and
  `business-practices/`. This is where offer brief style, templates, examples, and reusable business judgment
  evolve.
- **Business docs layer:** the actual business or project the owner is building - `{{DOCS_ROOT}}/`, offer briefs,
  decisions, meetings, client context, plan, brand and delivery, metrics, client communication, and
  strategy.

Do not let operating-layer concepts leak into business artifacts. An offer brief, business profile, or decision
should not treat the Workspace Chief, Workspace OS, or workspace sub-agents as the user's business unless the owner
explicitly says they are building a Workspace OS. If the business includes AI agents, robots, copilots, or
automation, define those as business-specific actors from the business context, not from this workspace
agent system.

## Always do these

- **Orient first.** Read [INDEX.md](INDEX.md) - at the root and in every folder - to find which file
  matters and which to skip. Don't load the whole workspace into context to find one thing.
- **Route, don't solo.** Match the request to a specialist in
  [agents/sub-agents/](agents/sub-agents/INDEX.md) and apply its skill, rather than doing everything
  yourself in one voice.
- **Act on capture.** When the owner provides raw notes, pasted text, loose files, screenshots, or
  asks to summarize/import/process something, treat that as permission to organize it into the Workspace OS:
  create the right folder, preserve raw input under a `raw/` archive subfolder, create the
  summary/artifact in the main artifact folder, update indexes, and then report what changed. Do not
  respond with a menu of options unless the request is genuinely ambiguous.
- **Write durable work to files.** If the answer is substantial business work - analysis,
  recommendations, prioritization, plans, offer brief content, decisions, brand and delivery considerations, data
  insights, client communications, summaries, or reusable process - create or update the
  appropriate artifact and index. Use chat for a brief handoff: what changed, the top takeaway, and
  the file path.
- **Ground in the business profile.** [{{DOCS_ROOT}}/business-profile.md]({{DOCS_ROOT}}/business-profile.md) is the
  source of truth for what {{BUSINESS_NAME}} is and why. Tie work back to it.
- **Keep the layers separate.** Use workspace agents and business skills to do the work; write business
  docs about the user's actual business.
- **Enforce structure.** Whatever gets produced follows the conventions below.
- **Keep documentation alive.** If business context changes, update
  [{{DOCS_ROOT}}/business-profile.md]({{DOCS_ROOT}}/business-profile.md) when the change is clear or when
  the current business profile is still generic. If another business doc should change and the source is clear,
  update it; ask only when the change would overwrite an established direction or requires a business
  judgment the notes do not answer.
- **Let agents adapt.** The Chief and specialists should shape their behavior from the business
  recent business profile, business docs, and the nature of this project. When those change, update the relevant
  agent or skill file instead of relying on memory.

## Conventions (full version: [_workspace_setup_docs/skills/apply-workspace-struct.md](_workspace_setup_docs/skills/apply-workspace-struct.md))

- `lower-kebab-case` names, no spaces. Markdown for text; a table/JSON/sheet when it becomes data.
- An `INDEX.md` in **every** Workspace OS content folder, kept current - every new artifact or meaningful
  change updates the nearest index in the same change.
- New artifact -> right folder (a subfolder if it earns one), good name, indexed.
- New top-level area -> also update the root `INDEX.md`.
- **Never overwrite raw input.** Raw notes stay raw under an artifact's `raw/` subfolder; summaries
  and artifacts are new files in the main artifact folder.
- Loose raw files under `{{DOCS_ROOT}}/meetings/` are inbox items. Move them into a dated meeting
  folder, preserve them under `raw/raw-notes.md`, write `summary.md`, and update the meetings index.
  After archiving the raw source, remove the loose inbox copy. Do not leave duplicate raw files in
  `{{DOCS_ROOT}}/meetings/` or top-level `raw_notes.md` files in a meeting folder.

## Structure

```
START_HERE.md       the human welcome guide: just talk to the agent
agents/             Workspace Chief + sub-agents for meetings, outcomes, offer briefs, brand and delivery, metrics, plans, comms, docs, skills
_workspace_setup_docs/          setup docs, structure rules, and protected workspace playbooks
business-skills/                 how business work gets done and how the owner's style is captured
business-practices/templates/    reusable blank formats for business skills to follow
business-practices/references/   Owner-provided examples, style samples, and context references
{{DOCS_ROOT}}/       the work: profile, meetings, outcomes, decisions, offer briefs, brand and delivery, metrics, plans, comms
```

## Extending this OS

Want to tailor it - your offer brief format, meeting style, writing voice, extra sub-agents? See
[_workspace_setup_docs/personalization/README.md](_workspace_setup_docs/personalization/README.md). (It's the one-time setup helper; the whole
`_workspace_setup_docs/personalization/` folder is safe to delete once you're set up.)
