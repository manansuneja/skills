# Practical Agent Skills for Product Work

Free, open-source skills that give AI agents durable context and repeatable ways of working.

This repository is the canonical home for every published skill below. If you used an older
standalone repository, reinstall the skill from `manansuneja/skills` to receive future updates.

## Start Here: Give Your PM Agent A Memory

Meeting notes, product decisions, research, outcomes, and PRDs usually end up scattered across
documents and chats. Then the next AI conversation starts from zero.

[PM OS Setup](skills/product-management/pm-os-setup) turns a plain folder into a product workspace
your agent can navigate. It creates a Chief PM, organized product documents, useful indexes, and
reusable product practices—so the agent can find prior context instead of guessing from one prompt.

Install it globally:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

[View PM OS Setup on skills.sh](https://www.skills.sh/manansuneja/skills/pm-os-setup)

Once installed, ask your agent to run `pm-os-setup` in the folder you want to turn into a product
workspace. You do not need to code. The workspace is plain Markdown, portable between tools, and
yours to adapt.

## Also Available

### Workflow Create

[Workflow Create](skills/agent-workflows/workflow-create) connects individual skills into a reusable
workflow. One coordinator runs the steps in sequence while every skill remains usable on its own.

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```

### Workspace OS Setup

[Workspace OS Setup](skills/business/workspace-os-setup) builds a plain-file workspace that gives an
agent lasting context about a studio, business, team, practice, or client project.

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
```

[View Workspace OS Setup on skills.sh](https://www.skills.sh/manansuneja/skills/workspace-os-setup)

## Browse Or Install Everything

List the available skills without installing them:

```bash
npx skills@latest add manansuneja/skills --list
```

Install all published skills globally:

```bash
npx skills@latest add manansuneja/skills --skill '*' -g
```

If `npx` is not recognized, install [Node.js](https://nodejs.org/en/download) and try again.

Using Claude Code too? Add `-a claude-code` to any command so the skill is installed or linked under
Claude Code's `.claude/skills` location:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g -a claude-code
```



## No Terminal

For Claude desktop or web, download this repo as a ZIP from GitHub. Upload only the specific nested skill folder you want:

- `skills/agent-workflows/workflow-create`
- `skills/product-management/pm-os-setup`
- `skills/business/workspace-os-setup`

In Claude, go to `Customize > Skills`, choose `+ Create skill`, upload the folder, and turn the skill on.

## Catalog Rules

Every public skill in this repo must be listed in the root README, its category README, `.claude-plugin/plugin.json`, and `skills.sh.json`.

Every public skill README must include the exact install command and a bottom section named `What This Skill Does And How To Use It`.

Local plans, tests, announcements, and unpublished skills live outside this public repo in the surrounding `skills-to-publish` workspace.
