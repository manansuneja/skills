# Start Here: Skills

Skills are how this PM OS learns your way of working. You do not need to edit these files by hand.
Tell the Chief PM what you want to change, and it should route the work to the skill-librarian.

## How to update skills

Talk naturally:

- "Update the PRD skill so every PRD starts with the customer problem."
- "Create a skill for how I like launch plans written."
- "Make stakeholder updates shorter and more executive-friendly."
- "Remove the old research synthesis skill if nothing uses it."
- "When we write roadmaps, always include confidence and dependencies."
- "Use this meeting minutes example as the style for future summaries."
- "Use this story template for all feature stories."

The agent should update the skill, update the skill index, update the matching sub-agent or routing,
and then tell you what changed plus one realistic test prompt.

## Templates and references

Use these folders to teach skills without stuffing every format into every skill:

- [templates/](templates/INDEX.md) - reusable blank structures, like story, feature, epic, PRD,
  meeting summary, decision, roadmap, or stakeholder update templates. Markdown and JSON are both
  fine.
- [references/](references/INDEX.md) - examples and style/context samples, like how you write meeting
  minutes, what a good PRD looks like, or the tone of a stakeholder update.

You can paste files into either folder and tell the Chief PM what they should influence. The agent
should update the folder index and the relevant skill so future work uses the new template or
reference.

## Base skills

| Skill | What it does | Usually applied by |
|---|---|---|
| [apply-pmos-struct.md](apply-pmos-struct.md) | Keeps names, folders, links, and indexes clean | Everyone |
| [summarize-notes.md](summarize-notes.md) | Turns raw notes into filed meeting summaries | meeting-summarizer |
| [synthesize-outcomes.md](synthesize-outcomes.md) | Creates insights, recommendations, prioritization, and MVP outcomes | outcome-synthesizer |
| [brainstorm.md](brainstorm.md) | Helps explore options, trade-offs, and directions | brainstorm-partner |
| [to-prd.md](to-prd.md) | Turns discussion into PRD hierarchy, features, and stories | prd-writer |
| [design-considerations.md](design-considerations.md) | Captures UX flows, design trade-offs, and accessibility notes | design-partner |
| [data-insights.md](data-insights.md) | Turns metrics, experiments, and evidence into product insight | data-insights-analyst |
| [roadmap-planning.md](roadmap-planning.md) | Creates roadmaps, release plans, and sequencing recommendations | roadmap-planner |
| [stakeholder-comms.md](stakeholder-comms.md) | Drafts updates, briefs, launch notes, and client summaries | stakeholder-communicator |
| [document-product-context.md](document-product-context.md) | Updates durable product context and documentation | documentation-steward |
| [manage-workspace-skills.md](manage-workspace-skills.md) | Creates, updates, merges, or removes workspace skills | skill-librarian |

## Shared support folders

| Folder | What it is for |
|---|---|
| [templates/](templates/INDEX.md) | Reusable blank artifact templates for skills to follow |
| [references/](references/INDEX.md) | PM-provided examples, style samples, and context references |

## What must stay in sync

When a skill changes, the agent should check and update:

- [INDEX.md](INDEX.md), so the skill catalog stays accurate.
- [templates/INDEX.md](templates/INDEX.md) or [references/INDEX.md](references/INDEX.md), if shared
  templates or examples changed.
- [../agents/pm-chief.md](../agents/pm-chief.md), if routing should change.
- [../agents/sub-agents/INDEX.md](../agents/sub-agents/INDEX.md), if a specialist was added,
  changed, or removed.
- The matching file under [../agents/sub-agents/](../agents/sub-agents/), when the skill needs a
  persona that applies it.
- Any tool-facing copies, such as `.github/agents/` or `.claude/agents/`, if this workspace later
  adds them.

If a skill is removed, remove or rewrite the matching sub-agent and routing in the same change. Do
not leave orphaned agent files pointing at missing skills.
