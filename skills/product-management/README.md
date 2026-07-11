# Product Management

Give your agent lasting product context instead of starting every chat from zero.

## Skills

- [PM OS Setup](pm-os-setup) builds a PM workspace that stores your product context as organized, searchable files and keeps it useful through a Chief PM agent.

Install:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

For Claude Code on the same machine, add `-a claude-code` so it is installed or linked under
Claude Code's `.claude/skills` location:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g -a claude-code
```
