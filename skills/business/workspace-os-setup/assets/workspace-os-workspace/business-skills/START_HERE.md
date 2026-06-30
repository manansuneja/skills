# Start Here: Business Skills

Business skills are how this Workspace OS learns your way of doing business work. You do not need to edit
these files by hand. Tell the Workspace Chief what you want to change, and it should route the work to the
skill-librarian.

Workspace setup rules live separately in [_workspace_setup_docs/](../_workspace_setup_docs/INDEX.md).
They keep the workspace organized and should stay boring unless the structure itself needs to change.

## How to update skills

Talk naturally:

- "Update the offer brief skill so every offer brief starts with the customer problem."
- "Create a skill for how I like launch plans written."
- "Make client updates shorter and more executive-friendly."
- "Remove the old research synthesis skill if nothing uses it."
- "When we write plans, always include confidence and dependencies."
- "Use this meeting minutes example as the style for future summaries."
- "Use this story template for all client stories."

The agent should update the skill, update the skill index, update the matching sub-agent or routing,
and then tell you what changed plus one realistic test prompt.

## Templates and references

Use these folders to teach skills without stuffing every format into every skill:

- [business-practices/templates/](../business-practices/templates/INDEX.md) - reusable blank structures, like story, offer, project, offer brief,
  meeting summary, decision, plan, or client update templates. Markdown and JSON are both
  fine.
- [business-practices/references/](../business-practices/references/INDEX.md) - examples and style/context samples, like how you write meeting
  minutes, what a good offer brief looks like, or the tone of a client update.

You can paste files into either folder and tell the Workspace Chief what they should influence. The agent
should update the folder index and the relevant skill so future work uses the new template or
reference.

## Base skills

| Skill | What it does | Usually applied by |
|---|---|---|
| [summarize-notes.md](summarize-notes.md) | Turns raw notes into filed meeting summaries | meeting-summarizer |
| [synthesize-outcomes.md](synthesize-outcomes.md) | Creates insights, recommendations, prioritization, and scope outcomes | outcome-synthesizer |
| [brainstorm.md](brainstorm.md) | Helps explore options, trade-offs, and directions | brainstorm-partner |
| [offer-brief.md](offer-brief.md) | Turns discussion into offer, package, deliverable, or project briefs | offer-brief-writer |
| [brand-and-delivery.md](brand-and-delivery.md) | Captures UX flows, brand and delivery trade-offs, and accessibility notes | brand-and-delivery-partner |
| [metrics-review.md](metrics-review.md) | Turns metrics, experiments, and evidence into business insight | metrics-analyst |
| [business-planning.md](business-planning.md) | Creates plans, release plans, and sequencing recommendations | planning-partner |
| [client-comms.md](client-comms.md) | Drafts updates, briefs, launch notes, and client summaries | client-communicator |
| [document-business-context.md](document-business-context.md) | Updates durable business context and documentation | documentation-steward |

## Shared support folders

| Folder | What it is for |
|---|---|
| [business-practices/templates/](../business-practices/templates/INDEX.md) | Reusable blank artifact templates for skills to follow |
| [business-practices/references/](../business-practices/references/INDEX.md) | Owner-provided examples, style samples, and context references |

## What must stay in sync

When a skill changes, the agent should check and update:

- [INDEX.md](INDEX.md), so the skill catalog stays accurate.
- [business-practices/templates/INDEX.md](../business-practices/templates/INDEX.md) or [business-practices/references/INDEX.md](../business-practices/references/INDEX.md), if shared
  templates or examples changed.
- [../agents/workspace-chief.md](../agents/workspace-chief.md), if routing should change.
- [../agents/sub-agents/INDEX.md](../agents/sub-agents/INDEX.md), if a specialist was added,
  changed, or removed.
- The matching file under [../agents/sub-agents/](../agents/sub-agents/), when the skill needs a
  persona that applies it.
- Any tool-facing copies, such as `.github/agents/` or `.claude/agents/`, if this workspace later
  adds them.

If a skill is removed, remove or rewrite the matching sub-agent and routing in the same change. Do
not leave orphaned agent files pointing at missing skills.
