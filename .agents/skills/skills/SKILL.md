---
name: skills
description: Create, edit, move, remove, and validate Codex skills in the repository's Codex skill tree.
---

# Skill — skills

Maintain Codex skills as self-contained packages under `.agents/skills/`.

## Surface boundary

Create each skill at `.agents/skills/<name>/SKILL.md`. Do not place instructions
for another harness in this tree. A skill may be symlinked into another skill
tree only when the instructions are genuinely identical and contain no
harness-specific model, tool, path, or behavior. Similar skills that differ on
any of those points must remain independent implementations.

## Creation workflow

1. Choose a short lowercase hyphenated name.
2. Write discriminating YAML frontmatter with `name` and `description`.
3. Keep essential decisions and workflow in `SKILL.md`; add scripts,
   references, or assets only when they have a concrete repeated use.
4. Keep model names and runtime behavior specific to Codex.
5. Validate the skill with the available skill validator and test any scripts.
6. Commit only the skill files and related Codex configuration intended by the
   task.

For lightweight reusable workers, store a real TOML profile in
`.codex/agents/`; do not use a symlink. Select its model and reasoning effort
explicitly.
