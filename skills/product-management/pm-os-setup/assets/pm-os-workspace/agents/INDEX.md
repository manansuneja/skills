# agents/ - Index

The agents that run this PM OS. You only ever talk to the **Chief PM**; it delegates to sub-agents.

| File | Role |
|---|---|
| [pm-chief.md](pm-chief.md) | Chief PM - the single entry point. Reads the request, picks the sub-agent, enforces structure. |
| [sub-agents/](sub-agents/INDEX.md) | Specialists the Chief delegates to for meetings, outcomes, brainstorming, PRDs, design, data, roadmaps, stakeholder comms, docs, and skills. |

**Adding an agent?** Create it under `sub-agents/`, add it to [sub-agents/INDEX.md](sub-agents/INDEX.md),
and register it in the routing table inside [pm-chief.md](pm-chief.md).

