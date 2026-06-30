# Skill: document-context

> **For you and your agents:** This skill controls what becomes durable memory and how it stays
> connected. Tell the Workspace Chief what should be captured differently.

Use this when important knowledge should become durable memory instead of remaining in chat.

Follow the machinery/content boundary in [AGENTS.md](../../AGENTS.md). Capture durable context, not
every tangent.

## Where content goes

| Context | Location |
|---|---|
| Purpose, category, domain model, goals, constraints | `{{DOCS_ROOT}}/workspace-profile.md` |
| Meeting or source-note summary | `{{DOCS_ROOT}}/meetings/<MMM-DD-YYYY>-<title>/summary.md` |
| Recommendation or synthesis | `{{DOCS_ROOT}}/outcomes/<MMM-DD-YYYY>-<topic>.md` |
| Committed choice | `{{DOCS_ROOT}}/decisions/<MMM-DD-YYYY>-<decision>.md` |
| Category-specific content | The best-fitting customized area and its index |
| Reusable workflow or format | `workspace-best-practices/skills/` or `templates/` |
| Example, voice, or source reference | `workspace-best-practices/references/` |

## Rules

- Update durable context without another permission step when the owner asked to process or document
  material and the source is clear.
- Ask before overwriting an established direction or making a judgment the source does not support.
- Preserve raw input and write synthesized artifacts separately.
- Update the nearest index in the same change.
- If a new workflow or output structure recurs, evolve the skill/template/sub-agent system rather
  than relying on chat memory.
