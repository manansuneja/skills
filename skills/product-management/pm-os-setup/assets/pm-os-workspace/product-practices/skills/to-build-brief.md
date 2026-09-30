# Skill: to-build-brief

> **For you and your agents:** Reusable build-handoff workflow managed through the Chief PM.

Turn a PRD into a brief that a coding agent or an engineering team can build from without guessing.
The PRD says what and why; the build brief adds what to load, what not to touch, and how to prove it
works.

## Templates and references

Before using the default structure, check:

- [product-practices/templates/build-brief.md](../templates/build-brief.md) for the brief.
- [product-practices/templates/feature-prd.md](../templates/feature-prd.md) and
  [stories.md](../templates/stories.md) for the source requirements.
- [product-practices/references/](../references/INDEX.md) for PM-provided engineering briefs, ticket
  examples, or coding-agent prompt conventions.

If the PM adds a better template or reference example, follow that and keep this skill's guidance.

## How to do it well

- **Derive, don't invent.** Scope, non-goals, and acceptance criteria trace back to the PRD, stories,
  and decisions. If they are missing, send the gap back to the
  [prd-writer](../../agents/sub-agents/prd-writer.md) instead of filling it in.
- **Make acceptance criteria testable.** Each one is something a person or test can check as pass or
  fail. "Feels fast" is not a criterion; "search returns in under 300 ms on the sample data" is.
- **List the context to load.** Name the exact files, links, and decisions the builder should read
  first so it does not guess at product intent.
- **Name the no-go areas.** Non-goals and code or systems to leave alone prevent the most expensive
  surprises.
- **Say how to verify.** Give tests to run, steps to click through, and what good output looks like.
- **Surface open questions.** Builders should ask before guessing on these.
- **Right altitude for the audience.** For a coding agent, be explicit and self-contained. For an
  engineering team, leave design choices to them unless a constraint is firm.
- **No secrets.** Do not paste credentials, tokens, or private customer data into a brief.

## Filing

Write `build-brief.md` beside the PRD: `product-docs/projects/<project-slug>/build-brief.md`, or in
the feature folder for a multi-feature project. Set its status, link it from the project `INDEX.md`,
and log the handoff in `status.md`. Apply
[apply-pmos-struct](../../_workspace_setup_docs/skills/apply-pmos-struct.md).

Application code does not live in this workspace. Link the repository from the project's `brief.md`.
Ask before external writes such as creating issues or opening pull requests.

## Learn durable build practice

Determine from meaning and scope whether new guidance applies only to this brief or establishes a
durable convention, such as a prompt format, definition of done, or required verification step. Apply
it now and update this skill or its template in the same task. Ask only when persistence is genuinely
ambiguous and would materially change future briefs.
