# Skill: summarize-notes

Turn raw, messy notes into a summary a busy person can act on in 30 seconds - and that an agent can
reuse months later.

## Templates and references

Before using the default structure, check:

- [product-practices/templates/meeting-summary.md](../product-practices/templates/meeting-summary.md) for the current meeting summary
  template.
- [product-practices/references/](../product-practices/references/INDEX.md) for PM-provided meeting minute examples, style samples, or
  notes formats.

If the PM adds a better meeting template or reference example, follow that and keep this skill's
workflow guidance.

## How to do it well

- **Lead with the answer.** TL;DR and decisions first; detail below.
- **Separate facts from interpretation.** Don't invent decisions that weren't made; put your read
  in "Notes & context," not in "Decisions."
- **Keep the human signal.** A pain point someone mentioned as an aside is often more valuable than
  the feature they asked for. Capture it.
- **Make actions real.** Owner + verb + (due). "Discuss pricing" is not an action; "Sasha drafts
  pricing options by Fri" is.
- **Flag, don't bury.** If something deserves its own artifact (a decision, a PRD), say so to the
  Chief instead of hiding it three bullets deep.

## Filing

If the notes are loose, first file them under
`product-docs/meetings/<MMM-DD-YYYY>-<short-title>/raw/raw-notes.md` and remove the loose inbox copy
after the archive exists. Then write `summary.md` in the meeting folder. Never edit raw notes. Treat
`summary.md` as the main context surface; open `raw/` only when you need to verify source details.
Then apply [apply-pmos-struct](../_workspace_setup_docs/skills/apply-pmos-struct.md) and update
[the meetings index](../product-docs/meetings/INDEX.md).
