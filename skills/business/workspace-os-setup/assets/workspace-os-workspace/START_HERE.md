# Welcome to {{WORKSPACE_NAME}} Workspace OS

> **For you:** Start here, then spend most of your time in [{{DOCS_ROOT}}/]({{DOCS_ROOT}}/INDEX.md).
> The agent-managed folders can stay in the background.

This workspace helps you build memory with an AI agent. You do not need to learn commands or choose
the perfect file first—talk naturally, and the Workspace Chief should route, organize, and save the
work.

## Start with a request

- “Capture these notes and connect them to what we already know.”
- “Help me brainstorm directions, then save the strongest options.”
- “Turn this research into a useful knowledge note.”
- “Draft this in my writing style.”
- “Capture this decision and why we made it.”
- “Create a reusable way of doing this so I do not have to repeat myself.”

## Where you should focus

- [{{DOCS_ROOT}}/]({{DOCS_ROOT}}/INDEX.md) is your primary workspace: profile, notes, knowledge,
  outcomes, decisions, projects, content, or whichever areas personalization keeps.
- [workspace-best-practices/](workspace-best-practices/INDEX.md) is the customization center for
  skills, templates, examples, voice, and style.
- [INDEX.md](INDEX.md) is the full map when you need it.

`agents/`, `_workspace_setup_docs/`, `AGENTS.md`, `CLAUDE.md`, and `.cursor/` are agent-facing
machinery. You can safely ignore them in normal use.

## Customize outputs without configuration

Skills are important: they tell agents how to think, what to produce, and which structure or format
to use. Templates define exact output shapes; references teach examples, voice, and style.

Go to [workspace-best-practices/](workspace-best-practices/INDEX.md), point the agent at anything you
want changed, and describe the intention:

- “Update this skill so every proposal includes scope, timeline, and exclusions.”
- “Create a sourcing-status template for this studio.”
- “Use this finished document as the voice and format for future work.”
- “Simplify these skills; this workspace needs fewer steps.”

You do not need to know which file or agent to configure. The Workspace Chief updates the right
skills, templates, references, specialists, routes, and indexes for you.

## Shape the workspace as you work

Ask naturally whenever you want more structure:

- “Add a folder and subfolders for each interior-design project.”
- “Create a tracker for sourcing status, budget, and approvals.”
- “Add a place for campaign ideas, drafts, and published content.”
- “Track the stages that matter for this kind of project.”

You can also create folders, subfolders, and files manually inside the workspace. The next agent
session performs a lightweight structure check, creates missing indexes, and connects clear additions
to the workspace map and routing. You do not need to maintain the indexes yourself.

## First-time customization

If `_workspace_setup_docs/personalization/` exists, tell your agent:

> Customize my workspace.

The agent will ask one short intake, model how your category of work operates, then keep useful areas,
add fitting folders, subfolders, and trackers, and remove irrelevant empty starter folders. It will
ask before deleting or relocating anything that contains your content.

It will also rename the root folder to match the workspace name as the last step, and tell you the new
path; your editor may need to reopen the folder. Say so during the intake if you'd rather it stayed as
is.

## How the workspace learns

Describe preferences in plain language: “make updates shorter,” “use this as my writing example,” or
“always include sources.” The workspace should add only the smallest useful skill or folder, then
grow naturally as repeated work and new intentions appear.

To update a globally installed copy of the setup skill when new changes are published:

```bash
npx skills@latest update workspace-os-setup -g
```
