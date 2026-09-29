# Aether Skills

Canonical skill files live here in `.agents/skills/<name>/SKILL.md`.
Both Claude Code and Codex discover them automatically.

## How it works

```
.agents/skills/<name>/SKILL.md     ← canonical source (Codex reads directly)
.claude/skills/<name>              ← symlink → ../../.agents/skills/<name>
                                      (Claude Code reads via symlink)
```

Each `SKILL.md` has YAML frontmatter with `name` and `description`. The
description tells the harness when to load the skill automatically and
populates the `/` auto-complete in Claude Code.

**The rule:** a skill is symlinked only when its content has no
harness-specific model, tool, path, or behavior. A skill that needs any of
those has independent files in each tree that uses it. `remember` and `skills`
are the current examples.

Because Codex and Claude read the same file for every symlinked skill, check
`ls -l .claude/skills/<name>` before editing, and keep shared skills
harness-neutral.

## Adding a new skill

1. Decide: shared, or specific to one harness.
2. Shared: create `.agents/skills/<name>/SKILL.md` with frontmatter, then
   symlink: `ln -sfn "../../.agents/skills/<name>" ".claude/skills/<name>"`.
3. Harness-specific: create real files in that harness's tree
   (`.agents/skills/<name>/` for Codex, `.claude/skills/<name>/` for Claude),
   and a separate version in the other tree if it needs one.
4. Add a line to the table below.
5. If the skill should be mentioned in `AGENTS.md` §Skill Loading, add it there.

## Role skills

Read exactly one role skill before work begins:

| Role | Use when | Skill |
|---|---|---|
| `researcher` | source research, bibliography, book acquisition | `.agents/skills/researcher/SKILL.md` |
| `writer` | drafting or revising prose | `.agents/skills/writer/SKILL.md` |
| `curator` | website structure, frontmatter, review/publish workflow | `.agents/skills/curator/SKILL.md` |
| `analyst` | reports, synthesis, continuity, audits | `.agents/skills/analyst/SKILL.md` |

## Cross-role skills

Load these only when triggered:

| Skill | Use when |
|---|---|
| `prose` | drafting, editing, reviewing, or evaluating writing |
| `sensitive-content` | touching private, operational, health-adjacent, collaboration-private, or publishing-sensitive material |
| `passwords` | any task involving passwords, API tokens, or credentials (`gopass`) |

## Task skills

Capability workflows any role may load when the task involves that tooling:

| Skill | Use when |
|---|---|
| `audio-transcription` | creating a timed transcript from existing audio/video |
| `video` | turning a recording into cleaned video, a transcript, and publishing drafts |
| `water-of-life` | intake, processing, and stewardship for The Water of Life observational archive |
| `solar-journal` | Solar Journal entries, AM dating, and Living Year design |
| `phoenix-calculator` | Phoenix zodiacal point calculation and AM year assignment |

## Harness skills

These have separate implementations per harness (Claude Code vs Codex) because
they contain harness-specific model, tool, or runtime guidance. They are not
symlinked.

| Skill | Use when |
|---|---|
| `remember` | recovering working context from a prior thread or session before continuing it |
| `skills` | working on the skill system itself |

## See also

- `AGENTS.md` — authoritative repo contract
- `protocols/orchestration.md` — claim/release protocol
- `soul.md` — voice, themes, and boundaries
