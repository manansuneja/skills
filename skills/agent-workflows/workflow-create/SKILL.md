---
name: workflow-create
description: Turns a repeatable process into a reusable agent workflow. It can create new step-skills, connect skills published by other creators without modifying them, adopt and compose skills the user owns, or update and remove workflows it created. Use when the user invokes /workflow-create, says "/workflow-create connect these skills", provides skill names or GitHub URLs to wire together, or asks to create, connect, compose, change, repair, validate, or delete a skill workflow.
---

# Workflow Create

Create, connect, compose, update, and delete reusable skill workflows. Build from a broad goal,
connect skills published by other creators without changing them, or adopt skills the user owns.
Treat `/workflow-create` as the user-facing invocation for this skill.

The output is a maintained operating procedure: a parent coordinator skill, bounded child skills, a single linkage ledger, a short README, runStatus tracking, validation checks, and enough handoff structure for future runs to work without relying on chat memory.

This skill creates and maintains the workflow family. It stays focused on the workflow and context, and defers skill-authoring craft to Anthropic's `skill-creator`: it uses the installed `skill-creator` if present, otherwise the agent retrieves it from the canonical source, then shapes the parent and child skills to its standards (see Phase 0 and [`references/skill-standards.md`](references/skill-standards.md)). Every skill it generates carries a Workflow Creator signature so a family member is always identifiable later (see Signature And Watermark). The generated parent skill runs the actual workflow later whenever the user invokes it; it should not call `skill-creator` during ordinary workflow runs unless the workflow itself is explicitly about creating or modifying skills.

## Quick Start

Use this skill to turn a repeatable process into a reusable family, connect independently published
skills into one workflow, adopt skills the user owns, or change an existing family. The user need
not say “build me a workflow”: invoking the skill on a bare goal is enough.

```text
/workflow-create "Build me a reusable workflow for launching niche content sites."
/workflow-create plan-only "Design a workflow for researching jobs, tailoring resumes, preparing interviews, and tracking follow-ups."
/workflow-create compose "wire my-voice-it, voice-distance-check, and polish-my-voice-it into one publishing workflow."
/workflow-create connect these skills - owner/research-skills --skill research, https://github.com/other/writing-skill - into one content workflow
/workflow-create update "Add a publish step to the acme-website workflow."
/workflow-create delete "Remove the content-site workflow."
```

Expected result for `create`, `connect`, and `compose`:

- One parent coordinator skill named `<prefix>-workflow`.
- Usually two to five steps. `connect` keeps third-party skills unchanged and records them as external dependencies. `compose` adopts user-owned skills into the family and may rename them after confirmation.
- A coordinator `linkages.md` that registers every family member, the run order, and a version stamp.
- A short coordinator `README.md`.
- A `runStatus.md` pattern written into the active project during each run.
- A static validation result.

## Operating Rule

Default to building the smallest useful workflow. First decide whether the goal even needs a family (the family gate in Phase 2). When it does, aim for two to five child skills; use more than five only when the domain has clear standalone responsibilities that would otherwise make a child too broad.

Ask when the goal is too ambiguous to decompose precisely, when the likely skill boundaries are uncertain, or when multiple decompositions would produce meaningfully different workflows. A broad goal yields a generic workflow, so sharpening a vague goal into a specific one (see Phase 1) is mandatory, not optional. Otherwise proceed with clear assumptions and record them.

Before creating files, collect enough upfront context to avoid mid-work interruptions. Prefer one focused intake round that captures the project name, workflow name, purpose, concrete examples, success criteria, and install root. It is fine to ask the user directly for these.

## Skill Design Principles

Every generated skill should be:

- Concise: keep `SKILL.md` lean and move durable details into directly linked references.
- Responsible for one thing: a child skill owns one bounded capability, not a multi-step workflow.
- Composable: it can be run by the parent, reused by another workflow, or called standalone.
- Progressively disclosed: metadata triggers the skill, `SKILL.md` gives the core procedure, references load only when needed.
- Harness-agnostic: write paths, commands, and state conventions that work in any agent that can read instructions and invoke skills (Claude Code, Codex, Cursor, CLI agents).
- Process over prose: actionable workflows with checkpoints, evidence, and exit criteria, not essays about best practices.
- Assumption-aware: surface assumptions before acting, stop when requirements conflict, and touch only the intended workflow files.

