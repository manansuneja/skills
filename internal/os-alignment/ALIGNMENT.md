# Workspace OS Family Alignment

This is an internal repository contract. `workspace-os-setup` and `pm-os-setup` remain separate,
standalone public skills with no runtime dependency on each other.

## Shared behaviors

Both skills must preserve these behaviors:

1. Default to an intentionally opened current folder; create a nested workspace only when the
   current location is broad or unsafe.
2. Personalize by reconciling **keep, add, remove, and ask** sets—not by only adding material.
3. Remove clearly irrelevant generated-empty areas, while asking before deleting or relocating
   user-authored content.
4. Rename the workspace root safely as the final filesystem operation; never create a replacement
   root and move files into it.
5. Run lightweight structural reconciliation whenever `AGENTS.md` is read: preserve manually added
   content, create missing indexes, update maps, and connect useful routing.
6. Keep a small default library and evolve content areas, skills, templates, references,
   specialists, and Chief routing together.
7. Keep the human surface obvious, label agent-facing machinery, maintain current `INDEX.md` files,
   and never overwrite raw input.
8. Keep tool wiring minimal and generate optional adapters only when the user asks.
9. Determine whether guidance is task-local or a durable operating preference from meaning and
   scope rather than magic phrases. A single request may require both immediate work and a
   skill/template/reference update; complete both in the same task when durability is clear.

## Intentional differences

| Concern | Workspace OS | PM OS |
|---|---|---|
| Chief | Workspace Chief | Chief PM |
| Primary content | `workspace-hub-docs/` or `project-docs/` | `product-docs/` |
| Reusable practices | `workspace-best-practices/{skills,templates,references}` | `product-practices/{skills,templates,references}` |
| Profile | `workspace-profile.md` | `product-vision.md` |
| Tailoring model | Category, entities, lifecycle, recurring work | Product stage, PM scope, users, evidence, delivery lifecycle |
| Minimal content core | Profile, meetings, outcomes, decisions | Vision, meetings, outcomes, decisions, PRDs |
| Minimal skill core | Summarize, brainstorm, outcomes, context | Summarize, brainstorm, outcomes, product context, PRDs |

Design, data, research, roadmaps, experiments, stakeholder communications, launch planning, and other
PM lanes are profile-driven additions rather than unconditional PM OS defaults.

## Maintenance workflow

1. Decide whether a change affects a shared behavior or one domain only.
2. For shared behavior, update both skill packages in the same change.
3. Preserve each skill's domain vocabulary and standalone assets; do not symlink or import across
   skill folders.
4. Update this contract when a new shared invariant or intentional difference appears.
5. Run `python3 internal/os-alignment/check-alignment.py`, scaffold smoke tests, Markdown-link checks,
   and the catalog validator.
