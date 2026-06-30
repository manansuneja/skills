# Manage Workspace Skills

Use this when the PM wants to create, update, improve, merge, or remove a workspace skill.

Skills are the PM OS's reusable judgment. They should be specific enough to guide future agents, but
small enough that a human can scan them quickly.

Shared templates live in `product-practices/templates/`. Shared examples, samples, and style references live in
`product-practices/references/`. Prefer putting reusable artifact shapes there instead of bloating individual
skills.

## Before editing

1. Check `product-skills/START_HERE.md` and `product-skills/INDEX.md` to see what already exists.
2. Check `product-practices/templates/INDEX.md` and `product-practices/references/INDEX.md` for reusable formats or
   examples the skill should use.
3. Check `agents/pm-chief.md` and `agents/sub-agents/INDEX.md` to see which agents should use the skill.
4. If available, use the local or installed `skill-creator` skill as the authoring guide.
5. If `skill-creator` is not available, ask whether to install it:

   ```text
   npx skills add https://github.com/anthropics/skills --skill skill-creator
   ```

## Create a skill

- Name it `lower-kebab-case.md`.
- Put it under `product-skills/`.
- Start with a short purpose statement: when to use it and what outcome it should produce.
- Include only the workflow, standards, and examples needed to make the skill usable.
- If the skill needs a reusable output shape, put that shape in `product-practices/templates/` and link to it.
- If the skill needs examples or voice/context samples, put those in `product-practices/references/` and link to
  them.
- Avoid repeating broad workspace rules already covered by `apply-pmos-struct.md`.
- Decide whether it needs a matching sub-agent persona under `agents/sub-agents/`. If it does, create
  that file, add it to `agents/sub-agents/INDEX.md`, and register the route in `agents/pm-chief.md`.
- If the skill is only structural glue, document who applies it instead of creating a fake specialist.

## Update a skill

- Preserve what works.
- Replace vague instructions with concrete steps, decision rules, or examples.
- Remove stale product assumptions if the product vision changed.
- Keep the skill aligned with `product-docs/product-vision.md`.
- Update the matching sub-agent if the skill's purpose, workflow, or handoff changed.
- Update `agents/pm-chief.md` if the trigger language, route, or specialist changed.

## Remove or merge a skill

- Remove the skill file only after checking where it is referenced.
- Remove or rewrite the matching sub-agent if it no longer has a skill to apply.
- Remove the row from `product-skills/INDEX.md`.
- Remove or update the row from `agents/sub-agents/INDEX.md`.
- Remove or update routing in `agents/pm-chief.md`.
- Update any tool-facing copies if they exist, such as `.github/agents/` for GitHub Copilot or
  `.claude/agents/` for Claude Code.
- Search the workspace for stale links to the removed skill or sub-agent before handing back.

## After editing

- Update `product-skills/START_HERE.md` if the base skill list or instructions changed.
- Update `product-skills/INDEX.md`.
- Update `product-practices/templates/INDEX.md` or `product-practices/references/INDEX.md` if templates or references
  changed.
- Update `agents/sub-agents/INDEX.md`.
- Update `agents/pm-chief.md` and the relevant sub-agent if routing changed.
- Ensure no sub-agent points at a missing skill, and no routed skill is missing a clear owner.
- Run `apply-pmos-struct.md`: check names, folders, links, and nearest `INDEX.md` updates.
- Tell the PM what changed and suggest one realistic test prompt.
