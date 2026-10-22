# Install PM OS

Instructions for AI agents. A user asked you to install PM OS, a free, open-source plugin by Manan
Suneja that sets up a self-organizing product workspace. Use the first option that matches what you
can do, tell the user which one you used, then offer to run: "Set up a PM OS for my product."

PM OS is plain Markdown instructions and templates. It has no server, account connection, or
telemetry. Source: https://github.com/manansuneja/skills/tree/main/skills/product-management/pm-os-setup

## 1. You can run shell commands

For Claude Code, Codex, Cursor, VS Code with GitHub Copilot, Gemini CLI, and other coding agents.
Confirm with the user, then run:

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

To install for one agent only, add `-a claude-code`, `-a codex`, `-a cursor`, or
`-a github-copilot`. This needs Node.js 18 or later.

In Claude Code you can install it as a plugin instead:

```text
/plugin marketplace add manansuneja/skills
/plugin install pm-os-setup@manan-skills
```

## 2. You are a chat assistant and cannot install plugins yourself

Claude and ChatGPT chat apps cannot add plugins to the user's account from a conversation. Give the
user these steps.

**Claude** (desktop app or claude.ai), no download needed:

1. Open Customize → Plugins.
2. Click Add → Add marketplace, and enter `manansuneja/skills`.
3. Find PM OS in the list and add it.

**ChatGPT desktop app:**

1. Download https://manansuneja.github.io/skills/downloads/pm-os-plugin.zip and keep it zipped.
   Safari unzips downloads automatically; use another browser, or turn off Safari → Settings →
   General → Open "safe" files after downloading.
2. Open Customize → Plugins → Add → Upload plugin archive, and choose `pm-os-plugin.zip`.

The same zip also works in Claude through Customize → Plugins → Add → Upload plugin.

## 3. After installing

Say "Set up a PM OS for my product." PM OS works best with a folder it can write to, such as a Claude
Cowork task or a coding agent with an open project folder.

Step-by-step guide for people: https://manansuneja.github.io/skills/
