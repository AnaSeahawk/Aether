# Aether Skills

Canonical skill files live here in `.agents/skills/<name>/SKILL.md`.
Both Claude Code and Codex discover them automatically.

Skills are part of the archive's ecosystem: they follow "The Archive Is an
Ecosystem" (`Components/the-vessel/in-development/living-design/the-archive-is-an-ecosystem.md`)
— structure follows observation, and nothing is deleted; it is composted.

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

| Role | Use when | Skill | Status | Lineage | Last tended |
|---|---|---|---|---|---|
| `researcher` | source research, bibliography, book acquisition | `.agents/skills/researcher/SKILL.md` | active | original | 2026-08-09 |
| `writer` | drafting or revising prose | `.agents/skills/writer/SKILL.md` | active | original | 2026-09-21 |
| `curator` | website structure, frontmatter, review/publish workflow | `.agents/skills/curator/SKILL.md` | active | original | 2026-10-08 |
| `analyst` | reports, synthesis, continuity, audits | `.agents/skills/analyst/SKILL.md` | active | original | 2026-09-19 |

## Cross-role skills

Load these only when triggered:

| Skill | Use when | Status | Lineage | Last tended |
|---|---|---|---|---|
| `prose` | drafting, editing, reviewing, or evaluating writing | active | original | 2026-09-30 |
| `sensitive-content` | touching private, operational, health-adjacent, collaboration-private, or publishing-sensitive material | active | original | 2026-09-20 |
| `passwords` | any task involving passwords, API tokens, or credentials (`gopass`) | active | original | 2026-09-19 |

## Task skills

Capability workflows any role may load when the task involves that tooling:

| Skill | Use when | Status | Lineage | Last tended |
|---|---|---|---|---|
| `audio-transcription` | creating a timed transcript from existing audio/video | active | original | 2026-09-28 |
| `video` | turning a recording into cleaned video, a transcript, and publishing drafts | active | original | 2026-09-28 |
| `water-of-life` | intake, processing, and stewardship for The Water of Life observational archive | active | original | 2026-09-28 |
| `solar-journal` | Solar Journal entries, AM dating, and Living Year design | active | original | 2026-09-28 |
| `phoenix-calculator` | Phoenix zodiacal point calculation and AM year assignment | active | original | 2026-09-28 |
| `stt-interpreter` | decoding phonetic near-misses in dictated prompts | active | adapted from LiGoldragon/primary stt-interpreter | 2026-10-08 |
| `frontmatter` | generating content frontmatter with Sun position, status, visibility, claim_tier | active | adapted from `~/.claude/commands/frontmatter.md` | 2026-10-08 |

## Harness skills

These have separate implementations per harness (Claude Code vs Codex) because
they contain harness-specific model, tool, or runtime guidance. They are not
symlinked.

| Skill | Use when | Status | Lineage | Last tended |
|---|---|---|---|---|
| `remember` | recovering working context from a prior thread or session before continuing it | active | split from a shared skill (2026-09-06, "separate Codex and Claude skill surfaces") | Codex 2026-10-08 · Claude 2026-10-07 |
| `skills` | working on the skill system itself | active | split from a shared skill (2026-09-06, "separate Codex and Claude skill surfaces") | Codex 2026-09-28 · Claude 2026-09-28 |

## Compost

When a skill is retired, it is recorded here rather than deleted: its name,
the date it was composted, why, what replaced it, and the path to its last
living version in git history (e.g. a commit hash or tag), so the lineage
stays traceable.

| Composted | Date | Why | What grew from it |
|---|---|---|---|
| `frontmatter` personal command (`~/.claude/commands/frontmatter.md`, outside the repo) | 2026-10-08 | Lived on one machine only; invisible to Codex and to the registry | Shared skill `.agents/skills/frontmatter/` (commit a8d73a8), identical instructions |

## Seasonal review

The skill tree is walked each solstice and equinox, alongside the rest of the
archive. What recurred is named, what no longer serves moves to Compost, and
what waits at the edges is left to grow. Next review: winter solstice,
around 2026-12-21.

## See also

- `AGENTS.md` — authoritative repo contract
- `protocols/orchestration.md` — claim/release protocol
- `soul.md` — voice, themes, and boundaries
- `Components/the-vessel/in-development/living-design/the-archive-is-an-ecosystem.md` — the foundation principle this file follows
