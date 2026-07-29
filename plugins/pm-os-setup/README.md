# PM OS Setup Plugin

This package distributes the canonical `pm-os-setup` skill as a plugin for Codex/ChatGPT and Claude Code.

The bundled skill creates and personalizes a durable, Markdown-based Product Management workspace for
vision, users, meetings, decisions, outcomes, PRDs, and reusable product practices.

## Package layout

- `.codex-plugin/plugin.json` provides the Codex and ChatGPT plugin manifest.
- `.claude-plugin/plugin.json` provides the Claude Code plugin manifest.
- `skills/pm-os-setup/` contains the full, independently usable skill, including its workspace template,
  scaffold helpers, and product-profile reference.

The catalog source at `skills/product-management/pm-os-setup/` remains canonical. When the workflow
changes, update that source and refresh this bundled copy before releasing a new plugin version.
