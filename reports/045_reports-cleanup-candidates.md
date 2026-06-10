# 45. Reports Cleanup Candidates

**Date:** 2026-06-10
**Agent:** Codex / GPT-5
**Role:** analyst
**Session topic:** Review of `reports/` for stale, superseded, or low-value report files that can be deleted after Ana confirms.

---

## Scope

I reviewed all top-level reports currently present in `reports/` and the three researcher reports in `reports/researcher/`.

No reports were deleted in this pass. Ana asked for flags, not deletion. Also, the analyst skill says substantive stale deletion should be confirmed before replacing or removing historical reports.

## Index Facts

- Top-level numbered reports present: `001` through `044`, with gaps.
- Duplicate prefix: two `010_*` reports.
- Missing prefixes: `019` and `034`.
- Report `020` explicitly says it replaces stale report `019`.
- Report `036` explicitly says stale report `034_current-state-flow-readability-audit.md` was removed and replaced by `036`.
- No files exist yet under `reports/analyst/` besides `.gitkeep`.
- Researcher lane contains three reports, all still useful source work.

## Current-State Corrections

Report `043` is still the best recent full audit anchor, but several of its immediate findings have already moved:

- `sediment-field-guide.md` now has `claim_tier: observation` and visible boundary language.
- `the-map-and-the-cut.md` and `the-mother-wound.md` now use the corrected Dictionary tier order in YAML.
- Both of those hot pages also now have visible claim-posture blocks near the top.
- `Foundations/README.md` now links the actual three files and no longer uses stale date-prefixed filenames.
- `REVIEW_QUEUE.md` now declares itself a priority board, not a complete inventory.
- The June 4 fresh plasma experiment is now public, indexed, and listed in the SB README/review queue.
- The "first distillation from inside" piece now exists as report `044`; it is still a report draft, not yet a site file.

Still-live themes from `043`: source proximity on high-risk pages, method/protocol boundaries, operator accounts in experiment reports, run-sheet/calibration discipline, and careful public/private summary workflow.

## Clear Delete Candidates

These reports look safe to delete after Ana confirms, because their active value has been absorbed elsewhere or their live facts are now stale.

| Report | Why it can go | Current replacement / source of truth | Risk |
|---|---|---|---|
| `reports/002_living-loop-archive-audit.md` | Superseded by `003` and later audits. Its remaining astro lookup task is now obsolete under current AGENTS guidance: leave blank astro fields alone unless efficient tooling exists. | `reports/003_full-archive-audit.md`; current AGENTS instructions. | Low |
| `reports/005_sovereign-biophysics-audit.md` | Old 31-file SB inventory; counts, statuses, and action items are now outdated. | `reports/036_*`, `037_*`, `043_*`, and this report. | Low |
| `reports/007_immortal-sisters-content-draft.md` | Draft has been written into the site as `sun-bu-er-and-the-inner-furnace.md`, with later revisions. | `Components/website/sovereign-biophysics-distillation/00-orientation/sun-bu-er-and-the-inner-furnace.md` | Low |
| `reports/008_beauty-and-the-binding-content-draft.md` | Draft has been written into the site and revised. | `Components/website/sovereign-biophysics-distillation/00-orientation/beauty-and-the-binding.md` | Low |
| `reports/009_why-the-distillation-is-missing-content-draft.md` | Draft has been written into the site and expanded, including the later fourth-silence material. | `Components/website/sovereign-biophysics-distillation/00-orientation/why-the-distillation-is-missing.md` | Low |
| `reports/010_in-the-name-of-love-content-draft.md` | Draft has been written into the site and revised with clearer boundary language. | `Components/website/sovereign-biophysics-distillation/00-orientation/in-the-name-of-love.md` | Low |
| `reports/011_architectural-audit-sb-yrf-007-010.md` | Its immediate placement work is done. Remaining YRF/bridge concerns are better preserved in `013`, `014`, and `035`. | Site orientation files; `reports/013_*`, `014_*`, `035_*`. | Low to medium |
| `reports/016_archive-voice-audit.md` | The audit's concrete fixes were implemented and recorded in `017`. | `reports/017_sb-forward-audit.md` | Low |
| `reports/022_aether-archive-state-of-repo.md` | Whole-repo state is stale: review queue, links, and Vessel structure have changed substantially. | `reports/031_*`, `033_*`, `036_*`, `043_*`. | Low |
| `reports/030_sovereign-biophysics-full-archive-audit-may2026.md` | Old 68-file archive audit; inventory and several open items are outdated. | `reports/036_*`, `037_*`, `039_*`, `043_*`. | Low to medium |
| `reports/031_whole-git-audit-sovereign-biophysics.md` | Explicitly partly superseded by `033`; many broken-link/private-boundary findings were closed later. | `reports/033_*`, `036_*`, `037_*`, `043_*`. | Medium |
| `reports/040_sb-catchup-june3.md` | Short catch-up brief now superseded by `043` plus current-state corrections in this report. | `reports/043_archive-flow-accuracy-audit-june4.md`; this report. | Low |

