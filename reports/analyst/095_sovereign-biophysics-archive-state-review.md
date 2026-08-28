# 95. Sovereign Biophysics Archive State Review

**Date:** 2026-08-28
**Agent:** Claude (Sonnet)
**Session topic:** Structural and metadata review of the Sovereign Biophysics archive

---

## Scope and method

This is a structural/state review, not a content or prose review. It covers
organization, frontmatter metadata, cross-reference integrity, and continuity
against the last SB-specific review (`reports/060_sovereign-biophysics-drive-draft-placement-review.md`,
2026-07-27). Per `.agents/skills/sensitive-content/SKILL.md`, body text was
not read beyond what filenames, metadata, and index entries already
answered. No sensitive passages are quoted here.

Reviewed: `Components/website/sovereign-biophysics-distillation/` (86 content
files across 7 layers, plus its `README.md` frontispiece), cross-checked
against `Components/website/REVIEW_QUEUE.md` and `PUBLISH_CHECKLIST.md`.

## Archive shape

| Layer | Files |
|---|---|
| 00-orientation | 37 |
| 10-method | 16 |
| 20-experiments | 10 |
| 30-analysis | 11 |
| 40-synthesis | 4 |
| 50-presentations | 1 |
| Dictionary | 7 |

The README's reading-path spine (11 sequenced entries, Manifesto through
"Current State of the Work — June 2026") links only to files that exist.
Every file on disk is referenced somewhere in `README.md` — no orphaned
content found.

## Metadata tallies

**status:** reviewed 44, draft 37, review 2, approved 2, active 1
**visibility:** public 60, community 25, private 1
**claim_tier:** 15 distinct values in use, led by interpretation (18),
practice (15), orientation (12), synthesis (11), preliminary-observation (7)

## Findings

1. **Status vocabulary has drifted from the AGENTS.md spec.** `AGENTS.md`
   defines `status` as draft/review/approved/published. In practice the
   archive uses `reviewed` (past tense, 44 files) almost everywhere instead
   of `review`, `published` never appears, and one file
   (`10-method/sediment-field-guide.md`) uses the one-off value `active`.
   This is long-standing and consistent enough that it reads as the
   archive's real convention rather than a mistake — but it means
   `AGENTS.md` no longer describes actual practice. Worth reconciling one
   way or the other (update the spec, or normalize the outlier).

2. **`claim_tier` in file frontmatter does not use the Dictionary's own
   taxonomy.** `Dictionary/claim-tiers.md` defines six named tiers
   (`tier_0_poetic` through `tier_5_documented_external_record`) as an
   evidentiary-strength scale. No file in the archive uses any of those six
   names. Instead, frontmatter uses a free vocabulary of 15 values
   (interpretation, practice, orientation, synthesis, observation, hypothesis,
   personal-account, evidential, etc.) that mixes content-type labels
   (practice, orientation, synthesis) with rough confidence labels
   (observation, hypothesis, interpretation) — closer to the looser
   language in `PUBLISH_CHECKLIST.md` item 2 ("observation/interpretation/
   hypothesis") than to the Dictionary page a reader is pointed to for this
   exact field. The Dictionary currently describes a system that isn't
   applied anywhere. Either the Dictionary should be rewritten to document
   the vocabulary actually in use, or a pass should retag files against the
   six-tier scale.

3. **One visibility/queue mismatch:** `00-orientation/the-measure-of-your-fire.md`
   carries `visibility: private` in its own frontmatter, but
   `REVIEW_QUEUE.md` lists it under "Core Public Orientation" as "new draft
   (2026-07-28), awaiting Ana's review" — i.e., the queue is tracking it on
   the public track while the file itself is still marked private. Per
   `AGENTS.md`, frontmatter isn't access control, so this isn't a leak by
   itself, but it's worth flagging before the file moves further: either the
   frontmatter should be updated to match its actual review track, or the
   queue entry should reflect that it's still private-only.

4. **Continuity from report 060 — resolved.** The two Drive drafts that
   060 reviewed for placement (`solar-distillation-urine-report.md`,
   `the-fertilizer-we-flush.md`, both then `in-development/`, `status:
   draft`, `visibility: private`) are no longer in `in-development/`. They
   now exist as `30-analysis/analysis-solar-distillation-resource-recovery.md`
   and `30-analysis/analysis-the-fertilizer-we-flush.md`, both carrying
   `status: review`, `visibility: public`, `claim_tier: evidential`, and
   both are indexed in the README's Analysis section and in
   `REVIEW_QUEUE.md`. This matches 060's placement recommendation (Analysis
   layer, not Orientation or Method) and its assessment that the solar
   report was "closest to ready." The `in-development/` folder itself no
   longer exists under the SB tree.

## Bottom line

The archive's index and reading path are internally consistent — nothing
orphaned, nothing broken. The open work is metadata hygiene, not structure:
reconcile the `status` vocabulary with `AGENTS.md`, decide what `claim_tier`
is actually supposed to encode and make the Dictionary match it, and clear
the one visibility/queue mismatch on `the-measure-of-your-fire.md` before it
moves further toward public.
