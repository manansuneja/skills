# Welcome to {{PROJECT_NAME}} PM OS

> **For you:** This is the human welcome guide. Work mainly in `product-docs/`; the agent manages
> indexes, skills, routes, and setup machinery for you.

This workspace is for running product work with an AI agent. You do not need to learn commands or
choose the right file first. Open the folder in your agent tool and talk naturally.

## How to start

Try requests such as:

- “I had a customer meeting. Here are the notes.”
- “What should we prioritize for the MVP?”
- “Turn this into a PRD with features and stories.”
- “Capture this decision and its rationale.”
- “Help me explore options for onboarding.”
- “Create a reusable format for experiment readouts.”

The agent should act as the Chief PM, use only relevant context, create or update durable product
artifacts, and give you a short handoff with paths and top takeaways.

## Your product workspace

Core product work starts in [product-docs/](product-docs/INDEX.md):

- `product-vision.md` — product, users, problem, stage, goals, bets, and constraints.
- `meetings/` — summaries with preserved raw source archives.
- `outcomes/` — recommendations, prioritization, MVP cuts, and next steps.
- `decisions/` — decisions and why they were made.
- `prds/` — product-area, initiative, feature, and story requirements.

Your setup may add research, design, experiments, data, roadmaps, launches, stakeholder
communications, or other areas when they fit your product stage and responsibilities. It should not
add every possible PM lane by default.

## Let the workspace evolve

Ask the agent directly whenever you want to add a folder, subfolder, tracker, workflow, template,
skill, or specialist. Describe the intention; the agent handles files, indexes, and routing.

You can also add a folder or file manually. The next agent session should detect it automatically,
preserve it, create any missing `INDEX.md`, connect it to the workspace map, and ask only when its
purpose or placement is unclear.

## Customize how product work is done

[product-practices/](product-practices/INDEX.md) is the shared customization center:

- [skills/](product-practices/skills/INDEX.md) controls recurring judgment, workflows, and output
  structure.
- [templates/](product-practices/templates/INDEX.md) contains exact reusable formats.
- [references/](product-practices/references/INDEX.md) contains examples, source material, product
  principles, voice, and style guidance.

You do not need to configure these files manually. Add an example or describe what you prefer, then
ask the agent to update the appropriate product practice. It should synchronize the matching skill,
specialist, Chief PM route, and indexes.

The workspace should also recognize durable guidance from context. When you describe an
organization-wide method, canonical format, recurring workflow, or correction meant to improve
future work, the agent should complete the immediate task and capture that practice without making
you separately say “reuse this later.” Truly task-specific instructions should remain local.

## First-time personalization

If `_workspace_setup_docs/personalization/` exists, tell your agent:

> Customize my workspace.

It will ask a few lightweight questions, shape the workspace around your product and PM scope, remove
irrelevant generated-empty areas, personalize product practices and agents, and safely rename the
root folder at the end. The personalization helper disappears when setup is complete.
