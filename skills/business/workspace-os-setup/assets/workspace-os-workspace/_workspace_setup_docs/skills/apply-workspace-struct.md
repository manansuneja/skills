# Skill: apply-workspace-struct

The structural glue of the Workspace OS. The Workspace Chief applies this after any task that creates, moves,
renames, meaningfully edits, or documents anything. It keeps the workspace findable by both the owner
and future agents. This is the skill that makes the memory compound instead of pile up.

## Naming

- **`lower-kebab-case` for descriptive names.** No spaces, no capitals, no `&` or other punctuation
  outside the date prefix. Use hyphens. (`raw-notes.md`, `q3-onboarding-brief.md` - not
  `Raw Notes.md` or `Q3 offer brief.md`.) Agents and Markdown links read these reliably; spaces and capitals
  cause broken links and ambiguity.
- **Date-prefix time-ordered things** with `MMM-DD-YYYY`: meetings, outcomes, decisions.
  Example: `Jan-15-2026-pricing-sync`. Use a three-letter English month abbreviation with title
  case, a two-digit day, and a four-digit year.
- **Use topic-first folders for offer briefs.** Offer brief work should mirror how a business owner thinks about scope:
  broader area/package -> offer -> client story. Use stable folders like `landing-page/header/`, not
  date-prefixed files like `Jan-15-2026-header.md`. Put dates in the offer brief body and index instead.
- **Markdown (`.md`) for all text.** It's the standard agents read best.

## Folders

- **A thing that has more than one file deserves a folder.** A meeting has a summary plus archived
  raw notes -> it gets its own folder. A standalone decision can be a single file.
- **Create the subfolder when you create the artifact** - don't dump files at the top level.
- **Mirror the existing shape.** Look at how similar artifacts are already organized and match it.

### Conventions in this workspace

| Artifact | Lives at |
|---|---|
| Meeting | `{{DOCS_ROOT}}/meetings/<MMM-DD-YYYY>-<title>/` -> `summary.md` + `raw/raw-notes.md` |
| Outcome | `{{DOCS_ROOT}}/outcomes/<MMM-DD-YYYY>-<topic>.md` |
| Offer brief area / package | `{{DOCS_ROOT}}/offers/<area-or-package-slug>/overview.md` + `INDEX.md` |
| Offer brief | `{{DOCS_ROOT}}/offers/<area-or-package-slug>/<offer-or-deliverable-slug>/brief.md` + optional `client-story.md` |
| Standalone offer brief | `{{DOCS_ROOT}}/offers/<offer-or-deliverable-slug>/brief.md` only when no parent area is useful |
| Decision | `{{DOCS_ROOT}}/decisions/<MMM-DD-YYYY>-<decision>.md` |
| Brand and delivery note | `{{DOCS_ROOT}}/brand-and-delivery/<MMM-DD-YYYY>-<topic>.md` |
| Metric insight | `{{DOCS_ROOT}}/metrics/<MMM-DD-YYYY>-<topic>.md` |
| Plan | `{{DOCS_ROOT}}/plans/<MMM-DD-YYYY>-<topic>.md` |
| Client communication | `{{DOCS_ROOT}}/client-comms/<MMM-DD-YYYY>-<topic>.md` |
| Business profile | `{{DOCS_ROOT}}/business-profile.md` (single source of truth) |

If a new *type* of artifact appears (research, prototypes, support docs...), create a new top-level folder
under `{{DOCS_ROOT}}/`, give it an `INDEX.md`, and add it to the root [INDEX.md](../../INDEX.md).

## INDEX.md - the rule that makes everything work

- **Every Workspace OS content folder has an `INDEX.md`.** Tool config folders like `.cursor/` and archival
  `raw/` subfolders do not need one.
- **Every new artifact or meaningful content change updates the nearest `INDEX.md`.** No silent files
  and no stale links.
- **New top-level area -> also update the root `INDEX.md`.**
- **Skill changes update their maps.** Adding, updating, merging, or removing a skill must update
  `business-skills/INDEX.md`, `business-skills/START_HERE.md` when the guide changes, the owning sub-agent, and the
  Workspace Chief route if routing changed.
- **Template/reference changes update their maps.** Adding, updating, renaming, or removing files in
  `business-practices/templates/` or `business-practices/references/` must update that folder's `INDEX.md`.
- A stale index is worse than none - it sends agents to the wrong place. Update it in the same step
  you create or change the file, not "later."

## Business docs

- If business direction, audience, positioning, goal, or strategy changes and the source is clear,
  update `{{DOCS_ROOT}}/business-profile.md`. Ask first only when the change conflicts with an
  established direction or needs judgment the source material does not answer.
- If another business doc should change and the needed update is clear, route through the
  documentation-steward or make the update. Ask only when you are unsure what should be captured.
- Keep documentation connected: every durable artifact should be findable from an `INDEX.md`.
- Check the boundary in [AGENTS.md](../../AGENTS.md): business docs describe the user's business, while
  Workspace Chief, sub-agents, skills, and indexes are workspace machinery. If a business artifact mentions
  workspace machinery as if it is the business, fix it or ask the owner if that was intentional.

## Capture vs. data

- **Capture** (notes, summaries, discussion) -> Markdown prose.
- **Data** (comparisons, scoring, structured lists, anything you'd filter or sort) -> a Markdown
  table, or a `.json` / sheet. Give the note coordinates instead of leaving it as a floating sentence.

## Never overwrite raw input

Raw notes, transcripts, and pasted material stay exactly as captured. Summaries and artifacts are
always **new** files. Store the raw layer under an artifact-local `raw/` folder so it remains
available as source evidence without becoming the main context surface.

Loose raw notes are inbox items, not final organization. If a notes file lands directly under
`{{DOCS_ROOT}}/meetings/`, create the dated meeting folder, move the raw source into `raw/`
(`raw/raw-notes.md` for text notes), write `summary.md`, and update `{{DOCS_ROOT}}/meetings/INDEX.md`.
After the raw archive exists, remove the loose inbox file. If a meeting folder still has an old
top-level `raw_notes.md`, move it to `raw/raw-notes.md` and remove the top-level file.

## Checklist before you finish any task that changed the workspace

1. Right folder? (Created a subfolder if it earned one.)
2. Descriptive slug in `lower-kebab-case`, date-prefixed as `MMM-DD-YYYY` only if time-ordered,
   `.md` for text?
3. Raw input left untouched?
4. Nearest `INDEX.md` updated? (And root index, if a new area.)
5. Operating-layer concepts kept out of business artifacts unless explicitly intended?
6. Business docs updated or explicitly left unchanged?
