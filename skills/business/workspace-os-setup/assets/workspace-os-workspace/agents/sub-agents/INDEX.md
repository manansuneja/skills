# sub-agents/ - Index

Specialists the [Workspace Chief](../workspace-chief.md) delegates to (the owner talks to the Chief, not to these
directly). Each is a **persona** - a character with a point of view - that applies a
[skill](../../business-skills/INDEX.md). The skill is the reusable *how*; the agent is the *who*. Same markdown
underneath; the personality is the part a bare skill doesn't give you.

| File | Does | Uses skill |
|---|---|---|
| [meeting-summarizer.md](meeting-summarizer.md) | Turns raw meeting notes into a clean, filed summary | [summarize-notes](../../business-skills/summarize-notes.md) |
| [outcome-synthesizer.md](outcome-synthesizer.md) | Turns context into durable insights, recommendations, prioritization, and scope choices | [synthesize-outcomes](../../business-skills/synthesize-outcomes.md) |
| [brainstorm-partner.md](brainstorm-partner.md) | Thinks through problems and explores options with the owner | [brainstorm](../../business-skills/brainstorm.md) |
| [offer-brief-writer.md](offer-brief-writer.md) | Turns a discussion or notes into a structured offer brief | [offer-brief](../../business-skills/offer-brief.md) |
| [brand-and-delivery-partner.md](brand-and-delivery-partner.md) | Captures UX flows, brand and delivery considerations, accessibility notes, and trade-offs | [brand-and-delivery](../../business-skills/brand-and-delivery.md) |
| [metrics-analyst.md](metrics-analyst.md) | Turns metrics, experiments, and quantitative evidence into business insight | [metrics-review](../../business-skills/metrics-review.md) |
| [planning-partner.md](planning-partner.md) | Turns context into plans, release plans, and sequencing recommendations | [business-planning](../../business-skills/business-planning.md) |
| [client-communicator.md](client-communicator.md) | Drafts client updates, exec briefs, launch notes, and client summaries | [client-comms](../../business-skills/client-comms.md) |
| [documentation-steward.md](documentation-steward.md) | Keeps business docs, business profile, and indexes current | [document-business-context](../../business-skills/document-business-context.md) |
| [skill-librarian.md](skill-librarian.md) | Creates and updates workspace skills as the owner's process evolves | [manage-workspace-skills](../../_workspace_setup_docs/skills/manage-workspace-skills.md) |

All sub-agents also apply [apply-workspace-struct](../../_workspace_setup_docs/skills/apply-workspace-struct.md) when they create files.

**Adding one?** Copy the shape of these files, add a row here, and register it in the
routing table inside [../workspace-chief.md](../workspace-chief.md). Removing one? Remove or reroute the matching
skill in [../../business-skills/INDEX.md](../../business-skills/INDEX.md) in the same change.
