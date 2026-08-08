# Skills for Builders

Practical agent skills for PMs, designers, operators, small business owners, and product builders.

## ChatGPT and Codex plugin pilot

[PM OS](https://manansuneja.github.io/skills/) is being tested as the first one-click plugin
release. The public directory listing is not live yet; the existing GitHub, `npx`, Claude, and manual
installation paths below remain supported.

For local ChatGPT/Codex testing, clone this repository, generate the package, then register the repo
marketplace:

```bash
python -m pip install -r scripts/requirements-plugins.txt
python scripts/build_plugins.py
python scripts/validate_plugins.py
codex plugin marketplace add .
```

The portable Agent Plugins 1.0 package is generated at
`dist/plugins/portable/pm-os-setup`; the ChatGPT/Codex test package is generated at
`dist/plugins/openai/pm-os-setup`. Both contain the same digest-locked skill payload. Generated
packages are disposable and are never committed.

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

- [Workflow Creator](skills/agent-workflows/workflow-create) connects multiple skills into a reusable workflow: one coordinator runs them in sequence, while every skill also works on its own.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```



### Product Management

- [PM OS](skills/product-management/pm-os-setup) builds a PM workspace that gives your agent lasting context about your product, users, decisions, meetings, and PRDs.

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
