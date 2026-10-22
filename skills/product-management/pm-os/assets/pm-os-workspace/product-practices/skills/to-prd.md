# Skill: to-prd

> **For you and your agents:** Reusable PRD workflow managed through the Chief PM.

Turn a discussion, notes, or a feature idea into a PRD that's clear enough to build from.

Create Markdown by default. A request such as “create a PRD” means a `.md` artifact in PM OS—not a
Word document, PDF, or presentation. Use another format only when the PM explicitly requests it or
the delivery context clearly requires it. If that choice would materially affect usability and
intent is still unclear, ask one concise question.

## Templates and references

Before using the default structures, check:

- [product-practices/templates/project-brief.md](../templates/project-brief.md) for a project's
  brief, including its feature map.
- [product-practices/templates/feature-prd.md](../templates/feature-prd.md) for feature or sub-feature PRDs.
- [product-practices/templates/stories.md](../templates/stories.md) for stories and acceptance criteria.
- [product-practices/references/](../references/INDEX.md) for PM-provided PRD, feature, epic, story, or product spec
  examples.

If the PM adds a better template or reference example, follow that and keep this skill's filing and
product-boundary guidance.

## Learn durable PRD practice

During PRD work, determine from meaning and scope whether new guidance applies only to the current
artifact or establishes a durable PRD convention. Organizational structures, canonical methods,
recurring formats, and corrections to the normal approach are strong evidence of durability even
without an explicit request to save them. Apply the guidance to the current PRD and update this skill
or its related template/reference in the same task. Ask only when persistence is genuinely ambiguous
and would materially change future PRDs.

## Product boundary

Follow the operating-layer vs product-layer rule in [AGENTS.md](../../AGENTS.md). The PRD is for the
user's actual product or project, not for this PM OS workspace. If the product includes AI agents,
robots, copilots, or automation, describe those as product-specific actors from the product context.

## How to do it well

- **Pull from the workspace, don't invent.** Problem, user, and goal should trace back to meetings,
  research, or the vision. Cite where they came from.
- **Keep the product boundary.** Product requirements are about the user's product; workspace agents
  are only the machinery helping write and maintain the artifact.
- **Make scope a decision, not an accident.** Non-goals are as important as goals.
- **Surface open questions loudly.** A PRD with clear unknowns is more useful than false confidence.
- **Right altitude.** Define *what* and *why*; leave *how* to design and eng unless the PM specifies.

## Filing

Requirements live inside a project. Start one first with
[run-projects](run-projects.md) if none exists.

```text
product-docs/projects/<project-slug>/
  INDEX.md
  brief.md              feature map and scope for the whole project
  prd.md                single-feature project
  features/<feature-slug>/
    prd.md              multi-feature project
    stories.md
```

Do not date-prefix PRD filenames or folders; put dates in the PRD body and index. Apply
[apply-pmos-struct](../../_workspace_setup_docs/skills/apply-pmos-struct.md) and update the project's
`INDEX.md` plus [the portfolio](../../product-docs/projects/INDEX.md).

When scope is agreed, offer a build brief with [to-build-brief](to-build-brief.md).

When the PM explicitly requests a `.docx`, PDF, presentation, or another deliverable and a compatible
installed capability exists, generate it from the Markdown source and store both together. Never
install or connect a capability automatically.
