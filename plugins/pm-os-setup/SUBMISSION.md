# PM OS public submission packet

Use this file while completing the OpenAI plugin submission form. Submit as
**Skills only**. Do not add an MCP server, authentication, app, or UI to this
release.

## Publisher and listing

- Plugin name: `PM OS`
- Developer identity: `Manan Suneja`
- Category: `Productivity`
- Website: `https://manansuneja.github.io/skills/`
- Support: `https://manansuneja.github.io/skills/support.html`
- Privacy: `https://manansuneja.github.io/skills/privacy.html`
- Terms: `https://manansuneja.github.io/skills/terms.html`
- Availability: all countries offered by the submission form

Short description:

> Build a durable product-management workspace.

Long description:

> Create and personalize a Markdown-first product workspace with a living
> workboard for vision, customer context, meetings, decisions, outcomes, and
> PRDs. It can route specialized work through compatible installed
> capabilities when requested, while keeping outputs organized without
> overwriting existing work.

## Starter prompts

1. Set up a PM OS for my product.
2. Create a PM workspace for product discovery.
3. Personalize my PM OS for weekly planning.

## Upload candidate

- Version: `1.2.4`
- Bundle: `dist/plugins/releases/pm-os-setup-1.2.4-skill-bundle.zip`
- Bundle SHA-256: `17b41a147cc74f94cc222682f9840dc14bfc10cf63fdfa8e7b3c2078178dec02`
- Skill payload digest: `49615bc67adb3d1100321d3b4be4e7ac8a3b657e5b62e85430380243fcef4b65`
- Logo source: `plugins/pm-os-setup/assets/logo-v2-marketplace.jpg`

Do not rebuild or edit the skill after completing the manual tests. If the
bundle changes, bump the version and repeat the tests against the new digest.

## Test cases

Copy the five positive and three negative cases from `evals.json`. Complete the
observations required by `TESTING.md` before submission, including activation,
questions asked, created files, safety behavior, missing steps, usefulness, and
the tested bundle digest.

## Release notes

> Introduces PM OS as a Markdown-first product-management workspace for
> desktop, mobile conversation mode, and file-capable agent clients. It adds a
> living workboard, safe existing-workspace detection, Markdown-first artifact
> routing, and optional use of compatible installed capabilities without any
> first-party server, account connection, authentication, or telemetry.

## Portal checklist

- [ ] Verified identity is `Manan Suneja`.
- [ ] Submitter has Apps Management write access.
- [ ] All four public URLs return HTTP 200 without authentication.
- [ ] Exact bundle and production logo uploaded.
- [ ] Five positive and three negative cases include completed observations.
- [ ] Country availability and policy attestations completed.
- [ ] Final preview uses `PM OS` consistently.
- [ ] Submission sent for review.
