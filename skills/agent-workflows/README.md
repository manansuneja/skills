# Agent Workflows

Turn repeatable work into agent workflows you can run with one command.

## Skills

- [Workflow Creator](workflow-create) connects multiple skills into a reusable workflow. One coordinator runs them in sequence, while every skill also works on its own.

Install:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```

For Claude Code on the same machine, add `-a claude-code` so it is installed or linked under
Claude Code's `.claude/skills` location:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g -a claude-code
```