## Lifecycle

This skill supports five verbs. Infer the verb from the request; default to `create`.

- `create` (default): build a new workflow family. Modifiers:
  - `plan-only`: produce architecture, naming, and contracts without writing skill files.
  - `shell` / `scaffold-only`: write the coordinator and child skill shells, `linkages.md`, and `README.md` with minimal references.
- `connect`: wire independently published or shared skills into one workflow without renaming or editing them. Accept installed skill names, local paths, GitHub URLs, and `owner/repo --skill name` references. Generate the coordinator and dependency ledger around them. See Connect Lifecycle.
- `compose`: adopt skills the user owns into a workflow family. These become family members and are re-prefixed only after explicit confirmation. See Compose Lifecycle.
- `update`: modify an existing family. Add a child, edit a child, remove a child, repair drift (paths, frontmatter names, orphans), re-sync `linkages.md` and `README.md`, and bump the version stamp. This absorbs the older `extend-existing` and `repair-linkages` flows. See Update Lifecycle.
- `delete`: remove an existing family safely, with confirmation and orphan protection. See Delete Lifecycle.

## Naming Convention

The naming prefix is what binds a family. There are no family folders; skills are installed flat and grouped by their shared prefix.

- Workflow prefix: `<workflow-slug>` when there is no separate project or brand, or `<project-slug>-<workflow-slug>` when one brand or project will host multiple workflows.
- Coordinator skill: `<prefix>-workflow`. Exactly one per family. The `-workflow` suffix marks the single entrypoint that runs the whole sequence and calls the children. Children never use it.
- Child skills: `<prefix>-<phase-action>` with short, concrete phase verbs such as `init`, `research`, `scaffold`, `draft`, `design`, `transform`, `audit`, `publish`. An optional `-it` suffix is allowed but drop it when the name grows long.
- Project run folder: `<prefix>-workflow-run/runStatus.md`, created in the active project, never inside the skill folder.

Examples:

```text
voice-workflow              (coordinator)
voice-capture
voice-polish
voice-publish

acme-website-workflow  (coordinator)   runs the whole website workflow
acme-website-init
acme-website-design
acme-website-audit

acme-content-workflow  (coordinator)   a second, separate workflow under the same brand
acme-content-research
acme-content-draft
```

