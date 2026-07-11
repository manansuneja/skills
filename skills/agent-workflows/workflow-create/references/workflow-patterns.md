# Workflow Skill Family Patterns

Use these patterns when `/workflow-create` generates, updates, or repairs a reusable workflow family.

Families are installed flat under the skills root and bound by a shared naming prefix:

- Prefix: `<workflow-slug>` or `<project-slug>-<workflow-slug>`.
- Coordinator: `<prefix>-workflow` (exactly one per family; the only `-workflow` skill).
- Children: `<prefix>-<phase-action>`.
- External dependencies: independently published skills keep their original names and folders; the coordinator records and calls them but does not adopt them into the prefix.
- Project run folder: `<prefix>-workflow-run/runStatus.md`.

## Parent SKILL.md Pattern

```md
---
name: <prefix>-workflow
description: Coordinates and runs the full <workflow purpose> workflow from one broad brief. Use when the user asks to run, create, or manage the whole <workflow> end to end. For a single step, use that step's skill instead.
metadata:
  generator: workflow-create
  generator-version: <stamp matching linkages.md Version>
  workflow-prefix: <prefix>
  role: coordinator
---

# <Workflow Name> Workflow

Coordinate <goal> from one user brief. This parent skill sequences child skills, preserves shared context, records status, and checks dependency drift.

This skill is the workflow coordinator and user-facing entrypoint. It does not create the family; `/workflow-create` created it using `skill-creator` standards. When invoked, this parent runs the child skills in order according to mode. Do not call `skill-creator` during ordinary workflow runs unless this workflow is explicitly about creating or modifying skills.

## Derive Inputs

Parse the request into: verbatim request, project/workflow prefix, goal, 2-3 use cases, trigger phrases, negative triggers, mode, audience, outputs, constraints, assets, assumptions, open questions, success criteria.

## Workflow Pattern

State the pattern: sequential, multi-tool, iterative, context-aware, or domain-intelligence. Explain why this workflow needs a coordinator instead of one large skill.

## Global Dependency Registry

Read `linkages.md` before running. Verify paths, frontmatter names, child orchestration notes, external dependency sources/hashes, and the version stamp. Use its load-when notes to load only the references needed for the current run or child step. Never edit or silently reinstall a connected external dependency.

## Run Setup

Create one run tracker in the active project:

```text
<target-or-project>/<prefix>-workflow-run/runStatus.md
```

Store run state in the active user workspace, never in the installed skill family. Prefer the target project or repo root when the request names one. If the target workspace is not obvious, ask where to store the run folder. If the user skips, use `.workflow-runs/<prefix>-workflow-run/runStatus.md` under the current working directory and tell the user.

Keep most-recent run state. Pass the exact `runStatus.md` path to every child invocation. Write handoffs so any child is resumable from `runStatus.md` alone.

## Output Resolution

Before producing deliverables, resolve where they land and in what form — the same lightweight way as `runStatus.md`. Do a basic project check (repo? type — web app / library / docs / plain folder? where similar files already live? what's installed?), pick a sensible portable default (Markdown for prose, a self-contained file for a visual, an existing convention when one exists), and ask the user only when context demands — ambiguous destination, heavy scaffolding, a new dependency, or an overwrite. Record the resolved location in `runStatus.md` and pass it to children. Never write deliverables into the installed skill folder. The coding agent supplies the judgment to read the project and decide; the coordinator only pauses to resolve this deliberately instead of scattering files.

## Skill Sequence

List child skills in exact default order with skip conditions and expected outputs. This default order comes from `linkages.md`.

## Run-Scope Sequence Overrides

Accept run-scope direction to reorder, skip, subset, or stop early for this run only (for example "run only research and publish", "skip audit", "draft before research", "stop after design"). Default order is the `linkages.md` Chain. Before applying an override, check dependency safety: if a skipped or moved-earlier step normally feeds a later step and that input is not already in `runStatus.md` or safely derivable, warn and either ask or mark the dependent step `blocked`. Record the default order, the effective order, and a reason for each skip or move in `runStatus.md`. Never write run-scope changes into `linkages.md`; route requests to make an order change permanent to `/workflow-create update`.

## Coordination Rules

The parent owns mode selection, sequencing, run-scope overrides, handoff packets, `runStatus.md`, status transitions, dependency drift, selective reference loading, output recording, and final synthesis. Children own their phase only. Only the parent writes `runStatus.md`.

## Finish Criteria

Summarize completed steps, skipped steps, blockers, artifacts, and validation.

## Validation

Define triggering tests (obvious request, paraphrased request, unrelated non-trigger), functional tests (artifacts, child handoff, error handling, edge cases), comparison to manual prompting, stop criteria, and evidence (files written, tests run, logs, reports, approval).

---

_Generated by workflow-create (Workflow Creator) · family `<prefix>` · v<stamp>. This signature marks the skill as part of a Workflow Creator family._
```

