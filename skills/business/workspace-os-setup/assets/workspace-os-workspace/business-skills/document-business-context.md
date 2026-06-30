# Document Business Context

Use this when business knowledge should become durable memory instead of staying buried in chat.

Follow the operating-layer vs business-layer rule in [AGENTS.md](../AGENTS.md). Business docs describe
the user's actual business or project; workspace agents and skills are only the machinery maintaining
the workspace.

## When to update docs

Update documentation when the work changes or clarifies:

- Business profile, audience, problem, goal, positioning, strategy, or success measures.
- A decision and its reasoning.
- An insight, prioritization, recommendation, package cut, or synthesis that future agents will need.
- Brand and delivery considerations, metrics, plan plans, or client communications that should be
  findable later.
- An offer brief, meeting summary, or other artifact that future agents will need to find.
- A new recurring workflow, sub-agent, skill, or convention.

Do not file every tangent. Capture durable context, not noise.

## Templates and references

Before creating a durable artifact, check [business-practices/templates/](../business-practices/templates/INDEX.md) for the matching template
and [business-practices/references/](../business-practices/references/INDEX.md) for Owner-provided examples. In particular,
[business-practices/templates/decision.md](../business-practices/templates/decision.md) is the default structure for decision records.

## Where it goes

| Context | File or folder |
|---|---|
| Business purpose, audience, goal, positioning | `{{DOCS_ROOT}}/business-profile.md` |
| Meeting output | `{{DOCS_ROOT}}/meetings/<MMM-DD-YYYY>-<short-title>/summary.md` |
| Business insight, recommendation, prioritization, package cut | `{{DOCS_ROOT}}/outcomes/<MMM-DD-YYYY>-<topic>.md` |
| Committed decision | `{{DOCS_ROOT}}/decisions/<MMM-DD-YYYY>-<decision-slug>.md` |
| Offer or project spec work | `{{DOCS_ROOT}}/offers/<area-or-package-slug>/<offer-or-deliverable-slug>/brief.md` or `{{DOCS_ROOT}}/offers/<offer-or-deliverable-slug>/brief.md` |
| Brand and delivery consideration or UX note | `{{DOCS_ROOT}}/brand-and-delivery/<MMM-DD-YYYY>-<topic>.md` |
| Metric read, experiment result, or quantitative insight | `{{DOCS_ROOT}}/metrics/<MMM-DD-YYYY>-<topic>.md` |
| Plan, release plan, or sequencing note | `{{DOCS_ROOT}}/plans/<MMM-DD-YYYY>-<topic>.md` |
| Client update, brief, launch note, or client summary | `{{DOCS_ROOT}}/client-comms/<MMM-DD-YYYY>-<topic>.md` |
| New operating convention | `AGENTS.md`, a skill file, or an agent file |

## Rules

- Update business docs without a separate permission step when the owner asked to process, summarize,
  import, or document source material and the source clearly changes durable context.
- Ask before making broad business-doc changes only when the update conflicts with established context
  or requires business judgment the source does not answer.
- Keep workspace operations separate from business facts.
- Never overwrite raw notes or raw input.
- Update the nearest `INDEX.md` in the same change as the artifact.
- If the business profile changes, update `{{DOCS_ROOT}}/business-profile.md` deliberately and mention it
  in your handoff.
- If another business doc should probably change but you are not sure what to capture, ask the owner and
  explain why.
