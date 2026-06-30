# sub-agents/ - Index

Specialists the [Chief PM](../pm-chief.md) delegates to (the PM talks to the Chief, not to these
directly). Each is a **persona** - a character with a point of view - that applies a
[skill](../../product-skills/INDEX.md). The skill is the reusable *how*; the agent is the *who*. Same markdown
underneath; the personality is the part a bare skill doesn't give you.

| File | Does | Uses skill |
|---|---|---|
| [meeting-summarizer.md](meeting-summarizer.md) | Turns raw meeting notes into a clean, filed summary | [summarize-notes](../../product-skills/summarize-notes.md) |
| [outcome-synthesizer.md](outcome-synthesizer.md) | Turns context into durable insights, recommendations, prioritization, and MVP choices | [synthesize-outcomes](../../product-skills/synthesize-outcomes.md) |
| [brainstorm-partner.md](brainstorm-partner.md) | Thinks through problems and explores options with the PM | [brainstorm](../../product-skills/brainstorm.md) |
| [prd-writer.md](prd-writer.md) | Turns a discussion or notes into a structured PRD | [to-prd](../../product-skills/to-prd.md) |
| [design-partner.md](design-partner.md) | Captures UX flows, design considerations, accessibility notes, and trade-offs | [design-considerations](../../product-skills/design-considerations.md) |
| [data-insights-analyst.md](data-insights-analyst.md) | Turns metrics, experiments, and quantitative evidence into product insight | [data-insights](../../product-skills/data-insights.md) |
| [roadmap-planner.md](roadmap-planner.md) | Turns context into roadmaps, release plans, and sequencing recommendations | [roadmap-planning](../../product-skills/roadmap-planning.md) |
| [stakeholder-communicator.md](stakeholder-communicator.md) | Drafts stakeholder updates, exec briefs, launch notes, and client summaries | [stakeholder-comms](../../product-skills/stakeholder-comms.md) |
| [documentation-steward.md](documentation-steward.md) | Keeps product docs, product vision, and indexes current | [document-product-context](../../product-skills/document-product-context.md) |
| [skill-librarian.md](skill-librarian.md) | Creates and updates workspace skills as the PM's process evolves | [manage-workspace-skills](../../_workspace_setup_docs/skills/manage-workspace-skills.md) |

All sub-agents also apply [apply-pmos-struct](../../_workspace_setup_docs/skills/apply-pmos-struct.md) when they create files.

**Adding one?** Copy the shape of these files, add a row here, and register it in the
routing table inside [../pm-chief.md](../pm-chief.md). Removing one? Remove or reroute the matching
skill in [../../product-skills/INDEX.md](../../product-skills/INDEX.md) in the same change.
