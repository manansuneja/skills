# AGENTS.md — {{WORKSPACE_NAME}} Workspace

> **Agent-facing:** This is the operating guide for AI agents. The user should work mainly in
> `{{DOCS_ROOT}}/` and ask the Workspace Chief to change workspace machinery.

Read this file, then [INDEX.md](INDEX.md). This is a Workspace OS with durable memory and a small,
human-first working surface.

## Personalization state

If `_workspace_setup_docs/personalization/` exists, the scaffold is still generic. Before substantial
work, offer:

> Customize my workspace.

When asked, follow `_workspace_setup_docs/personalization/AGENTS.md`. Personalization must reconcile
the structure—keep, add, remove, and ask—not merely add more folders. It may remove clearly irrelevant
generated-empty folders. It must ask once before deleting or relocating user-authored content.

After applying and validating the answers, delete `_workspace_setup_docs/personalization/`. Then
rename the root directory itself to match the workspace name as the final filesystem operation—do
this by default, with no separate approval question, unless the owner asked to keep the current name,
the destination already exists, or the root holds unrelated material. Never create a new root and move
the contents into it. Report the old and new paths and note that the editor may need to reopen the
folder.

The absence of the personalization folder means setup is complete. Do not recreate it.

## One front door

For normal work, act through the **Workspace Chief**:
[agents/workspace-chief.md](agents/workspace-chief.md). It coordinates requests and uses specialists
and workspace skills as needed. The user normally just talks in the workspace.

## Automatic structural reconciliation

Whenever this file is read at the start of a session, perform a lightweight structure check before
substantial work:

1. Compare the actual folder/file tree with the nearest `INDEX.md` maps. Scan path names and index
   presence; do not load every file's contents.
2. Check `{{DOCS_ROOT}}/`, `workspace-best-practices/`, and immediate root entries for user-created
   folders, subfolders, or files that are missing from indexes. Skip `raw/`, hidden/tool folders,
   agent-facing machinery, dependency/build folders, and archives unless the task needs them.
3. Treat manually added content as intentional. Preserve it, infer purpose from its name and nearby
   material, create a missing `INDEX.md`, and add it to the parent/docs-root/root maps as applicable.
4. Connect a new recurring area to the workspace profile, Workspace Chief routing, a skill, template,
   or tracker only when that connection is useful. Do not invent machinery for a one-off folder.
5. Integrate clear cases without asking. Ask one concise question only when meaning or placement is
   genuinely ambiguous, or when a move/rename could break references. Never delete user-created
   content during reconciliation.

Briefly mention anything integrated in the task handoff. The user should not have to maintain indexes
or announce that they created a folder.

## Keep the layers separate

- **Workspace machinery:** `AGENTS.md`, `agents/`, `_workspace_setup_docs/`, indexes, and tool config.
- **Reusable ways of working:** `workspace-best-practices/skills/` plus `workspace-best-practices/templates/` and
  `workspace-best-practices/references/`.
- **User content:** `{{DOCS_ROOT}}/`—the actual business, studio, project, research, knowledge,
  writing, or other work this workspace exists to support.

Do not describe Workspace OS machinery as the user's actual work unless that is explicitly what they
are building.

When deciding where new content belongs, ask whether it will be *reused* across many future pieces of
work (a voice/tone guide, a format, a recurring checklist) or whether it *is* the work, knowledge, or
plan itself. The former belongs in `workspace-best-practices/`; the latter belongs in
`{{DOCS_ROOT}}/`—even when it surfaces during a request that is mostly about hub-docs content, such as
a brand voice guide that comes up while setting up content/marketing folders.

## Always do these

- **Orient first.** Read the root index and only the relevant folder indexes/files.
- **Ground the work.** Use
  [{{DOCS_ROOT}}/workspace-profile.md]({{DOCS_ROOT}}/workspace-profile.md) for purpose, audience,
  category, domain model, priorities, tracking needs, and constraints.
- **Fit the domain.** Use the category's natural entities, lifecycle, terminology, recurring
  artifacts, and tracking needs. Keep the machinery generic, not the user's information architecture.
- **Route deliberately.** Match the request to a specialist and its workspace skill when useful.
- **Act on capture.** Organize provided notes/files, preserve raw input under an artifact-local
  `raw/` folder, create the durable artifact separately, and update indexes.
- **Save substantial work.** Put analysis, synthesis, decisions, plans, writing, and reusable context
  in the appropriate content area; use chat for a short handoff with paths and takeaways.
- **Keep structure focused.** Do not create a top-level folder because it might be useful someday.
  Reuse an existing area when purposes overlap.
- **Keep documentation alive.** Update the workspace profile when durable direction changes and the
  source is clear. Ask before overwriting an established direction.
- **Keep skills and routes synchronized.** Changes to a skill, specialist, or content area must update
  linked files, indexes, and Workspace Chief routing in the same change.
- **Recognize durable preferences.** On every request, determine from meaning and scope whether
  guidance applies only to the current artifact or should govern future work. Strong evidence
  includes organizational standards, broadly stated methods, canonical examples, recurring
  workflows, and corrections intended to change the normal approach. Do not require special wording.
- **Handle mixed intent.** When a request asks for immediate work and also establishes a durable
  preference, complete the artifact and update the relevant existing skill/template/reference in
  the same task. Ask one concise question only when persistence is genuinely ambiguous and would
  materially affect future outputs.
- **Let the workspace evolve.** Capture durable preferences and recurring workflows in the smallest
  useful skill/template and optional specialist. Keep truly one-off work one-off.
- **Keep audience labels.** Agent-only files and folder indexes must say so near the top.

## Structure rules

Follow
[_workspace_setup_docs/skills/apply-workspace-struct.md](_workspace_setup_docs/skills/apply-workspace-struct.md):

- Use `lower-kebab-case`; use dates only for time-ordered artifacts.
- Keep an `INDEX.md` in every Workspace OS content folder.
- Update the nearest index after any meaningful change; update the root index for top-level changes.
- Never overwrite raw input.
- Remove stale links and orphaned routes when files or folders are removed.

## Audience map

```text
START_HERE.md                    user welcome guide
{{DOCS_ROOT}}/                   primary user + agent working surface
workspace-best-practices/       shared customization center
  skills/                       output/workflow instructions
  templates/                    exact reusable formats
  references/                   examples, sources, voice, and style
INDEX.md                         shared map
agents/                          agent-facing roles
_workspace_setup_docs/          agent-facing setup and structure rules
AGENTS.md, CLAUDE.md, .cursor/   agent/tool-facing wiring
```

## Updating the installed setup skill

If the user asks how to update the globally installed `workspace-os-setup` skill, provide:

```bash
npx skills@latest update workspace-os-setup -g
```

Do not run it silently unless the user explicitly asks.
