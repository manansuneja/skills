# Document Product Context

Use this when product knowledge should become durable memory instead of staying buried in chat.

Follow the operating-layer vs product-layer rule in [AGENTS.md](../AGENTS.md). Product docs describe
the user's actual product or project; workspace agents and skills are only the machinery maintaining
the workspace.

## When to update docs

Update documentation when the work changes or clarifies:

- Product vision, audience, problem, goal, positioning, strategy, or success measures.
- A decision and its reasoning.
- A PRD, meeting summary, or other artifact that future agents will need to find.
- A new recurring workflow, sub-agent, skill, or convention.

Do not file every tangent. Capture durable context, not noise.

## Where it goes

| Context | File or folder |
|---|---|
| Product purpose, audience, goal, positioning | `product-docs/product-vision.md` |
| Meeting output | `product-docs/meetings/<YYYY-MM-DD>-<short-title>/summary.md` |
| Committed decision | `product-docs/decisions/<YYYY-MM-DD>-<decision-slug>.md` |
| Feature/spec work | `product-docs/prds/<YYYY-MM-DD>-<feature-slug>.md` |
| New operating convention | `AGENTS.md`, a skill file, or an agent file |

## Rules

- Ask before making broad product-doc changes unless the PM explicitly asked for documentation.
- Keep workspace operations separate from product facts.
- Never overwrite raw notes or raw input.
- Update the nearest `INDEX.md` in the same change as the artifact.
- If the product vision changes, update `product-docs/product-vision.md` deliberately and mention it
  in your handoff.
- If another product doc should probably change but you are not sure, ask the PM and explain why.
