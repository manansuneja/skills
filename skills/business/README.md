# Business

Give your agent lasting context about a studio, business, team, or client project.

## Skills

- [Workspace OS Setup](workspace-os-setup) builds a plain-file workspace for your clients, projects,
  decisions, and reusable ways of working, organized by a Workspace Chief agent.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g
```

For Claude Code on the same machine, add `-a claude-code` so it is installed or linked under Claude
Code's `.claude/skills` location:

```bash
npx skills@latest add manansuneja/skills --skill workspace-os-setup -g -a claude-code
```
