# Welcome to {{BUSINESS_NAME}} Workspace OS

This workspace is for running business work with an AI agent. You do not need to learn commands or
pick the right file first. Open this folder in your agent tool and talk naturally.

## How to start

Say what you need in plain language:

- "I had a meeting. Here are the notes."
- "What should we prioritize for the package?"
- "Turn this into an offer brief with packages and client stories."
- "Capture this decision."
- "Help me think through the onboarding flow."
- "Draft a client update from this progress."
- "Create or update a skill for how I like offer briefs written."

The agent should read [AGENTS.md](AGENTS.md), act as the Workspace Chief, route the work to the right
specialist, create or update the right files, and give you a short handoff with the file path and top
takeaway.

## What gets organized

Business work lives in [{{DOCS_ROOT}}/]({{DOCS_ROOT}}/INDEX.md):

- `meetings/` - meeting summaries plus raw source archives.
- `outcomes/` - recommendations, prioritization, scope cuts, and conclusions.
- `decisions/` - decisions and why they were made.
- `offers/` - area/package -> offer -> client stories.
- `brand-and-delivery/` - brand and delivery considerations, UX flows, usability notes, and trade-offs.
- `metrics/` - metric reads, funnels, experiments, and quantitative evidence.
- `plans/` - now/next/later plans, releases, themes, and sequencing.
- `client-comms/` - updates, briefs, launch notes, and alignment messages.

You can paste notes, drag files into the workspace, or describe the work in chat. The agent should
preserve raw input, create durable artifacts, update indexes, and keep the context connected over
time.

## First-time personalization

If `_workspace_setup_docs/personalization/` still exists, the workspace is still generic. Tell your agent:

> Customize my workspace.

It will ask a few lightweight questions, personalize the business context and working style, then
delete `_workspace_setup_docs/personalization/` when it is done.

## Keeping Workspace OS updated

If you installed Workspace OS globally and want the latest `workspace-os-setup` changes from GitHub, run:

```bash
npx skills@latest update workspace-os-setup -g
```

## How it learns your style

If you want a different format, voice, folder, or workflow, just say so. The agent can update the
business skills in [business-skills/](business-skills/INDEX.md). Start with
[business-skills/START_HERE.md](business-skills/START_HERE.md) to see the base skill set. When a skill changes, the
agent should also update the indexes, matching sub-agent, and routing so your preferences become part
of the OS instead of something you repeat every time.

You can also add examples and templates:

- Put reusable blank formats in [business-practices/templates/](business-practices/templates/INDEX.md), such as story,
  offer, project, meeting summary, offer brief, plan, or client update templates.
- Put examples and style samples in [business-practices/references/](business-practices/references/INDEX.md), such as how you
  write meeting minutes or what a good update sounds like.

Then tell the agent what they should influence.
