# 102. Skills Review and Cleanup

**Date:** 2026-09-28  
**Agent:** Claude Code (Opus 5.5)  
**Session topic:** Review of all fifteen skills, the Water of Life originals folder, cleanup Steps 1–5 completed, four decisions open

Replaces Report 101, which recorded the review and plan before any fix was
made.

---

## Purpose

Report 100 closed the roadmap from Report 096. This session reread every
skill, found where skills contradict each other or the repo contract, and
fixed everything that did not need a decision from Ana. Four decisions remain
open.

This is a public-safe report. Private surfaces are named by path only.

---

## Inventory

Fifteen skills, about 2,700 lines in total. The largest is `solar-journal`
(316 lines plus two reference files).

| Group | Skills | Condition |
|---|---|---|
| Roles | researcher, writer, curator, analyst | Sound; ownership boundaries agree |
| Cross-role | prose, sensitive-content, passwords | Sound; `passwords` is especially rigorous |
| Tools | audio-transcription, video, phoenix-calculator | Sound; each has a runnable script |
| Projects | water-of-life, solar-journal | Detailed, current, carry many settled decisions |
| Harness | remember, skills | Separate Claude and Codex versions, as intended |

Canonical files live in `.agents/skills/`. Thirteen are symlinked into
`.claude/skills/`; `remember` and `skills` have separate Claude versions.

Already consistent before this session: privacy, consent, and approval rules
across `AGENTS.md`, `curator`, `sensitive-content`, and `water-of-life`; the
pramāṇa vocabulary; and Anno Mundi arithmetic between `solar-journal` and
`phoenix-calculator`.

---

## Completed

| Step | Change | Commit |
|---|---|---|
| — | Private originals folder created: `the-vessel/80-archive-raw/water-of-life/README.md` | Vessel `b26d530` |
| 1 | `water-of-life`: raw submission or recording is deleted only after its original is pushed to the Vessel; 001–004 recorded as having no original | `30b4528` |
| 2 | One placement rule in the skills README and both `skills` skills: shared skills live in `.agents/skills/` with a `.claude/skills/` symlink; harness-specific skills get independent files per tree; check for a symlink before editing | `f39d34b` |
| 3 | Claude artifact URL and runtime-storage note removed from `solar-journal`; Phoenix calendar requirements written in plain terms, not connector parameters | `da1c94a` |
| 4 | `solar-journal` defines ordinal `º` vs cardinal `°` and uses `º` in its degree key; the reference file's worked example now uses the first-degree method it prescribes | `f8fbb19` |
| 4 | User-level `/frontmatter` command (outside the repo) rewritten: emits `status`, `visibility`, `claim_tier`; uses `º`; no astro.com lookup; has a header | not in git |
| 5 | `video` intro agrees that hosted transcription is the default; `curator` and `AGENTS.md` state the Vessel is already private; `AGENTS.md` points to `ARCHITECTURE.md` instead of "Four Pillars" and lists all loadable skills; README `remember` line corrected | `be70289` |
| 5 | `tools/mother_spirit_video` archive entries now start `visibility: private`, `claim_tier: anumana` (was `community` and the pre-pramāṇa `personal-account`) | `be70289` |

### Water of Life originals

The four observations published 2026-08-31 to 2026-09-01 (001–004) had their
raw submissions deleted without an original kept. From now on every original
is kept in the Vessel, pushed before any raw copy is deleted, and never
deleted from there.

Deleting raw copies from Formspree and email continues, as the public privacy
page commits. If Ana wants to stop that as well, the privacy page must change
first.

---

## Decisions for Ana

1. **Aphorisms vs. prose rule.** `prose` deletes negative-contrast
   constructions on sight; `solar-journal` says not to define the journal by
   what it isn't; two of its fixed aphorisms do exactly that ("The clock is
   not wrong…", "This is not a system to follow…"). Either name the aphorisms
   as a deliberate exception, or rewrite those two. Recommendation: keep them
   as a named exception.
2. **Pramāṇa glosses.** In the Caraka Saṃhitā, *anumāna* is usually rendered
   "inference" and *yukti* as reasoning that joins several factors. The repo
   glosses them "reasoned together" and "applied framework". If that is a
   deliberate house meaning, one sentence in `curator` saying so would stop a
   future agent from "correcting" it. Not verified against the Sharma
   translation.
3. **Collaborator names.** Two public skills (`audio-transcription`, `video`)
   use real collaborators' names as examples. Recommendation: replace them
   with neutral placeholders.
4. **Lost hardware-cut script.** `video` describes a GPU segment-cut method
   whose script lived in a past session's temporary folder and is gone.
   Rebuild it as a `mother_spirit_video` command, or remove the reference.

## Noticed, not changed

- About forty website content files carry `sun:` values written with `°`
  (e.g. `sun: 18° Sagittarius`). By the new convention these are ordinal and
  would take `º`. Changing them is a content edit in the website submodule and
  was left alone.
- The Solar Journal product repo has an artboard named `DailyEntry.dc.html`,
  and its README lists "Daily entry pages". The skill says the body pages are
  not daily-entry pages and not to name a template `daily-entry`.
