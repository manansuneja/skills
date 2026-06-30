# Skill: synthesize-outcomes

Turn business context into a durable recommendation artifact. Use this for insight synthesis, top
priorities, scope, trade-off analysis, opportunity ranking, plan cuts, and "what should we do
next?" questions.

## Templates and references

Before using the default structure, check:

- [business-practices/templates/outcome.md](../business-practices/templates/outcome.md) for the current outcome template.
- [business-practices/references/](../business-practices/references/INDEX.md) for Owner-provided examples of prioritization notes,
  recommendation docs, or strategic readouts.

If the owner adds a better outcome template or reference example, follow that and keep this skill's
judgment rules.

## How to do it well

- **Write the artifact, not a chat essay.** The durable answer belongs in
  `{{DOCS_ROOT}}/outcomes/`; chat is only the handoff.
- **Ground every recommendation.** Tie reasoning to business profile, meeting summaries, decisions, or
  explicit user input.
- **Separate evidence from judgment.** Say what the sources show, then say what you recommend.
- **Prioritize by outcome, not option volume.** For lean-scope work, ask what must be true for users to get
  value, then rank options against that.
- **Create follow-on artifacts only when warranted.** A committed choice can become a decision file.
  Buildable offer or project scope can become an offer brief. Exploratory recommendations stay in outcomes.

## Filing

Write to `{{DOCS_ROOT}}/outcomes/<MMM-DD-YYYY>-<topic>.md`, update
[the outcomes index](../{{DOCS_ROOT}}/outcomes/INDEX.md), and apply
[apply-workspace-struct](../_workspace_setup_docs/skills/apply-workspace-struct.md). In chat, report only the file path, the top
recommendation, and any follow-up artifact path.
