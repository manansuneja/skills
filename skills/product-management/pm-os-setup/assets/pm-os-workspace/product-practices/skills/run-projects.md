# Skill: run-projects

> **For you and your agents:** Reusable project workflow managed through the Chief PM.

Keep each initiative in one place with an honest stage, health, and next step, and keep the portfolio
readable at a glance.

## Templates and references

Before using the default structures, check:

- [product-practices/templates/project-brief.md](../templates/project-brief.md) for `brief.md`.
- [product-practices/templates/project-status.md](../templates/project-status.md) for `status.md`.
- [product-practices/references/](../references/INDEX.md) for PM-provided status updates, roadmap
  formats, or portfolio examples.

If the PM adds a better template or example, follow that and keep this skill's filing guidance.

## Start a project

1. Create `product-docs/projects/<project-slug>/` with a stable `lower-kebab-case` slug.
2. Write `brief.md` from the source material — vision, meetings, outcomes — and ask only for what the
   sources cannot answer: the outcome, owner, and stage.
3. Write `status.md` with the stage, health, a short Now/Next, and the first log entry.
4. Add a project `INDEX.md` that maps the folder and states the current status in one line.
5. Add a row to [the portfolio](../../product-docs/projects/INDEX.md) and, when active work changed,
   the root [INDEX.md](../../INDEX.md).
6. Move or link existing material that belongs to the project. Preserve raw input; never delete
   user-authored files to tidy up.

## Stages

| Stage | Question it answers | Typical artifacts | Ready to move on when |
|---|---|---|---|
| discover | Is this worth doing? | meetings, research, outcomes | The problem and user are evidenced |
| define | What exactly are we building? | brief, PRD, stories, decisions | Scope, non-goals, and acceptance criteria are agreed |
| build | Is it being built right? | build brief, status log | Acceptance criteria are verified |
| launch | Is it reaching users? | release notes, launch checklist | It is live and the owner is named |
| learn | Did it work? | outcome, decision | Results are written down and the next step is chosen |

Stage is a fact recorded in `status.md`, not a gate. Projects may skip stages or loop back. Change
the stage when reality changes, and log why.

## Keep status honest

- **Health is a judgment.** `at risk` means a named risk could miss the outcome; `blocked` means work
  cannot proceed without something named. Write what, and since when.
- **One line per log entry,** newest first: stage changes, decisions, what shipped, what was learned.
- **Update when something changes,** not on a schedule. Refresh `Updated` and the portfolio row in the
  same change.
- **Track repeated fields in tables:** risks, milestones, and dependencies — not as folders.

## Roll-ups

When asked for a status update or weekly readout, read each active project's `status.md`, then
summarize by exception: what moved, what is at risk or blocked, and what needs a decision. Save
substantial roll-ups in `product-docs/outcomes/`; chat carries only the handoff.

## Wrap up

When a project finishes or pauses, set its stage to `done` or `parked`, log the outcome or reason, and
update the portfolio. Keep the folder; do not delete history.

## Filing by scope

An artifact that belongs to one project is filed inside it: `decisions/`, `meetings/`, `outcomes/`,
and `raw/` subfolders appear when first needed. Product-wide artifacts stay in the global folders.
Every decision is also listed in the global decisions log. Apply
[apply-pmos-struct](../../_workspace_setup_docs/skills/apply-pmos-struct.md) afterward.

## Learn durable project practice

During project work, determine from meaning and scope whether new guidance applies only to the
current project or establishes a durable convention — a stage vocabulary, status format, cadence, or
health definition. Apply it now and update this skill or its template in the same task. Ask only when
persistence is genuinely ambiguous and would materially change future projects.
