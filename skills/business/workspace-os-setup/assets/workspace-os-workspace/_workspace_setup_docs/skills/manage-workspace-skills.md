# Manage Workspace Best Practices

> **Agent-facing:** The user supplies intention, preferences, and examples. The agent manages the
> skill/template/reference files, specialists, routing, and indexes.

Use this when a reusable workflow, output structure, format, example, or specialist should be created,
changed, merged, or removed.

## Decision rule

- Decide the layer first: will this be reused across many future pieces of work
  (→ `workspace-best-practices/`), or is it the work/knowledge itself (→ `{{DOCS_ROOT}}/`)? A
  voice/tone guide, brand examples, and exact output formats are reused references, not hub-docs
  content, even if they came up while discussing a content or marketing area.
- Keep the four common skills only while useful: summarize notes, brainstorm, synthesize outcomes,
  and document context.
- Create or update a skill immediately for an explicit reusable preference.
- Create a skill for a recurring workflow or output shape; keep one-off work one-off.
- Add a specialist only when a distinct recurring role improves routing. The Workspace Chief can
  apply many skills directly.
- When content folders/subfolders change, review related skills, templates, references, and agents in
  the same pass. Less is more.

## Implement

1. Inspect `workspace-best-practices/`, `agents/sub-agents/INDEX.md`,
   `agents/workspace-chief.md`, and the relevant content indexes.
2. Put reusable judgment and workflow instructions in
   `workspace-best-practices/skills/<lower-kebab-case>.md`.
3. Put exact output shapes in `workspace-best-practices/templates/` and examples, source material,
   voice, or style samples in `workspace-best-practices/references/`.
4. State what triggers the skill, what it produces, which template/reference it uses, and where the
   output belongs. Skills are authoritative for output structure and format.
5. Add, revise, merge, or remove the matching specialist and Workspace Chief route only as needed.
6. Update every affected index and search for stale links or orphaned routes.
7. Apply [apply-workspace-struct.md](apply-workspace-struct.md).

Tell the owner what changed in plain language and offer one realistic test prompt. Do not ask them to
configure files manually.
