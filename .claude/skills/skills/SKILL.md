---
name: skills
description: Create, edit, move, remove, and validate Claude skills in the repository's Claude skill tree.
---

# Skill — skills

Maintain Claude skills as self-contained packages reachable from
`.claude/skills/`.

## Surface boundary

Aether keeps one copy of each skill that Claude and Codex share.

- **Shared skill** — the content has no harness-specific model, tool, path, or
  behavior. Write it at `.agents/skills/<name>/SKILL.md` and symlink it:
  `ln -sfn "../../.agents/skills/<name>" ".claude/skills/<name>"`. Codex reads
  the same file, so keep it harness-neutral.
- **Claude-specific skill** — the content names Claude models, Claude tools, or
  Claude runtime behavior. Write real files at `.claude/skills/<name>/SKILL.md`,
  not a symlink. If Codex needs the same skill, it gets its own version in
  `.agents/skills/<name>/`.

Before adding Claude-specific content to a symlinked skill, split it into two
independent files first. List every skill in `.agents/skills/README.md`.

## Creation workflow

1. Choose a short lowercase hyphenated name, and decide shared or
   Claude-specific.
2. Write discriminating YAML frontmatter with `name` and `description`.
3. Keep essential decisions and workflow in `SKILL.md`; add scripts,
   references, or assets only when they have a concrete repeated use.
4. In a Claude-specific skill, say `Sonnet` or `Opus` and let the harness
   select the installed version. A shared skill names no model.
5. Validate the skill with the available skill validator and test any scripts.
6. Commit only the skill files and related Claude configuration intended by the
   task.

Use Sonnet with light thinking for mechanical scaffolding once the parent has
fixed the skill's design and constraints. Use higher thinking only when the
delegated work itself requires judgment.