## Optional Later Cleanup

These are not urgent deletion candidates, but they could be removed if Ana wants a leaner report directory after preserving any useful facts elsewhere.

| Report | Keep/delete note |
|---|---|
| `reports/021_castaneda-epub-downloads.md` | Transaction log. Safe to delete if git history and bibliography inventory are considered enough provenance; keep if MD5/download provenance matters. |
| `reports/026_book-catalogue-local-system-2026-05-18.md` | Large acquisition catalogue. Keep until the bibliography has a proper README/catalogue that replaces it. |
| `reports/027_sovereign-biophysics-executive-summary.md` | Some action items became stale, but it still holds a useful executive synthesis. Do not use it as a current task list. |
| `reports/028_sovereign-biophysics-current-state-may18.md` | Useful changelog for the session that added root/refinement, refining-the-source, Reich analysis, and related links. Some acquisition status is now stale. |
| `reports/042_june4-fresh-plasma-distillation-log.md` | The live website experiment now carries the June 4 data. Keep for provenance until the next clean H2 run is logged; then it could be deleted. |
| `reports/043_archive-flow-accuracy-audit-june4.md` | Do not delete yet. It is still the latest full audit anchor, but this report supersedes several of its closed findings. |

## Keep

These reports still hold unique research, source maps, or continuity and should stay for now.

**Foundational / changelog memory**

- `reports/001_agent-instructions-restructure.md`
- `reports/003_full-archive-audit.md`
- `reports/017_sb-forward-audit.md`
- `reports/033_current-state-after-protective-layer.md`
- `reports/035_vessel-public-private-architecture-plan.md`
- `reports/036_whole-git-archive-flow-report.md`
- `reports/037_archive-stability-executive-report.md`
- `reports/039_sovereign-biophysics-archive-review-june1.md`

**Research and source synthesis**

- `reports/004_bibliography-audit-content-opportunities.md`
- `reports/006_thebookofsol-analysis-and-crosspollinaton.md`
- `reports/010_retroactive-validation-research.md`
- `reports/015_agni-bidirectional-krama.md`
- `reports/018_dreaming-as-healing-traditions.md`
- `reports/020_castaneda-urine-complete-search.md`
- `reports/023_session-intelligence-may14-2026.md`
- `reports/024_flower-ornament-scripture-avatamsaka-sutra.md`
- `reports/025_the-medicine-cross-traditional-synthesis.md`
- `reports/029_cmqigong-executive-summaries.md`
- `reports/041_water-memory-austin-emoto-review.md`
- `reports/researcher/001_stem-cells-ontology-and-artifact-map.md`
- `reports/researcher/002_urine-derived-stem-cells-artifact-map.md`
- `reports/researcher/003_stem-cells-urine-niche-soil-field-note.md`

**Working architecture / draft material**

- `reports/012_sb-full-read-audit.md`
- `reports/013_yrf-draft-audit.md`
- `reports/014_bridge-piece-outline.md`
- `reports/032_perceptual-formation-biological-memory.md`
- `reports/038_sovereign-biophysics-full-review-may29.md`
- `reports/044_living-year-felt-from-inside-draft.md`

## Keep With Caution

- `reports/041_water-memory-austin-emoto-review.md` should be kept for the Austin/Emoto source review, but its `T5 hypothesis` language is wrong relative to the current Dictionary. Use `tier_4_hypothesis` for hypothesis material and `tier_5_documented_external_record` for documented external record.
- Reports `027` and `028` should be treated as historical executive summaries, not current task lists. Later reports show that several acquisitions and architecture steps moved after they were written.
- Report `038` remains valuable, but its biggest missing-piece recommendation has been partially answered by report `044`.
- Report `043` remains valuable, but the closed items listed in "Current-State Corrections" above should not be repeated as open work.

## Recommended Cleanup Sequence

1. Delete only the clear candidates above after Ana approves the list.
2. Do not delete source/research reports unless their findings have been moved into a bibliography README, source note, or site document.
3. After deletion, create a short `reports/README.md` index or an analyst dashboard so the remaining reports are navigable by role: audit, source research, draft, session intelligence.
4. Keep future stale handling strict: when a current report replaces an older stale report, say so explicitly in the new report and remove the stale one only after Ana confirms if the content is substantive.

## Bottom Line

The report directory does not need a purge. It needs a trim.

The easiest safe cleanup is to remove old draft reports whose content now lives in site files, plus stale audit snapshots that later reports explicitly superseded. The source research reports should stay. They are still doing archival work.
