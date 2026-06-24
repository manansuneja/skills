# Manage Workspace Skills

Use this when the PM wants to create, update, improve, merge, or remove a workspace skill.

Skills are the PM OS's reusable judgment. They should be specific enough to guide future agents, but
small enough that a human can scan them quickly.

## Before editing

1. Check `skills/INDEX.md` to see what already exists.
2. Check `agents/pm-chief.md` and `agents/sub-agents/INDEX.md` to see which agents should use the skill.
3. If available, use the local or installed `skill-creator` skill as the authoring guide.
4. If `skill-creator` is not available, ask whether to install it:

   ```powershell
   npx skills add https://github.com/anthropics/skills --skill skill-creator
   ```

## Create a skill

- Name it `lower-kebab-case.md`.
- Put it under `skills/`.
- Start with a short purpose statement: when to use it and what outcome it should produce.
- Include only the workflow, standards, and examples needed to make the skill usable.
- Avoid repeating broad workspace rules already covered by `apply-pmos-struct.md`.

## Update a skill

- Preserve what works.
- Replace vague instructions with concrete steps, decision rules, or examples.
- Remove stale product assumptions if the product vision changed.
- Keep the skill aligned with `product-docs/product-vision.md`.

## After editing

- Update `skills/INDEX.md`.
- Update `agents/pm-chief.md` or the relevant sub-agent if routing changed.
- Run `apply-pmos-struct.md`: check names, folders, links, and nearest `INDEX.md` updates.
- Tell the PM what changed and suggest one realistic test prompt.