The frontmatter `metadata.generator: workflow-create` is the canonical machine-readable signature; the footer is the human-visible one. Keep both on every generated skill.

## Child SKILL.md Pattern

```md
---
name: <prefix>-<phase-action>
description: Performs <specific phase> for <workflow>. Use when <phase trigger>, either independently or as part of /<prefix>-workflow. For the full workflow, use /<prefix>-workflow.
metadata:
  generator: workflow-create
  generator-version: <stamp matching linkages.md Version>
  workflow-prefix: <prefix>
  role: child
---

# <Child Skill Name>

Own <phase> inside <workflow>.

Keep this skill concise, responsible for one bounded capability, composable, progressively disclosed, and harness-agnostic. Write it as a workflow with checkpoints and exit criteria, not an essay.

## Orchestration Linkage

- Parent: `/<prefix>-workflow`
- Previous: `/<previous-skill>` or none
- Next: `/<next-skill>` or complete
- When used by `/<prefix>-workflow`, read and update this run's project `runStatus.md` for this step only.
- When used standalone, derive a local brief from the current request, do not create or touch any workflow `runStatus.md`, and produce this phase's output independently.

## Inputs

When a parent run is active, read the exact `runStatus.md` path provided by the parent and update only the assigned row or notes. When used standalone, derive the minimum brief from the user's current request and ask only for missing inputs that cannot be safely inferred.

## Workflow

1. Confirm the assigned phase and inputs.
2. Produce only this phase's output.
3. If part of a parent run, update only this phase's status row. If standalone, do not touch `runStatus.md`.
4. Report artifacts and blockers.

Do not take over sibling phases or become a nested multi-step workflow.

## Outputs

List expected files, edits, summaries, or reports.

## Validation, Evidence, Exit Criteria

Define how this phase proves its work, the concrete proof it leaves behind, and what must be true before it reports `done`.

## Error Handling and Rollback

State common failure modes, fallback behavior, recovery, and whether this phase has irreversible effects.

## Boundaries and Why Separate

State what this child must not own, and briefly why it exists as a standalone skill.

---

_Generated by workflow-create (Workflow Creator) · family `<prefix>` · v<stamp>. This signature marks the skill as part of a Workflow Creator family._
```

## Decomposition Checklist

Use this before generating child skills:

- First apply the family gate: if the goal is one bounded capability, build a single skill wrapped in a minimal `<prefix>-workflow` coordinator with a one-entry `linkages.md`. Do not invent phases.
- Aim for two to five child skills by default; more than five needs a clear standalone responsibility per extra child.
- Split a phase only when it passes at least two tests: distinct expertise, distinct artifact, independent reuse, separate references/scripts/assets, separate validation, different failure or rollback behavior.
- Merge phases when they share inputs, produce one combined artifact, share a validation bar, or would rarely be useful alone.
- Reject a child boundary if it would become a multi-step workflow instead of one bounded capability.
- Ask the user when the best boundaries are ambiguous or would materially change the workflow.

## linkages.md Pattern

`linkages.md` lives in the coordinator folder and is the single registry of family membership, run order, load-when guidance, and version. There is no separate `index.md`.

