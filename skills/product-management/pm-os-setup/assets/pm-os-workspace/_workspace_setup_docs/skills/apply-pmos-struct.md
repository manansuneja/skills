# Skill: Apply PM OS Structure

> **Agent-facing:** Protected PM OS playbook. The PM normally does not need to edit this file.

Apply this after any task that creates, moves, renames, removes, or meaningfully edits workspace
content. It keeps product memory focused, connected, and findable.

## Naming

- Use `lower-kebab-case` for descriptive files and folders.
- Prefix genuinely time-ordered artifacts with `MMM-DD-YYYY`, such as
  `Jan-15-2026-pricing-decision.md`.
- Use stable topic-first folders for ongoing areas. For PRDs, mirror product scope with area,
  initiative, feature, and story levels when useful.
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

1. List the actual tree under `product-docs/` and `product-practices/`, plus immediate root entries.
   Compare paths with nearest indexes. Inspect names and index presence first; read contents only
   when necessary to infer purpose.
2. Ignore `raw/`, hidden/tool folders, workspace machinery, dependency/build outputs, and archives
   unless the task involves them.
3. For a user-created folder or subfolder missing an index:
   - preserve contents and location;
   - infer a concise purpose from its name and nearby material;
   - create `INDEX.md` with the appropriate audience label;
   - link it from its parent and the product-docs/root map when applicable.
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
| PRD | `product-docs/prds/<area-or-initiative>/<feature>/prd.md` with stories as needed |
| Profile-driven artifact | The customized area and format defined by its product skill/template |

If a new artifact type repeats, create a focused area with `INDEX.md` and update product-docs and
root maps.

## INDEX.md rules

- Every PM OS content folder has an `INDEX.md`; tool config and `raw/` archives do not need one.
- Every meaningful change updates the nearest index in the same change.
- A top-level add, rename, or removal also updates product-docs and root indexes.
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
4. Are nearest, product-docs, and root indexes current?
5. Are links, routes, skills, and specialists free of orphans?
6. Is the audience label clear?
7. Is product vision current without mixing PM OS machinery into product content?
8. Are all user-created folders, subfolders, and files accounted for?
9. Do product practices and specialists match the current content structure?
