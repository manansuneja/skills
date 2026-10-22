# Welcome to {{PROJECT_NAME}} PM OS

> **For you:** This is the human welcome guide. Work mainly in `product-docs/`; the agent manages
> indexes, skills, routes, and setup machinery for you.

This workspace is for running product work with an AI agent. You do not need to learn commands or
choose the right file first. Open the folder in your agent tool and talk naturally.

## How to start

Try requests such as:

- “I had a customer meeting. Here are the notes.”
- “What should we prioritize for the MVP?”
- “Start a project for the onboarding redesign.”
- “Turn this into a PRD with features and stories.”
- “Write a build brief my coding agent can follow.”
- “Where do all my projects stand?”
- “Capture this decision and its rationale.”
- “Help me explore options for onboarding.”
- “Create a reusable format for experiment readouts.”

The agent should act as the Chief PM, use only relevant context, create or update durable product
artifacts, and give you a short handoff with paths and top takeaways. Product writing stays in fast,
portable Markdown unless you explicitly ask for another format. When an appropriate installed skill
is available, the Chief PM can use it as a specialist and still file the result inside PM OS.

## Your product workspace

Core product work starts in [product-docs/](product-docs/INDEX.md):

- `product-vision.md` — product, users, problem, stage, goals, bets, and constraints.
- `projects/` — one folder per initiative: brief, status, requirements, build brief, and the
  meetings, decisions, and outcomes that belong to it.
- `meetings/` — product-wide summaries with preserved raw source archives.
- `outcomes/` — product-wide recommendations, prioritization, and next steps.
- `decisions/` — every decision and why it was made, across all projects.

Active work lives in a project; knowledge that outlives any one project stays in the shared folders.
You do not need to decide where things go; the agent files them by scope.

## Think and build

Each project has a stage: discover, define, build, launch, or learn. Early on, the agent helps you
think: evidence, options, decisions, and requirements. Later it helps you build: a build brief that a
coding agent or an engineering team can work from, a check of what comes back against the acceptance
criteria, and a record of what you learned. Your PM profile in `AGENTS.md` records whether you hand
work to engineers or also build with coding agents. Application code stays in your code repository,
not in this workspace.

Your setup may add research, design, experiments, data, roadmaps, launches, stakeholder
communications, or other areas when they fit your product stage and responsibilities. It should not
add every possible PM lane by default.

## Let the workspace evolve

Ask the agent directly whenever you want to add a folder, subfolder, tracker, workflow, template,
skill, or specialist. Describe the intention; the agent handles files, indexes, and routing.

You can also add a folder or file manually. The next agent session should detect it automatically,
preserve it, connect it to the nearest useful index, and ask only when its purpose or placement is
unclear. Substantial areas get their own human-readable `INDEX.md`; tiny folders can stay listed in
their parent index.

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
