---
name: skills
description: Create, edit, move, remove, and validate Claude skills in the repository's Claude skill tree.
---

# Skill — skills

Maintain Claude skills as self-contained packages under `.claude/skills/`.

## Surface boundary

Create each skill at `.claude/skills/<name>/SKILL.md`. Do not place instructions
for another harness in this tree. A skill may be symlinked from another skill
tree only when the instructions are genuinely identical and contain no
harness-specific model, tool, path, or behavior. Similar skills that differ on
any of those points must remain independent implementations.

## Creation workflow

1. Choose a short lowercase hyphenated name.
2. Write discriminating YAML frontmatter with `name` and `description`.
3. Keep essential decisions and workflow in `SKILL.md`; add scripts,
   references, or assets only when they have a concrete repeated use.
4. Keep model names and runtime behavior specific to Claude. Say `Sonnet` or
   `Opus` and let the harness select the installed version.
5. Validate the skill with the available skill validator and test any scripts.
6. Commit only the skill files and related Claude configuration intended by the
   task.

Use Sonnet with light thinking for mechanical scaffolding once the parent has
fixed the skill's design and constraints. Use higher thinking only when the
delegated work itself requires judgment.
