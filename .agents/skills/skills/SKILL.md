---
name: skills
description: Maintain shared Codex and Claude skills. Use when creating, editing, moving, removing, or validating an agent skill.
---

# Skill — skills

Keep every skill available to both Codex and Claude from one canonical source.

## Required parity

For every skill change, update the canonical Codex file at
`.agents/skills/<name>/SKILL.md` and ensure Claude has the matching entry at
`.claude/skills/<name>`.

Use a symlink rather than a copied Claude version:

```sh
ln -sfn "../../.agents/skills/<name>" ".claude/skills/<name>"
```

For a new, moved, renamed, or removed skill, make the equivalent change to both
paths in the same commit. Verify the Claude entry resolves to the canonical
directory before finishing.
