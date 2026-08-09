---
name: analyst
description: Session intelligence, synthesis, continuity, and audits across conversations. Use for reports, state audits, cross-document synthesis, and session handovers.
---

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
- `.agents/skills/sensitive-content/SKILL.md` when a synthesis, audit, or report touches
  private, health-adjacent, operational, or publishing-sensitive material.
- The most recent report in `reports/analyst/` (if any) — to understand current
  state before adding to it.
- The most recent session intelligence report in `reports/` (check the highest
  numbered file) — to understand what the last session concluded.

---

## Report naming

Use the global zero-padded three-digit prefix convention described in
`AGENTS.md` §Report Protocol. Scan `reports/` and `reports/analyst/` for the
next available number.

Slug: lowercase, hyphen-separated, descriptive. Example:
`reports/analyst/078_password-skill-migration.md`.

---

## Context maintenance

When multiple reports in the same arc carry overlapping rules or findings:

1. Identify what is still load-bearing vs. what has been superseded.
2. Migrate durable rules into `AGENTS.md`, role skills, or `soul.md`.
3. Replace stale reports with new numbered reports per `AGENTS.md` stale-report
   handling.

Review by topic, not only chronologically. When a rule appears in three
reports, it probably belongs in a permanent guidance file.

---

## Handover discipline

When writing a report that will be the primary context for a future session:

- Preserve Ana's intent and useful context only.
- Exclude transcript chronology, resolved mistakes, generic advice, and
  restated rules the next agent will read from guidance files.
- Name live open decisions explicitly.

---

## See also

- `AGENTS.md` — the authoritative repo contract
- `.agents/skills/sensitive-content/SKILL.md` — privacy and publication boundaries
- `.agents/skills/prose/SKILL.md` — craft discipline for writing
- `protocols/orchestration.md` — claim/release flow
