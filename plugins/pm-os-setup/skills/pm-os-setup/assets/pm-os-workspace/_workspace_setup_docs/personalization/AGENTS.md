# Setup Agent Guide — Personalize This PM OS

> **Agent-facing:** This is the one-time apply guide. The PM should answer the intake, then stay
> focused on `product-docs/` rather than editing this file.

Turn this generic PM OS into a focused workspace shaped around the product stage, PM scope, users,
active bets, evidence, recurring decisions, and output preferences. This is product-context intake
and structure reconciliation, not a filesystem tour.

Use the machinery vs product-layer boundary in [../../AGENTS.md](../../AGENTS.md). The PM OS operates
in the background; product files describe the user's actual product or project.

When setup is complete, delete `_workspace_setup_docs/personalization/` as the final content cleanup.
Its absence tells future sessions that personalization is complete. Durable behavior belongs in
`AGENTS.md`, `agents/`, `_workspace_setup_docs/`, `product-practices/`, and `product-docs/`.

## Setup goals

By the end, the workspace should have:

- A concise `product-docs/product-vision.md` grounded in the real product and users.
- A product-stage and PM-scope-appropriate information architecture.
- A small, relevant set of content areas, subfolders, and trackers under `product-docs/`.
- No clearly irrelevant generated-empty product areas.
- A customized Chief PM and only useful specialist routes.
- A minimal `product-practices/` library whose skills and templates match recurring work and output
  preferences.
- Current `INDEX.md` files, healthy links, and clear audience labels.
- A safe root-folder rename completed by default.
- No unnecessary tool-adapter clutter.

## Step 1 — Ask one lightweight intake

Ask these four questions in one friendly message. Rough notes, links, file paths, or “skip for now”
are fine.

1. What should this workspace be called? Explain that the root folder will be renamed at the end
   using their exact name or `<project-slug>-workspace`, unless they prefer to keep its current name.
   Mention that the editor may need to reopen the renamed folder.
2. What are they building, who is it for, what problem or opportunity matters, and which product
   surfaces or actors should the workspace understand?
3. What stage is the product in, what three to five kinds of PM work should be easiest now, and what
   should be tracked—for example research, bets, experiments, requirements, releases, metrics,
   dependencies, customers, or stakeholder commitments? Ask what they explicitly do not need.
4. What is the next useful outcome, and which files, links, notes, decisions, examples, constraints,
   formats, or writing style should be used?

Do not ask about every PM artifact. Preferences should emerge from examples and become skills over
time. Detect the host tool when possible and ask about wiring only when requested. If answers are
thin, ask at most one follow-up round.

## Step 2 — Build a reconciliation plan

Work from the workspace root. Read the root and product-docs indexes, inspect the actual folders, and
build a compact product operating model:

- Users, buyers, operators, partners, systems, and other relevant actors.
- Product surfaces, capabilities, workflows, and relationships.
- Current stage, lifecycle, bets, decisions, risks, and dependencies.
- Evidence sources and repeated artifacts.
- Status, dates, owners, confidence, metrics, or next actions worth tracking.
- The PM's natural product and organizational vocabulary.

Translate that model into folders, subfolders, structured trackers, templates, skills, and agent
routes. Decide the layer first: `product-docs/` holds current product work;
`product-practices/skills/`, `templates/`, and `references/` hold reusable judgment, formats, and
examples. Build three synchronized plans—product structure, product practices, and agents—with the
same four sets:

- **Keep:** supports current/near-term work, contains user-authored material, or is a necessary
  cross-cutting area.
- **Add:** needed now or soon and has a purpose distinct from an existing area.
- **Remove:** clearly irrelevant generated folders containing only their unchanged starter
  `INDEX.md`.
- **Ask:** relevance is uncertain or the area contains user-authored files, raw input, custom links,
  index content, or nested artifacts.

Use the installed `pm-os-setup/references/product-profiles.md` when the host makes it available.
Requirements determine immediate scope; product and PM context supply vocabulary and high-confidence
gaps. Do not union every stage or PM-role profile.

