# {{PROJECT_NAME}} - PM OS Index

> This is the map of the workspace. Read this **first**, every time, before touching anything else.
> It tells an agent which folder matters, which file to open, and which files to skip - so it
> moves through the workspace like someone who has been here before, instead of wandering.

## How to use this index

- **Start here.** For any request, scan this index, then open only the file(s) that matter.
- **Don't read everything.** The point of the index is to *avoid* loading the whole workspace into context.
- **Keep it current.** Whenever you create, move, rename, or meaningfully edit a PM OS artifact,
  update the nearest `INDEX.md` and, if it's a new top-level area, this root index. A stale map is
  worse than no map.

## Who to talk to

You only talk to one agent: the **Chief PM** ([agents/pm-chief.md](agents/pm-chief.md)).
It reads your request and delegates to the right sub-agent. See [agents/INDEX.md](agents/INDEX.md).

Working agents should also read [AGENTS.md](AGENTS.md) - the operating guide for this workspace.
[CLAUDE.md](CLAUDE.md) is a compatibility pointer to the same guide for tools that expect that name.
Setting it up for the first time? See [_setup/README.md](_setup/README.md).
New here? See [START_HERE.md](START_HERE.md) for the plain-language user guide.

## Map

| Folder | What lives here | Open when |
|---|---|---|
| [agents/](agents/INDEX.md) | The Chief PM and its sub-agents (who does what) | Deciding who should handle a request |
| [skills/](skills/INDEX.md) | Repeatable judgment - how this PM wants work done | An agent needs the "how" for a task |
| [product-docs/](product-docs/INDEX.md) | The actual work: vision, meetings, outcomes, PRDs, decisions, design, data, roadmaps, comms | Looking for or producing real artifacts |

## Tool config

| Folder | What lives here | Open when |
|---|---|---|
| [.cursor/rules/](.cursor/rules/pm-os.mdc) | Cursor project rule that points back to AGENTS.md | Cursor needs persistent workspace guidance |

## Quick links

- **Product vision** -> [product-docs/product-vision.md](product-docs/product-vision.md)
- **Skills guide** -> [skills/START_HERE.md](skills/START_HERE.md)
- **Skill templates** -> [skills/templates/INDEX.md](skills/templates/INDEX.md)
- **Skill references** -> [skills/references/INDEX.md](skills/references/INDEX.md)
- **Meetings** (summaries + raw source archives) -> [product-docs/meetings/INDEX.md](product-docs/meetings/INDEX.md)
- **Outcomes** (insights, recommendations, prioritization) -> [product-docs/outcomes/INDEX.md](product-docs/outcomes/INDEX.md)
- **PRDs** -> [product-docs/prds/INDEX.md](product-docs/prds/INDEX.md)
- **Decisions log** -> [product-docs/decisions/INDEX.md](product-docs/decisions/INDEX.md)
- **Design** -> [product-docs/design/INDEX.md](product-docs/design/INDEX.md)
- **Data insights** -> [product-docs/data-insights/INDEX.md](product-docs/data-insights/INDEX.md)
- **Roadmaps** -> [product-docs/roadmaps/INDEX.md](product-docs/roadmaps/INDEX.md)
- **Stakeholder comms** -> [product-docs/stakeholder-comms/INDEX.md](product-docs/stakeholder-comms/INDEX.md)
- **Cursor rule** -> [.cursor/rules/pm-os.mdc](.cursor/rules/pm-os.mdc)

## The one rule that makes this work

When you produce a new artifact, **give it coordinates**: put it in the right folder (create a
subfolder if it deserves one), name it in `lower-kebab-case.md` (no spaces, no capitals), and add a
line to the nearest `INDEX.md`. If product direction changes, update
[product-docs/product-vision.md](product-docs/product-vision.md). Capture is not memory. Connection is.

See [skills/apply-pmos-struct.md](skills/apply-pmos-struct.md) for the full naming and structure rules.
