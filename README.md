# Skills for Product Builders

Skills for PMs, designers, and product-minded builders using agents to shape, decide, create, and ship.

This repo is a public catalog of agent skills. It is not just for developers: the skills here are built for product work, design work, planning, writing, decision-making, and vibe-coding as a product builder.

## Install

Install one skill globally so it is available in every project:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

Or list everything available:

```bash
npx skills@latest add manansuneja/skills --list
```

If `npx` is not recognized, install [Node.js](https://nodejs.org/en/download) and try again.

## Skills

### Agent Workflows

- [Workflow Creator](skills/agent-workflows/workflow-create) turns a repeatable process into a reusable skill family: one coordinator plus focused child skills, linked with run tracking and validation.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```

### Product Management

- [PM OS Setup](skills/product-management/pm-os-setup) scaffolds a Product Management operating system with a Chief PM coordinator, specialist agents, reusable skills, product docs, and workspace memory.

Install:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

## No Terminal

For Claude desktop or web, download this repo as a ZIP from GitHub. Upload only the specific nested skill folder you want:

- `skills/agent-workflows/workflow-create`
- `skills/product-management/pm-os-setup`

In Claude, go to `Customize > Skills`, choose `+ Create skill`, upload the folder, and turn the skill on.

## Catalog Rules

Every public skill in this repo must be listed in the root README, its category README, `.claude-plugin/plugin.json`, and `skills.sh.json`.

Local plans, tests, announcements, and unpublished skills live outside this public repo in the surrounding `skills-to-publish` workspace.