Every generated name must conform to the Agent Skills open standard (https://agentskills.io/specification):

- 1–64 characters.
- Lowercase letters, digits, and hyphens only (`a-z`, `0-9`, `-`).
- Must not start or end with a hyphen, and must not contain consecutive hyphens (`--`).
- Must match the skill's parent folder name exactly.
- Never contains `claude` or `anthropic`.

These rules apply to `workflow-create` itself and to every coordinator and child skill it generates. `validate_workflow_family.py` enforces them, and `skills-ref validate` (the official validator) confirms spec conformance — see Phase 7.

## Phase 0: Preflight — Skill Authoring Standards

`workflow-create` stays light. [`references/skill-standards.md`](references/skill-standards.md) inlines the **stable skill-format basics** (folder layout, frontmatter, progressive disclosure, the harness-fatal YAML rules) for offline self-sufficiency, and **points to Anthropic's `skill-creator`** for the deeper, evolving craft and the scaffolding/validation tooling. Run this preflight for `create`, `connect`, `compose`, `shell`, and `update`; skip for `plan-only` and `delete`.

Resolve the standards via [`references/skill-standards.md`](references/skill-standards.md):

1. If `skill-creator` is already installed (host agent exposes it, or a folder exists under `${SKILLS_ROOT}/skill-creator`), use it. The installed copy is whatever the user last pulled, so upstream updates are captured this way.
2. If it is not present, **retrieve it** from the canonical source (`npx skills add anthropics/skills --skill skill-creator`, or fetch the files into `${SKILLS_ROOT}/skill-creator`), then follow it. The agent does the fetch at authoring time — this skill only points to where it lives.
3. If retrieval is impossible (offline/unreachable), proceed using the non-negotiable frontmatter rules in `references/skill-standards.md` and tell the user `skill-creator` could not be fetched.

Whichever path, generation must satisfy `skill-creator`'s standards and the local frontmatter rules, the Phase 5 requirements (including the watermark) still apply, and the family is checked with `scripts/validate_workflow_family.py` before finishing (it hard-fails on invalid YAML frontmatter and merge-conflict markers — the breakage that silently de-registers a skill).

Before that validation, run the optional **pruning pass** described in `references/skill-standards.md` (resolved the same way as `skill-creator`, but never blocking): it catches what structural checks don't — description duplication, sprawl past the line budget, vague completion criteria, and dead prose.

## Phase 1: Understand Goal And Name

Capture:

- Verbatim user request.
- Project or brand name (optional). Drives the first prefix segment when present.
- Workflow name (required). Drives the workflow prefix segment.
- Purpose, in one or two sentences, for the README and coordinator context.
- Desired outcome.
- Two to three concrete use cases the workflow should support.
- Trigger phrases that should invoke the coordinator, and negative triggers that should not.
- Example inputs and outputs when available.
- Target user or audience.
- Constraints, assets, URLs, and references.
- For `connect`: each dependency's skill name, source repository or URL, install scope, expected path, and installed `SKILL.md` hash.
- Desired automation level and validation expectation.
- Success criteria for the workflow and for each child skill.
- Distribution target: personal install, team install, public package, or repository template.
- Install scope: global (default) or project-local. See Install Scope below.
- Host harness: which agent is running this skill (Claude Code, Codex, Cursor, etc.). Detect it rather than asking — see Detect The Host Harness below.

It is fine to ask the user directly for project name, workflow name, and purpose. Auto-derive a candidate workflow name from the goal, then confirm it. Convert the confirmed project and workflow names into the lowercase kebab-case prefix described in the Naming Convention.

**Sharpen a broad goal before decomposing.** The quality of the generated skills is bounded by how specific the goal is — a broad one-liner (for example, "launch niche content sites") produces a generic, mediocre workflow. When the goal is vague, do not proceed on it; ask one focused round of questions that narrows it into a specific, well-scoped goal, prioritizing the answers that change the skill breakdown:

- Who or what it's for, and what "good" output looks like.
- The concrete steps the user already does by hand, in order.
- Inputs available at the start, and the artifact expected at the end.
- Tools, platforms, formats, or style the workflow must respect.
- What should be explicitly out of scope.

If the user has already defined the skills or the breakdown in their prompt (the steps, their order, or the child skills), treat that as the decomposition and honor it — confirm only what is genuinely ambiguous rather than re-deriving it. If the goal is already specific and well-scoped, proceed with explicit assumptions and record them in the brief.

When the goal is vague or the user asks what this can do, offer the closest worked example from [`references/examples.md`](references/examples.md) as a starting template (for example, "something like the `clarify` writing workflow" or "composed like the `ship` example"), then sharpen their specific goal from there. The examples span the simple → complex range and the create/compose lifecycles.

### Detect The Host Harness

`.agents/skills` is the standard, cross-client home for skills under the Agent Skills open standard: compliant agents scan it specifically so skills installed by one tool are visible to the others. **Prefer the standard `.agents/skills` location, and treat `.claude/skills` as the single exception — used only when Claude Code itself is the installing harness.** That exception is safe because most compliant agents also scan `.claude/skills` for pragmatic compatibility, so a Claude-Code install is still broadly discoverable, and the opt-in symlink (see Cross-Harness Access) closes any remaining gap.

Determine the host harness with a simple, detection-first approach — do not ask the user which agent they are in.

1. **Self-identify (primary).** You are the running agent. If you are Claude Code, the host harness is Claude Code. If you are Codex, Cursor, Gemini CLI, or another agent, use that identity. This is the main signal — rely on it.
2. **Confirm from the environment (optional sanity check).** Claude Code exports `CLAUDECODE=1` (plus `CLAUDE_CODE_*` vars) into the shell. If you want to corroborate, a quick `env | grep -i claudecode` is enough. Filesystem checks like "does `~/.claude` exist" are weak — a directory only means the tool is *installed*, not that it is the active harness — so prefer self-identification and env vars over directory probing.
3. **Map harness → skills home (standard-first):**
   - **Claude Code** (the only exception) → `${USER_ROOT}/.claude/skills` (global) or `<project-root>/.claude/skills` (project-local), its native home.
   - **Every other / unknown harness** → `${USER_ROOT}/.agents/skills` (global) or `<project-root>/.agents/skills` (project-local), the standard cross-client home.

Set `${SKILLS_ROOT}` to the resolved home for the detected harness and chosen scope. This is where the real folders are written — no symlink needed for the host harness to find them. Cross-linking to *other* harnesses is a separate, opt-in step (see Cross-Harness Access).

### Install Scope

The family installs at one of two scopes, independent of harness. The path follows the standard-first rule above — `.agents/skills` by default, `.claude/skills` only when Claude Code is the installing harness:

- **Global (default).** Under the user's home: `.agents/skills` (standard), or `.claude/skills` when Claude Code is the host. Available across all of the user's projects.
- **Project-local.** Under a named `<project-root>`: `<project-root>/.agents/skills` (standard), or `<project-root>/.claude/skills` when Claude Code is the host. Use when the user wants the workflow checked into and scoped to one repo (shareable with collaborators, versioned with the code).

Default to global, but always tell the user which scope and which path you are using and offer the other. If the request clearly implies one ("install this in this repo", "just for this project", "make it available everywhere"), follow that. If scope is ambiguous and the choice would matter, ask.

Resolve install locations from the user's home directory or the named project root, not hardcoded machine-specific paths. If the chosen `${SKILLS_ROOT}` does not exist, create it for `create` or `shell` modes and tell the user where it was created. For `plan-only`, state the resolved root and that it should be created before install.

Generated families are plain Markdown folders with front matter, not locked to any home. The coordinator `README.md` lists the member folders and their paths so the user can move or copy the whole set into any agent's skill, rule, or prompt location (`.cursor/rules/`, Claude Code, Gemini CLI, Codex, Aider, Windsurf, OpenCode).

### Cross-Harness Access (opt-in)

For global installs, read [`references/cross-harness-access.md`](references/cross-harness-access.md)
after creating or updating the family. Offer one optional symlink into the other common skills root;
act only on a clear yes, touch only this run's family folders, and skip for project-local installs.

## Phase 2: Family Gate

Before decomposing, decide whether the goal needs a family at all.

If the goal collapses to one bounded capability, build a single skill and stop. Follow `references/skill-standards.md` and emit just that skill, wrapped in a minimal coordinator so the workflow can grow later: a `<prefix>-workflow` coordinator plus a `linkages.md` with one entry. Do not invent extra phases to justify a family.

Only proceed to a multi-skill decomposition when at least two phases each pass the split test in Phase 3. A coordinator that sequences a single real step is acceptable only as the single-skill case above; never split one capability into two children to look like a workflow.

## Phase 3: Decompose Domain

Spend real design time here. The goal is the smallest set of standalone, composable skills that run well in sequence and independently.

For a proven shape to borrow from, consult [`references/examples.md`](references/examples.md): it shows how five real goals were gated and split (medium sequential, complex multi-tool, context-aware with a child-owned reference, a composed family with conditional steps, and a single-skill case where the gate fired) and *why* each boundary was drawn. Adapt the closest one rather than decomposing from scratch.

Split the workflow into phases with crisp verbs. A phase deserves a child skill only when it satisfies at least two of these tests:

- Requires distinct expertise.
- Produces a distinct artifact.
- Can be reused independently.
- Would make the parent too large if embedded.
- Needs separate references, scripts, or assets.
- Has its own validation or quality bar.
- Has different failure modes, permissions, or rollback needs.

Do not create a child skill merely because something is a step. Merge phases when they share the same inputs, produce one combined artifact, have the same validation bar, or would rarely be useful alone.

Split/merge checks:

- Standalone test: could a user sensibly call this child by itself?
- Contract test: does it have clear inputs, outputs, and done criteria?
- Context test: would separating it reduce context load or avoid mixing domains?
- Coupling test: if it always needs the previous child and cannot infer missing context, merge it.
- Count test: if there are more than five child skills, justify each one or merge the weakest boundaries.

Prefer phase verbs like `research`, `scaffold`, `draft`, `transform`, `validate`, `publish`, and `audit`. Avoid vague phases like `strategy`, `misc`, or `support`. Name every skill with the workflow prefix per the Naming Convention.

Classify the workflow pattern and record it in `linkages.md`:

- `sequential`: phases must run in a fixed order.
- `multi-tool`: phases coordinate multiple MCP servers, local tools, APIs, or apps.
- `iterative`: output quality improves through validation and refinement loops.
- `context-aware`: the coordinator chooses different tools or paths based on input.
- `domain-intelligence`: the value is embedded judgment, policy, standards, or review.

Before moving to contracts, produce a short decomposition review:

```md
## Decomposition Review

- Project / workflow prefix:
- Family needed? (yes / single-skill)
- Candidate child skills:
- Why these boundaries:
- What was merged and why:
- Open decomposition questions:
```

If open questions would change the number, names, order, or responsibilities of child skills, ask the user before writing files. Offer a recommended decomposition, but invite correction.

## Phase 4: Design Contracts

Write a contract for each child before creating files:

```md
## <skill-name>

- Role:
- Trigger:
- Inputs:
- Outputs:
- Reads:
- Writes:
- Validation:
- Evidence:
- Exit criteria:
- Error handling:
- Rollback or recovery:
- Skip conditions:
- Boundaries:
- Orchestration note:
- Standalone usage:
- Why this is separate:
```

The parent is the coordinator skill and single user-facing entrypoint. It does not replace the child skills or own their implementation. Standalone, the parent mainly parses the verb and mode, initializes `runStatus.md`, checks `linkages.md`, sequences child skills, passes handoff context, and synthesizes the final result. Children own their bounded phase.

## Phase 5: Generate Skill Family

Install skills flat under the skills root. The family is bound by the shared naming prefix, not by a wrapping folder. Only the coordinator folder holds family-level files.

```text
${SKILLS_ROOT}/
  <prefix>-workflow/
    SKILL.md
    linkages.md
    README.md
    references/
    scripts/
  <prefix>-<phase-a>/
    SKILL.md
    references/
  <prefix>-<phase-b>/
    SKILL.md
    references/
```

The coordinator folder is the family hub. It holds `SKILL.md`, the single `linkages.md` (registry, run order, load-when notes, and version stamp), a short `README.md`, and any change-checking helper script. Do not create `linkages.md`, `README.md`, or `index.md` inside child folders.

`README.md` is human-facing and short: what the workflow does, the coordinator command to call, the modes, what each child does, where `runStatus.md` appears during a run, and the member skill paths so the user can copy the set into another harness.

There is no separate `index.md`. The navigation and load-when guidance live inside `linkages.md`.

Do not add README, changelog, or setup files inside child skill folders. If human-facing docs are needed for a public package, put them at the repository root.

Follow `skill-creator`'s standards (resolved in Phase 0 — installed or fetched) for every generated skill: correct frontmatter, clear trigger descriptions, concise bodies, progressive disclosure, direct `references/` links. Always enforce the non-negotiable frontmatter rules in [`references/skill-standards.md`](references/skill-standards.md) on top, even when offline. This is a creation-time responsibility, not a runtime responsibility of the generated coordinator.

Generated skills must follow core requirements:

- Folder name and frontmatter `name` match exactly.
- Names use lowercase kebab-case, no spaces, underscores, capitals, `claude`, or `anthropic`.
- Exactly one skill in the family is named `<prefix>-workflow`; it is the coordinator.
- `SKILL.md` is named exactly `SKILL.md`.
- `SKILL.md` is saved as UTF-8 without BOM and starts at byte 1 with literal `---`; no invisible bytes may appear before frontmatter.
- Description states what the skill does and when to use it, includes realistic trigger phrases, stays under 1024 characters, and contains no angle brackets.
- Every generated skill carries the Workflow Creator signature (see Signature And Watermark below).
- Use `scripts/` for deterministic fragile checks, `references/` for on-demand context, and `assets/` for files used in output.
- Keep references one level deep; if a reference is longer than 100 lines, include a short table of contents.

### Signature And Watermark

Every skill this tool generates or adopts — coordinator and children, on `create`, `shell`, `compose`, and `update` — must carry a Workflow Creator signature. External dependencies connected from other creators are never signed, renamed, or edited; their original package remains intact.

Write the signature in two places in each generated `SKILL.md`:

1. A `metadata` block in the frontmatter (the canonical, machine-readable marker):

   ```yaml
   metadata:
     generator: workflow-create
     generator-version: <stamp matching the linkages.md Version>
     workflow-prefix: <prefix>
     role: coordinator   # or: child
   ```

2. A short human-visible footer as the last line of the body:

   ```md
   ---

   _Generated by workflow-create (Workflow Creator) · family `<prefix>` · v<stamp>. This signature marks the skill as part of a Workflow Creator family._
   ```

Detection contract: the canonical signal is the frontmatter field `metadata.generator: workflow-create`. A harness built on top can recursively scan skill folders and treat any `SKILL.md` whose `metadata.generator` equals `workflow-create` as Workflow-Creator-generated, then read `workflow-prefix` to group families and `generator-version` to detect staleness. Keep these key names stable; do not rename them per family.

When the `update` lifecycle bumps the version stamp, update `generator-version` in every touched skill's signature to match.

### Description And Triggering

Because the family is installed flat and every child is standalone-callable, members compete to match a user request. Write descriptions so routing stays correct:

- The coordinator (`<prefix>-workflow`) description must claim the full, multi-step workflow and the broad trigger phrases.
- Each child description must claim only its one phase and explicitly direct full-workflow requests to `/<prefix>-workflow`.

## Phase 6: Wire Workflow

The generated parent skill must:

- State clearly that it is the workflow coordinator and user-facing entrypoint, not the creator of the family.
- Read `linkages.md` before running, and verify child paths, frontmatter names, and orchestration notes against it.
- For external dependencies, verify the original name, path, recorded source, and `SKILL.md` hash. If a dependency is missing or has drifted, block that step and show the recorded install/update command instead of silently replacing it.
- Take the default run order from `linkages.md`, but honor run-scope sequence overrides in the brief: reordering steps, skipping steps, running only a subset, or stopping early (see Run-Scope Sequence Overrides below). Run-scope overrides apply to that run only and never edit `linkages.md`.
- Create or update one `runStatus.md` per run in the active project, never inside the installed skill family.
- Prefer the target project or repo root when the request names one. If the target workspace is not obvious, ask where to store the run folder. If the user skips, use the current working directory fallback and tell the user the chosen path.
- Store the file at `<target-or-project>/<prefix>-workflow-run/runStatus.md`. For fallback cases, use `<cwd>/.workflow-runs/<prefix>-workflow-run/runStatus.md`.
- Resolve where this run's **deliverables** land and in what form, using the same lightweight rule as `runStatus.md`: do a basic check of the project (is it a repo? what type — web app, library, docs, plain folder? where do similar files already live? what's already installed?), pick a sensible portable default (Markdown for prose, a self-contained file for a visual, reuse an existing convention when one exists), and **ask the user only when context demands** it — when the destination is ambiguous, the choice would scaffold heavily, install a dependency, or overwrite something. Record the resolved location in `runStatus.md`. Never write deliverables into the installed skill folder. This is a best-practice nudge, not a rigid spec: the coding agent supplies the intelligence to read the project and decide; the coordinator's job is only to pause and resolve this deliberately instead of scattering files. Leave format/tool/path specifics to the children and to how the user later evolves them.
- Preserve the user request, derived inputs, dependency checks, step table, outputs, blockers, and log in `runStatus.md`. Keep most-recent run state; overwrite or append a short prior-run note rather than keeping full run history.
- Mark each step `in-progress`, then `done`, `skipped`, or `blocked`.
- Pass only relevant context to each child, including the exact `runStatus.md` path for this run.
- Record each child's important outputs, changed files, and artifacts in `runStatus.md` immediately after that step completes.
- Stop on dependency drift that could change behavior.
- Write handoffs so any child is resumable from `runStatus.md` alone, without the parent's working memory. The agent may stay in one context or, if its context is constrained, continue in a fresh context or subagent; either way `runStatus.md` is the resume point. Do not encode harness-specific context-management mechanics.

