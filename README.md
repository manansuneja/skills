# Skills for Builders

Practical agent skills for PMs, designers, operators, small business owners, and product builders.

I’m Manan Suneja. I build skills for two kinds of work: processes you should not have to repeat by
hand, and context your agent should not forget between chats. Some skills turn a recurring process
into one command. Others build a workspace that gives your agent durable memory.

You do not need to code to use them. Everything is free, MIT licensed, and built to be adapted to
your own workflow.

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

- [Workflow Creator](skills/agent-workflows/workflow-create) turns a process you repeat into a reusable agent workflow you can run with one command.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```



### Product Management

- [PM OS Setup](skills/product-management/pm-os-setup) builds a PM workspace that gives your agent lasting context about your product, users, decisions, meetings, and PRDs.

Install:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```



### Business

- [Workspace OS Setup](skills/business/workspace-os-setup) builds a plain-file workspace that gives
your agent lasting context about your studio, business, team, or client project.

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