```md
# <Workflow Name> Linkages

Registry and run map for `/<prefix>-workflow`. Project-specific run state lives in `runStatus.md` inside the active project.

Workflow prefix: <prefix>
Coordinator: /<prefix>-workflow
Pattern: <sequential | multi-tool | iterative | context-aware | domain-intelligence>
Version: <semver or date stamp>
Run status pattern: <prefix>-workflow-run/runStatus.md

Path variables:

- `${USER_ROOT}`: current user's home directory.
- `${SKILLS_ROOT}`: skills root resolved from the detected host harness and install scope — `.claude/skills` under the home dir (global) or named project root (project-local) when the host is Claude Code, else `.agents/skills` at the matching location. See "Detect The Host Harness" in SKILL.md.
- `${PARENT_SKILL_DIR}`: the coordinator folder, `${SKILLS_ROOT}/<prefix>-workflow`.

## Chain

This Chain is the default run order. The coordinator may reorder, skip, or subset it for a single run via run-scope overrides; those are recorded in `runStatus.md`, never here. Status is `active` for a normal step, or `default-skip` / `optional` for a step that the default run skips unless asked. Changing the default order or a default-skip flag is a permanent change and goes through `/workflow-create update`.

| Order | Skill | Path | Frontmatter name | Previous | Next | Status | Kind |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - | `/<prefix>-workflow` | `${SKILLS_ROOT}/<prefix>-workflow` | `<prefix>-workflow` | none | coordinator | active | coordinator |
| 1 | `/<prefix>-<phase-one>` | `${SKILLS_ROOT}/<prefix>-<phase-one>` | `<prefix>-<phase-one>` | none | `/external-skill` | active | generated |
| 2 | `/external-skill` | `${SKILLS_ROOT}/external-skill` | `external-skill` | `/<prefix>-<phase-one>` | complete | active | external |

## External Dependencies

Include this section only for connected workflows. Hash is the SHA-256 of the installed `SKILL.md`.

| Skill | Source | Install command | Expected path | SKILL.md SHA-256 | Last verified |
| --- | --- | --- | --- | --- | --- |
| `/external-skill` | `https://github.com/owner/repo` | `npx skills@latest add owner/repo --skill external-skill -g` | `${SKILLS_ROOT}/external-skill` | `<sha256>` | `<yyyy-mm-dd>` |

## References And Load-When

| File | Purpose | Load when | Owner |
| --- | --- | --- | --- |
| <skill>/references/<file>.md | <what it contains> | <when needed> | /<skill> |

## Global Checks

At the start of every run, compare filesystem paths, frontmatter names, and orchestration notes against this table. Flag any `<prefix>-*` skill on disk that is missing from this table as an orphan and ask the user whether it belongs.

## Trigger Quality

- Should trigger:
  - `<obvious user request>`
  - `<paraphrased user request>`
- Should not trigger:
  - `<adjacent but unrelated task>`

## Change Log

- `<date>` Created workflow ledger. Version <stamp>.
```

## README.md Pattern

Create this file in the coordinator folder, not inside a child skill folder:

````md
# <Workflow Name> Workflow

Call `/<prefix>-workflow` once to run the full skill chain.

## How To Run

```text
/<prefix>-workflow "<brief>"
/<prefix>-workflow shell "<brief or workflow idea>"
/workflow-create connect these skills - owner/repo --skill external-skill - into a <purpose> workflow
```

## Modes

- create / run: run the complete child sequence.
- shell: create or run only the minimal scaffold.
- plan-only: plan without writing implementation files.

## Child Sequence

1. `/<prefix>-<phase-one>` - <role>
2. `/<prefix>-<phase-two>` - <role>

## Custom Order

Ask in the brief to change the sequence for a single run, for example "run only <phase-one> and <phase-two>", "skip <phase>", "<phase-two> before <phase-one>", or "stop after <phase>". This applies to that run only. To change the default order permanently, use `/workflow-create update`.

## Tracking

During a run, the coordinator creates or updates `<prefix>-workflow-run/runStatus.md` in the target project/workspace, never inside the installed skill folder. If no project path is obvious, it asks where to store it; if you skip, it uses `.workflow-runs/<prefix>-workflow-run/runStatus.md` under the current directory.

## Member Skills (for moving the family)

This family is plain Markdown installed flat under the skills root. To copy it into another harness, move these folders:

- `<prefix>-workflow/`
- `<prefix>-<phase-one>/`
- `<prefix>-<phase-two>/`

## External Dependencies

List connected skills separately with their original source and install command. They are required
at runtime but are not copied, renamed, or authored by this workflow.

Targets include `.cursor/rules/`, Claude Code, Gemini CLI, Codex, Aider, Windsurf, OpenCode, or any harness that reads Markdown skills.
````

## runStatus.md Pattern

```md
# <Workflow Name> Run Status

Workflow: <name>
Prefix: <prefix>
Coordinator: /<prefix>-workflow
Brief: <verbatim user brief>
Started: <ISO timestamp>

## Derived Inputs

