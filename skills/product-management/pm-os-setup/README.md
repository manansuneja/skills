# PM OS Setup

[![skills.sh](https://skills.sh/b/manansuneja/skills)](https://skills.sh/manansuneja/skills)

PM OS Setup creates a Product Management operating system: a structured workspace with a Chief PM
coordinator, specialist agents, reusable skills, product memory, and automatic indexes.

It is not just a PRD generator. It is a product mindspace your agents can actually navigate.

You give the command. The Chief PM finds the right context, routes the work, applies the right skill,
creates the artifact, and keeps the workspace organized in the background.

Your taste and ways of working become reusable skills. Your docs stay linked. Your product context
stays current. Your agent does not have to rediscover the map every time you ask it to help.

It works with Claude Code, Cursor, Codex, GitHub Copilot, and plain agent chats because the generated  
workspace is mostly Markdown. Tool-specific wiring stays minimal by default.

## What This Helps PMs Do

- Build a structured product workspace instead of another folder of loose notes.
- Work through one Chief coordinator that routes to the right specialist automatically.
- Capture your PM taste, standards, and ways of working as reusable skills.
- Turn brainstorms, decisions, meetings, and feature ideas into durable artifacts.
- Create PRDs and decision docs without manually rebuilding context every time.

## Quickstart

You do not need to be a developer — you just need an agent that can run skills, like
[Claude Code](https://code.claude.com/docs/en/quickstart) or [Cursor](https://cursor.com/download).
Don't have one yet? Install either from those links. (Cursor can also add skills from its own UI, so
you can skip the terminal entirely — see [Other ways to install](#other-ways-to-install).)

**1. Install the skill:**

```bash
npx skills@latest add manansuneja/skills --skill pm-os-setup -g
```

If `npx` isn't recognized, install [Node.js](https://nodejs.org/en/download) and try again.

**2. Run it:**

```text
/pm-os-setup Set up a PM OS for Acme.
```

The agent asks whether to use the current folder or create a new one, then scaffolds the workspace and  
offers to personalize it. If your tool doesn't show slash commands, just say it plainly:  
`Use pm-os-setup to set up a PM OS for Acme.`

## Other Ways To Install

The Quickstart works in any tool with a terminal (Claude Code, Cursor, Codex, Copilot). If you don't
have a terminal or would rather not use one, pick one of these instead.

### No terminal — Claude desktop or web

If you use Claude in the desktop app or at [claude.ai](https://claude.ai), upload the skill as a file:

1. Download the `manansuneja/skills` repo as a ZIP — in GitHub, click the green **Code** button > **Download ZIP**.
2. Unzip it and find `skills/product-management/pm-os-setup`.
3. In Claude, go to **Customize > Skills**.
4. Click **+**, choose **+ Create skill**, then **Upload a skill**, and upload that `pm-os-setup` folder.
5. Make sure the skill's toggle is **ON** in your list.

Then start a chat and ask: `Use pm-os-setup to set up a PM OS for Acme.`

## What It Creates

```text
acme-workspace/
|-- AGENTS.md
|-- CLAUDE.md
|-- INDEX.md
|-- README.md
|-- agents/
|   |-- pm-chief.md
|   `-- sub-agents/...
|-- product-docs/
|   |-- product-vision.md
|   |-- meetings/...
|   |-- prds/...
|   `-- decisions/...
|-- skills/
|   |-- apply-pmos-struct.md
|   |-- summarize-notes.md
|   |-- brainstorm.md
|   |-- to-prd.md
|   `-- ...
`-- _setup/
    |-- README.md
    `-- AGENTS.md
```

Every PM OS content folder also includes an `INDEX.md` so agents can find the right context without  
loading the whole workspace.

After the scaffold is created, the agent reads `_setup/AGENTS.md` and personalizes the workspace
around your product: product vision, Chief PM behavior, specialist agents, docs, and skills.

That personalization keeps the workspace machinery separate from the product. For example, if your
product is an AI agent or robot, the product docs should describe that product's agents or robots -
not accidentally turn the workspace's Chief PM into the product.

## Stays Tidy On Its Own

You never have to file, rename, or organize anything. Every time you create or change something — a
meeting summary, a PRD, a decision, a new skill — the workspace cleans up after itself in the
background: the artifact lands in the right folder with a sensible name, the indexes update so your
agent can still find everything, and your product vision stays current.

So it never decays into a junk drawer of loose Markdown files. You just keep talking, deciding, and
shipping — the workspace quietly keeps itself navigable around you.

## After Setup

On your first session the agent offers to personalize the workspace around your product, then gets out
of the way. From there you just talk to the **Chief PM** in plain language and it routes the work:

```text
Summarize these meeting notes and save them in the right place.
Help me brainstorm onboarding improvements and capture the best direction.
Turn this feature idea into a PRD using our product vision as context.
Update the product vision based on this new strategy note.
```

It comes with a handful of starter skills — `summarize-notes`, `brainstorm`, `to-prd`,
`document-product-context` — that grow with you over time (see [Growing Your Skills](#growing-your-skills)).

## Growing Your Skills

The skills you start with are just a base — beginner versions meant to be reshaped around how *you*
work. Skills are where your PM taste lives: the way you like PRDs structured, how you run a
brainstorm, what a good decision doc looks like to you. The more you tune them, the more the workspace
feels like an extension of you instead of a generic template.

You don't edit skill files by hand. Just tell the Chief PM what you want, in plain language:

```text
Update the to-prd skill so PRDs always open with the problem and a one-line bet.
My brainstorms should push back harder before converging — adjust the brainstorm skill.
Create a new skill for how I like launch plans written.
Create a skill for weekly exec updates in my voice.
```

The Chief PM routes this through the **skill-librarian**, which writes or revises the skill, then keeps
the workspace tidy around the change. New skills are picked up automatically — the next time the work
matches, your agent applies them without being reminded.

A good habit: any time you find yourself explaining *how* you want something done for the second or
third time, ask the Chief PM to capture it as a skill. That repeated instruction becomes reusable, and
you stop re-teaching it.
