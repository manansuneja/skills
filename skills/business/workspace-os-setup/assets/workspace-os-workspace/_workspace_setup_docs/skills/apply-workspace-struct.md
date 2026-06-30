# Skill: Apply Workspace Structure

> **Agent-facing:** Protected Workspace OS playbook. The user normally does not need to edit this file.

Apply this after any task that creates, moves, renames, removes, or meaningfully edits workspace
content. It keeps the workspace focused and findable instead of letting memory become a pile.

## Naming

- Use `lower-kebab-case` for descriptive files and folders. Avoid spaces, capitals, and punctuation.
- Prefix genuinely time-ordered artifacts with `MMM-DD-YYYY`, such as
  `Jan-15-2026-pricing-decision.md`.
- Use stable topic-first folders for ongoing bodies of work. Put dates inside the artifact when the
  topic should remain stable.
- Use Markdown for narrative text.

## Focused folder lifecycle

- A top-level content area must support active or near-term work and have a distinct purpose grounded
  in the workspace category or requirements.
- Use category-specific subfolders for real entities or lifecycle stages; use structured trackers for
  repeated fields and status rather than flattening domain detail into generic buckets.
- Reuse an existing area when its purpose overlaps; do not create a new folder for every artifact.
- When personalization or later cleanup shows an area is irrelevant:
  - remove it directly only when it is generated-empty (no content beyond an unchanged starter
    `INDEX.md`);
  - ask once before deleting or relocating user-authored files, raw input, custom index content,
    links, or nested artifacts;
  - keep it if relevance is uncertain and the user does not answer.
- Removing an area also removes or revises stale index rows, links, specialist routes, skills, and
  templates that served only that area.
- Adding or materially changing an area also reviews whether its recurring outputs need a skill,
  template, reference, or distinct specialist. Keep all layers synchronized and minimal.
- Do not recreate a removed starter area merely because the generic scaffold once contained it.

## Automatic structural reconciliation

Run this lightweight pass whenever `AGENTS.md` is read at the start of a session:

1. List the actual tree under `{{DOCS_ROOT}}/` and `workspace-best-practices/`, plus immediate root
   entries. Compare paths with the nearest indexes. Inspect names and index presence first; read file
   contents only when needed to infer purpose.
2. Ignore `raw/`, hidden/tool folders, workspace machinery, dependency/build outputs, and archives
   unless the current task specifically involves them.
3. For a user-created folder or subfolder missing an index:
   - preserve its contents and location;
   - infer a concise purpose from its name and nearby material;
   - create `INDEX.md` with the appropriate audience label;
   - link it from the parent index and docs-root/root map when applicable.
4. For an unindexed user-created file, add it to the nearest index and connect it to an existing
   area, tracker, template, skill, or route when the relationship is clear.
5. If a root-level user folder clearly belongs under `{{DOCS_ROOT}}/`, integrate it into the maps
   immediately. Move or rename it only when placement is unambiguous and references will remain safe;
   otherwise leave it in place, index it, and ask one concise question.
6. Do not ask permission merely to create indexes, update maps, or connect clear routing. Do not
   delete, overwrite, or silently rename user-created content.

Report reconciled additions briefly. This is background maintenance, not a task the user must manage.

## Artifact placement

- A thing with multiple files earns its own folder—for example, a meeting with a clean summary and a
  `raw/` archive.
- Mirror the shape of similar existing artifacts.
- These are starter patterns, not mandatory areas; use them only when the folder survived
  personalization or the user has now approved it.

| Artifact | Typical location |
|---|---|
| Meeting | `{{DOCS_ROOT}}/meetings/<MMM-DD-YYYY>-<title>/summary.md` + `raw/raw-notes.md` |
| Outcome | `{{DOCS_ROOT}}/outcomes/<MMM-DD-YYYY>-<topic>.md` |
| Decision | `{{DOCS_ROOT}}/decisions/<MMM-DD-YYYY>-<decision>.md` |
| Workspace profile | `{{DOCS_ROOT}}/workspace-profile.md` |
| Category-specific artifact | The customized area and format defined by its best-practice skill/template |

If a new artifact type repeatedly appears, create a focused area with an `INDEX.md` and update the
docs-root and root indexes.

## INDEX.md rules

- Every Workspace OS content folder has an `INDEX.md`. Tool config and `raw/` archives do not need one.
- Every meaningful change updates the nearest index in the same change.
- A top-level add, rename, or removal also updates the docs-root and root indexes.
- Skill changes update `workspace-best-practices/skills/INDEX.md`, the owning specialist, and Workspace Chief route.
- Template/reference changes update the relevant `workspace-best-practices/*/INDEX.md`.
- Search for stale links after moves, renames, or removals.

## Audience labels

Keep the intended surface obvious near the top of files and folder indexes:

- `{{DOCS_ROOT}}/`: **Your primary workspace** or **Your workspace content**.
- `workspace-best-practices/`: **For you and your agents**—the shared customization center.
- `agents/`, `_workspace_setup_docs/`, `AGENTS.md`, `CLAUDE.md`, and tool rules: **Agent-facing**.

Do not make the user learn or manually maintain agent-facing machinery.

## Profile and layer boundary

- Update `{{DOCS_ROOT}}/workspace-profile.md` when durable purpose, audience, focus, objective, or
  constraints change and the source is clear.
- Ask before overwriting an established direction or making a judgment the source does not support.
- Content files describe the user's real work. Workspace Chief, sub-agents, skills, and indexes are
  machinery; do not present them as the user's subject matter unless explicitly intended.

## Never overwrite raw input

Preserve notes, transcripts, pasted material, and source files exactly under an artifact-local
`raw/` folder. Create summaries and synthesized artifacts separately. A loose source is an inbox item:
archive it, create the clean artifact, update the index, then remove the duplicate inbox copy only
after the archive exists.

## Checklist

1. Does every kept or new area support active/near-term work?
2. Is the artifact in the right folder with a clear `lower-kebab-case` name?
3. Is raw input preserved?
4. Are the nearest, docs-root, and root indexes current as applicable?
5. Are links, routes, skills, and specialists free of orphans?
6. Is the audience label clear?
7. Is the workspace profile current without mixing machinery into user content?
8. Are all user-created folders, subfolders, and files accounted for in the nearest indexes?
9. Do the relevant skills, templates, and sub-agents still match the current content structure?
