# agents/ - Index

The agents that run this Workspace OS. You only ever talk to the **Workspace Chief**; it delegates to sub-agents.

| File | Role |
|---|---|
| [workspace-chief.md](workspace-chief.md) | Workspace Chief - the single entry point. Reads the request, picks the sub-agent, enforces structure. |
| [sub-agents/](sub-agents/INDEX.md) | Specialists the Chief delegates to for meetings, outcomes, brainstorming, offer briefs, brand and delivery, metrics, plans, client comms, docs, and skills. |

**Adding an agent?** Create it under `sub-agents/`, add it to [sub-agents/INDEX.md](sub-agents/INDEX.md),
and register it in the routing table inside [workspace-chief.md](workspace-chief.md).