Each generated child skill must include:

```md
## Orchestration Linkage

- Parent: `/<prefix>-workflow`
- Previous: `/<previous-skill>` or none
- Next: `/<next-skill>` or complete
- When used by `/<prefix>-workflow`, read and update this run's project `runStatus.md` for this step only.
- When used standalone, derive a local brief from the current request, do not create or touch any workflow `runStatus.md`, and produce this phase's output independently.
```

Children must be callable standalone as well as by the parent. When a parent run is active, children read the project `runStatus.md`, respect sibling boundaries, and update only their assigned row or notes. When no parent run exists, children do not write `runStatus.md` at all; they ask only for missing inputs that cannot be safely inferred, then complete their bounded phase. Only the coordinator owns `runStatus.md`.

### Run-Scope Sequence Overrides

The generated coordinator must let the user change which children run, and in what order, for a single run — without editing the family. Build this into the parent so it can follow plain-language direction such as "run only research and publish", "skip the audit step", "do draft before research this time", or "stop after design".

The coordinator must:

- Treat the `linkages.md` Chain as the default order, then parse any reorder, skip, subset, or stop-early directives from the brief into an effective order for this run.
- Check dependency safety before applying: if a skipped or moved-earlier step normally produces inputs a later step needs, and those inputs are not already present in `runStatus.md` or safely derivable, warn the user and either ask how to proceed or mark the dependent step `blocked`. Respect each child's documented skip conditions.
- Record both the default order and the effective order in `runStatus.md`, with a one-line reason for every skipped or reordered step. Mark un-run steps `skipped`.
- Apply the override to this run only. Never write run-scope changes into `linkages.md`.

