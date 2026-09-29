---
name: skills
description: Create, edit, move, remove, and validate Codex skills in the repository's `.agents/skills/` tree, which Codex shares with Claude.
---

# Skill — skills

Maintain Codex skills as self-contained packages under `.agents/skills/`.

## Surface boundary

`.agents/skills/` is Codex's skill tree and also the canonical copy of every
skill Aether shares with Claude. Claude reads a shared skill through a symlink
at `.claude/skills/<name>`.

- **Shared skill** — the content has no harness-specific model, tool, path, or
  behavior. Write it at `.agents/skills/<name>/SKILL.md` and symlink it:
  `ln -sfn "../../.agents/skills/<name>" ".claude/skills/<name>"`.
- **Codex-specific skill** — the content names Codex models, Codex tools, or
  Codex runtime behavior. Write it at `.agents/skills/<name>/SKILL.md` with no
  symlink. If Claude needs the same skill, it gets its own version in
  `.claude/skills/<name>/`.

Check `ls -l .claude/skills/<name>` before editing: if it is a symlink, Claude
reads your change. Before adding Codex-specific content to a symlinked skill,
split it into two independent files first. List every skill in
`.agents/skills/README.md`.

## Creation workflow

1. Choose a short lowercase hyphenated name, and decide shared or
   Codex-specific.
2. Write discriminating YAML frontmatter with `name` and `description`.
3. Keep essential decisions and workflow in `SKILL.md`; add scripts,
   references, or assets only when they have a concrete repeated use.
4. Name Codex models and runtime behavior only in a Codex-specific skill. A
   shared skill names no model.
5. Validate the skill with the available skill validator and test any scripts.
6. Commit only the skill files and related Codex configuration intended by the
   task.

For lightweight reusable workers, store a real TOML profile in
`.codex/agents/`; do not use a symlink. Select its model and reasoning effort
explicitly.
