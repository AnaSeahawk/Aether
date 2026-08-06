# 90. Water Magicians — Lane Pointer

**Date:** 2026-08-06
**Role:** analyst
**Session topic:** Replacement for stale report 056; corrected paths and a deliberate narrowing of what this public report carries.

---

## Replacement Note

This report replaces `reports/056_water-magicians-report.md`, deleted under the stale-report rule. Report 056 was flagged in the August 4 link integrity audit (report 088, item 2) for two dead relative links. Reviewing it turned up more than dead links.

Three things made it stale:

1. **Both link targets moved.** The lane was renamed from `35-collaboration-private/water-magicians/` to `35-water-magicians-private/`, and the living-journal template moved to a different lane entirely (`32-living-year-archive-participation-private/`). Four occurrences of the retired path, two of them live links.
2. **Its state description is five weeks out of date.** It described the lane as of July 1, before the source-packet board, review-status board, media consent log, harvest scan, and three further Telegram continuations existed. It also carried the attribution framing retired in report 089.
3. **It carried private working material in a public repo.** See below.

## Why This Replacement Is Short

Report 056 was a full lane description published to a public repository. It set out each collaborator's role and named strengths, the proposed donation support lane, the money boundary — income split three ways, whose platform income is untouched — thread-level signal counts from private Telegram analysis, and open questions including who holds funds and whether the other two are comfortable being named publicly.

None of that was cleared for public use. Report 056 said so itself, in its own closing section: *"Nothing in Water Magicians is cleared for public use by default… Any quote, paraphrase, public summary, support-page language, book use, or teaching use still needs review. This applies even to material cited in this report."* The report stated the boundary and then sat outside it.

This is the same class of problem as report 074 (see report 089): private lane detail reaching the public repo by inattention rather than by decision. It differs in one way that matters — 074 exposed people outside the collaboration, while 056 exposes the three collaborators' own working arrangements. That is less acute. It is still not public material, and two of the three people involved have not reviewed it.

So this replacement deliberately does **not** restate the lane's contents. Report 087 already set the right principle: lane detail belongs in the private boards and is referenced by path, not copied into public reports. What follows is a pointer.

**As with 074: this removes the material from the current tree, not from public git history.** Rewriting pushed public history is not recommended, consistent with report 087 and report 089.

## What The Lane Is

Water Magicians is a private, consent-led collaboration between three people, held inside the private `the-vessel` repository. Its working name is provisional. Nothing in it is cleared for public use by default.

## Where The Detail Actually Lives

All within `Components/the-vessel/35-water-magicians-private/` unless noted:

| For | See |
|---|---|
| Lane entry point and current map | `README.md` |
| What exists, what blocks it, what is next | `source-packet-board.md` |
| What is harvested and awaiting whose review | `review-status-board.md` |
| Consent and attribution boundaries | `consent-map.md` |
| Media clearance status | `media-consent-and-use-log.md` |
| Support-lane draft (previously linked from 056) | `collective-archive-support-path.md` |
| Living-journal template (previously linked from 056) | `../32-living-year-archive-participation-private/living-journal-participation-template.md` |
| Cross-lane state as of July 30 | `reports/analyst/087_archive_state_and_consolidation_july30.md` |

## What Still Holds From 056

Two things are worth carrying forward, both boundary statements rather than lane detail:

- The first shared product is the living source field itself — kept clean enough that later books, gatherings, images, and teachings can grow from it. Not the book, not a membership, not a public archive.
- Raw source stays raw. Transcripts are navigation aids. Reports are private synthesis. Public language is created only after review by the relevant person.

## Related Cleanup Still Open

Report 057 also references the retired `35-collaboration-private/` path. Reports 077 and 079 carry both the retired path and the retired attribution framing; 079 has been awaiting Ana's confirmation for delete-and-replace since report 087 flagged it on July 30.

The root-level reports `038`–`060` predate the June restructure generally, and report 087 recommended a cleanup pass over them. This report handles one of that set. The rest remain.
