# Cross-Harness Access

Read this after creating or updating a global workflow family when the user may want the same skills
available to another agent harness.

After writing the family to the host harness's skills home, offer one optional symlink step. Act only
on a clear yes and only for family folders touched in the current run. Skip for project-local installs.

- Claude Code host: offer links from `.claude/skills/<member>` into `.agents/skills/<member>`.
- Any other host: offer links from `.agents/skills/<member>` into `.claude/skills/<member>`.

For every member:

1. If the target root is missing, offer to create it.
2. If the target entry is already the correct symlink, skip it.
3. If a real directory or different link exists, explain the collision and replace it only after
   confirmation.
4. If symlinks are unavailable, offer a copy and explain that later edits will not stay synchronized.
5. Report the source and target paths created or skipped.

Never touch unrelated skill folders. For public workflow instructions, use `${USER_ROOT}` and
`${SKILLS_ROOT}` placeholders rather than machine-specific absolute paths.
