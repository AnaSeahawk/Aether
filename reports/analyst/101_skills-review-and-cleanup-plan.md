# 101. Skills Review and Cleanup Plan

**Date:** 2026-09-28  
**Agent:** Claude Code (Opus 5.5)  
**Session topic:** Read-only review of all fifteen skills, the Water of Life originals folder, and an ordered cleanup plan

---

## Purpose

Report 100 closed the four-phase roadmap from Report 096. This report is a
fresh read of every skill as it stands a week later: what works, where skills
contradict each other or the repo contract, and what to do about it. It also
records one change already made this session: a private folder for Water of
Life originals.

This is a public-safe report. Private surfaces are named by path only.

---

## Inventory

Fifteen skills, about 2,700 lines in total. None is overlong; the largest is
`solar-journal` (316 lines plus two reference files).

| Group | Skills | Condition |
|---|---|---|
| Roles | researcher, writer, curator, analyst | Sound; ownership boundaries agree |
| Cross-role | prose, sensitive-content, passwords | Sound; `passwords` is especially rigorous |
| Tools | audio-transcription, video, phoenix-calculator | Sound; each has a runnable script |
| Projects | water-of-life, solar-journal | Detailed, current, carry many settled decisions |
| Harness | remember, skills | Separate Claude and Codex versions, as intended |

Canonical files live in `.agents/skills/`. Thirteen are symlinked into
`.claude/skills/`; `remember` and `skills` have separate Claude versions.

## What works

- Every path the skills reference exists, apart from the originals folder
  (now created) and the private continuity folder
  `the-vessel/90-ops/agent-reports/`, which is created on first use.
- Privacy, consent, and publication-approval rules agree across `AGENTS.md`,
  `curator`, `sensitive-content`, and `water-of-life`, including the Water of
  Life post-publication deletion rule.
- The pramāṇa vocabulary from Report 100 has propagated everywhere.
- Anno Mundi arithmetic and the Aries-ingress year boundary agree between
  `solar-journal` and `phoenix-calculator`.

---

## Findings

### 1. The skills disagree on where a new skill goes

- `.agents/skills/README.md`: write the canonical skill in `.agents/skills/`,
  then symlink it into `.claude/skills/`.
- Claude `skills` skill: create each skill at `.claude/skills/<name>/`.
- Codex `skills` skill: calls `.agents/skills/` "the Codex skill tree" and says
  to keep model names Codex-specific there. That tree is also the shared
  source Claude reads through thirteen symlinks.

An agent that follows its own `skills` skill can put Codex-only content into
a shared skill, or duplicate a skill that should be a symlink. This is the
main governance gap.

### 2. Harness-specific content inside shared (symlinked) skills

`CLAUDE.md` allows a symlink only when the content contains no
harness-specific model, tool, path, or behavior.

- `solar-journal` names a Claude artifact URL and the artifact runtime's `db`
  capability.
- `phoenix-calculator` names parameters of one specific calendar connector
  (`self_attendance`, `add_google_meet`).
- `audio-transcription` contains a Codex UI profile (`agents/openai.yaml`).
  This one is harmless; Claude ignores it.

### 3. Prose rules and the Solar Journal aphorisms conflict

