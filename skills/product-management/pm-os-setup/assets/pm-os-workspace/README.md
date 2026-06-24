# {{PROJECT_NAME}} PM OS

This is a lightweight Product Management workspace with memory. It helps your AI agent remember the
product, preserve decisions, keep docs findable, and turn repeated PM work into reusable skills.
As you chat, brainstorm, summarize meetings, write PRDs, and create artifacts, the agents maintain
the context and structure around the work.

The PM OS is the operating layer. Your product vision, PRDs, and decisions should describe the
actual product or project, not the Chief PM or workspace agents unless the product is explicitly this
PM OS.

## Start here

On your first session, your agent should offer to personalize this workspace. If it doesn't, tell it:

> Read `_setup/AGENTS.md` and interview me to personalize this PM OS.

The setup feels like a product intake, not a technical install. Your agent asks about the product,
users, goals, current work, and how you like PM work done, then personalizes the Chief PM, product
vision, docs, and skills around that context. When it's finished it removes the `_setup/` folder — so
if you no longer see `_setup/`, this workspace is already personalized.

## Day to day

Talk to the **Chief PM**. In plain language:

- "Summarize these meeting notes."
- "Help me think through this product direction."
- "Turn this discussion into a PRD."
- "Capture this decision."
- "Update the product vision."
- "Create or update a skill for how I like this work done."

The Chief PM routes the work to specialists and then runs
`skills/apply-pmos-struct.md` so files, indexes, links, and product docs stay clean after changes.
That automatic maintenance pass is what keeps the workspace usable as it grows, without asking you to
manually tidy context after every PM task.

## What stays current

- `product-docs/product-vision.md` - the source of truth for what this product is and why.
- `product-docs/meetings/`, `prds/`, and `decisions/` - durable product memory.
- `INDEX.md` files - maps that keep the workspace navigable.
- `agents/pm-chief.md` - the customized PM coordinator for this product.
- `skills/` - reusable PM workflows that improve over time.
- `skills/apply-pmos-struct.md` - the automatic structure pass agents use after meaningful changes.

## Tool notes

- Cursor is already wired through `.cursor/rules/pm-os.mdc`.
- Claude Code reads `CLAUDE.md`, which points to `AGENTS.md`.
- GitHub Copilot can use generated flat files under `.github/agents/` if you choose to wire it later.

The canonical source of truth stays in `AGENTS.md`, `agents/`, `skills/`, and `product-docs/`.
