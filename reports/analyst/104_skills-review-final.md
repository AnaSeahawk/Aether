# 104. Skills Review and Cleanup — Final

**Date:** 2026-09-29  
**Agent:** Claude Code (Opus 5.5)  
**Session topic:** Review of all fifteen skills, the Water of Life originals folder, cleanup completed, all decisions closed

Replaces Reports 101–103, which recorded earlier states of the same
work.

---

## Purpose

Report 100 closed the roadmap from Report 096. This session reread every
skill, found where skills contradict each other or the repo contract, and
fixed everything. Ana's four decisions were then applied. Nothing from this
review remains open.

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

## Decisions (closed)

| Decision | Ana's answer | Applied |
|---|---|---|
| Solar Journal aphorisms vs. `prose` negative-contrast rule | Keep the aphorisms | Named as a deliberate exception in `prose` and `solar-journal` (`f707711`) |
| Pramāṇa glosses for *anumāna* and *yukti* | Intentional house meanings | `curator` says so and forbids "correcting" them (`f707711`) |
| Collaborator names in public skills | Fiona Gardner has consented and is part of the project; keep her name | Kept in the `audio-transcription` example prompt, now described as recurring names (this commit). The `video` mention of another collaborator went with the lost-script reference |
| Lost hardware-cut script | Not needed | Reference removed from `video`; the method description stays (`f707711`) |

## Follow-up completed

**Website `sun:` values.** All 48 website files with a `sun:` value were
checked against Swiss Ephemeris before editing. Only 2 were clearly ordinal;
16 were whole cardinal degrees, 29 were ambiguous because the Sun crossed a
degree boundary on that date, and 1 named the wrong sign. With Ana's
approval, every value was recalculated as the ordinal degree at noon
Europe/Madrid on the file's date: 27 numbers changed, 21 kept their number
and gained `º`. The rule is now recorded in `curator`. Website `aa24098`,
Aether `dff38e3`.

The three `moon:` values were left unchanged: the Moon moves about 13° a
day, so a date alone cannot verify them.

**Solar Journal artboard.** `DailyEntry.dc.html` renamed `EntryPage.dc.html`,
with the canvas title and README updated (solar-journal `0a4dc47`). The Sep 4
design-canvas snapshot in `published/solar-journal.html` still carries the
old name as history.
