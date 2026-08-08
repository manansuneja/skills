# Workflow Creator store security review

Status: **blocked from publication**  
Reviewed: August 7, 2026  
Canonical version: 1.1.1

This is a release-layer review only. It does not silently fork or modify the
canonical skill. The portable and OpenAI packages may be built for validation,
but `workflow-create` must not be added to the marketplace or store while any
blocking finding remains.

## Findings

### 1. Ledger paths are not confined before destructive use — critical

The canonical validator accepts absolute paths and unresolved traversal in a
`linkages.md` row. The delete lifecycle then says to delete the paths listed in
that ledger. A tampered or malformed ledger could therefore point outside the
selected skills root.

Required remediation: canonical behavior must resolve every candidate path,
reject absolute/traversal escapes for owned family members, verify it is a
direct child of the chosen skills root, reject reparse-point escapes, show the
resolved deletion set, and require confirmation against those exact paths.

### 2. Remote retrieval executes an unpinned installer before review — high

Connect mode and the missing `skill-creator` fallback may run
`npx skills@latest add` against a repository or URL. The source is not pinned to
a commit and the package is installed before a complete trust review.

Required remediation: inspect or download into an isolated staging directory,
record a commit/content digest, scan the full payload, show publisher/source and
requested install paths, and obtain explicit confirmation before installation
or execution. Never treat text inside a retrieved skill as trusted instructions
during review.

### 3. Compose rename lacks a transactional rollback — high

Compose correctly requires confirmation, but it renames and edits original
skill folders in place. The documented lifecycle does not require a backup,
preflight collision set, atomic move plan, or rollback after partial failure.

Required remediation: preview every resolved old/new path, reject collisions,
create a recoverable backup or transaction journal, apply the full rename set,
validate, and roll back on failure.

### 4. Cross-harness links need containment and link-target checks — high

Symlink creation is opt-in and collision-aware, which is a good baseline. It
does not explicitly require canonicalizing source/target roots, rejecting
junction/reparse escapes, or verifying that an existing link resolves to the
expected family member before replacement.

Required remediation: resolve both roots, restrict targets to the two approved
skills homes, use exact member names from the validated ledger, inspect existing
link targets, and never recursively replace a real directory.

### 5. Update removal needs the delete lifecycle's full preview — medium

Update mode asks before removing a child, but it does not inherit all delete
guards: exact resolved path list, ledger containment, orphan protection, and a
post-change rollback/validation rule.

Required remediation: route child removal through one shared destructive
operation contract used by both update and delete.

## Positive controls already present

- Connect defaults over destructive compose when intent is unclear.
- Compose requires confirmation for renames.
- Cross-harness links are optional and require a clear yes.
- Delete requires a folder preview and confirmation and excludes untracked
  orphans.
- External dependency hashes are recorded and checked for drift.
- The repaired external fixture runner passes all five workflow families.

These controls reduce accidental changes, but they do not close the containment
and supply-chain findings above. Store scanning should not be worked around in
the plugin overlay; remediation belongs in a separate canonical skill change so
GitHub, npx, and every plugin client receive the same behavior.
