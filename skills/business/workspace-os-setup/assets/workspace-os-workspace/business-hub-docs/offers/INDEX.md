# offers/ - Index

Offer and project briefs live here as a hierarchy, not a pile of dated files. Model the work the way a business owner thinks
about it: broader area/package -> offer -> client story. Use the labels that fit the business; the folder
shape matters more than the exact vocabulary.

```text
{{DOCS_ROOT}}/offers/<area-or-package-slug>/
  INDEX.md
  overview.md
  <offer-or-deliverable-slug>/
    INDEX.md
    brief.md
    client-story.md
```

For a genuinely standalone offer or deliverable, use:

```text
{{DOCS_ROOT}}/offers/<offer-or-deliverable-slug>/
  INDEX.md
  brief.md
  client-story.md
```

Do not date-prefix offer brief filenames or folders; use the date column below for chronology.

| Date | Area / Offer | File |
|---|---|---|
| _none yet_ | Ask the Chief: "turn the X discussion into an offer brief" | - |

The [offer-brief-writer](../../agents/sub-agents/offer-brief-writer.md) uses [offer-brief](../../business-skills/offer-brief.md) to
create these and adds a row here.

If you find an older flat or date-prefixed offer brief, move it into the hierarchy and update this index in
the same change.
