# Plugin release overlays

`skills/` remains the canonical source for every skill in this repository. This
directory contains only release metadata, evaluation cases, and store assets.
The build copies Git-tracked canonical files into disposable packages under
`dist/plugins/`; generated skill payloads must never be edited or committed.

## Release commands

```bash
python scripts/build_plugins.py
python scripts/validate_plugins.py
python scripts/test_plugins.py --plugin pm-os-setup
```

Use `python scripts/build_plugins.py --refresh-digests` only when a canonical
skill change is paired with an intentional version bump. Review and commit the
resulting `plugins/catalog.json` change with that release.

The build produces:

- `dist/plugins/portable/<name>/` for Agent Plugins 1.0 clients.
- `dist/plugins/openai/<name>/` for ChatGPT/Codex local testing.
- deterministic ZIP archives under `dist/plugins/releases/`.

Only `pm-os-setup` is listed in the local marketplace during the pilot.
`workspace-os-setup` and `workflow-create` have production metadata now so the
same pipeline can validate them without implying store availability.

## Manifest layers

- `plugins/catalog.json` is this repository's release source of truth.
- Generated portable packages use the Agent Plugins 1.0 root `plugin.json`.
- `.agents/plugins/marketplace.json` is the Codex local-marketplace catalog.

Agent Plugins 1.0 does not define or require a repository-level `plugins.json`,
so this project intentionally does not generate one.
