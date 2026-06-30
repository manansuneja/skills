# Document Product Context

Use this when product knowledge should become durable memory instead of staying buried in chat.

Follow the operating-layer vs product-layer rule in [AGENTS.md](../AGENTS.md). Product docs describe
the user's actual product or project; workspace agents and skills are only the machinery maintaining
the workspace.

## When to update docs

Update documentation when the work changes or clarifies:

- Product vision, audience, problem, goal, positioning, strategy, or success measures.
- A decision and its reasoning.
- An insight, prioritization, recommendation, MVP cut, or synthesis that future agents will need.
- Design considerations, data insights, roadmap plans, or stakeholder communications that should be
  findable later.
- A PRD, meeting summary, or other artifact that future agents will need to find.
- A new recurring workflow, sub-agent, skill, or convention.

Do not file every tangent. Capture durable context, not noise.

## Templates and references

Before creating a durable artifact, check [templates/](templates/INDEX.md) for the matching template
and [references/](references/INDEX.md) for PM-provided examples. In particular,
[templates/decision.md](templates/decision.md) is the default structure for decision records.

## Where it goes

| Context | File or folder |
|---|---|
| Product purpose, audience, goal, positioning | `product-docs/product-vision.md` |
| Meeting output | `product-docs/meetings/<MMM-DD-YYYY>-<short-title>/summary.md` |
| Product insight, recommendation, prioritization, MVP cut | `product-docs/outcomes/<MMM-DD-YYYY>-<topic>.md` |
| Committed decision | `product-docs/decisions/<MMM-DD-YYYY>-<decision-slug>.md` |
| Feature/spec work | `product-docs/prds/<area-or-mvp-slug>/<feature-slug>/prd.md` or `product-docs/prds/<feature-slug>/prd.md` |
| Design consideration or UX note | `product-docs/design/<MMM-DD-YYYY>-<topic>.md` |
| Metric read, experiment result, or quantitative insight | `product-docs/data-insights/<MMM-DD-YYYY>-<topic>.md` |
| Roadmap, release plan, or sequencing note | `product-docs/roadmaps/<MMM-DD-YYYY>-<topic>.md` |
| Stakeholder update, brief, launch note, or client summary | `product-docs/stakeholder-comms/<MMM-DD-YYYY>-<topic>.md` |
| New operating convention | `AGENTS.md`, a skill file, or an agent file |

## Rules

- Update product docs without a separate permission step when the PM asked to process, summarize,
  import, or document source material and the source clearly changes durable context.
- Ask before making broad product-doc changes only when the update conflicts with established context
  or requires product judgment the source does not answer.
- Keep workspace operations separate from product facts.
- Never overwrite raw notes or raw input.
- Update the nearest `INDEX.md` in the same change as the artifact.
- If the product vision changes, update `product-docs/product-vision.md` deliberately and mention it
  in your handoff.
- If another product doc should probably change but you are not sure what to capture, ask the PM and
  explain why.
