# Setup Agent Guide - Personalize This PM OS

You are helping a PM turn this generic PM OS into a workspace shaped around their product.

This setup is a product-context intake, not a filesystem tour. Do not start by explaining folders.
Ask for the product context that will make the Chief PM and specialists useful.

Use the operating-layer vs product-layer boundary in [../AGENTS.md](../AGENTS.md) as the source of
truth. The PM OS maintains the workspace in the background; it is not the user's product unless the
PM explicitly says they are building a PM OS.
Keep that boundary in your own reasoning during intake. Do not explain it to the PM unless their
answers suggest they are mixing the workspace with the product.

When setup is done, delete `_setup/` yourself as the final cleanup step - its absence is how future
sessions know this workspace is personalized. Do not ask the PM for a separate cleanup command.
Durable behavior belongs in `AGENTS.md`, `agents/`, `skills/`, and `product-docs/`.

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

Ask four lightweight questions in one friendly message. Tell the PM rough notes, links, file paths,
or "skip for now" are all fine.

1. What should this workspace be called?
2. What are you building, who is it for, and what problem or opportunity should the workspace keep
   in mind?
3. Where are things today, and what is the next useful outcome? Include stage, current bet,
   near-term goal, or active decision only if known.
4. Is there existing context I should use, such as files in this workspace, folders elsewhere,
   pasted notes, docs, links, decisions, examples, or constraints? Also mention any format or style
   you already want me to follow. If not, I will start with the default PM OS formats and we can
   customize them into skills later.

Do not ask separately about every artifact type. PRD, meeting, decision, brainstorm, and follow-up
preferences can emerge from examples and get captured as skills over time. Detect the main tool from
the host environment when possible; ask only if tool-specific wiring is requested or unclear.

If the answers are thin, ask at most one follow-up round. Prioritize missing product context,
near-term goal, and context files over PM-process preferences.

## Step 2 - Apply the context

Work from the workspace root.

1. Replace `{{PROJECT_NAME}}` outside `_setup/`.
2. Update `START_HERE.md` with a short product-specific introduction if useful.
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

```text
npx skills add https://github.com/anthropics/skills --skill skill-creator
```

Do not run external install commands silently.

## Step 4 - Handoff and cleanup

Prepare a short completion summary with:

- The updated product vision.
- The customized Chief PM summary.
- Any skills or agents changed.
- The key rule: after meaningful changes, the Chief PM applies `apply-pmos-struct.md` so indexes,
  product docs, filenames, and links stay current.

Check the core context is answered: workspace name, product/users, problem/opportunity, stage or
near-term goal, and any existing files or examples the PM wanted used. If setup is complete, **delete
the entire `_setup/` folder before reporting back** - it has done its job, and its absence is how
future sessions know this workspace is personalized. Keep the root `START_HERE.md` as the user's guide.
Do not recreate `_setup/` later. Then send the completion summary.

If required context is missing and you cannot personalize responsibly, leave `_setup/` in place and
ask the smallest follow-up question needed. Do not present deletion as a separate user decision once
the personalization work is complete.
