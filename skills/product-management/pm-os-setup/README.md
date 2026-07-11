# PM OS Setup

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

**Build a PM workspace that gives your agent lasting context about your product.**

PM OS Setup stores your vision, users, meetings, decisions, outcomes, and PRDs as organized files.
A Chief PM agent uses that context to find past work, route new work, and keep recurring outputs
consistent. You stop pasting the same background into every chat.

It is built for PMs and requires no code or database. The workspace starts small, then adds research,
experiments, roadmaps, or specialists only when your work needs them.

## What It Helps PMs Do

- Start every session with an agent that already knows the product: vision, users, open bets, and
  the last decision made.
- Turn meetings, decisions, prioritization calls, MVP cuts, and PRDs into indexed files instead of
  chat scrollback you will never find again.
- Work through one Chief PM that finds context and routes recurring work to the right practice.
- Teach it your formats, voice, and product principles once — every future PRD, readout, or
  stakeholder update follows them.
- Grow the workspace by describing intent: "add a customer-research area and track interview
  status."
- Drop in files and folders yourself; the next session integrates them — no tidying homework.

The generated workspace is plain text files (Markdown, under the hood) and works with Claude Code,
Cursor, Codex, GitHub Copilot, and other file-capable agents. Tool-specific wiring stays minimal.

## Quickstart

Install globally:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

Then ask your agent:

```text
/pm-os-setup Set up a PM OS for Acme.
```

If slash commands are unavailable, say:

```text
Use pm-os-setup to set up a PM OS for Acme.
```

The agent scaffolds the intentionally selected current folder by default, creates a separate folder
when the current location is broad or unsafe, and offers to personalize the result.

## Updating The Skill

```bash
npx skills@latest update pm-os-setup -g
```

## Other Ways To Install

To upload it manually in a desktop or web agent:

1. Download the `manansuneja/skills` repository ZIP.
2. Find `skills/product-management/pm-os-setup`.
3. Upload that standalone folder through the agent's skill interface.
4. Enable the skill and ask it to set up a PM OS.

## What It Creates

```text
acme-workspace/
├── START_HERE.md
├── INDEX.md
├── AGENTS.md
├── CLAUDE.md
├── product-docs/
│   ├── product-vision.md
│   ├── meetings/
│   ├── outcomes/
│   ├── decisions/
│   └── prds/
├── product-practices/
│   ├── skills/
│   ├── templates/
│   └── references/
├── agents/
│   ├── pm-chief.md
│   └── sub-agents/
└── _workspace_setup_docs/
    ├── skills/
    └── personalization/
```

Every content folder has an `INDEX.md`. `START_HERE.md`, `product-docs/`, and
`product-practices/` are the human-facing surfaces; agents and protected setup machinery are clearly
labeled.

## Product-Aware Personalization

Say:

```text
Customize my workspace.
```

The agent asks a lightweight intake, models users, product surfaces, stage, bets, evidence, recurring
artifacts, decisions, tracking needs, and PM responsibilities, then builds synchronized plans for:

- product folders and trackers;
- product skills, templates, and references;
- specialists and Chief PM routing.

Personalization uses keep/add/remove/ask reconciliation. It can remove irrelevant untouched starter
areas, but asks before deleting or relocating user-authored content. The workspace root is renamed
safely as the final operation.

## A Workspace That Evolves

Ask the Chief PM directly:

```text
Add a customer-research area and track interview status.
Create a reusable skill for experiment readouts.
Use this PRD as the format and tone for future specs.
Add a design specialist because we review flows every week.
Remove roadmap machinery; this workspace is only for discovery.
```

The agent keeps product areas, product practices, specialists, routing, and indexes synchronized.
Manually added folders and files are preserved and integrated automatically.

## Product Practices

`product-practices/` is the shared customization center:

- `skills/` contains reusable PM judgment and workflows.
- `templates/` contains exact reusable artifact structures.
- `references/` contains examples, source material, product principles, voice, and style guidance.

The PM supplies intentions and examples; the agent manages configuration and connections.

## Pairs With

- [Workflow Creator](../../agent-workflows/workflow-create) — once your product work lives in the
  OS, turn the recurring rituals (meeting notes → action list, raw notes → PRD) into one-command
  workflows your agent runs end to end.
- [Workspace OS Setup](../../business/workspace-os-setup) — the same operating-system move for a
  studio, small business, or client project instead of a product.

## What This Skill Does And How To Use It

PM OS Setup builds and personalizes a PM workspace with a Chief PM agent, organized product
context, reusable practices, and a structure that starts small and grows with the work.

Install it with:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

Run it with:

```text
/pm-os-setup Set up a PM OS for Acme.
```

After scaffolding, say `Customize my workspace` to tailor the product structure and reusable
practices to the product stage, PM scope, and preferred ways of working.
