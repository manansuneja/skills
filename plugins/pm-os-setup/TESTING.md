# PM OS plugin acceptance test

Do not submit the plugin until every pending item in `release-evidence.json` has
real evidence. Automated output proves package integrity and scaffold behavior;
it does not replace activation-quality testing in an agent client.

## Rebuild the exact candidate

```bash
python -m pip install -r scripts/requirements-plugins.txt
python scripts/build_plugins.py
python scripts/validate_plugins.py
python scripts/test_plugins.py --plugin pm-os-setup
```

The submission upload is
`dist/plugins/releases/pm-os-setup-1.2.4-skill-bundle.zip`. Before upload, its
SHA-256 must equal `submissionArchive.sha256` in `release-evidence.json`.

## ChatGPT/Codex local acceptance

1. Run `codex plugin marketplace add .` from the repository root.
2. Confirm `manan-skills` appears in `codex plugin marketplace list`.
3. Install `pm-os-setup@manan-skills` in the Plugins Directory.
4. Start a new Work conversation with a disposable empty folder.
5. Run every case in `evals.json`. Record activation, questions asked, created
   files, safety behavior, missing steps, output usefulness, and the tested
   payload digest.
6. Confirm negative cases create no workspace and the destructive case removes
   nothing.

## Public mobile acceptance

Run this only after a review or public build is available in the universal directory. The local
`manan-skills` marketplace cannot be loaded from a phone.

1. Install PM OS from the ChatGPT mobile Plugins Directory.
2. Start a new conversation without attaching a writable project root and ask it to set up PM OS.
3. Confirm it discloses Conversation mode before setup and does not claim to create a folder tree,
   local files, or a ChatGPT Project.
4. Confirm it maintains a compact Markdown PM OS Index and keeps ordinary artifacts Markdown-first.
5. Confirm it offers a supported download/export or continuation in a file-capable environment.
6. Repeat once with no related installed capability and once with an already authorized storage or
   document capability. It must neither invent access nor install/connect another capability.

## VS Code independent-client acceptance

Enable plugins, then register the portable package in user `settings.json`:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "/absolute/path/to/dist/plugins/portable/pm-os-setup": true
  }
}
```

Reload VS Code, open `Chat: Configure Skills`, and confirm `pm-os-setup` appears
from the portable package. Run one positive setup case in a disposable folder
and one negative non-activation case.

## Submission checklist

- Verify the publisher identity as Manan Suneja and confirm Apps Management
  write access.
- Deploy the GitHub Pages site and open the landing, support, privacy, and terms
  URLs without authentication.
- Upload the production logo and exact digest-locked skill bundle.
- Choose `Skills only`, `Productivity`, broad supported-country availability,
  and the three starter prompts in `listing.json`.
- Paste the five positive and three negative cases from `evals.json` with their
  completed observations.
- Use the release notes in `release-evidence.json`.
- Keep publishing manual until at least the PM OS review cycle is complete.
