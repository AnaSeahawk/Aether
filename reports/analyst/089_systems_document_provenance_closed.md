# 89. Systems Document Provenance — Corrected And Closed

**Date:** 2026-08-05
**Role:** analyst
**Session topic:** Closing the systems-document correction thread; replacing report 074 with only what remains valid.

---

## Replacement Note

This report replaces `reports/analyst/074_megan_macdonald_systems_hypothesis_corrected_integration.md`, deleted under the stale-report rule. Report 074 had itself replaced 073.

Two things made 074 stale:

1. **It carried named third parties and their personal health accounts in a public repo.** `AnaSeahawk/Aether` is public. Report 074 named two private individuals and stated one of their practice duration and health history. That material was never ours to publish, and it was published by inattention rather than by decision.
2. **It was built on an ownership/attribution frame that has been retired.** See [Scope correction](#scope-correction) below.

A single line in `reports/analyst/075_full_archive_audit_current_intention_flow.md` carried the same names. Those names have been removed from that line in place. (Report 075 was subsequently deleted in full and replaced by `reports/analyst/092_june_audit_superseded.md`.) That is a deliberate exception to the no-in-place-edit rule — the rule exists so the report index stays trustworthy against *stale claims*, and it should not require leaving a third party's health history published while a replacement report is written.

**What this does not do:** the repository's history is public and already pushed. Removing this material from the current tree stops it reaching future readers of these files; it does not scrub it from git history. Rewriting pushed public history is possible but destructive and is not recommended here, consistent with the same call made in report 087 about raw media.

## What The Source Document Actually Is

`Components/the-vessel/80-archive-raw/2026-06-26-megan-macdonald-integrated-systems-hypothesis.docx`
SHA-256: `fe2129ba7d21612dc8782d014ea3cc9175dd1569eea68ec5e9478e76859e9b4c`

It was AI-expanded from **slide screenshots and Ana's own notes from attending**. No recording or transcript of the presentation existed, and none was given to the AI.

So it is an expansion of Ana's notes — one of Ana's working artifacts. It is not a transcript, not an authored article, and not a record of anyone's exact language. Its Western-medical argumentative style is a product of that expansion.

The file stays in `80-archive-raw/` as provenance. No public archive entry exists or is planned.

One factual conflation in it — a long-practice example attached to the wrong person — was a note-taking error while attending, and has been corrected. The correction is recorded privately in `Components/the-vessel/35-water-magicians-private/megan-feedback-source-correction.md`. It was an isolated incident and is closed.

## <a id="scope-correction"></a>Scope Correction

Reports 073, 074, and 075 built a large attribution apparatus around that one small correction. That apparatus is retired. Recorded here so the report trail does not keep propagating it:

- **No one is claiming or assigning ownership of ideas.** There is no ownership question to adjudicate, and no one involved wants one.
- The work is **building shared vocabulary for Sovereign Biophysics**, not partitioning intellectual property. Deciding who owns which idea inside a collaboration is not possible and is not the goal.
- **Collaboration is mutually influencing by nature**, the AI included. That is accepted, not a problem to be contained.

What is **not** retired, and did not come from that apparatus:

- **Review continues, and the people whose work generates the language take part in editing it.** That is a requirement of getting the work right.
- **Named individuals' personal and health accounts stay private absent their own consent.** This is a privacy boundary about people outside the collaboration. It is unrelated to ownership and is the boundary report 074 itself breached.
- **Synthesis gets labelled as synthesis.** Not to assign credit — so that a reader can tell what was observed from what was generated.

## What Remains Valid: The Five-System Overlay

The genuinely useful content of 074 was the mapping between the document's five-system structure and Aether's own observation fields. It stands, and is carried forward here intact.

| System frame | Aether observation field | Existing archive threads | Use |
|---|---|---|---|
| Inflammatory regulation | Skin changes, clearing phase, dietary simplification, old baseline clearing through fluids, dreams, and digestion | `clearing-nourishment`, `topical-practice`, `current-state` | Useful as a grouping lens. Keep "inflammation" as hypothesis unless biomarkers are measured. |
| Lymphatic and mucosal clearance | Tissue softening, fluidity, mucus/sinus/gut references, mucosal pathways, topical and intimate body records | `restoration-of-continuity`, `topical-practice`, `rasa-qi-flow` | Strong fit with "restoration of continuity." Keep operational mucosal detail private. |
| Digestive and metabolic regulation | Agni, dietary baseline, source-state variation, stool density, wheat/ghee clearing, food as grounding, fluid as record | `clearing-nourishment`, `source-state`, `living-record` | Strong fit. This is where Aether already has source-state and diet/output observations. |
| Endocrine regulation | Menstrual/artava line, serum/retentate hormone question, cycle timing, HPG-axis hypothesis, women's witness field | `menstrual-artava`, `three-waters`, `topical-practice` | Useful but fraction-specific. Whole filtrate, distilled fractions, and serum must not be collapsed. |
| Nervous system and energy | Rasa/qì flow, dream return after cannabis removal, movement, grounding, HRV as possible future metric | `rasa-qi-flow`, `restoration-of-continuity`, `living-record` | Strong bridge if framed as regulation and participation, not proof of mechanism. |

The best sentence-level bridge:

> The AI-expanded systems document can be treated as a hypothesis map: it helps group Aether's observations by regulatory system, while Aether's own archive preserves the measured and lived record that the map must remain accountable to.

## Language Guardrails That Still Stand

These predate the correction thread and are independently sound:

- Avoid "proves," "disease reversal," "personalized vaccine," "non-placebo," and direct equivalence between clinical plasma exchange and endogenous practice.
- Hormone language needs fraction discipline. Aether's biochemistry note keeps steroid hormones primarily with the retentate/serum question, not the distilled spirit/essence.
- The five-system map is an interpretive overlay. Aether's own measured and lived archive stays the source of record.
- It should not enter the canonical Sovereign Biophysics reader path.

## What Changed In This Pass

- Deleted `reports/analyst/074_megan_macdonald_systems_hypothesis_corrected_integration.md`.
- Created this report.
- Removed named third parties and health details from `reports/analyst/075_full_archive_audit_current_intention_flow.md` (one line).
- Repointed the two references to the deleted 074 (in `075` and `077`) at this report, so no report links to a file that no longer exists.
- Rewrote `Components/the-vessel/35-water-magicians-private/megan-feedback-source-correction.md` down to provenance plus the factual fix; filename kept so existing links stay live.
- Removed the note from the "ready for named review" list on `review-status-board.md` and from `collaborator-read-path.md`; it blocks nothing and owes no review.
- Updated pointers in the Water Magicians `README.md`, `source-packet-board.md`, `july-large-call-harvest-scan.md`, and `QUEUE.md`.

## Status

**Closed.** This thread needs no further reports. The durable content is the five-system overlay above and the provenance note in the private lane.

The one open item is not analytic: report 077 (line 415) and report 079 (lines 141, 444) still reference the retired attribution framing. Both are already stale-report candidates for other reasons — 079 was flagged in report 087 and awaits Ana's confirmation. Whenever they are replaced, that framing should not carry forward.
