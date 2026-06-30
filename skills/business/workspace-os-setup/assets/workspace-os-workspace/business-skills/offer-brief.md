# Skill: offer-brief

Turn a discussion, notes, or an offer or project idea into an offer brief that's clear enough to build from.

## Templates and references

Before using the default structures, check:

- [business-practices/templates/project-brief.md](../business-practices/templates/project-brief.md) for area, package, initiative, or project-set
  overviews.
- [business-practices/templates/offer-brief.md](../business-practices/templates/offer-brief.md) for offer or deliverable briefs.
- [business-practices/templates/client-story.md](../business-practices/templates/client-story.md) for stories and acceptance criteria.
- [business-practices/references/](../business-practices/references/INDEX.md) for Owner-provided offer brief, offer, project, story, or business spec
  examples.

If the owner adds a better template or reference example, follow that and keep this skill's filing and
business-boundary guidance.

## Business boundary

Follow the operating-layer vs business-layer rule in [AGENTS.md](../AGENTS.md). The offer brief is for the
user's actual business or project, not for this Workspace OS workspace. If the business includes AI agents,
robots, copilots, or automation, describe those as business-specific actors from the business context.

## How to do it well

- **Pull from the workspace, don't invent.** Problem, user, and goal should trace back to meetings,
  research, or the business profile. Cite where they came from.
- **Keep the business boundary.** Business requirements are about the user's business; workspace agents
  are only the machinery helping write and maintain the artifact.
- **Make scope a decision, not an accident.** Non-goals are as important as goals.
- **Surface open questions loudly.** An offer brief with clear unknowns is more useful than false confidence.
- **Right altitude.** Define *what* and *why*; leave *how* to brand and delivery and eng unless the owner specifies.

## Filing

Prefer a hierarchy:

```text
{{DOCS_ROOT}}/offers/<area-or-package-slug>/
  INDEX.md
  overview.md
  <offer-or-deliverable-slug>/
    INDEX.md
    brief.md
    client-story.md
```

Use `{{DOCS_ROOT}}/offers/<offer-or-deliverable-slug>/brief.md` only for a genuinely standalone offer where no
parent area, package, or initiative is useful. Do not date-prefix offer brief filenames or folders; put dates in
the offer brief body and index. Apply [apply-workspace-struct](../_workspace_setup_docs/skills/apply-workspace-struct.md) and update
[the offer briefs index](../{{DOCS_ROOT}}/offers/INDEX.md) plus any nested `INDEX.md` files.