To make an ordering change permanent (a new default order, or a step that should be skipped by default), the change must go through `/workflow-create update`, which re-syncs `linkages.md` and bumps the version. If the user asks the coordinator to make a sequence change "permanent" or "always", the coordinator should say so and route them to the update lifecycle rather than silently persisting it.

## Phase 7: Validate

Run static validation before finishing:

- Frontmatter names match folder names and the `linkages.md` registry.
- Every `SKILL.md` starts at byte 1 with literal `---` and has no UTF-8 BOM before frontmatter.
- Exactly one family skill is named `<prefix>-workflow`.
- Every family skill name starts with the workflow prefix.
- Parent `linkages.md` lists every member and matches actual paths.
- No `<prefix>-*` skill exists on disk that is missing from `linkages.md` (orphan check); if found, ask the user whether it belongs.
- Every child has an orchestration linkage note and points back to `/<prefix>-workflow`.
- Parent `SKILL.md` references `linkages.md` and `runStatus.md`.
- Coordinator `README.md` exists and names the command, modes, child sequence, and runStatus location.
- Every child includes standalone-mode instructions and does not require a previous sibling run.
- Every generated skill (coordinator and children) carries the `metadata.generator: workflow-create` signature and matching footer.
- Every external dependency is marked `external` in the Chain, remains unmodified, resolves to a valid `SKILL.md`, and has a source plus install command in `## External Dependencies`.
- The coordinator describes how it accepts run-scope sequence overrides and records the effective order in `runStatus.md`.
- Linkage paths use placeholders for distributable workflows instead of creator-specific absolute paths.

