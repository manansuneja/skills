# Skill: Apply PM OS Structure

> **Agent-facing:** Protected PM OS playbook. The PM normally does not need to edit this file.

Apply this after any task that creates, moves, renames, removes, or meaningfully edits workspace
content. It keeps product memory focused, connected, and findable.

## Naming

- Use `lower-kebab-case` for descriptive files and folders.
- Prefix genuinely time-ordered artifacts with `MMM-DD-YYYY`, such as
  `Jan-15-2026-pricing-decision.md`.
- Use stable topic-first folders for ongoing areas. Active work lives in
  `product-docs/projects/<project-slug>/`; PRDs mirror product scope inside it with feature and
  story levels when useful.
- Use Markdown for narrative text and structured formats for repeated data.

## Focused folder lifecycle

- A top-level product area must support active or near-term work and have a purpose grounded in the
  product stage, PM scope, or explicit requirements.
- Use product-surface, customer, or lifecycle subfolders for real structure; use trackers for repeated
  fields, owners, status, evidence, metrics, confidence, dates, and dependencies.
- Reuse an existing area when its purpose overlaps. Do not scaffold every possible PM lane.
- When personalization or cleanup shows an area is irrelevant:
  - remove it directly only when it is generated-empty—nothing beyond an unchanged starter
    `INDEX.md`;
  - ask once before deleting or relocating user-authored files, raw input, custom indexes, links, or
    nested artifacts;
  - keep it when relevance is uncertain and the PM does not answer.
- Removing an area also removes or revises stale index rows, links, specialist routes, skills, and
  templates serving only that area.
- Adding or materially changing an area triggers a review of its skills, templates, references,
  trackers, and optional specialist. Keep every layer synchronized and minimal.
- Do not recreate an optional starter area merely because an older scaffold contained it.

## Automatic structural reconciliation

Run this lightweight pass whenever `AGENTS.md` is read at the start of a session:

1. List the actual tree under `product-docs/` (including each project folder) and
   `product-practices/`, plus immediate root entries.
   Compare paths with nearest indexes. Inspect names and index presence first; read contents only
   when necessary to infer purpose.
2. Ignore `raw/`, hidden/tool folders, workspace machinery, dependency/build outputs, and archives
   unless the task involves them.
3. For a user-created folder or subfolder missing from the nearest index:
   - preserve contents and location;
   - infer a concise purpose from its name and nearby material;
   - link it from the nearest useful parent index;
   - create a human-readable local `INDEX.md` only when it is a meaningful content domain,
     substantial subdomain, or multi-file artifact that benefits from its own workboard/map.
4. For an unindexed user-created file, add it to the nearest index and connect it to an existing
   product area, tracker, template, skill, or route when the relationship is clear.
5. If a root-level user folder clearly belongs under `product-docs/`, integrate it into maps
   immediately. Move or rename it only when placement is unambiguous and references remain safe;
   otherwise leave it in place, index it, and ask one concise question.
6. Do not ask permission merely to create indexes, update maps, or connect clear routing. Never
   delete, overwrite, or silently rename user-created content.

Report reconciled additions briefly. This is background maintenance, not work the PM must manage.

## Artifact placement

- A thing with multiple files earns its own folder—for example, a meeting with a summary and `raw/`
  archive or a feature with a PRD and stories.
- Mirror the shape of similar artifacts already in the workspace.
- These are starter patterns, not mandatory areas. Optional product lanes should exist only when
  personalization or later usage earns them.

