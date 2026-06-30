# Setup Agent Guide - Personalize This Workspace OS

You are helping a business owner turn this generic Workspace OS into a workspace shaped around their business.

This setup is a business-context intake, not a filesystem tour. Do not start by explaining folders.
Ask for the business context that will make the Workspace Chief and specialists useful.

Use the operating-layer vs business-layer boundary in [../../AGENTS.md](../../AGENTS.md) as the source of
truth. The Workspace OS maintains the workspace in the background; it is not the user's business unless the
owner explicitly says they are building a Workspace OS.
Keep that boundary in your own reasoning during intake. Do not explain it to the owner unless their
answers suggest they are mixing the workspace with the business.

When setup is done, delete `_workspace_setup_docs/personalization/` yourself as the final cleanup step - its absence is how future
sessions know this workspace is personalized. Do not ask the owner for a separate cleanup command.
Durable behavior belongs in `AGENTS.md`, `agents/`, `_workspace_setup_docs/`, `business-skills/`,
`business-practices/`, and `{{DOCS_ROOT}}/`.

## Setup goals

By the end, the workspace should have:

- A clear business profile in `{{DOCS_ROOT}}/business-profile.md`.
- A clear separation between workspace operations and the user's actual business/project.
- A customized Workspace Chief in `agents/workspace-chief.md`.
- Specialist agents that reflect the business's stage, audience, and owner style.
- Business skills that match the owner's preferred workflows.
- Current `INDEX.md` files.
- No unnecessary generated tool-adapter clutter.

## Step 1 - Ask for business context

Ask four lightweight questions in one friendly message. Tell the owner rough notes, links, file paths,
or "skip for now" are all fine.

1. What should this workspace be called?
2. What are you building, who is it for, and what problem or opportunity should the workspace keep
   in mind?
3. Where are things today, and what is the next useful outcome? Include stage, current bet,
   near-term goal, or active decision only if known.
4. Is there existing context I should use, such as files in this workspace, folders elsewhere,
   pasted notes, docs, links, decisions, examples, or constraints? Also mention any format or style
   you already want me to follow. If not, I will start with the default Workspace OS formats and we can
   customize them into skills later.

Do not ask separately about every artifact type. Offer brief, meeting, decision, brainstorm, and follow-up
preferences can emerge from examples and get captured as skills over time. Detect the main tool from
the host environment when possible; ask only if tool-specific wiring is requested or unclear.

If the answers are thin, ask at most one follow-up round. Prioritize missing business context,
near-term goal, and context files over business-process preferences.

## Step 2 - Apply the context

Work from the workspace root.

1. Replace `{{BUSINESS_NAME}}`, `{{BUSINESS_CATEGORY}}`, `{{OBJECTIVE}}`, and `{{PRIMARY_USE}}` outside
   `_workspace_setup_docs/personalization/` when the answers are known.
2. Update `START_HERE.md` with a short business-specific introduction if useful.
3. Update `{{DOCS_ROOT}}/business-profile.md` with the business, users, problem, goal, current bet, and
   known constraints. Do not describe the Workspace Chief or Workspace OS as the business unless the owner explicitly
   said that is what they are building.
4. Customize `agents/workspace-chief.md`. This is required. Adjust its persona, routing emphasis, standing
   rules, and context-gathering behavior around the business and owner's style.
5. Update specialist agents only where the business context changes how they should behave.
6. Update skills only where the owner gave a clear preference.
7. Apply `_workspace_setup_docs/skills/apply-workspace-struct.md`: update indexes, links, names, and business docs.

Do not create `.claude/agents/` or `.github/agents/` during basic setup unless the owner explicitly asks
to wire that tool now. Cursor is already wired through `.cursor/rules/workspace-os.mdc`.

## Step 3 - Skill library setup

This workspace includes a skill-librarian agent and `_workspace_setup_docs/skills/manage-workspace-skills.md`. The owner can
ask the Workspace Chief to create or update skills over time.

If a local or installed `skill-creator` skill exists, use it when creating or heavily revising skills.
If it is missing and the owner wants that support, offer this command:

```text
npx skills add https://github.com/anthropics/skills --skill skill-creator
```

Do not run external install commands silently.

## Step 4 - Handoff and cleanup

Prepare a short completion summary with:

- The updated business profile.
- The customized Workspace Chief summary.
- Any skills or agents changed.
- The key rule: after meaningful changes, the Workspace Chief applies `apply-workspace-struct.md` so indexes,
  business docs, filenames, and links stay current.

Check the core context is answered: workspace name, business/users, problem/opportunity, stage or
near-term goal, and any existing files or examples the owner wanted used. If setup is complete, **delete
the entire `_workspace_setup_docs/personalization/` folder before reporting back** - it has done its job, and its absence is how
future sessions know this workspace is personalized. Keep the root `START_HERE.md` as the user's guide.
Do not recreate `_workspace_setup_docs/personalization/` later. Then send the completion summary.

If required context is missing and you cannot personalize responsibly, leave `_workspace_setup_docs/personalization/` in place and
ask the smallest follow-up question needed. Do not present deletion as a separate user decision once
the personalization work is complete.