Run `scripts/validate_workflow_family.py <coordinator-skill-dir> --skills-root <skills-root>` after creating or updating a family. If validation fails, fix the generated files and rerun it. This validator checks family structure (linkages, orphans, watermark, prefix discipline), not behavior.

When available, also run the **`skills-ref` reference validator** on each generated skill folder as a spec-conformance sanity check (frontmatter, naming rules, directory layout):

```bash
skills-ref validate <coordinator-skill-dir>
skills-ref validate <each-child-skill-dir>
```

`skills-ref` is the Agent Skills standard's reference library — a Python CLI from `agentskills/agentskills/skills-ref`, installed with `pip install -e .` or `uv sync` from that subdirectory (it is not on npm). Its README notes it is a demonstration reference, not a production tool, so treat its result as a spec sanity-check and keep `scripts/validate_workflow_family.py` as the enforced gate. The two are complementary: `skills-ref` checks the open-standard skill format, `validate_workflow_family.py` enforces the family/coordinator contract. If `skills-ref` is not installed, do not block on it — the family validator already covers the harness-fatal cases. A structurally valid family can still have semantic handoff gaps, so also run the forward test below.

For forward validation, run the generated parent on a small example in plan-only mode. Prove that the parent can derive inputs, initialize `runStatus.md`, hand off to children, record status, and summarize completion or blockers.

