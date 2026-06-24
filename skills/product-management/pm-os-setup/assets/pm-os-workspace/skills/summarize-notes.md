# Skill: summarize-notes

Turn raw, messy notes into a summary a busy person can act on in 30 seconds - and that an agent can
reuse months later. Default to the structure below; adapt the headings to the meeting if needed.

## Default summary structure

```markdown
# <Meeting title> - <YYYY-MM-DD>

**Attendees:** ...
**Purpose:** one line - why this meeting happened.

## TL;DR
2-4 sentences. What a reader needs if they read nothing else.

## Decisions
- <decision> - and the reasoning, if it was given.

## Action items
- [ ] <action> - owner - due (if mentioned)

## Open questions
- <question that wasn't resolved>

## Notes & context
The discussion worth keeping - points, quotes, and the "small thing someone said" that might matter
later. Preserve a striking user/stakeholder quote verbatim; that's often the gold.
```

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

Write to `summary.md` next to the `raw_notes.md`. Never edit the raw notes. Then apply
[apply-pmos-struct](apply-pmos-struct.md) and update [the meetings index](../product-docs/meetings/INDEX.md).



