# {{BUSINESS_NAME}} - Workspace OS Index

> This is the map of the workspace. Read this **first**, every time, before touching anything else.
> It tells an agent which folder matters, which file to open, and which files to skip - so it
> moves through the workspace like someone who has been here before, instead of wandering.

## How to use this index

- **Start here.** For any request, scan this index, then open only the file(s) that matter.
- **Don't read everything.** The point of the index is to *avoid* loading the whole workspace into context.
- **Keep it current.** Whenever you create, move, rename, or meaningfully edit a Workspace OS artifact,
  update the nearest `INDEX.md` and, if it's a new top-level area, this root index. A stale map is
  worse than no map.

## Who to talk to

You only talk to one agent: the **Workspace Chief** ([agents/workspace-chief.md](agents/workspace-chief.md)).
It reads your request and delegates to the right sub-agent. See [agents/INDEX.md](agents/INDEX.md).

Working agents should also read [AGENTS.md](AGENTS.md) - the operating guide for this workspace.
[CLAUDE.md](CLAUDE.md) is a compatibility pointer to the same guide for tools that expect that name.
Setting it up for the first time? See [_workspace_setup_docs/personalization/README.md](_workspace_setup_docs/personalization/README.md).
New here? See [START_HERE.md](START_HERE.md) for the plain-language user guide.

## Map

| Folder | What lives here | Open when |
|---|---|---|
| [agents/](agents/INDEX.md) | The Workspace Chief and its sub-agents (who does what) | Deciding who should handle a request |
| [_workspace_setup_docs/](_workspace_setup_docs/INDEX.md) | Workspace setup rules, structural playbooks, and one-time personalization docs | A change affects the Workspace OS structure itself |
| [business-skills/](business-skills/INDEX.md) | Repeatable business judgment - how this owner wants work done | An agent needs the "how" for a business task |
| [business-practices/](business-practices/INDEX.md) | Templates, examples, and style references that shape business skills | A skill needs a reusable format or example |
| [{{DOCS_ROOT}}/]({{DOCS_ROOT}}/INDEX.md) | The actual work: profile, meetings, outcomes, offer briefs, decisions, brand and delivery, metrics, plans, comms | Looking for or producing real artifacts |

## Tool config

| Folder | What lives here | Open when |
|---|---|---|
| [.cursor/rules/](.cursor/rules/workspace-os.mdc) | Cursor project rule that points back to AGENTS.md | Cursor needs persistent workspace guidance |

## Quick links

- **Business profile** -> [{{DOCS_ROOT}}/business-profile.md]({{DOCS_ROOT}}/business-profile.md)
- **Skills guide** -> [business-skills/START_HERE.md](business-skills/START_HERE.md)
- **Skill templates** -> [business-practices/templates/INDEX.md](business-practices/templates/INDEX.md)
- **Skill references** -> [business-practices/references/INDEX.md](business-practices/references/INDEX.md)
- **Meetings** (summaries + raw source archives) -> [{{DOCS_ROOT}}/meetings/INDEX.md]({{DOCS_ROOT}}/meetings/INDEX.md)
- **Outcomes** (insights, recommendations, prioritization) -> [{{DOCS_ROOT}}/outcomes/INDEX.md]({{DOCS_ROOT}}/outcomes/INDEX.md)
- **offer briefs** -> [{{DOCS_ROOT}}/offers/INDEX.md]({{DOCS_ROOT}}/offers/INDEX.md)
- **Decisions log** -> [{{DOCS_ROOT}}/decisions/INDEX.md]({{DOCS_ROOT}}/decisions/INDEX.md)
- **Brand and delivery** -> [{{DOCS_ROOT}}/brand-and-delivery/INDEX.md]({{DOCS_ROOT}}/brand-and-delivery/INDEX.md)
- **Metric insights** -> [{{DOCS_ROOT}}/metrics/INDEX.md]({{DOCS_ROOT}}/metrics/INDEX.md)
- **Plans** -> [{{DOCS_ROOT}}/plans/INDEX.md]({{DOCS_ROOT}}/plans/INDEX.md)
- **Client comms** -> [{{DOCS_ROOT}}/client-comms/INDEX.md]({{DOCS_ROOT}}/client-comms/INDEX.md)
- **Cursor rule** -> [.cursor/rules/workspace-os.mdc](.cursor/rules/workspace-os.mdc)

## The one rule that makes this work

When you produce a new artifact, **give it coordinates**: put it in the right folder (create a
subfolder if it deserves one), name it in `lower-kebab-case.md` (no spaces, no capitals), and add a
line to the nearest `INDEX.md`. If business direction changes, update
[{{DOCS_ROOT}}/business-profile.md]({{DOCS_ROOT}}/business-profile.md). Capture is not memory. Connection is.

See [_workspace_setup_docs/skills/apply-workspace-struct.md](_workspace_setup_docs/skills/apply-workspace-struct.md) for the full naming and structure rules.