Add a validation section to the generated parent covering triggering tests (obvious request, paraphrased request, unrelated non-trigger), functional tests (valid output, expected artifacts, child handoff, error handling, edge cases), how the workflow improves over manual prompting, and stop criteria for iterative workflows. For workflows with external tools or MCPs, include connection/auth checks, fallback behavior, and rollback for each irreversible step.

## Phase 8: Prepare Distribution

When the workflow is public, team-facing, or package-like:

- Keep human-facing docs at the repository root, not inside child skill folders.
- Include install instructions that explain the selected skills root.
- Include portability instructions: the family is plain Markdown, and the coordinator `README.md` lists the member folders to copy.
- For connected workflows, list external dependencies separately with their source and install command; do not imply they are authored or redistributed by the workflow creator.
- Explain the outcome the workflow enables, not only the files it creates.
- Package only after validation passes when packaging is requested.

## Update Lifecycle

Use when the user wants to change an existing family (add, edit, or remove a child; reorder the default sequence; mark a step default-skipped or optional; repair drift; extend phases).

1. Locate the family by its `<prefix>-workflow` coordinator and read its `linkages.md`.
2. Run the orphan and drift checks: compare `linkages.md` against the `<prefix>-*` skills on disk. For any orphan, ask the user whether it belongs in the workflow or is a separate standalone skill; never absorb or delete it without confirmation.
3. Apply the change following `references/skill-standards.md`: add a new child folder, edit an existing child, remove a child, or change the default run order (reorder steps, or mark a step default-skipped/optional in the Chain).
4. Re-sync `linkages.md` (run order, paths, frontmatter names, previous/next) and `README.md`. For a reorder, also update each affected child's Previous/Next orchestration note.
5. Bump the version stamp in `linkages.md`, update the `generator-version` in every touched skill's signature to match, and append a change-log line.
6. Re-run validation (Phase 7).

