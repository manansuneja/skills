# Manage Product Practices

> **Agent-facing:** The PM supplies intentions, preferences, and examples. The agent manages skills,
> templates, references, specialists, routing, and indexes.

Use this when a reusable PM workflow, output structure, exact format, example, or specialist should
be created, changed, merged, or removed.

## Decision rule

- Decide the layer first: current product work belongs in `product-docs/`; reusable judgment,
  formats, and examples belong in `product-practices/`.
- Keep the small PM core only while useful: summarize notes, brainstorm, synthesize outcomes,
  document product context, and write PRDs.
- Determine durability semantically from intent and scope. Consider whether the guidance is presented
  as an organizational standard, broadly applicable method, canonical example, recurring workflow,
  or correction to the normal approach. Do not require a direct request to remember or reuse it.
- When confidence is high, update the relevant existing skill/template/reference immediately. When
  the same request also asks for an artifact, do both in the same task.
- Ask one concise question only when persistence is genuinely ambiguous and would materially affect
  future outputs. Otherwise keep truly task-local guidance local.
- Create a new skill only when no existing skill owns the reusable judgment or output shape.
- Add a specialist only when a distinct recurring role improves routing. The Chief PM can apply many
  skills directly.
- When product folders or lifecycle stages change, review related skills, templates, references,
  agents, and routes in the same pass. Less is more.

## Implement

1. Inspect `product-practices/`, `agents/sub-agents/INDEX.md`, `agents/pm-chief.md`, and relevant
   product indexes.
2. Put reusable judgment and workflow instructions in
   `product-practices/skills/<lower-kebab-case>.md`.
3. Put exact output shapes in `product-practices/templates/` and examples, source material, voice,
   principles, or style samples in `product-practices/references/`.
4. State the semantic conditions that make the skill relevant, what it produces, which
   template/reference it uses, and where the output belongs. Avoid brittle keyword lists. Skills are
   authoritative for output structure and format.
5. Add, revise, merge, or remove a matching specialist and Chief PM route only as needed.
6. Update every affected index and search for stale links or orphaned routes.
7. Apply [apply-pmos-struct.md](apply-pmos-struct.md).

Tell the PM what changed in plain language and offer one realistic test prompt. Do not ask them to
configure files manually.
