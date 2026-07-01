# AGENTS.md — {{PROJECT_NAME}} PM Workspace

> **Agent-facing:** This is the operating guide for AI agents. The PM should work mainly in
> `product-docs/` and ask the Chief PM to change workspace machinery.

Read this file, then [INDEX.md](INDEX.md). This is a PM operating system with durable product memory
and a small, human-first working surface.

## Personalization state

If `_workspace_setup_docs/personalization/` exists, the scaffold is still generic. Before
substantial product work, offer:

> Customize my workspace.

When asked, follow `_workspace_setup_docs/personalization/AGENTS.md`. Personalization must reconcile
the structure—keep, add, remove, and ask—not merely add more folders. It may remove clearly
irrelevant generated-empty folders. It must ask once before deleting or relocating user-authored
content.

After applying and validating the answers, delete `_workspace_setup_docs/personalization/`. Then
rename the root directory itself to match the workspace name as the final filesystem operation. Do
this by default unless the PM asked to keep the current name, the destination exists, or the root
contains unrelated material. Never create a new root and move the contents into it. Report the old
and new paths and note that the editor may need to reopen the folder.

The absence of the personalization folder means setup is complete. Do not recreate it.

## One front door

For normal work, act through the **Chief PM**: [agents/pm-chief.md](agents/pm-chief.md). It coordinates
requests and applies specialists and product skills as needed. The PM normally just talks in the
workspace.

## Automatic structural reconciliation

Whenever this file is read at the start of a session, perform a lightweight structure check before
substantial work:

1. Compare the actual folder/file tree with the nearest `INDEX.md` maps. Scan paths and index
   presence; do not load every file's contents.
2. Check `product-docs/`, `product-practices/`, and immediate root entries for user-created folders,
   subfolders, or files missing from indexes. Skip `raw/`, hidden/tool folders, agent-facing
   machinery, dependency/build folders, and archives unless the task needs them.
3. Treat manually added content as intentional. Preserve it, infer purpose from its name and nearby
   material, create a missing `INDEX.md`, and update the parent, product-docs, or root map as needed.
4. Connect a recurring area to product vision, Chief PM routing, a skill, template, tracker, or
   specialist only when useful. Do not invent machinery for one-off content.
5. Integrate clear cases without asking. Ask one concise question only when meaning or placement is
   genuinely ambiguous or a move could break references. Never delete user-created content during
   reconciliation.

Briefly mention anything integrated in the task handoff. The PM should not have to maintain indexes
or announce that they created a folder.

## Keep the layers separate

- **Workspace machinery:** `AGENTS.md`, `agents/`, `_workspace_setup_docs/`, indexes, and tool config.
- **Reusable product practices:** `product-practices/skills/`, `product-practices/templates/`, and
  `product-practices/references/`.
- **Product work:** `product-docs/`—the actual product vision, evidence, decisions, requirements, and
  current artifacts.

Do not describe the Chief PM, agents, or PM OS as the user's product unless that is explicitly what
they are building. Decide whether new material is current product work or a reusable way of doing
future product work, then place it in `product-docs/` or `product-practices/` accordingly.

## Always do these

- **Orient first.** Read the root index and only relevant folder indexes/files.
- **Ground the work.** Use [product-docs/product-vision.md](product-docs/product-vision.md) for the
  product, users, problem, goals, stage, active bets, and constraints.
- **Fit the product context.** Use the product stage, PM scope, users, surfaces, evidence, recurring
  decisions, outputs, and natural vocabulary. Do not force every PM lane into every workspace.
- **Route deliberately.** Match the request to a specialist and product skill when useful.
- **Act on capture.** Organize provided notes/files, preserve raw input under an artifact-local
  `raw/` folder, create the durable artifact separately, and update indexes.
- **Save substantial work.** Put analysis, recommendations, decisions, PRDs, and plans in the right
  product area; use chat for a short handoff with paths and takeaways.
- **Keep structure focused.** Do not create a top-level area because it might be useful someday.
- **Keep documentation alive.** Update product vision and related durable context when the source is
  clear. Ask before overwriting established direction.
- **Keep skills and routes synchronized.** Changes to a skill, specialist, or product area must
  update linked files, indexes, and Chief PM routing in the same change.
- **Let the workspace evolve.** Turn explicit reusable preferences and recurring workflows into the
  smallest useful skill/template and optional specialist. Keep one-off work one-off.
- **Keep audience labels.** Agent-only files and folder indexes must say so near the top.

## Structure rules

Follow
[_workspace_setup_docs/skills/apply-pmos-struct.md](_workspace_setup_docs/skills/apply-pmos-struct.md):

- Use `lower-kebab-case`; use dates only for time-ordered artifacts.
- Keep an `INDEX.md` in every PM OS content folder.
- Update the nearest index after meaningful changes and the root index after top-level changes.
- Never overwrite raw input.
- Remove stale links and orphaned routes when files or folders are removed.

## Audience map

```text
START_HERE.md                    user welcome guide
product-docs/                   primary PM + agent working surface
product-practices/              shared customization center
  skills/                       output/workflow instructions
  templates/                    exact reusable formats
  references/                   examples, sources, voice, and style
INDEX.md                         shared map
agents/                          agent-facing roles
_workspace_setup_docs/          agent-facing setup and structure rules
AGENTS.md, CLAUDE.md, .cursor/   agent/tool-facing wiring
```

## Updating the installed setup skill

If the PM asks how to update the globally installed `pm-os-setup` skill, provide:

```bash
npx skills@latest update pm-os-setup -g
```

Do not run it silently unless the PM explicitly asks.
