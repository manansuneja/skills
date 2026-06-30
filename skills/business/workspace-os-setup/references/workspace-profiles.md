# Workspace Profiles

Use this reference when the user wants a tailored Workspace OS or gives primary uses during setup.
Profiles are suggestion pools, not folder bundles. Select the smallest useful combination.

## Contents

- [Selection Rules](#selection-rules)
- [Fit the Workspace to the Domain](#fit-the-workspace-to-the-domain)
- [Reconcile During Personalization](#reconcile-during-personalization)
- [Context Cues](#context-cues)
- [Primary-Use Profiles](#primary-use-profiles)
  - [Client Management](#client-management)
  - [Brainstorming And Offers](#brainstorming-and-offers)
  - [Knowledge And Study](#knowledge-and-study)
  - [Content Marketing And Writing](#content-marketing-and-writing)
  - [Operations](#operations)
  - [Project Delivery](#project-delivery)
  - [General Workspace Hub](#general-workspace-hub)

## Selection Rules

1. Choose `workspace-hub-docs/` for an ongoing workspace or `project-docs/` for one bounded project.
2. Start from the user's category and explicit requirements. Requirements determine immediate scope;
   category knowledge supplies the right vocabulary, expected entities, and high-confidence gaps.
3. Prefer roughly three to seven active top-level content areas, with useful category-specific
   subfolders beneath them. Do not flatten a real workflow into generic buckets or create an area
   only because it might become useful someday.
4. Keep `workspace-profile.md`; keep or add other areas only when they support current or near-term
   work. An `INDEX.md` does not justify a folder by itself.
5. Start with the common skills: summarize notes, brainstorm, synthesize outcomes, and document
   context. Add or adapt a category-specific skill only for an explicit reusable preference or a
   workflow likely to repeat. Add a specialist only when its route remains distinct and useful.
6. Update the root and docs-root indexes, `workspace-best-practices/skills/INDEX.md`,
   `agents/sub-agents/INDEX.md`, and `agents/workspace-chief.md` when their contents or routes change.

## Fit the Workspace to the Domain

Before choosing folders, build a compact domain model from the intake and category knowledge:

1. **Entities:** What distinct things exist—clients, projects, rooms, campaigns, sources, lessons,
   products, cases, vendors, or deliverables?
2. **Lifecycle:** What stages do those things move through—intake, concept, approval, sourcing,
   production, installation, publication, review, or archive?
3. **Recurring artifacts:** What gets created repeatedly—briefs, proposals, moodboards, research
   notes, drafts, approvals, reports, or updates?
4. **Tracking:** What status, dates, owners, dependencies, costs, evidence, or next actions matter?
5. **Vocabulary:** What would the user naturally call these things?

Translate this model into the smallest useful information architecture:

- Use top-level folders for durable domains and subfolders for meaningful entity/lifecycle detail.
- Use a table, CSV, JSON, or sheet for repeated fields and status tracking rather than turning every
  field into a folder.
- Prefer category language over generic labels when it improves recognition.
- Create a skill or template for a recurring artifact; create a specialist only for a distinct route.
- Whenever a content folder or lifecycle changes, review its skills, templates, and specialists in
  the same pass. The information architecture and operating behavior should tell the same story.
- If a category pattern is highly likely and low-cost, include it even when the intake did not name it.
  If it would materially expand the workspace or is uncertain, ask once.

For an interior-design studio, `projects/<project>/concept/`, `sourcing/`, `approvals/`, and
`installation/` may fit better than a flat generic project folder. For a writing workspace,
`content/<piece>/research/`, `drafts/`, and `published/` may fit better. Use only the stages the owner
actually expects.

## Reconcile During Personalization

Personalization is subtractive as well as additive. Build a keep/add/remove/ask plan from the intake
and the actual filesystem before editing.

- **Keep:** directly supports an explicit use, contains user-authored material, or is a necessary
  cross-cutting area.
- **Add:** directly supports work the user expects now or soon and has a clear purpose distinct from
  existing folders.
- **Remove automatically:** generated folders that are clearly irrelevant and contain no artifact
  beyond their generated `INDEX.md`. Report them in the handoff.
- **Ask once:** any folder whose relevance is uncertain or that contains user-authored files, raw
  material, links, or nested artifacts. Never delete that content from inference alone.

When removing a generated area, also remove or revise orphaned generated skills, specialists, routes,
templates, and index entries. Search for stale links afterward.

Treat user-created folders and subfolders as new evidence about the desired domain model. Preserve
their contents and integrate them into indexes and routing; do not classify them as generated clutter.

## Context Cues

Use these only as candidate vocabulary:

- **Creative or interior-design studio:** clients, projects, proposals, inspiration, installation,
  vendors, sourcing, brand/delivery, and client communications.
- **Consulting, coaching, or professional services:** offers, clients, meetings, outcomes, knowledge,
  proposals, client communications, and plans.
- **Agency or freelance practice:** pipeline, clients, projects, delivery, briefs, approvals, assets,
  operations, and client communications.
- **Ecommerce or product work:** catalog/offers, content, marketing, metrics, operations, suppliers,
  plans, and decisions.
- **Local service work:** clients, jobs, operations, procedures, finance, marketing, reviews, and
  scheduling.
- **Knowledge, education, or personal research:** knowledge base, research, notes, sources, content,
  and study plans.

For example, an interior-design studio focused on knowledge capture, brainstorming, and writing may
need `knowledge-base/`, `research/`, `ideas/`, `content/`, and `outcomes/`—not `vendors/` merely because
vendors are common in the industry.

## Primary-Use Profiles

### Client Management

Candidate folders:

- `clients/`
- `projects/`
- `proposals/`
- `intake/`
- `client-comms/`

Candidate skills and specialists: client management, client intake, project delivery, and client
communications. Keep only the routes the user expects to exercise.

### Brainstorming And Offers

Candidate folders:

- `ideas/`
- `research/`
- `experiments/`
- `offers/`
- `outcomes/`

Emphasize the common `brainstorm.md`. Create offer shaping, offer brief, or market-research skills and
templates only when those workflows are active.

### Knowledge And Study

Candidate folders:

- `knowledge-base/`
- `research/`
- `notes/`
- `sources/`
- `study-plans/`

Emphasize knowledge capture, research synthesis, study planning, note summarization, and a knowledge
steward only when useful.

### Content Marketing And Writing

Candidate folders:

- `content/`
- `marketing/`
- `editorial-calendar/`
- `campaigns/`
- `voice-and-style/`
- `research/`

Emphasize content ideation, writing/editing, repurposing, campaign planning, and voice/style
references. Do not add sales, vendors, or client-delivery areas unless the user also named them.

### Operations

Candidate folders:

- `operations/`
- `sops/`
- `finance/`
- `vendors/`
- `metrics/`

Add vendors or finance only when they are part of the stated operational scope. Emphasize operational
reviews, procedure building, metrics, and planning as needed.

### Project Delivery

Candidate folders:

- `project-briefs/`
- `delivery/`
- `assets/`
- `approvals/`
- `risks/`
- `client-comms/`

Emphasize project delivery, note summarization, client communications, and planning. A bounded
project usually needs fewer general hub areas.

### General Workspace Hub

When the user is unsure, keep the scaffold modest rather than broad. Preserve `workspace-profile.md`
and a few cross-cutting areas such as `notes/`, `outcomes/`, `decisions/`, or `plans/` only when their
purpose is understandable from the intake. Let repeated usage earn additional folders.