Remove clearly irrelevant generated-empty folders without a second question and report them later.
For all **Ask** items, send one consolidated confirmation listing exact actions. Never delete or
relocate user-authored content from inference alone. If the PM does not answer, keep it.

When removing a product area, remove or revise generated skills, templates, specialists, routes, and
index rows serving only that area. Do not leave orphaned machinery.

Begin with product vision, meetings, outcomes, decisions, PRDs, and the skill core: summarize notes,
brainstorm, synthesize outcomes, document product context, and write PRDs. Remove even a common area,
skill, or specialist when it clearly does not fit. Add design, data, research, roadmap, experiment,
launch, stakeholder communication, or other lanes only when scope earns them.

## Step 3 — Apply the product context and structure

1. If this is a legacy scaffold, move a top-level `product-skills/` directory into
   `product-practices/skills/` in place. Preserve content and update every link. Do not create a
   replacement workspace root.
2. Replace unresolved `{{PROJECT_NAME}}` tokens outside this personalization folder when the name is
   known.
3. Apply the keep/add/remove/confirmed-ask plan. Use product language and useful lifecycle or
   product-surface subfolders. Give each new content folder an `INDEX.md`. Use a table, CSV, JSON, or
   sheet for repeated fields and status. Remove stale links and index rows.
4. Update `START_HERE.md` with a short product-specific introduction when useful.
5. Update `product-docs/product-vision.md` with product, users, problem/opportunity, stage, active
   bets, intended outcomes, evidence, key actors/surfaces, and known constraints. Do not describe the
   Chief PM or PM OS as the product unless that is what the user is building.
6. Customize `agents/pm-chief.md`: adjust persona, routes, standing rules, and context gathering to
   the product, PM scope, and kept content areas.
7. Apply product-practice and agent plans with the product structure. Create or update skills and
   templates when outputs need repeatable judgment, structure, or format. Remove unused generic
   skills and specialists. Add a specialist only for a distinct recurring role.
8. Apply `_workspace_setup_docs/skills/apply-pmos-struct.md`: verify names, audience labels, indexes,
   links, product-vision references, and synchronized routing.

Do not generate `.claude/agents/` or `.github/agents/` during basic setup unless the PM asks. Cursor
is already wired through `.cursor/rules/pm-os.mdc`.

## Step 4 — Validate, summarize, and clean up

Confirm the workspace name, product/users, problem/opportunity, stage, active work, next outcome, and
requested sources are captured. Search for stale paths, missing targets, orphaned routes, and
unresolved template tokens.

Prepare a concise handoff covering:

- Updated product vision, current stage, and focus.
- How the product-doc structure and trackers fit the PM's scope.
- Areas kept, added, removed, or deliberately retained.
- Skills, templates, references, or agents changed and which outputs they control.
- The final root path or why it remained unchanged.

If personalization is complete, delete `_workspace_setup_docs/personalization/` and remove its row
from `_workspace_setup_docs/INDEX.md`. Keep `START_HERE.md`. If required context is missing, leave
personalization in place and ask the smallest necessary follow-up.

## Step 5 — Rename the root last

Do this by default as the final step—no separate confirmation is required. Skip it only if the PM
asked to keep the current folder name.

1. Compute the same-parent destination. Use the PM's exact folder name when supplied; otherwise use
   `<project-slug>-workspace` in `lower-kebab-case`.
2. Confirm the destination does not exist, the parent is writable, and this is the intended PM OS
   root rather than a broad folder containing unrelated projects. Ask before renaming when unrelated
   material exists.
3. Finish every edit, validation, personalization-folder deletion, and summary preparation first.
4. Rename the directory itself as one move (`mv -- old new` on macOS/Linux or
   `Move-Item -LiteralPath old -Destination new` on PowerShell). Do not `mkdir` a new root and move
   or copy contents into it.
5. Make the rename the final filesystem operation. Report old and new absolute paths and tell the PM
   their editor may need to reopen the new folder.

If a safety check fails, leave the root unchanged and report the exact blocker. Product
personalization may still be complete.
