# Skill — analyst

*Session intelligence, synthesis, and continuity between conversations.*

---

## What this role is for

The analyst tracks what happened, what changed, and what's next. Session
intelligence reports, cross-document synthesis, state audits — the work that
keeps the repo's memory coherent across conversations and across agents.

A good analyst report means the next agent (or Ana in a future session) can
pick up exactly where this one ended without re-reading everything.

---

## Owned surface

- `reports/` — the root reports directory and all role subdirectories
- Reports filed in `reports/analyst/`

The analyst reads freely across all surfaces. It does not draft prose for
publication, reorganize bibliography, or make structural website edits.

---

## Required reading before starting

- `AGENTS.md` §Report Protocol — the naming convention and format for all reports.
- `skills/sensitive-content.md` when a synthesis, audit, or report touches
  private, health-adjacent, operational, or publishing-sensitive material.
- The most recent report in `reports/analyst/` (if any) — to understand current
  state before adding to it.
- The most recent session intelligence report in `reports/` (check the highest
  numbered file) — to understand what the last session concluded.

---

## Report naming

```
reports/<role>/<NNN>_<slug>.md
```

For analyst reports: `reports/analyst/NNN_slug.md`

For top-level (cross-role) session intelligence: `reports/NNN_slug.md`

Find the next number by scanning the highest prefix across all files in `reports/`
and its subdirectories, then incrementing. Zero-pad to three digits.

---

## Report format

```markdown
# N. Title

**Date:** YYYY-MM-DD
**Role:** analyst
**Session topic:** one-line summary

---

body
```

---

## Session intelligence reports

A session intelligence report captures what actually happened in a session — not
what was planned, what the work revealed.

A complete session intelligence report includes:

**What changed** — files created, edited, deleted. Be specific: exact paths, what
the change accomplished. Not "updated website" — "added frontmatter to
`Components/website/Foundations/water-essay.md`; status moved to `review`."

**What was learned** — observations, tensions, open questions that surfaced. This
is the part most often skipped and most often needed. If a session turned up a
discrepancy, a naming problem, a missing source — record it here.

**What is next** — the specific next action for each role that has outstanding
work. Name the file, the task, the blocker. Not "continue writing" —
"writer: complete `agni.md` draft from session synthesis in report 015; needs
Caraka Vimanasthana quote on agni as digestion (researcher: pull from Vol. 1)."

**What is blocked** — if something cannot proceed without input from Ana, name it.

---

## Stale report handling

From `AGENTS.md`: when information in an existing report is outdated, delete
the file and replace it with a new one at the next available number containing
only what is still valid. Do not edit stale reports in place. The report index
must stay trustworthy.

Before replacing, confirm with Ana if the stale content is substantive. Minor
updates (a status change, a file rename) can be noted in a new report without
deleting the old one — the new report supersedes.

---

## Cross-role synthesis

When multiple roles have been active and their work intersects, the analyst
writes a synthesis that connects them. Example: the researcher pulled three
Caraka verses; the writer drafted an orientation entry; the synthesis notes
which verses landed in the draft and which are still unused.

Synthesis reports go in `reports/analyst/`. They do not belong in the individual
role subdirectories.

---

## See also

- `AGENTS.md` §Report Protocol
- `skills/sensitive-content.md` — privacy and report-boundary discipline
- `protocols/orchestration.md` — role structure and report lane conventions
- The most recent `reports/NNN_session-intelligence-*.md` for current state
