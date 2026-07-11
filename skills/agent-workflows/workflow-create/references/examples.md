# Example Workflow Families

Named, ready-to-show example families spanning the complexity range. Use them two ways:

- **During intake** (SKILL.md Phase 1/3): offer a user a concrete template to point at —
  "build something like the `clarify` workflow", "compose mine like the `ship` example".
- **For decomposition reference:** each entry shows how a goal was sharpened, gated, and
  split, so a new family can borrow a proven shape instead of starting abstract.

All five were generated and validated for real in a local development sandbox
(`testing/`, kept out of the published package); each passes
`validate_workflow_family.py`.

Each coordinator also carries a short **Output Resolution** section — the lightweight
best practice of doing a basic project check, defaulting sensibly, and asking the user
only when context demands (ambiguous destination, heavy scaffolding, a new dependency, an
overwrite). It's a nudge, not a rigid spec: the coding agent reads the live project and
decides specifics. `dataviz` (library + destination routing) and `meeting-actions`
(inline-vs-file) show it most clearly.

## Contents

- [At a glance](#at-a-glance)
- [clarify — clarify my thoughts (medium)](#clarify--clarify-my-thoughts-medium)
- [ship — engineering delivery, connected (complex)](#ship--engineering-delivery-connected-complex)
- [bizplan — business idea → plan → site (complex)](#bizplan--business-idea--plan--site-complex)
- [dataviz — creative data visualization (medium)](#dataviz--creative-data-visualization-medium)
- [meeting-actions — notes → actions (simple, gate fires)](#meeting-actions--notes--actions-simple-gate-fires)
- [Offering examples during intake](#offering-examples-during-intake)

## At a glance

| Workflow | Prefix | Coordinator | Lifecycle | Pattern | Tier | Children |
| --- | --- | --- | --- | --- | --- | --- |
| Clarify my thoughts | `clarify` | `clarify-workflow` | create | sequential | medium | 3 |
| Engineering delivery | `ship` | `ship-workflow` | **connect** | sequential + conditional | complex | 5 (external) |
| Business idea → plan | `bizplan` | `bizplan-workflow` | create | sequential + multi-tool | complex | 4 |
| Creative data viz | `dataviz` | `dataviz-workflow` | create | context-aware + iterative | medium | 3 |
| Meeting → actions | `meeting-actions` | `meeting-actions-workflow` | create | single step | simple | 1 (gate fired) |

---

## clarify — clarify my thoughts (medium)

- **Purpose:** turn raw, unfinished thoughts into one short, clear, well-shaped piece, in the writer's own voice.
- **Coordinator:** `/clarify-workflow`
- **Children:** `clarify-distill` (find the single core point) → `clarify-shape` (small narrative shape) → `clarify-polish` (simple, spacious, voice intact).
- **Tier:** medium · **Pattern:** sequential (iterative polish loop).
- **Why this shape:** the three phases are judged on different bars — meaning, then structure, then surface. Reversing them produces clean prose that says nothing, so they must be separate and ordered. Each is useful standalone (just distill; just polish a draft). The decomposition exists to stop the #1 single-prompt failure: polishing something that never had a point.

## ship — engineering delivery, connected (complex)

- **Purpose:** take a feature from idea to shipped by chaining standalone engineering skills into one reusable flow.
- **Coordinator:** `/ship-workflow`
- **External steps:** `to-prd` → `to-issues` → `tdd`, with `diagnose` (**default-skip**, invoked only on a hard failure) and `improve-codebase-architecture` (**optional**). Every skill keeps its original name and source.
- **Tier:** complex · **Pattern:** sequential + conditional.
- **Why this shape:** this is the `connect` lifecycle — the steps are distinct disciplines published as standalone skills, so the coordinator depends on them without rewriting or renaming them. `linkages.md` records each source, install command, path, and hash. The example exercises external dependencies, active/default-skip/optional statuses, and conditional branching back to the build step.
- **Note:** composition can also author fresh gap-filler children alongside adopted ones; this family adopted every member to keep the focus on the adoption mechanics.

## bizplan — business idea → plan → site (complex)

- **Purpose:** think a business idea through end to end and render it as a simple plan you can actually look at.
- **Coordinator:** `/bizplan-workflow`
- **Children:** `bizplan-research` (validate problem/customer/market) → `bizplan-model` (revenue, pricing, unit economics, GTM, risks) → `bizplan-plan` (synthesize `business-plan.md`) → `bizplan-site` (render a single-page visual website).
- **Tier:** complex · **Pattern:** sequential + multi-tool.
- **Why this shape:** each phase consumes the last (can't model before validating, can't render before writing), so the order is forced. The phases need genuinely different expertise and produce distinct artifacts, and two use tools (web research; web build) — the textbook case for a coordinator over one sprawling skill. The coordinator's job is to keep the customer/problem definition consistent across all four steps.

## dataviz — creative data visualization (medium)

- **Purpose:** turn data or a rough idea into a visual that tells a story — a clean component chart when right, creative SVG when the story deserves more.
- **Coordinator:** `/dataviz-workflow`
- **Children:** `dataviz-insight` (find the one story + data shape) → `dataviz-design` (choose chart-vs-SVG, encoding, framing) → `dataviz-build` (evilcharts component or hand-built SVG).
- **Tier:** medium · **Pattern:** context-aware + iterative.
- **Why this shape:** insight is analytical, design is editorial judgment, build is production — different failure modes, so they split. The design step branches (a routing test sends clean comparisons to a charting component like evilcharts, and a single hero relationship or process to creative SVG), which makes the workflow context-aware. It owns the family's one reference, `dataviz-design/references/visual-vocabulary.md` (chart-type selection + creative SVG patterns + honest-encoding rules), wired via `linkages.md` load-when — the example that demonstrates child-owned references.

## meeting-actions — notes → actions (simple, gate fires)

- **Purpose:** turn raw meeting notes into a clean, owner-assigned action list.
- **Coordinator:** `/meeting-actions-workflow`
- **Children:** `meeting-actions-extract` (the single capability).
- **Tier:** simple · **Pattern:** single step.
- **Why this shape:** the **family gate fired**. Parsing, assigning, and formatting actions share inputs, produce one artifact, and share one bar — they'd always run together and never be useful alone, failing the split test. So the tool built one skill, wrapped in a minimal coordinator with a one-entry `linkages.md` so it can grow later via `update`. This is the deliberate counter-example: proof the tool knows when *not* to build a family.

## Offering examples during intake

When a user's goal is vague or they ask "what can this do?", offer the closest example as a
starting template rather than abstract questions:

- Writing / thinking → `clarify`.
- "Connect these published skills into one workflow" → `ship` (connect).
- A big multi-stage deliverable with research + a built artifact → `bizplan`.
- Charts, graphics, "show this visually" → `dataviz`.
- A small single-purpose task → `meeting-actions`, and explain the family gate so the user
  isn't surprised when one skill is the right answer.

Then sharpen their specific goal from there (Phase 1) before decomposing (Phase 3).
