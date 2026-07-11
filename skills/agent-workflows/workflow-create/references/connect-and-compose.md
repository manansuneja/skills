# Connect And Compose Lifecycles

Read this reference when `/workflow-create` is connecting existing skills instead of authoring every
step from scratch.

## Contents

- [Choose Connect Or Compose](#choose-connect-or-compose)
- [Connect Lifecycle](#connect-lifecycle)
- [Compose Lifecycle](#compose-lifecycle)

## Choose Connect Or Compose

Use `connect` for independently published, shared, or third-party skills. Preserve their names,
folders, metadata, and files. The generated coordinator depends on them but does not claim ownership.

Use `compose` only for skills the user owns and explicitly wants adopted into one family. Adoption
may rename and annotate those skills after confirmation.

When ownership is unclear, default to `connect`. Never rename a skill merely because it appears in a
workflow.

## Connect Lifecycle

Trigger on the explicit `connect` verb, `/workflow-create connect these skills - ...`, or a request
to wire skills from other creators, repositories, or URLs.

1. **Parse each reference.** Accept an installed skill name, local skill folder, GitHub repository or
   skill-folder URL, or `owner/repo --skill name`. Preserve the source string verbatim in the brief.
2. **Resolve before designing.** Search the selected project/global skills roots for installed
   names. For a repository reference, use `npx skills@latest add <source> --list` or inspect the
   repository to confirm the available skill and canonical name. Do not guess a missing name.
3. **Install only what is missing.** Use the chosen install scope and the exact source, for example
   `npx skills@latest add owner/repo --skill skill-name -g`. Connecting named skills authorizes this
   normal setup step. If the source contains multiple plausible skills, ask which one. Never
   overwrite a same-name skill from a different source; surface the collision.
4. **Inspect the contract.** Read each resolved `SKILL.md` and extract its job, triggers, inputs,
   outputs, side effects, required tools, and constraints. Design handoffs from what the skill
   actually promises, not its marketing description.
5. **Preserve the dependency.** Never rename its folder or frontmatter, add Workflow Creator
   metadata, insert orchestration text, or edit its scripts/references/assets. Compute and record a
   SHA-256 hash of its installed `SKILL.md`.
6. **Design the chain.** Generate a new `<prefix>-workflow` coordinator. Add newly authored,
   prefix-named gap steps only when the connected skills leave a real missing responsibility.
7. **Record reproducibility.** Mark connected rows `external` in the Chain. Add an
   `## External Dependencies` table containing skill, source, install command, expected path,
   `SKILL.md` hash, and last-verified date.
8. **Wire runtime checks.** Before calling an external skill, verify its path, frontmatter name, and
   hash. A missing dependency blocks that step and produces the recorded install command. Hash drift
   pauses the workflow for review; never silently reinstall or overwrite it.
9. **Document ownership.** The coordinator README lists external dependencies separately and links
   to their original sources. Do not imply the connected skills are authored, bundled, or licensed
   by the workflow creator.
10. **Validate and forward-test.** Run the family validator, then a plan-only example that proves the
    coordinator can route into the unchanged dependencies and carry outputs between them.

The workflow package contains the coordinator and any newly authored gap skills. External skills
remain separate dependencies and keep their original update paths.

## Compose Lifecycle

Use when the user owns the named skills and wants them adopted into a uniform family.

1. Locate each skill on disk. If a skill cannot be found, report what resolved and ask for the
   missing path or name.
2. Show the proposed `<prefix>-<name>` renames and explain that old invocation names will stop
   working. Proceed only after explicit confirmation.
3. Rename the confirmed folders and frontmatter names, preserve their capabilities and resources,
   add `metadata.generator: workflow-create`, `adopted: true`, the human footer, and an Orchestration
   Linkage block.
4. Author only the gap steps required for a complete chain.
5. Generate the coordinator, `linkages.md`, and README, then run the normal family validation.

If the user declines a rename, leave that skill unchanged and switch it to an external `connect`
dependency instead of forcing adoption.