| Artifact | Typical location |
|---|---|
| Product vision | `product-docs/product-vision.md` |
| Meeting | `product-docs/meetings/<MMM-DD-YYYY>-<title>/summary.md` + `raw/raw-notes.md` |
| Outcome | `product-docs/outcomes/<MMM-DD-YYYY>-<topic>.md` |
| Decision | `product-docs/decisions/<MMM-DD-YYYY>-<decision>.md` |
| Project | `product-docs/projects/<project-slug>/` with `INDEX.md`, `brief.md`, `status.md` |
| PRD | `product-docs/projects/<project-slug>/prd.md`, or `features/<feature-slug>/prd.md` with stories as needed |
| Build brief | `product-docs/projects/<project-slug>/build-brief.md`, or beside the feature's PRD |
| Project-scoped meeting, outcome, decision | `product-docs/projects/<project-slug>/{meetings,outcomes,decisions}/` |
| Profile-driven artifact | The customized area and format defined by its product skill/template |

If a new artifact type repeats, create a focused area with `INDEX.md` and update product-docs and
root maps.

Narrative artifacts are Markdown-first. A plain request for a PRD, brief, plan, decision, or
synthesis creates `.md`. Use an installed document, presentation, spreadsheet, design, research, or
other specialized capability only when requested or clearly required. Store any heavier deliverable
beside its Markdown source or supporting context and index both.

## Filing by scope

- Work that belongs to one initiative goes inside its project; subfolders appear when first needed.
- Knowledge that outlives a project or spans projects stays in the global `meetings/`, `outcomes/`,
  and `decisions/` folders, plus `product-vision.md`.
- Every decision, whatever its scope, also gets a row in the global decisions log with a Scope value.
- A project's stage and health live in `status.md` and are mirrored in the portfolio table and, when
  active work changes, the root workboard. Update them in the same change.
- Finished or paused projects keep their folders: set the stage to `done` or `parked` and log why.
- Application code never lives in the workspace; link the repository from the project's `brief.md`.

## INDEX.md rules

- Root `INDEX.md` is a human-first living workboard plus high-level navigation, not an exhaustive
  machine inventory.
- Meaningful content domains, substantial subdomains, and multi-file artifacts get a local
  `INDEX.md`. Tiny leaf folders, tool config, and `raw/` archives do not need one.
- Every meaningful change updates the nearest useful index in the same change.
- A change to active work, waiting items, recent decisions/outcomes, or top-level navigation also
  updates the root index.
- Skill changes update `product-practices/skills/INDEX.md`, the owning specialist, and Chief PM route.
- Template/reference changes update the relevant `product-practices/*/INDEX.md`.
- Search for stale links after moves, renames, or removals.

## Audience labels

Keep the intended surface obvious near the top:

- `product-docs/`: **Your primary product workspace** or **Your product content**.
- `product-practices/`: **For you and your agents**—the shared customization center.
- `agents/`, `_workspace_setup_docs/`, `AGENTS.md`, `CLAUDE.md`, and tool rules: **Agent-facing**.

Do not make the PM learn or manually maintain agent-facing machinery.

## Product boundary

- Update `product-docs/product-vision.md` when durable product purpose, audience, stage, goals, bets,
  evidence, or constraints change and the source is clear.
- Ask before overwriting established direction or making a judgment the source does not support.
- Product docs describe the user's product. Chief PM, specialists, skills, and indexes are machinery;
  do not present them as product actors unless explicitly intended.

## Never overwrite raw input

Preserve notes, transcripts, pasted material, screenshots, and source files exactly under an
artifact-local `raw/` folder. Create summaries and synthesized artifacts separately. A loose source
is an inbox item: archive it, create the clean artifact, update the index, and remove the duplicate
inbox copy only after the archive exists.

## Checklist

1. Does every kept or new area support active or near-term PM work?
2. Is the artifact in the right folder with a clear name?
3. Is raw input preserved?
4. Are the nearest useful index and the human workboard current?
5. Are links, routes, skills, and specialists free of orphans?
6. Is the audience label clear?
7. Is product vision current without mixing PM OS machinery into product content?
8. Are all user-created folders, subfolders, and files discoverable from the nearest useful index?
9. Do product practices and specialists match the current content structure?
10. Is each artifact filed by scope, with the project status, portfolio row, and decisions log in sync?
