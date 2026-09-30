# projects/ — Index

> **Your primary product workspace:** One folder per initiative, so everything a piece of work needs
> lives together. Tell the Chief PM to start, update, pause, or wrap a project; it maintains this page.

Start a project when work has its own outcome and an end: a feature, an MVP, an experiment, a launch.
Product-wide knowledge — vision, research, cross-project decisions — stays outside projects.

## Portfolio

| Project | Stage | Health | Owner | Next milestone | Updated |
|---|---|---|---|---|---|
| _none yet_ | Ask the Chief: "start a project for X" | - | - | - | - |

**Stage:** discover → define → build → launch → learn, then `done` or `parked`.
**Health:** on track, at risk, or blocked.

## Shape of a project

```text
product-docs/projects/<project-slug>/
  INDEX.md          short map of the folder plus the current one-line status
  brief.md          why, outcome, scope, feature map
  status.md         stage, health, now / next / blocked, risks, running log
  prd.md            requirements, for a single-feature project
  features/<feature-slug>/prd.md + stories.md     for a multi-feature project
  build-brief.md    handoff a coding agent or engineering team can build from
  decisions/ meetings/ outcomes/     created when first needed
  raw/              untouched source material
```

Do not date-prefix project, PRD, or brief files; put dates in the content and in the tables here.
Time-ordered artifacts inside a project (meetings, decisions, outcomes) keep their `MMM-DD-YYYY`
prefix.

## Filing by scope

- Belongs to one project → file it inside that project and list it in the project's `INDEX.md`.
- Spans projects or describes the product as a whole → file it in the global
  [meetings](../meetings/INDEX.md), [outcomes](../outcomes/INDEX.md), or
  [decisions](../decisions/INDEX.md) folder.
- Every decision also gets a row in the global [decisions log](../decisions/INDEX.md), whatever its
  scope, so cross-project choices stay findable in one place.

The [program-manager](../../agents/sub-agents/program-manager.md) keeps this portfolio current using
[run-projects](../../product-practices/skills/run-projects.md).
