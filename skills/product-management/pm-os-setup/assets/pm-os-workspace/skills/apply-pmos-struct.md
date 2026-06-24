# Skill: apply-pmos-struct

The structural glue of the PM OS. The Chief PM applies this after any task that creates, moves,
renames, meaningfully edits, or documents anything. It keeps the workspace findable by both the PM
and future agents. This is the skill that makes the memory compound instead of pile up.

## Naming

- **`lower-kebab-case` only.** No spaces, no capitals, no `&` or other punctuation in names.
  Use hyphens. (`raw-notes.md`, `q3-onboarding-prd.md` - not `Raw Notes.md` or `Q3 PRD.md`.)
  Agents and Markdown links read these reliably; spaces and capitals cause broken links and ambiguity.
- **Date-prefix time-ordered things** with `YYYY-MM-DD`: meetings, PRDs, decisions.
  Example: `2026-01-15-pricing-sync`. It sorts chronologically and reads at a glance.
- **Markdown (`.md`) for all text.** It's the standard agents read best.

## Folders

- **A thing that has more than one file deserves a folder.** A meeting has raw notes + a summary ->
  it gets its own folder. A standalone decision can be a single file.
- **Create the subfolder when you create the artifact** - don't dump files at the top level.
- **Mirror the existing shape.** Look at how similar artifacts are already organized and match it.

### Conventions in this workspace

| Artifact | Lives at |
|---|---|
| Meeting | `product-docs/meetings/<YYYY-MM-DD>-<title>/` -> `raw_notes.md` + `summary.md` |
| PRD | `product-docs/prds/<YYYY-MM-DD>-<feature>.md` (or a folder if it has attachments) |
| Decision | `product-docs/decisions/<YYYY-MM-DD>-<decision>.md` |
| Vision | `product-docs/product-vision.md` (single source of truth) |

If a new *type* of artifact appears (research, prototypes, comms...), create a new top-level folder
under `product-docs/`, give it an `INDEX.md`, and add it to the root [INDEX.md](../INDEX.md).

## INDEX.md - the rule that makes everything work

- **Every PM OS content folder has an `INDEX.md`.** Tool config folders like `.cursor/` and the
  transient `_setup/` folder do not need one.
- **Every new artifact or meaningful content change updates the nearest `INDEX.md`.** No silent files
  and no stale links.
- **New top-level area -> also update the root `INDEX.md`.**
- A stale index is worse than none - it sends agents to the wrong place. Update it in the same step
  you create or change the file, not "later."

## Product docs

- If product direction, audience, positioning, goal, or strategy changes, update
  `product-docs/product-vision.md` or ask the PM before doing so.
- If another product doc should change, route through the documentation-steward or ask the PM what
  should be captured.
- Keep documentation connected: every durable artifact should be findable from an `INDEX.md`.
- Check the boundary in [AGENTS.md](../AGENTS.md): product docs describe the user's product, while
  Chief PM, sub-agents, skills, and indexes are workspace machinery. If a product artifact mentions
  workspace machinery as if it is the product, fix it or ask the PM if that was intentional.

## Capture vs. data

- **Capture** (notes, summaries, discussion) -> Markdown prose.
- **Data** (comparisons, scoring, structured lists, anything you'd filter or sort) -> a Markdown
  table, or a `.json` / sheet. Give the note coordinates instead of leaving it as a floating sentence.

## Never overwrite raw input

Raw notes, transcripts, and pasted material stay exactly as captured. Summaries and artifacts are
always **new** files. The raw layer is the source of truth you can always return to.

## Checklist before you finish any task that changed the workspace

1. Right folder? (Created a subfolder if it earned one.)
2. `lower-kebab-case`, date-prefixed if time-ordered, `.md` for text?
3. Raw input left untouched?
4. Nearest `INDEX.md` updated? (And root index, if a new area.)
5. Operating-layer concepts kept out of product artifacts unless explicitly intended?
6. Product docs updated or explicitly left unchanged?



