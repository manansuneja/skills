# Workflow Creator

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

**Connect multiple skills to form a reusable workflow.**

One coordinator executes the skills in sequence and passes the work from one step to the next. You
can reuse the full workflow whenever you need it, while every individual skill remains usable on
its own. Workflow Creator can connect existing skills, write missing steps, or do both.

This is for PMs, designers, writers, operators, founders, and developers who can explain how they
work but do not want to rebuild the same prompt and handoffs every time.

## Install

You don't need to be a developer — you just need an agent that can run skills, like
[Claude Code](https://code.claude.com/docs/en/quickstart) or [Cursor](https://cursor.com/download).

Install globally so it's available in every project (recommended):

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```

Using Claude Code on the same machine too? Target it explicitly so the skill is installed or linked
under Claude Code's `.claude/skills` location:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g -a claude-code
```

Or install into a single project only:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create
```

If `npx` isn't recognized, install [Node.js](https://nodejs.org/en/download) and try again.

### No terminal — Claude desktop or web

If you use Claude in the desktop app or at [claude.ai](https://claude.ai), upload the skill as a file:

1. Download the `manansuneja/skills` repo as a ZIP — in GitHub, click the green **Code** button > **Download ZIP**.
2. Unzip it and find `skills/agent-workflows/workflow-create`.
3. In Claude, go to **Customize > Skills**.
4. Click **+**, choose **+ Create skill**, then **Upload a skill**, and upload that `workflow-create` folder.
5. Make sure the skill's toggle is **ON** in your list.

Then start a chat and ask: `Use workflow-create to build me a reusable workflow for ...`

---

## How to use it

Just talk to your agent and describe what you want:

```text
/workflow-create "Build me a reusable workflow for launching niche content sites."
```

It asks a few short questions, proposes the workflow, and creates the skills.

Include who the workflow is for, what a good result looks like, and the steps you already do by
hand. If you know the sequence, say it directly: `steps: research → scaffold → draft → publish`.

### Connect multiple skills into one workflow

You do not have to create every step yourself. Give Workflow Creator installed skill names, local
skill folders, GitHub URLs, or `owner/repo --skill name` references:

```text
/workflow-create connect these skills -
- owner/research-skills --skill research
- https://github.com/another-creator/writing-skills/tree/main/skills/draft
- polish-copy

Build one workflow that researches a topic, drafts the article, and polishes the final copy.
```

Workflow Creator reads what each skill does, places the skills in sequence, and builds the
coordinator around them. The coordinator passes each result to the next skill and tracks the full
run. Every connected skill keeps its original name and can still be called independently.

**What it builds, by example.** Take a familiar one — cooking a dish. Say the workflow is making your go-to pasta. The name `pasta` becomes the slug prefix on every skill it creates:

```text
pasta-workflow      ← one command makes the whole dish
├─ pasta-prep       → chop and measure the ingredients
├─ pasta-sauce      → build and simmer the sauce
├─ pasta-cook       → boil and time the pasta
└─ pasta-plate      → combine, season, and serve
```

Now `/pasta-workflow` runs prep → sauce → cook → plate every time — and you can still run any step on its own (chop for something else entirely).

**A run looks like this:**

```text
You: /pasta-workflow "make my go-to garlic butter pasta"

→ pasta-prep    chops the garlic, measures pasta + butter      ✓  records what's ready
→ pasta-sauce   melts butter, infuses the already-chopped garlic ✓  (doesn't re-chop)
→ pasta-cook    boils + times the pasta to al dente            ✓
→ pasta-plate   tosses pasta through the sauce, seasons, serves ✓

Done. A run log (runStatus.md) in your project shows each step, what it produced, and the finished dish.
```

Notice `pasta-sauce` picks up the garlic `pasta-prep` already chopped — it doesn't start over. That hand-off is the whole trick, and it's what the coordinator manages.

### The real work is the coordinator

Each step above is a complete skill on its own — `pasta-prep` can chop and measure for *any* recipe, not just this one. What turns four separate skills into one dish is the coordinator (`pasta-workflow`): the chef.

A chef doesn't re-teach knife skills. They run the steps in the right order, carry what just happened into the next step (the garlic's already chopped — don't start over), and keep the whole dish in mind so nothing drifts. That's exactly what `<prefix>-workflow` does for your skills: it sequences them, passes the context forward (in `runStatus.md`), and holds the goal so your agent never loses the plot.

In short, this is a **meta-skill** that connects individual skills into a reusable sequence. It
creates a **coordinator skill** that runs them in order and passes context and status between them.

A few things it can do:


| Command                          | What it does                                                                                             |
| -------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `/workflow-create "..."`         | **Create** a new workflow (the default).                                                                 |
| `/workflow-create connect "..."` | **Chain standalone skills** into one reusable workflow while keeping each independently callable. |
| `/workflow-create compose "..."` | **Adopt skills into one named family**; confirms before renaming them. |
| `/workflow-create update "..."`  | **Change** an existing one — add, remove, or reorder a step; fix something.                              |
| `/workflow-create delete "..."`  | **Remove** a workflow safely.                                                                            |


> **Keeping every skill independent?** Use `connect`. The coordinator chains them, but their original
> invocation names keep working.

> **Turning the skills into one named family?** Use `compose`. Workflow Creator can rename them, but
> it shows every rename and waits for confirmation first.

Want to see the plan before anything is written? Add `plan-only`:

```text
/workflow-create plan-only "Design a workflow for job hunting end to end."
```

---

## Example gallery

Five families built and validated to show the range — from a one-skill job to a composed engineering pipeline. Each was generated for real into an isolated sandbox, passes the validator, and is documented in [references/examples.md](references/examples.md).


| Workflow                                  | One line                                                                     | What it shows                                                                  |
| ----------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Clarify my thoughts** (`clarify`)       | Raw notes → one clear, well-shaped piece, in your voice.                     | A clean medium **sequential** family: distill → shape → polish.                |
| **Engineering delivery** (`ship`)         | A feature from idea to shipped through a sequence of standalone skills.      | **Connect** — reusable chain; every skill also works independently.           |
| **Business idea → plan** (`bizplan`)      | Validate an idea, model it, write the plan, render it as a site.             | A complex **multi-tool** family (web research + site build).                   |
| **Creative data viz** (`dataviz`)         | Data or an idea → a visual that tells a story, not a boring chart.           | **Context-aware**: clean chart vs. creative SVG, with a child-owned reference. |
| **Meeting → actions** (`meeting-actions`) | Notes → an owner-assigned action list.                                       | The **family gate firing**: one skill, because a family would be overkill.     |


> **The `clarify` example, expanded.** You paste a messy paragraph; `/clarify-workflow` runs `clarify-distill` (find the one point) → `clarify-shape` (give it a small story) → `clarify-polish` (simple, spacious, still yours). You can also call any step alone — just `/clarify-polish` on a draft you already structured.

> **Connect, expanded.** Point it at standalone skills — *"connect `to-prd`, `to-issues`, `tdd`, `diagnose`, and `improve-codebase-architecture` into one engineering workflow"* — and it builds `/ship-workflow` over them. The coordinator runs them in sequence, and every skill can still be called by itself.

> **Heads up:** it may ask for a short **project name**. That becomes the slug prefix on every skill it makes (e.g. `bizplan-research`, `bizplan-site`), so your workflow's skills stay grouped and easy to tell apart from the rest.

---

## What you get

- **One command** to run the whole workflow (the coordinator).
- **A few focused step-skills** you can also run on their own.
- **A dependency record** for connected external skills: original source, install command, path,
  and integrity hash.
- **A run log** (`runStatus.md`) saved into your project each time you run it, so you can always see what happened.
- A short README and a registry of all the parts.

---

## A few handy things

- **Run it your way.** When you run a workflow you made, you can change the order just by asking: *"skip the audit step"*, *"only do research and publish"*, *"stop after design."* That applies to that run only.
- **Works with your agent.** It writes new skills into the right place for whatever agent you're in (Claude Code, Cursor, Codex, …) so they're picked up automatically. Installs **globally** by default (available everywhere); ask for a **project-local** install to scope it to one repo. It can also offer to link the skills so your *other* agents can find them too.
- **Skills that just work.** Every generated skill follows the open skill format and is checked before it's finished, so it loads cleanly instead of being silently skipped for a formatting slip.
- **Always identifiable.** Every skill it creates is signed, so you (or a tool) can always tell it came from Workflow Creator.

---

## Pairs with

- [PM OS Setup](../../product-management/pm-os-setup) — once your product work lives in a PM
  workspace, use Workflow Creator to turn its recurring rituals (meeting notes → action list, raw
  notes → PRD) into one-command workflows.
- [Workspace OS Setup](../../business/workspace-os-setup) — the same move for a studio, business,
  or client-project workspace: capture the process once, run it forever.

## Learn more

- Check a generated workflow's structure: `python scripts/validate_workflow_family.py <your-workflow-folder>`

## What This Skill Does And How To Use It

Workflow Creator connects multiple skills to form a reusable workflow. A coordinator executes them
in sequence, while every individual skill can still be used on its own.

Install it with:

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
```

Run it by describing the workflow you want:

```text
/workflow-create "Build me a reusable workflow for launching niche content sites."
/workflow-create connect these skills - owner/repo --skill research, owner/other-repo --skill draft
```

Use `plan-only` when you want the architecture before files are written, `connect` to chain
standalone skills, `compose` to adopt them into one family, `update` to change an existing workflow,
and `delete` to remove one safely.
