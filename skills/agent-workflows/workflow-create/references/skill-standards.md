# Skill Authoring Standards

The skill *format* (folder layout, frontmatter, progressive disclosure) is a stable open standard, so the basics are inlined below for offline self-sufficiency. The deeper, evolving *craft* — and the scaffolding/validation scripts — live in Anthropic's `skill-creator`; point to it and fetch it when present/needed, so updates are captured without tracking a version here.

## Get the full standards (pointer, fetch if missing)

- **The open standard:** the Agent Skills specification at https://agentskills.io/specification (repo: https://github.com/agentskills/agentskills) defines the canonical skill format — frontmatter fields, naming rules, and directory layout. The inline basics below track it.
- **Reference validator:** `skills-ref` (the standard's Python reference CLI, in `agentskills/agentskills/skills-ref`) checks a skill against the spec — `skills-ref validate ./<skill-dir>` after installing it with `pip install -e .`/`uv sync` from that subdirectory. Its README flags it as a demonstration reference, not production, so use it as a sanity check alongside (not instead of) `scripts/validate_workflow_family.py`, which stays the enforced gate.
- **Craft (deeper, evolving):** Anthropic's `skill-creator`.
  - **Canonical source:** https://github.com/anthropics/skills/tree/main/skills/skill-creator
  - **Install (preferred):** `npx skills add anthropics/skills --skill skill-creator`
  - **Or fetch the files** from the repo above into `${SKILLS_ROOT}/skill-creator` when `npx` is unavailable.

Resolution order at authoring time:

1. If the host agent already exposes a `skill-creator` skill (or a folder exists under `${SKILLS_ROOT}/skill-creator`), use it directly — this is also how upstream updates get captured, since the installed copy is whatever the user/agent last pulled.
2. If not present, retrieve it from the canonical source above, then follow it.
3. If retrieval is impossible (offline, source unreachable), proceed using the inline basics below and tell the user `skill-creator` could not be fetched.

The inline basics below are the floor and always apply; `skill-creator`, when available, adds depth (degrees-of-freedom tuning, richer examples, packaging) on top.

## The basics (inline — stable format)

### Anatomy of a skill

A skill is a folder whose name matches its `name`, containing a required `SKILL.md` and optional resource directories:

```
skill-name/
├── SKILL.md          (required: frontmatter + instructions)
├── scripts/          (optional: executable code for deterministic steps)
├── references/       (optional: docs loaded only when needed)
└── assets/           (optional: files used in the skill's output)
```

- **`scripts/`** — deterministic code (validation, scaffolding, parsing). Prefer a script over prose when a step must be exact.
- **`references/`** — on-demand context: patterns, long examples, domain knowledge. Loaded only when `SKILL.md` links to them.
- **`assets/`** — templates, icons, fonts, boilerplate used *in the output*, not read into context.

Create only the directories a skill actually needs; delete unused scaffolding.

### Frontmatter

`SKILL.md` opens at line 1 with a YAML block holding exactly `name` and `description`:

```yaml
---
name: my-skill-name
description: >-
  <what it does> + <when to use it, with literal trigger phrases>
---
```

- **`name`** — must satisfy the Agent Skills spec: 1–64 characters; lowercase letters, digits, and hyphens only; no leading/trailing hyphen; no consecutive hyphens (`--`); matches the folder name exactly; never contains `claude` or `anthropic`.
- **`description`** — the single most important field; it (with the name) is the only thing the agent reads when deciding whether to invoke the skill. Write it in the third person, state **what** the skill does *and* **when** to use it, and embed the literal trigger phrases a user would say. Put *all* "when to use" info here, not in the body. Be slightly **pushy** to fight underuse: e.g. "use this whenever the user mentions <keywords>, even if they don't ask for it by name." Add negative triggers ("not for X") when routing collisions are likely.

### Progressive disclosure (keep it lean)

Content loads in three levels — keep each at its budget:

1. **Metadata** (~100 words: `name` + `description`) — always in context; costs tokens every turn.
2. **`SKILL.md` body** (aim < 500 lines) — loaded only when the skill triggers; holds the core procedure and decision logic.
3. **Bundled resources** (`scripts/`, `references/`, `assets/`) — unlimited, loaded on demand.

Push deep detail, long examples, and rubrics into `references/*.md` and link them by relative path. Reference files over ~300 lines should open with a short table of contents.

### Writing the body

- Imperative, concise, second-person instructions to the agent.
- Lead with decision/branching logic; defer detail to `references/`.
- Show input → output examples for any non-obvious transformation.
- State done-criteria so the agent knows when a step is complete.
- Explain the **why** behind requirements; prefer reasoning over rigid ALWAYS/NEVER.
- Don't restate general knowledge; spend tokens only on what's specific to this skill.
- Match instruction specificity to the task: tight steps where one path is correct, looser principles where many approaches are valid.

### Lack of surprise

A skill must not contain malware or exploits, and its behavior must match what its `description` leads the user to expect — no hidden side effects.

## Non-negotiable frontmatter rules (must never break)

A malformed frontmatter block makes the harness **silently skip the entire skill**, so these are enforced even when offline:

1. **Valid YAML, every time.** Starts at byte 1, line 1 with literal `---`, closes with `---`, contains exactly `name` and `description`, and is saved as UTF-8 without BOM. A UTF-8 BOM (`EF BB BF`) before `---` makes some installers miss the frontmatter and report "No skills found."
2. **Quote/fold any value with a colon.** A plain `description: Runs in two modes: url and repo` makes YAML read `two modes` as a key → the skill won't load. Descriptions almost always contain `: `, quotes, or apostrophes, so default to a folded block scalar:

   ```yaml
   description: >-
     Audit a site and produce a report. Runs in two modes: URL and repo.
     Use when the user says "aeo audit" or "score my AEO".
   ```

   `>-` folds newlines to spaces and strips the trailing newline; indent the body two spaces; colons, `"`, `'`, and `—` are all literal inside.
3. **Never leave merge-conflict markers** (`<<<<<<<`, `=======`, `>>>>>>>`) anywhere in the file.
4. **`name`** conforms to the spec: 1–64 chars, lowercase letters/digits/hyphens only, no leading/trailing or consecutive hyphens, matches the folder, and contains no `claude`/`anthropic`.

## Before finishing

The validator must catch UTF-8 BOMs before frontmatter in addition to invalid YAML and conflict markers.

Run `scripts/validate_workflow_family.py` on the generated family. It hard-fails on invalid YAML frontmatter and conflict markers (full strict parse when PyYAML is available, a colon-space heuristic otherwise), so these errors are caught before the skills ever reach the harness. When `skills-ref` is installed, also run `skills-ref validate ./<skill-dir>` on each generated skill folder as a spec-conformance sanity check (the two validators are complementary: spec format vs. family contract). Don't block on it if it isn't installed — the family validator covers the harness-fatal cases.
