# Workspace OS Setup

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

Workspace OS Setup creates a focused Markdown workspace for a studio, business, team, knowledge base,
personal practice, or client project. It includes a Workspace Chief, a minimal common specialist
core, an evolving best-practices library, durable memory, and automatic indexes.

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

## Customization Is Subtractive

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

## Manual Installation

Download the repository, then install or upload only:

```text
skills/business/workspace-os-setup
```

## What This Skill Does And How To Use It

Workspace OS Setup scaffolds and personalizes a focused Markdown workspace with durable memory,
agent coordination, reusable workflows, shared templates/references, and indexed content. Invoke
`$workspace-os-setup`, answer the short setup intake, then say `Customize my workspace` to reconcile
the structure; the root folder is renamed to match as part of that step.