- Goal:
- Mode:
- Outputs:
- Constraints:
- Assumptions:

## Dependency Checks

Registry: <path-to-linkages.md>

| Skill | Kind | Source | Expected path | Actual path | Status | Frontmatter name | Expected hash | Actual hash | Last checked | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Sequence

- Default order (from linkages.md): <list>
- Effective order this run: <list>
- Overrides applied: <reorder / skip / subset / stop-early, with a one-line reason each, or none>

## Steps

The Step column reflects the effective order for this run. Mark un-run steps `skipped` with a reason.

| Step | Skill | Status | Input | Output | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | /<prefix>-<phase-one> | pending | | | |

## Log

- `<timestamp>` Created workflow tracker.
```

## Validation Prompt Pattern

Use a tiny realistic request:

```text
Run /<prefix>-workflow in plan-only mode for: "<small representative goal>".
Create runStatus.md, derive inputs, walk the child sequence, and stop before producing expensive or irreversible external effects.
```

Validation succeeds when the parent can derive inputs, create `runStatus.md`, route each child, record skip or block behavior, and explain the final state.

## Skill Quality Checklist

Use this for every generated parent and child skill:

- Folder name and frontmatter `name` match exactly.
- Name is lowercase kebab-case with no spaces, underscores, capitals, `claude`, or `anthropic`.
- Every family skill name starts with `<prefix>-`.
- Connected external dependencies are exempt from the prefix and Workflow Creator signature rules; they must be marked `external`, remain unchanged, and have source/install/hash records.
- Exactly one family skill is named `<prefix>-workflow`; it is the coordinator.
- `SKILL.md` is named exactly `SKILL.md`.
- Description says what the skill does and when, includes realistic trigger phrases, is specific enough to avoid unrelated triggers, is under 1024 characters, and has no angle brackets.
- The coordinator description claims the full workflow; each child description claims only its phase and points broad requests to `/<prefix>-workflow`.
- Every skill carries the Workflow Creator signature: frontmatter `metadata.generator: workflow-create` (plus `generator-version`, `workflow-prefix`, `role`) and the matching footer line.
- Details live in directly linked `references/` files, not an oversized `SKILL.md`.
- No README, changelog, or setup docs inside child skill folders; `linkages.md` and `README.md` live only in the coordinator folder.
- Scripts are used for deterministic fragile validation.
- Skills are concise, single-capability, composable, progressively disclosed, and harness-agnostic.
- Child skills include standalone instructions, can run without a previous sibling call, and do not write `runStatus.md` when standalone.
- Every child has a clear "why separate" rationale.
- The workflow uses the smallest practical number of children; more than five includes a justification.
- Distributable linkage paths use placeholders, not creator-specific absolute paths.
- A concise `README.md` and a single `linkages.md` exist in the coordinator folder.
- The coordinator writes one `runStatus.md` per run in the active project, not inside the skill family.

## Flat Family Layout

```text
${SKILLS_ROOT}/
  <prefix>-workflow/
    SKILL.md
    linkages.md
    README.md
    references/
    scripts/
  <prefix>-<phase-action-a>/
    SKILL.md
    references/
  <prefix>-<phase-action-b>/
    SKILL.md
    references/
```

Skills install flat and are grouped by the shared prefix. Only the coordinator folder holds `linkages.md` and `README.md`. Runtime tracking is a `runStatus.md` created by the coordinator in the active project during each run.

Connected external dependencies remain separate sibling skill folders under their original names.
They are not part of the movable family package; reinstall them from the sources recorded in
`linkages.md`.

## Distribution Checklist

For public or team workflows:

- Keep human documentation at the repository root.
- Keep agent instructions inside skill folders.
- Include install-scope guidance: write to the detected host harness's native skills home (Claude Code → `.claude/skills`, else `.agents/skills`), at global (default) or project-local scope; create the chosen root for create/shell installs when absent and report the path.
- Include portability guidance: the family is plain Markdown; the coordinator `README.md` lists the member folders to copy into other harnesses.
- For connected workflows, list each external dependency's original source and install command; never present third-party skills as bundled family members.
- After install, offer the opt-in cross-harness symlink (Claude Code host → link into `.agents/skills`; other host → link into `.claude/skills`) so other agents can find the skills; only act on a yes. See "Cross-Harness Access" in SKILL.md.
- Package only after validation passes.
