# PM OS

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

**Build a PM workspace that gives your agent lasting context about your product.**

PM OS stores your vision, projects, meetings, decisions, outcomes, PRDs, and build briefs as organized
files. A Chief PM agent uses that context to find past work, route new work, and keep recurring
outputs consistent. You stop pasting the same background into every chat.

It is built for PMs and requires no code or database. The workspace starts small, then adds research,
experiments, roadmaps, or specialists only when your work needs them.

## What It Helps PMs Do

- Start every session with an agent that already knows the product: vision, users, open bets, and
  the last decision made.
- Turn meetings, decisions, prioritization calls, MVP cuts, and PRDs into indexed files instead of
  chat scrollback you will never find again.
- Run each initiative as a project with its own stage, health, risks, and running log, and see the
  whole portfolio at a glance.
- Go from PRD to build: get a build brief a coding agent or an engineering team can work from, then
  check what comes back against the acceptance criteria. Built for PMs and PM-builders.
- Work through one Chief PM that finds context and routes recurring work to the right practice.
- Teach it your formats, voice, and product principles once — every future PRD, readout, or
  stakeholder update follows them.
- Grow the workspace by describing intent: "add a customer-research area and track interview
  status."
- Drop in files and folders yourself; the next session integrates them — no tidying homework.
- Use compatible installed document, presentation, spreadsheet, design, or research capabilities as
  specialists when requested, while PM OS files and organizes the result.

The generated workspace is plain text files (Markdown, under the hood) and works with Claude Code,
Cursor, Codex, GitHub Copilot, and other file-capable agents. Tool-specific wiring stays minimal.
PRDs, briefs, decisions, and plans remain Markdown by default; heavier formats are created only when
you ask for them or the delivery context clearly requires them.

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

## Mobile And No-File Environments

On a mobile or web surface without a writable workspace root, PM OS runs in **Conversation mode**.
It can guide product work, maintain a compact Markdown PM OS Index, and create Markdown artifacts in
the conversation, but it will clearly disclose that it has not created a durable folder tree or a
ChatGPT Project. When supported, it can offer downloadable Markdown files or continue the full
workspace setup later in a file-capable desktop or coding environment.

## Updating The Skill

```bash
npx skills@latest update pm-os-setup -g
```

## No Terminal: Download And Upload

1. [Download the PM OS plugin (.zip)](https://manansuneja.github.io/skills/downloads/pm-os-plugin.zip).
   The same file works in Claude, ChatGPT, Cursor, and VS Code. On a Mac, Safari unzips downloads
   automatically; turn off `Safari > Settings > General > Open "safe" files after downloading` first,
   or use another browser, so you upload the original `.zip`.
2. Upload it:
   - **Claude** (desktop app or claude.ai): `Customize > Plugins > + Add > Upload plugin`.
   - **ChatGPT** (desktop app): `Customize > Plugins > Add > Upload plugin archive`.
   - **Cursor:** unzip it, move the `pm-os-plugin` folder into `~/.cursor/plugins/local/`, and run
     `Developer: Reload Window`.
   - **VS Code** (GitHub Copilot): unzip it, add `"chat.plugins.enabled": true` and
     `"chat.pluginLocations": { "/path/to/pm-os-plugin": true }` to your user `settings.json`, and
     reload.
3. Say: `Set up a PM OS for my product.`

For the full folder workspace, use the Claude desktop app, start a Cowork task, and pick an empty
folder. In Cursor or VS Code, open an empty folder first. The
[step-by-step guide](https://manansuneja.github.io/skills/) covers troubleshooting and a skill-only
download.

Terminal users can install the skill into Cursor or VS Code directly:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g -a cursor
npx skills@latest add manansuneja/skills --skill pm-os-setup -g -a github-copilot
```

## What It Creates

```text
acme-workspace/
├── START_HERE.md
├── INDEX.md
├── AGENTS.md
├── CLAUDE.md
├── product-docs/
│   ├── product-vision.md
│   ├── projects/
│   │   └── <project>/        brief, status, PRD, build brief, and project-scoped work
│   ├── meetings/
│   ├── outcomes/
│   └── decisions/
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

Active work lives in `projects/`, one folder per initiative; product-wide knowledge stays in the
shared folders, and every decision is logged in one place. The root `INDEX.md` is a living product
workboard—current work, waiting items, recent decisions, and navigation. Meaningful content domains have their own human-readable indexes; tiny leaf folders can
stay represented by their parent. `START_HERE.md`, `product-docs/`, and `product-practices/` are the
human-facing surfaces; agents and protected setup machinery are clearly labeled.

## Product-Aware Personalization

Say:

```text
Customize my workspace.
```

The agent asks a lightweight intake, including whether you hand specs to engineers or also build
with coding agents, models users, product surfaces, stage, bets, evidence, recurring artifacts,
decisions, tracking needs, and PM responsibilities, then builds synchronized plans for:

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

PM OS builds and personalizes a PM workspace with a Chief PM agent, organized product
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
