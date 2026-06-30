# Skills for Builders

Skills for PMs, designers, small business owners, and product-minded builders using agents to shape, decide, create, operate, and ship.

This repo is a public catalog of agent skills. It is not just for developers: the skills here are
built for product work, business operations, design, planning, writing, decision-making, and
vibe-coding.

## Install

Install one skill globally so it is available in every project:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
```

Or list everything available:

```bash
npx skills@latest add manansuneja/skills --list
```

If `npx` is not recognized, install [Node.js](https://nodejs.org/en/download) and try again.

Using Claude Code too? Add `-a claude-code` to the install command so the skill is installed or
linked under Claude Code's `.claude/skills` location. For example:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g -a claude-code
```

To install every published skill in this catalog into Claude Code:

```bash
npx skills@latest add manansuneja/skills --skill '*' -g -a claude-code
```



## Skills



### Agent Workflows

- [Workflow Creator](skills/agent-workflows/workflow-create) turns a repeatable process into a reusable skill family: one coordinator plus focused child skills, linked with run tracking and validation.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```



### Product Management

- [PM OS Setup](skills/product-management/pm-os-setup) scaffolds a Product Management operating system with a Chief PM coordinator, specialist agents, product-skills, product-practices, protected workspace setup docs, product docs, outcomes, design notes, data insights, roadmaps, stakeholder comms, and workspace memory.

Install:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```



### Business

- [Workspace OS Setup](skills/business/workspace-os-setup) scaffolds a focused Markdown operating
system for a studio, business, team, knowledge base, personal practice, or client project, with
agent coordination, reusable workflows, indexed memory, and subtractive personalization.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
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