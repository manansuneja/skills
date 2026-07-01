# PM OS Setup

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

PM OS Setup creates a focused Product Management workspace with a Chief PM, durable product memory,
reusable product practices, and automatic structure maintenance.

It begins with a small core—product vision, meetings, outcomes, decisions, and PRDs—then tailors the
workspace to the product stage, PM scope, users, evidence, recurring outputs, and immediate goals.
Research, design, experiments, data, roadmaps, launches, stakeholder communications, and specialists
appear when the work earns them rather than arriving as permanent clutter.

## What It Helps PMs Do

- Build durable product context instead of accumulating disconnected chats and notes.
- Work through one Chief PM that finds context and routes recurring work.
- Turn meetings, decisions, recommendations, prioritization, MVP cuts, and PRDs into indexed files.
- Teach the workspace preferred workflows, formats, examples, voice, and product principles.
- Add folders, trackers, skills, templates, and specialists by describing the intention.
- Integrate manually added files and folders automatically on the next agent session.
- Reconcile and remove irrelevant generated-empty areas during personalization.
- Safely rename the workspace root after setup without creating a replacement folder and moving
  files into it.

The generated workspace is mostly Markdown and works with Claude Code, Cursor, Codex, GitHub
Copilot, and other file-capable agents. Tool-specific wiring stays minimal.

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

## What This Skill Does And How To Use It

PM OS Setup scaffolds and personalizes a focused Product Management operating system with a Chief PM,
minimal evolving skills and specialists, indexed product memory, automatic structural reconciliation,
and safe root-folder renaming.

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
