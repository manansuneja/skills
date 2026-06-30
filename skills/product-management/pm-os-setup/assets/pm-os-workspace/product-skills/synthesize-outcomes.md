# Skill: synthesize-outcomes

Turn product context into a durable recommendation artifact. Use this for insight synthesis, top
priorities, MVP scope, trade-off analysis, opportunity ranking, roadmap cuts, and "what should we do
next?" questions.

## Templates and references

Before using the default structure, check:

- [product-practices/templates/outcome.md](../product-practices/templates/outcome.md) for the current outcome template.
- [product-practices/references/](../product-practices/references/INDEX.md) for PM-provided examples of prioritization notes,
  recommendation docs, or strategic readouts.

If the PM adds a better outcome template or reference example, follow that and keep this skill's
judgment rules.

## How to do it well

- **Write the artifact, not a chat essay.** The durable answer belongs in
  `product-docs/outcomes/`; chat is only the handoff.
- **Ground every recommendation.** Tie reasoning to product vision, meeting summaries, decisions, or
  explicit user input.
- **Separate evidence from judgment.** Say what the sources show, then say what you recommend.
- **Prioritize by outcome, not feature volume.** For MVP work, ask what must be true for users to get
  value, then rank features against that.
- **Create follow-on artifacts only when warranted.** A committed choice can become a decision file.
  Buildable feature scope can become a PRD. Exploratory recommendations stay in outcomes.

## Filing

Write to `product-docs/outcomes/<MMM-DD-YYYY>-<topic>.md`, update
[the outcomes index](../product-docs/outcomes/INDEX.md), and apply
[apply-pmos-struct](../_workspace_setup_docs/skills/apply-pmos-struct.md). In chat, report only the file path, the top
recommendation, and any follow-up artifact path.
