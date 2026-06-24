# Skill: to-prd

Turn a discussion, notes, or a feature idea into a PRD that's clear enough to build from. This
template is a sensible default - **if the PM has defined their own PRD format, replace the template
below with theirs and keep the rest of this guidance.**

## Product boundary

Follow the operating-layer vs product-layer rule in [AGENTS.md](../AGENTS.md). The PRD is for the
user's actual product or project, not for this PM OS workspace. If the product includes AI agents,
robots, copilots, or automation, describe those as product-specific actors from the product context.

## Default PRD template

```markdown
# <Feature name> - PRD
**Status:** draft | in review | approved   **Author:** ...   **Date:** <YYYY-MM-DD>

## Problem
What's broken or missing, and for whom. Anchor it to a real user and, where possible, a real quote
or signal from the meetings/research.

## Goal & non-goals
- **Goal:** the outcome this should achieve (and how we'd know).
- **Non-goals:** what this explicitly does *not* try to do.

## Users & context
Who this is for and the situation they're in when they hit this problem.

## Proposed solution
The approach, in plain language. Enough for design and eng to picture it. Link prototypes if any.

## Requirements
- Must: ...
- Should: ...
- Could (later): ...

## Success metrics
How we'll know it worked.

## Open questions
- ... (be honest - unknowns belong here, not hidden as assumptions)
```

## How to do it well

- **Pull from the workspace, don't invent.** Problem, user, and goal should trace back to meetings,
  research, or the vision. Cite where they came from.
- **Keep the product boundary.** Product requirements are about the user's product; workspace agents
  are only the machinery helping write and maintain the artifact.
- **Make scope a decision, not an accident.** Non-goals are as important as goals.
- **Surface open questions loudly.** A PRD with clear unknowns is more useful than false confidence.
- **Right altitude.** Define *what* and *why*; leave *how* to design and eng unless the PM specifies.

## Filing

Write to `product-docs/prds/<YYYY-MM-DD>-<feature-slug>.md`, apply
[apply-pmos-struct](apply-pmos-struct.md), and add a line to
[the PRDs index](../product-docs/prds/INDEX.md).