Confirm with the user before any change that alters the default run order or removes a child, since those can change behavior. Permanent ordering changes belong here; one-off ordering changes for a single run are handled by the coordinator at run time (see Run-Scope Sequence Overrides) and must not be written into `linkages.md`.

## Connect And Compose Lifecycles

Read [`references/connect-and-compose.md`](references/connect-and-compose.md) whenever the request
names existing skills.

- Use `connect` for skills published or owned by other people. Preserve them unchanged and register
  them as external dependencies with source, install command, path, and hash.
- Use `compose` only for skills the user owns and wants adopted into the family. Confirm every rename
  before modifying those skills.
- When ownership is unclear, default to non-destructive `connect`.

## Delete Lifecycle

Deleting a family removes files; treat it as destructive.

1. Read the `<prefix>-workflow` coordinator's `linkages.md` to get the exact member list.
2. Show the user the full list of folders that will be removed and confirm before deleting anything.
3. Delete only skills listed in `linkages.md`. Never auto-delete a `<prefix>-*` skill that is not in the ledger; surface it as an orphan and ask first.
4. Ask whether to remove the coordinator's `linkages.md` and `README.md` as well, or leave them as a tombstone.
5. Note that project `runStatus.md` files live in the user's projects, not the skill family; do not delete those unless the user explicitly asks.

## Reference Patterns

Read [`references/workflow-patterns.md`](references/workflow-patterns.md) when writing generated parent skills, child skills, the linkage ledger, run ledgers, or validation prompts. Read [`references/examples.md`](references/examples.md) for named, validated example families to offer during intake (Phase 1) or borrow a decomposition shape from (Phase 3). Worked, runnable versions of those families were generated into an isolated local sandbox (`testing/`, not shipped with the published skill) so simulating a run never touches installed skills.

## Finish Criteria

Finish only when the requested verb and mode are complete and the user can see:

- Coordinator skill path and child skill paths (or, for delete, the removed paths).
- Linkage ledger path and version.
- README path.
- runStatus location or pattern.
- Validation result.
- Trigger and functional test plan.
- Distribution notes when relevant.
- Any assumptions or unresolved decisions.
