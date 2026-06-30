# Workspace OS Setup

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

Workspace OS Setup creates a structured Markdown workspace for a small business, solo practice,
studio, agency, or client project. It gives the workspace a **Workspace Chief** coordinator,
specialist agents, reusable business skills, shared templates/references, durable business memory,
automatic indexes, and a setup flow that can bias the workspace toward client management,
brainstorming, knowledge, operations, or project delivery.

It is not just a notes folder. It is a business workspace your agents can navigate.

## What This Helps Business Owners Do

- Build a business hub or client-project workspace instead of another folder of loose notes.
- Work through one Workspace Chief that routes to the right specialist automatically.
- Capture working style, standards, templates, and examples as reusable skills.
- Turn meetings, brainstorms, decisions, offers, plans, metrics, and client updates into durable files.
- Keep every folder indexed so future agents can find context without rereading everything.

## Quickstart

**1. Install the skill:**

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
```

Using Claude Code on the same machine too?

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g -a claude-code
```

**2. Run it:**

```text
/workspace-os-setup Set up a Workspace OS for my interior design business.
```

For a bounded client project:

```text
/workspace-os-setup Set up a client-project Workspace OS for the Lake House redesign.
```

The agent asks a short intake, chooses the current folder or a new workspace folder, scaffolds the
workspace, and offers to personalize it.

## Updating The Skill

```bash
npx skills@latest update workspace-os-setup -g
```

## No Terminal

Download this repo as a ZIP from GitHub, unzip it, then open Claude's `Customize > Skills` and upload
only this folder:

```text
skills/business/workspace-os-setup
```

Turn the skill on, then ask: `Use workspace-os-setup to set up a Workspace OS for my business.`

## What It Creates

```text
acme-workspace/
|-- AGENTS.md
|-- CLAUDE.md
|-- INDEX.md
|-- START_HERE.md
|-- agents/
|   |-- workspace-chief.md
|   `-- sub-agents/...
|-- business-hub-docs/        # or project-docs/
|   |-- business-profile.md
|   |-- meetings/...
|   |-- outcomes/...
|   |-- offers/...
|   |-- decisions/...
|   |-- brand-and-delivery/...
|   |-- metrics/...
|   |-- plans/...
|   `-- client-comms/...
|-- business-skills/
|   |-- START_HERE.md
|   |-- summarize-notes.md
|   |-- brainstorm.md
|   |-- offer-brief.md
|   |-- metrics-review.md
|   |-- business-planning.md
|   `-- ...
|-- business-practices/
|   |-- templates/...
|   `-- references/...
`-- _workspace_setup_docs/
    |-- skills/
    |   |-- apply-workspace-struct.md
    |   `-- manage-workspace-skills.md
    `-- personalization/
        |-- README.md
        `-- AGENTS.md
```

Every content folder includes an `INDEX.md` so agents can find the right context quickly.

## After Setup

Talk to the Workspace Chief in plain language:

```text
Summarize these client meeting notes and save them.
Help me shape a new service package.
Turn this project idea into an offer brief.
Draft a client update from this plan change.
Update the business profile based on this strategy note.
Create a skill for how I like project proposals written.
```

The base starter skills cover notes, outcomes, brainstorming, offer briefs, brand/delivery notes,
metrics, planning, client communications, documentation, and workspace skill updates. The
`_workspace_setup_docs/personalization/` handoff helps make the generic scaffold specific to the
business, then removes itself when setup is complete.

## What This Skill Does And How To Use It

Workspace OS Setup scaffolds a Markdown business or client-project workspace with a Workspace Chief,
specialist agents, reusable business skills, business docs, templates/references, automatic indexes,
and workspace memory.

Install it with:

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
```

Run it by asking your agent to create a Workspace OS:

```text
/workspace-os-setup Set up a Workspace OS for my interior design business.
```

After scaffolding, tell your agent `Customize my workspace` to personalize the business profile,
Workspace Chief, specialist agents, and reusable business skills.
