# Product Profiles

Use this reference when tailoring PM OS. Profiles are suggestion pools, not folder bundles. Select
the smallest useful combination for the product stage, PM scope, and immediate requirements.

## Contents

- [Selection Rules](#selection-rules)
- [Fit PM OS to the Product](#fit-pm-os-to-the-product)
- [Product Docs vs. Product Practices](#product-docs-vs-product-practices)
- [Reconcile During Personalization](#reconcile-during-personalization)
- [Stage and Scope Profiles](#stage-and-scope-profiles)

## Selection Rules

1. Start from explicit responsibilities and the next useful outcome. Product-stage knowledge supplies
   vocabulary and likely gaps; it does not authorize a union of every PM artifact.
2. Keep `product-vision.md`. Begin with meetings, outcomes, decisions, and PRDs, then retain or add
   other areas only when they support current or near-term work.
3. Prefer roughly three to seven active top-level product areas. Use product-surface, customer,
   lifecycle, or initiative subfolders when they match how the PM actually thinks.
4. Use a table, CSV, JSON, or sheet for repeated fields, owners, status, evidence, confidence, dates,
   and dependencies rather than turning every field into a folder.
5. Begin with summarize notes, brainstorm, synthesize outcomes, document product context, and write
   PRDs. Add or adapt a skill only for an explicit reusable preference or recurring workflow. Add a
   specialist only when a distinct route stays useful.
6. Update product-docs and root indexes, `product-practices/skills/INDEX.md`,
   `agents/sub-agents/INDEX.md`, and `agents/pm-chief.md` whenever areas or routes change.

## Fit PM OS to the Product

Build a compact product operating model before choosing structure:

1. **Users and actors:** customers, buyers, admins, operators, partners, internal teams, or systems.
2. **Product surfaces:** apps, workflows, APIs, platforms, services, marketplaces, or operational
   processes.
3. **Stage and lifecycle:** discovery, validation, definition, build, launch, adoption, growth,
   optimization, migration, or sunset.
4. **Active bets and decisions:** hypotheses, initiatives, risks, dependencies, trade-offs, and
   unresolved questions.
5. **Evidence:** interviews, research, support signals, analytics, experiments, market context, and
   technical constraints.
6. **Recurring outputs:** briefs, PRDs, experiments, design reviews, roadmaps, updates, launch plans,
   or retrospectives.
7. **Tracking:** owners, status, dates, confidence, metrics, dependencies, decisions, and next steps.

Translate that model into the smallest useful information architecture. Prefer product language over
generic labels. Whenever a product area or lifecycle changes, review its skills, templates,
specialists, and Chief PM routes in the same pass.

## Product Docs vs. Product Practices

- **`product-docs/`:** the work itself—vision, evidence, decisions, requirements, current plans, and
  product artifacts.
- **`product-practices/skills/`:** reusable PM judgment and workflows.
- **`product-practices/templates/`:** exact repeatable output structures.
- **`product-practices/references/`:** standing examples, style samples, principles, source material,
  or writing guidance reused across future work.

Ask whether something is the current product work or a reusable way of doing future product work.
Place it accordingly.

## Reconcile During Personalization

Build keep/add/remove/ask sets from the intake and actual filesystem:

- **Keep:** supports active work, contains user-authored material, or is a necessary cross-cutting
  product area.
- **Add:** supports current or near-term PM work and has a distinct purpose.
- **Remove automatically:** clearly irrelevant generated folders containing only an unchanged starter
  `INDEX.md`.
- **Ask once:** relevance is uncertain or the area contains user-authored content, raw material,
  custom links, or nested artifacts.

When removing an area, also remove or revise generated skills, templates, specialists, routes, and
index rows that only served it. Treat manually added folders as evidence of intended scope: preserve
and integrate them rather than treating them as clutter.

## Stage and Scope Profiles

### Discovery and 0-to-1

Candidate areas: `research/`, `opportunities/`, `experiments/`, `prototypes/`, and `risks/`.
Emphasize customer evidence, problem framing, hypotheses, concept testing, and learning plans. Add
research or experiment skills only when those workflows will repeat.

### Delivery and Feature Development

Candidate areas: `prds/`, `design/`, `technical-notes/`, `delivery/`, and `releases/`.
Emphasize requirements, scope, UX/technical trade-offs, dependencies, acceptance, and release
readiness. Keep design or delivery specialists only when the PM repeatedly uses those routes.

### Growth and Optimization

Candidate areas: `data-insights/`, `experiments/`, `funnels/`, `segments/`, and `growth-bets/`.
Emphasize instrumentation, hypotheses, experiment design, evidence quality, and learning. Do not add
growth lanes merely because the product has metrics.

### Platform, API, or Infrastructure

Candidate areas: `consumers/`, `capabilities/`, `technical-notes/`, `migrations/`, `reliability/`, and
`dependencies/`. Emphasize contracts, internal customers, adoption, sequencing, constraints, and
cross-team decisions.

### Enterprise or Multi-Stakeholder

Candidate areas: `customers/`, `requirements/`, `stakeholders/`, `compliance/`, `rollouts/`, and
`stakeholder-comms/`. Emphasize buyer/user differences, commitments, governance, approvals, change
management, and communication cadence.

### Internal Tools and Operations

Candidate areas: `workflows/`, `operators/`, `processes/`, `adoption/`, `support/`, and
`data-insights/`. Emphasize workflow fit, operational constraints, enablement, service levels, and
measurable time or quality improvements.

### Portfolio, Roadmap, or Product Leadership

Candidate areas: `strategy/`, `roadmaps/`, `initiatives/`, `dependencies/`, `operating-reviews/`, and
`stakeholder-comms/`. Emphasize choices, resource allocation, confidence, sequencing, narrative, and
decision cadence.

### General PM Workspace

When context is thin, preserve the minimal scaffold rather than adding every PM lane. Let repeated
requests earn research, design, data, roadmap, launch, or communication areas over time.
