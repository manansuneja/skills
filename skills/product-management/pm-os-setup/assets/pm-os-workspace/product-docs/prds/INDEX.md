# prds/ - Index

Feature specs live here as a hierarchy, not a pile of dated files. Model the work the way a PM thinks
about it: broader area/MVP -> feature -> story. Use the labels that fit the product; the folder
shape matters more than the exact vocabulary.

```text
product-docs/prds/<area-or-mvp-slug>/
  INDEX.md
  overview.md
  <feature-slug>/
    INDEX.md
    prd.md
    stories.md
```

For a genuinely standalone feature, use:

```text
product-docs/prds/<feature-slug>/
  INDEX.md
  prd.md
  stories.md
```

Do not date-prefix PRD filenames or folders; use the date column below for chronology.

| Date | Area / Feature | File |
|---|---|---|
| _none yet_ | Ask the Chief: "turn the X discussion into a PRD" | - |

The [prd-writer](../../agents/sub-agents/prd-writer.md) uses [to-prd](../../skills/to-prd.md) to
create these and adds a row here.

If you find an older flat or date-prefixed PRD, move it into the hierarchy and update this index in
the same change.

