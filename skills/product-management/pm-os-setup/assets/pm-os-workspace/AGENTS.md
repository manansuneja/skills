# AGENTS.md — {{PROJECT_NAME}} PM Workspace

> **Agent-facing:** This is the operating guide for AI agents. The PM should work mainly in
> `product-docs/` and ask the Chief PM to change workspace machinery.

Read this file, then [INDEX.md](INDEX.md). This is a PM operating system with durable product memory
and a small, human-first working surface. Treat `INDEX.md` as the PM's living dashboard as well as
shared navigation; keep agent operating rules here instead of turning the index into machinery.

Read `_workspace_setup_docs/workspace-state.json` when deciding whether an installed setup update
requires a workspace migration. Never infer that a newer skill version authorizes structural edits.

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

## PM profile

**Profile:** `pm` _(default. Personalization asks how the PM works and updates this line.)_

- `pm` — defines the product and hands build work to an engineering team. The
  [Builder](agents/sub-agents/builder.md) stops at a build brief people can act on.
- `pm-builder` — also builds prototypes or features with coding agents. The Builder additionally
  writes coding-agent task prompts, scopes prototypes, checks results against acceptance criteria,
  and keeps ship notes.

Application code never lives in this workspace. Link the code repository from the project's
`brief.md`; the workspace holds the product thinking and the briefs that drive the build.

## Think and Build

Work moves between two modes. The PM does not pick one; the Chief reads the project's stage in
`status.md`.

- **Think** (discover, define): evidence, options, decisions, and requirements.
- **Build** (build, launch, learn): build briefs, handoff, verification, status, and what was learned.

## Automatic structural reconciliation

Whenever this file is read at the start of a session, perform a lightweight structure check before
substantial work:

1. Compare the actual folder/file tree with the nearest `INDEX.md` maps. Scan paths and index
   presence; do not load every file's contents.
2. Check `product-docs/` (including each project folder), `product-practices/`, and immediate root
   entries for user-created folders, subfolders, or files missing from indexes. Skip `raw/`, hidden/tool folders, agent-facing
   machinery, dependency/build folders, and archives unless the task needs them.
3. Treat manually added content as intentional. Preserve it, infer purpose from its name and nearby
   material, then update the nearest useful index. Create a local `INDEX.md` only when the folder is
   a meaningful content domain, a substantial subdomain, or a multi-file artifact that benefits from
   its own workboard/map. Represent tiny leaf folders in their parent index.
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
  current artifacts. Active work lives in `product-docs/projects/<project>/`; product-wide knowledge
  stays in the global folders.

Do not describe the Chief PM, agents, or PM OS as the user's product unless that is explicitly what
they are building. Decide whether new material is current product work or a reusable way of doing
future product work, then place it in `product-docs/` or `product-practices/` accordingly.

## Capability routing and output formats

- Treat PM OS as the organizer. When a compatible installed skill or tool can materially improve a
  specialized task, use it without hard-coding a plugin brand or requiring it as a dependency.
- Inspect only capabilities the host exposes. Never claim, install, connect, or authenticate a
  capability that is unavailable; fall back to the best local Markdown workflow.
- Default PRDs, briefs, decisions, research syntheses, plans, and other narrative artifacts to `.md`.
  “Create a PRD” means Markdown unless the PM asks for Word, PDF, slides, or another format.
- Use a heavier or binary format only when explicitly requested or clearly required by the context.
  Ask one concise format question only when the choice would materially affect usability.
- Store generated deliverables with their Markdown source or supporting context in the appropriate
  product area. Preserve raw input and update the nearest useful index.
- Ask before external writes such as creating issues, publishing, sending, or changing a connected
  system. Reading an already available source should still stay within the user's requested scope.

## Always do these

- **Orient first.** Read the root index and only relevant folder indexes/files.
- **Ground the work.** Use [product-docs/product-vision.md](product-docs/product-vision.md) for the
  product, users, problem, goals, stage, active bets, and constraints.
- **Fit the product context.** Use the product stage, PM scope, users, surfaces, evidence, recurring
  decisions, outputs, and natural vocabulary. Do not force every PM lane into every workspace.
- **Route deliberately.** Match the request to a workspace specialist/practice and any compatible
  installed capability when useful.
- **Act on capture.** Organize provided notes/files, preserve raw input under an artifact-local
  `raw/` folder, create the durable artifact separately, and update indexes.
- **Save substantial work.** Put analysis, recommendations, decisions, PRDs, and plans in the right
  product area; use chat for a short handoff with paths and takeaways.
- **File by scope.** Work that belongs to one initiative goes inside its project; product-wide
  work stays in the global folders. Every decision also gets a row in the global decisions log.
- **Keep projects honest.** Stage and health live in each project's `status.md` and are mirrored in
  the portfolio table. Update both in the same change.
- **Keep structure focused.** Do not create a top-level area because it might be useful someday.
- **Keep documentation alive.** Update product vision and related durable context when the source is
  clear. Ask before overwriting established direction.
- **Keep skills and routes synchronized.** Changes to a skill, specialist, or product area must
  update linked files, indexes, and Chief PM routing in the same change.
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
- **Keep audience labels.** Agent-only files must say so near the top. Content indexes are
  human-first shared surfaces and should read like useful workboards, not agent manifests.

## Structure rules

Follow
[_workspace_setup_docs/skills/apply-pmos-struct.md](_workspace_setup_docs/skills/apply-pmos-struct.md):

- Use `lower-kebab-case`; use dates only for time-ordered artifacts.
- Keep `INDEX.md` at the root and in meaningful content domains, substantial subdomains, and
  multi-file artifacts. Tiny leaf folders can remain represented by the nearest parent index.
- Update the nearest useful index after meaningful changes and the root index when active work,
  important status, or top-level navigation changes.
- Never overwrite raw input.
- Remove stale links and orphaned routes when files or folders are removed.

## Audience map

```text
START_HERE.md                    user welcome guide
product-docs/                   primary PM + agent working surface
  projects/                     one folder per initiative: brief, status, PRD, build brief
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
