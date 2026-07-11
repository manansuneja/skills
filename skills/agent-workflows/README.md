# Agent Workflows

Turn repeatable work into agent workflows you can run with one command.

## Skills

- [Workflow Creator](workflow-create) turns a repeated process into one command. It can create new steps, connect skills published by other people without modifying them, or adopt skills you own.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```

For Claude Code on the same machine, add `-a claude-code` so it is installed or linked under
Claude Code's `.claude/skills` location:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g -a claude-code
```
