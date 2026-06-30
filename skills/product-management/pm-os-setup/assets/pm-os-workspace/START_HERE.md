# Welcome to {{PROJECT_NAME}} PM OS

This workspace is for running product work with an AI agent. You do not need to learn commands or
pick the right file first. Open this folder in your agent tool and talk naturally.

## How to start

Say what you need in plain language:

- "I had a meeting. Here are the notes."
- "What should we prioritize for the MVP?"
- "Turn this into a PRD with features and stories."
- "Capture this decision."
- "Help me think through the onboarding flow."
- "Draft a stakeholder update from this progress."
- "Create or update a skill for how I like PRDs written."

The agent should read [AGENTS.md](AGENTS.md), act as the Chief PM, route the work to the right
specialist, create or update the right files, and give you a short handoff with the file path and top
takeaway.

## What gets organized

Product work lives in [product-docs/](product-docs/INDEX.md):

- `meetings/` - meeting summaries plus raw source archives.
- `outcomes/` - recommendations, prioritization, MVP cuts, and conclusions.
- `decisions/` - decisions and why they were made.
- `prds/` - area/MVP -> feature -> stories.
- `design/` - design considerations, UX flows, usability notes, and trade-offs.
- `data-insights/` - metric reads, funnels, experiments, and quantitative evidence.
- `roadmaps/` - now/next/later plans, releases, themes, and sequencing.
- `stakeholder-comms/` - updates, briefs, launch notes, and alignment messages.

You can paste notes, drag files into the workspace, or describe the work in chat. The agent should
preserve raw input, create durable artifacts, update indexes, and keep the context connected over
time.

## First-time personalization

If `_workspace_setup_docs/personalization/` still exists, the workspace is still generic. Tell your agent:

> Customize my workspace.

It will ask a few lightweight questions, personalize the product context and working style, then
delete `_workspace_setup_docs/personalization/` when it is done.

## Keeping PM OS updated

If you installed PM OS globally and want the latest `pm-os-setup` changes from GitHub, run:

```bash
npx skills@latest update pm-os-setup -g
```

## How it learns your style

If you want a different format, voice, folder, or workflow, just say so. The agent can update the
product skills in [product-skills/](product-skills/INDEX.md). Start with
[product-skills/START_HERE.md](product-skills/START_HERE.md) to see the base skill set. When a skill changes, the
agent should also update the indexes, matching sub-agent, and routing so your preferences become part
of the OS instead of something you repeat every time.

You can also add examples and templates:

- Put reusable blank formats in [product-practices/templates/](product-practices/templates/INDEX.md), such as story,
  feature, epic, meeting summary, PRD, roadmap, or stakeholder update templates.
- Put examples and style samples in [product-practices/references/](product-practices/references/INDEX.md), such as how you
  write meeting minutes or what a good update sounds like.

Then tell the agent what they should influence.
