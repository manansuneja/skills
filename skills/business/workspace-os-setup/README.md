# Workspace OS Setup

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

**Build a workspace that gives your agent lasting context about your business or project.**

Workspace OS Setup stores your clients, projects, meetings, decisions, and reusable ways of working
as plain files. A Workspace Chief agent keeps them organized and uses them when new work arrives, so
you get answers based on your business instead of generic advice.

It is for studio owners, consultants, small teams, and people running a practice or client project.
There is no database or code to maintain. It works with Claude Code, Cursor, Codex, and other
file-capable agents.

## What It Helps You Do

- Give your agent durable memory of your business: clients, projects, decisions, and how you like
  things done.
- Capture work as it happens — notes, briefs, outcomes — into folders that stay indexed
  automatically.
- Teach it your formats once (proposals, briefs, client updates) and reuse them forever.
- Shape the workspace by talking: "add a vendors tracker", "this workspace is only for discovery."
- Start minimal and grow only when the work earns it — no forty-folder template graveyard on
  day one.

## Install

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
```

Using Claude Code on the same machine too?

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g -a claude-code
```

Then ask:

```text
/workspace-os-setup Set up a Workspace OS for my interior design studio.
```

Or for a bounded project:

```text
/workspace-os-setup Set up a client-project Workspace OS for the Lake House redesign.
```

## What It Creates

```text
studio-name-workspace/
|-- START_HERE.md                 # user guide
|-- INDEX.md                      # shared map
|-- workspace-hub-docs/          # primary user workspace (or project-docs/)
|   |-- workspace-profile.md
|   `-- focused content areas...
|-- workspace-best-practices/    # user + agent customization center
|   |-- skills/                   # workflows, output structure, and format
|   |-- templates/                # exact reusable formats
|   `-- references/               # examples, sources, voice, and style
|-- agents/                       # agent-facing
|-- _workspace_setup_docs/        # agent-facing setup and structure rules
|-- AGENTS.md                      # agent-facing operating guide
|-- CLAUDE.md                      # tool compatibility
`-- .cursor/                       # tool compatibility
```

The user should spend most of their time in `workspace-hub-docs/` or `project-docs/` and use
`workspace-best-practices/` when they want to shape outputs. They describe intention and examples;
the agent handles configuration and synchronization.

## It Starts Small On Purpose

Most workspace templates fail the same way: forty empty folders you feel guilty about by week two.
This one goes the other direction — customization keeps what supports real work and removes the
rest.

After scaffolding, say:

```text
Customize my workspace.
```

The agent asks one short intake, then reconciles the structure:

- models the category's entities, lifecycle, terminology, recurring work, and tracking needs;
- keeps areas that support current or near-term work;
- adds fitting folders, subfolders, trackers, templates, skills, and routes;
- removes clearly irrelevant generated-empty folders;
- asks once before deleting or relocating anything containing user-authored content;
- synchronizes skills, specialists, routes, links, and indexes.

The default library contains only common skills for summarizing notes, brainstorming, synthesizing
outcomes, and documenting context. Category-specific skills and sub-agents are added only when the
scope or repeated work needs them.

For example, an interior-design studio focused on knowledge capture, brainstorming, marketing, and
writing does not automatically keep a vendors area simply because vendors are common in the field.

Customization also renames the root folder to match the workspace name by default—no opt-in question
needed unless the destination already exists or the folder holds unrelated material. The agent
completes all content changes first, then renames the directory itself as one final move and reports
the new path. It does not create a second folder and shuffle the contents into it.

Users can ask the Workspace Chief to add any folder, subfolder, tracker, or workflow later. If they
add content manually, the next agent session performs a lightweight structural reconciliation:
missing indexes and maps are created, and clear additions are integrated automatically.

Users can also open `workspace-best-practices/` and ask the agent to modify a skill, create a
business-specific template, learn from an example, or simplify the library. No manual configuration
is required.

## Updating

```bash
npx skills@latest update workspace-os-setup -g
```

## No Terminal — Claude Desktop Or Web

Download the `manansuneja/skills` repository as a ZIP from GitHub, unzip it, and find:

```text
skills/business/workspace-os-setup
```

In Claude, go to **Customize > Skills**, choose **+ Create skill**, upload that folder, and turn
the skill on. Then ask: `Use workspace-os-setup to set up a workspace for my studio.`

## Pairs With

- [PM OS Setup](../../product-management/pm-os-setup) — the same operating-system move, purpose-built
  for product managers and product context.
- [Workflow Creator](../../agent-workflows/workflow-create) — once your workspace holds how you
  work, turn the recurring jobs (client brief → proposal, notes → summary) into one-command
  workflows.

## What This Skill Does And How To Use It

Workspace OS Setup builds and personalizes a workspace of plain files and folders with lasting
context, a Workspace Chief agent, reusable workflows, shared templates and references, and
automatic indexes.

Install it with:

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
```

Run `/workspace-os-setup`, answer the short setup intake, then say `Customize my workspace` to
tailor the structure; the root folder is renamed to match as part of that step.
