# Agent Workflows

Skills for turning repeatable work into reusable agent workflows.

## Skills

- [Workflow Creator](workflow-create) creates, composes, updates, and deletes reusable skill workflow families.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```

For Claude Code on the same machine, add `-a claude-code` so it is installed or linked under
Claude Code's `.claude/skills` location:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g -a claude-code
```
