# Workflow Creator

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

**Turn something you do over and over into a reusable skill your coding agent can run for you — built once, run any time.**

`/workflow-create` is a skill that *creates skills*. You describe a workflow in plain language; it designs and writes a small set of skills for you (one main "coordinator" plus a few focused steps), wires them together, and gives you a single command to run the whole thing later.

> Workflow Creator **builds the machine**. The machine **runs whenever you call it.**

---

## New to skills?

Skills are just folders of Markdown instructions that teach a coding agent (like Claude Code) how to do a specific job. The agent loads them automatically when they're relevant — you don't have to wire anything up.

If you're getting started, these references will help:

- **Agent Skills — what they are:** [https://docs.claude.com/en/docs/agents-and-tools/agent-skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
- **Claude Code:** [https://docs.claude.com/en/docs/claude-code](https://docs.claude.com/en/docs/claude-code)
- **`skill-creator` (the authoring standards this tool follows — installed if present, else fetched):** [https://github.com/anthropics/skills/tree/main/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

Once your agent can use skills, you're ready.

---

## Install

You don't need to be a developer — you just need an agent that can run skills, like
[Claude Code](https://code.claude.com/docs/en/quickstart) or [Cursor](https://cursor.com/download).

Install globally so it's available in every project (recommended):

```bash
npx skills@latest add manansuneja/skills --skill workflow-create -g
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

It asks a couple of quick questions (a name, the purpose, maybe an example), proposes a design, and then creates the skills. That's it.

**The more specific your goal, the better the skills.** A broad one-liner like "launch niche content sites" gives the agent little to work with, so it'll ask you to sharpen it — who it's for, what good output looks like, the steps you already do by hand. The more of that you bring up front, the sharper the workflow. And if you already know the breakdown, just say so in the prompt (*"steps: research → scaffold → draft → publish"*) and it'll build exactly that.

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

In short, this is a **meta-skill** — a skill that wires up a workflow for you. It takes skills you already have, or brand-new ones it writes for you (using Anthropic's `skill-creator`), and sets up a **coordinator skill** that links them together — along with a built-in structure for sharing context and status between steps as they run.

A few things it can do:


| Command                          | What it does                                                                                             |
| -------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `/workflow-create "..."`         | **Create** a new workflow (the default).                                                                 |
| `/workflow-create compose "..."` | **Wire skills you already have** into one workflow. Name them and it builds the coordinator around them. |
| `/workflow-create update "..."`  | **Change** an existing one — add, remove, or reorder a step; fix something.                              |
| `/workflow-create delete "..."`  | **Remove** a workflow safely.                                                                            |


> **Got skills already?** Point it at them — *"wire `my-voice-it`, `voice-distance-check`, and `polish-my-voice-it` into one workflow"* — and it builds the coordinator over your existing skills instead of writing them from scratch. It renames them into the family (e.g. `my-voice-it → writing-voice`) so they group cleanly, and it'll always confirm that rename first, since it changes how you call them.

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
| **Engineering delivery** (`ship`)         | A feature from idea to shipped, wired from Matt Pocock's engineering skills. | **Compose** — adopting skills you already own; conditional + optional steps.   |
| **Business idea → plan** (`bizplan`)      | Validate an idea, model it, write the plan, render it as a site.             | A complex **multi-tool** family (web research + site build).                   |
| **Creative data viz** (`dataviz`)         | Data or an idea → a visual that tells a story, not a boring chart.           | **Context-aware**: clean chart vs. creative SVG, with a child-owned reference. |
| **Meeting → actions** (`meeting-actions`) | Notes → an owner-assigned action list.                                       | The **family gate firing**: one skill, because a family would be overkill.     |


> **The `clarify` example, expanded.** You paste a messy paragraph; `/clarify-workflow` runs `clarify-distill` (find the one point) → `clarify-shape` (give it a small story) → `clarify-polish` (simple, spacious, still yours). You can also call any step alone — just `/clarify-polish` on a draft you already structured.

> **Compose, expanded.** Point it at skills you already have — *"wire `to-prd`, `to-issues`, `tdd`, `diagnose`, and `improve-codebase-architecture` into one engineering workflow"* — and it builds `/ship-workflow` over them, renaming each into the family (e.g. `to-prd → ship-prd`) and confirming that rename first, since it changes how you call them.

> **Heads up:** it may ask for a short **project name**. That becomes the slug prefix on every skill it makes (e.g. `bizplan-research`, `bizplan-site`), so your workflow's skills stay grouped and easy to tell apart from the rest.

---

## What you get

- **One command** to run the whole workflow (the coordinator).
- **A few focused step-skills** you can also run on their own.
- **A run log** (`runStatus.md`) saved into your project each time you run it, so you can always see what happened.
- A short README and a registry of all the parts.

---

## A few handy things

- **Run it your way.** When you run a workflow you made, you can change the order just by asking: *"skip the audit step"*, *"only do research and publish"*, *"stop after design."* That applies to that run only.
- **Works with your agent.** It writes new skills into the right place for whatever agent you're in (Claude Code, Cursor, Codex, …) so they're picked up automatically. Installs **globally** by default (available everywhere); ask for a **project-local** install to scope it to one repo. It can also offer to link the skills so your *other* agents can find them too.
- **Skills that just work.** Every generated skill follows the open skill format and is checked before it's finished, so it loads cleanly instead of being silently skipped for a formatting slip.
- **Always identifiable.** Every skill it creates is signed, so you (or a tool) can always tell it came from Workflow Creator.

---

## Learn more

- Check a generated workflow's structure: `python scripts/validate_workflow_family.py <your-workflow-folder>`
