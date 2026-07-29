# agents/ — Index

> **Agent-facing:** The PM talks to the Chief PM; these files define routing and specialist roles.

The agents that run this PM OS. You only ever talk to the **Chief PM**; it delegates to sub-agents.

| File | Role |
|---|---|
| [pm-chief.md](pm-chief.md) | Chief PM - the single entry point. Reads the request, picks the sub-agent, enforces structure. |
| [sub-agents/](sub-agents/INDEX.md) | Minimal specialists for meetings, outcomes, brainstorming, PRDs, documentation, and product-practice maintenance. |

**Adding an agent?** Create it under `sub-agents/`, add it to [sub-agents/INDEX.md](sub-agents/INDEX.md),
and register it in the routing table inside [pm-chief.md](pm-chief.md).
