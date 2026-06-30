# Skill: to-prd

Turn a discussion, notes, or a feature idea into a PRD that's clear enough to build from.

## Templates and references

Before using the default structures, check:

- [templates/prd-overview.md](templates/prd-overview.md) for area, MVP, initiative, or feature-set
  overviews.
- [templates/feature-prd.md](templates/feature-prd.md) for feature or sub-feature PRDs.
- [templates/stories.md](templates/stories.md) for stories and acceptance criteria.
- [references/](references/INDEX.md) for PM-provided PRD, feature, epic, story, or product spec
  examples.

If the PM adds a better template or reference example, follow that and keep this skill's filing and
product-boundary guidance.

## Product boundary

Follow the operating-layer vs product-layer rule in [AGENTS.md](../AGENTS.md). The PRD is for the
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

Prefer a hierarchy:

```text
product-docs/prds/<area-or-mvp-slug>/
  INDEX.md
  overview.md
  <feature-slug>/
    INDEX.md
    prd.md
    stories.md
```

Use `product-docs/prds/<feature-slug>/prd.md` only for a genuinely standalone feature where no
parent area, MVP, or initiative is useful. Do not date-prefix PRD filenames or folders; put dates in
the PRD body and index. Apply [apply-pmos-struct](apply-pmos-struct.md) and update
[the PRDs index](../product-docs/prds/INDEX.md) plus any nested `INDEX.md` files.
