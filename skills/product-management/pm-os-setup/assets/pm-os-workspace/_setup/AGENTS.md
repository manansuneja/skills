# Setup Agent Guide - Personalize This PM OS

You are helping a PM turn this generic PM OS into a workspace shaped around their product.

This setup is a product-context intake, not a filesystem tour. Do not start by explaining folders.
Ask for the product context that will make the Chief PM and specialists useful.

Use the operating-layer vs product-layer boundary in [../AGENTS.md](../AGENTS.md) as the source of
truth. The PM OS maintains the workspace in the background; it is not the user's product unless the
PM explicitly says they are building a PM OS.

When setup is done and the PM confirms, delete `_setup/` yourself - its absence is how future sessions
know this workspace is personalized. Durable behavior belongs in `AGENTS.md`, `agents/`, `skills/`,
and `product-docs/`.

## Setup goals

By the end, the workspace should have:

- A clear product vision in `product-docs/product-vision.md`.
- A clear separation between workspace operations and the user's actual product/project.
- A customized Chief PM in `agents/pm-chief.md`.
- Specialist agents that reflect the product's stage, audience, and PM style.
- Skills that match the PM's preferred workflows.
- Current `INDEX.md` files.
- No unnecessary generated tool-adapter clutter.

## Step 1 - Ask for product context

Ask these in one friendly message. Keep it conversational.

1. Product or project name.
2. What the product/project is, who it serves, and the main problem it solves - distinct from this
   PM OS workspace.
3. Current stage and priority: idea, prototype, beta, launched, growth, turnaround, etc.
4. Current product bet or near-term goal.
5. Existing docs, notes, or decisions that should shape this workspace.
6. How the PM likes PRDs, meetings, decisions, brainstorming, and follow-ups handled.
7. Tool they will use most: Cursor, Claude Code, GitHub Copilot, Codex, or plain chat.

If the answers are thin, ask one follow-up round for the missing context. Be hungry for useful
context, but do not turn setup into a long survey.

## Step 2 - Apply the context

Work from the workspace root.

1. Replace `{{PROJECT_NAME}}` outside `_setup/`.
2. Update `README.md` with a short product-specific introduction.
3. Update `product-docs/product-vision.md` with the product, users, problem, goal, current bet, and
   known constraints. Do not describe the Chief PM or PM OS as the product unless the PM explicitly
   said that is what they are building.
4. Customize `agents/pm-chief.md`. This is required. Adjust its persona, routing emphasis, standing
   rules, and context-gathering behavior around the product and PM's style.
5. Update specialist agents only where the product context changes how they should behave.
6. Update skills only where the PM gave a clear preference.
7. Apply `skills/apply-pmos-struct.md`: update indexes, links, names, and product docs.

Do not create `.claude/agents/` or `.github/agents/` during basic setup unless the PM explicitly asks
to wire that tool now. Cursor is already wired through `.cursor/rules/pm-os.mdc`.

## Step 3 - Skill library setup

This workspace includes a skill-librarian agent and `skills/manage-workspace-skills.md`. The PM can
ask the Chief PM to create or update skills over time.

If a local or installed `skill-creator` skill exists, use it when creating or heavily revising skills.
If it is missing and the PM wants that support, offer this command:

```powershell
npx skills add https://github.com/anthropics/skills --skill skill-creator
```

Do not run external install commands silently.

## Step 4 - Handoff and cleanup

Show the PM:

- The updated product vision.
- The customized Chief PM summary.
- Any skills or agents changed.
- The key rule: after meaningful changes, the Chief PM applies `apply-pmos-struct.md` so indexes,
  product docs, filenames, and links stay current.

Then confirm setup is complete. Check the core questions are answered: product, users, problem,
stage/goal, and PM style. When the PM confirms, **delete the entire `_setup/` folder** - it has done
its job, and its absence is how future sessions know this workspace is personalized. Keep the root
`README.md` as the user's guide. Do not recreate `_setup/` later.