`prose` says to delete negative-contrast constructions ("X is not Y — it is
Z") on sight. `solar-journal` says "Don't define it by what it isn't." Yet
its fixed list of aphorisms includes "The clock is not wrong. It is simply
not the only authority." and "This is not a system to follow. It is an
orientation." An agent cannot follow all three rules at once.

### 4. Degree notation is only half-specified

`phoenix-calculator` distinguishes ordinal `º` (1-based: `10º Scorpio`) from
cardinal `°` (0-based: `9°52′ Scorpio`). `solar-journal` says "there is no
0°" and writes its 1–30 ordinal ranges with `°`, without naming the
distinction. That invites off-by-one errors on journal pages.

The user-level `/frontmatter` command (`~/.claude/commands/frontmatter.md`,
outside this repo) formats the ordinal sun degree with `°`.

### 5. The `/frontmatter` command is out of date

- It emits `type:` and `date:` but not `status` or `claim_tier`, which
  `curator` requires on every content file.
- It tells the agent to verify the moon at astro.com, which `AGENTS.md` says
  is not worth session time.
- It has no YAML header, so its listed description is its first line of
  instructions.

### 6. The `video` skill contradicts itself

Its introduction calls hosted transcription an optional choice over the
offline transcriber. Its body, and `audio-transcription`, make hosted the
default and offline available only on Ana's explicit request.

### 7. Stale statements

- `curator` and `AGENTS.md` §Sensitive Content still describe moving
  sensitive material to a private repo as "intended". The Vessel is already a
  live private repo.
- `AGENTS.md` §Content Architecture maps the website to "Four Pillars";
  `curator` says not to rely on that naming.
- The skills README describes `remember` as "persisting or recalling
  information across sessions". It only recovers a prior thread.
- `video` points to a hardware-cut script kept in a past session's
  temporary folder. That folder is gone, and the method exists only as a
  description.

### 8. Minor

- `writer` starts every new file at `visibility: private`; `video` creates
  archive entries at `visibility: community`.
- `AGENTS.md` §Skill Loading omits `solar-journal`, `phoenix-calculator`,
  `remember`, and `skills`.

### 9. Collaborator names in public skills

Two skills include real collaborators' names as worked examples: a
transcription prompt in `audio-transcription` and a past edit in `video`.
Aether is public, and Water Magicians material is consent-gated.

---

## Water of Life originals — done this session

The four observations published 2026-08-31 to 2026-09-01 (001–004) had their
raw submissions deleted without an original being kept. From now on, every
original is kept.

Created `Components/the-vessel/80-archive-raw/water-of-life/README.md` in the
private Vessel. It defines:

- naming that matches the published observation (`YYYYMMDD-NNN-original.md`,
  plus `-transcript` for interviews);
- the order of operations: the original is saved and pushed before the raw
  Formspree or email copy is deleted;
- that an original is never deleted from this folder;
- that 001–004 have no original, and their published versions are the only
  record.

Interpretation recorded: deleting raw submissions from Formspree and email
continues, as the public privacy page commits. What changes is that an
original is always kept in the Vessel first. If Ana meant to stop the
Formspree deletion as well, the privacy page must change too.

---

## Cleanup plan

Small steps, one commit and push per step.

**Step 1 — Water of Life skill.** In the form and interview workflows, make
"original saved and pushed" an explicit precondition for deleting the raw
copy. Note that 001–004 have no original.

**Step 2 — Skill placement rule.** Rewrite the README and both `skills` skills
around one rule: shared skills live in `.agents/skills/` with a symlink from
`.claude/skills/`; a skill that needs harness-specific content gets separate
files in each tree. The Codex `skills` skill stops calling the shared tree
Codex-only.

**Step 3 — Remove harness specifics from shared skills.** Move the artifact
URL and `db` note out of `solar-journal` (to the product repo or a
Claude-only note), and describe the Phoenix calendar requirements in plain
terms (no attendees, no video link, marked free) rather than connector
parameters.

**Step 4 — Notation.** Add the ordinal/cardinal distinction to
`solar-journal` and use `º` in its degree key. Rewrite `/frontmatter` to
emit `status`, `visibility`, and `claim_tier`, to use `º`, to drop the
astro.com instruction, and to have a proper header.

**Step 5 — Stale and contradictory text.** Fix the `video` introduction, the
"intended migration" wording in `curator` and `AGENTS.md`, the Four Pillars
section, the `remember` README line, the `writer`/`video` visibility
mismatch, and the §Skill Loading list.

**Step 6 — Decisions below, applied once Ana chooses.**

## Decisions for Ana

1. **Aphorisms vs. prose rule.** Either name the established aphorisms as a
   deliberate exception to the negative-contrast rule, or rewrite the two
   that use it. Recommendation: keep them as a named exception; they are
   settled language.
2. **Pramāṇa glosses.** In the Caraka Saṃhitā, *anumāna* is usually rendered
   "inference" and *yukti* as reasoning that joins several factors. The repo
   glosses them "reasoned together" and "applied framework". If that is a
   deliberate house meaning, one sentence in `curator` saying so would stop a
   future agent from "correcting" it. Not verified against the Sharma
   translation.
3. **Collaborator names.** Replace them with neutral placeholders in both
   skills. Recommendation: yes.
4. **Lost hardware-cut script.** Rebuild it as a `mother_spirit_video`
   command, or remove the reference.

---

## State at handoff

- Created: the Vessel originals README (private repo) and this report.
- No skill file has been edited yet; Steps 1–6 are pending.
