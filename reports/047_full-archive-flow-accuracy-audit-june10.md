# 47. Full Archive Flow and Accuracy Audit

**Date:** 2026-06-10
**Agent:** Codex / GPT-5
**Role:** analyst
**Session topic:** Full archive flow and accuracy audit after report cleanup, with recent-report carry-forward and current live flags.

---

## Scope

This pass reviewed the current archive flow across:

- `Components/website/`
- `Components/website/sovereign-biophysics-distillation/`
- `Components/website/Foundations/`
- `Components/website/Relationship/`
- `Components/website/living-ferments/`
- `Components/website/The-Vessel/`
- `Components/the-vessel/`
- `reports/`, especially reports `036` through `046`

No website or private Vessel files were edited. This report is the only intended file change.

## Executive Read

The archive is mechanically sound. The website, images, private Vessel links, Sovereign Biophysics spine, Relationship index, Foundations index, Living Ferments index, Journal index, and review queue paths all resolve.

The current problem is not broken flow. It is policy and boundary drift:

1. Metadata vocabulary is split between the repo contract and the live archive.
2. Some index/workflow files still lack the three required frontmatter fields.
3. `living-ferments/` is internally complete but still has no front-door or architecture decision.
4. `The-Living-Year/README.md` is a stranded redirect with no incoming links.
5. Method/protocol pages still create instructional force through structure, even when they include disclaimers.
6. High-risk analysis/synthesis pages need closer source proximity and visible claim posture.
7. June 4 H2 data is public and indexed now, but the next clean run still needs tighter run-sheet discipline.
8. Recent reports remain useful only when their closed findings are separated from their still-live patterns.

The archive does not need another architecture rebuild. It needs a normalization and boundary pass.

## Current Inventory

Current Markdown counts:

| Surface | Markdown files | Lines |
|---|---:|---:|
| `Components/website` | 126 | 15547 |
| `Components/website/sovereign-biophysics-distillation` | 77 | 10673 |
| `Components/website/Relationship` | 22 | 2045 |
| `Components/website/The-Vessel` | 12 | 1181 |
| `Components/website/living-ferments` | 5 | 769 |
| `Components/website/Foundations` | 4 | 652 |
| `Components/website/The-Living-Year` | 1 | 10 |

Sovereign Biophysics section counts:

| Section | Markdown files | Lines |
|---|---:|---:|
| `00-orientation` | 31 | 4650 |
| `10-method` | 16 | 2749 |
| `20-experiments` | 5 | 415 |
| `30-analysis` | 9 | 1348 |
| `40-synthesis` | 3 | 429 |
| `50-presentations` | 1 | 167 |
| `Dictionary` | 11 | 726 |

Submodule state was clean at scan time. Current pointers:

- `Components/website`: `42fc768`
- `Components/the-vessel`: `b470a8f`
- `Components/bibliography`: `1281577`
- `Components/wiki`: `ce59ff0`
- `Components/mother-spirit-webpage`: `44bd9ba`

## Mechanical Integrity

Checks run:

| Check | Result |
|---|---:|
| Website local Markdown/file links checked | 540 |
| Website broken local Markdown/file links | 0 |
| Website local image links checked | 41 |
| Website broken image links | 0 |
| Website internal anchor links found | 0 |
| Private Vessel local links checked | 11 |
| Private Vessel broken local links | 0 |
| Review queue code paths checked | 58 |
| Unexpected missing review queue paths | 0 |

The only review-queue path that does not resolve is `sovereign-biophysics-distillation/the-vessel.md`, and it appears only as a retired route in the cleanup notes. That is not an active broken path.

## Flow Assessment

### Whole Website

The website front door now points to:

- `Foundations/`
- `Relationship/`
- `sovereign-biophysics-distillation/`
- `The-Vessel/` displayed as The Living Record

This is coherent. The public/private naming is no longer the main problem.

Reachability from `Components/website/README.md`:

- Reachable: 116 of 126 Markdown files
- Unreachable: 10 files

Unreachable but normal workflow/admin files:

- `Components/website/ARCHITECTURE.md`
- `Components/website/PUBLISH_BATCH_2026-03-15.md`
- `Components/website/PUBLISH_CHECKLIST.md`
- `Components/website/REVIEW_QUEUE.md`

Meaningful unreachable content/lane files:

- `Components/website/The-Living-Year/README.md`
- `Components/website/living-ferments/README.md`
- `Components/website/living-ferments/body-alchemy.md`
- `Components/website/living-ferments/kefir-alchemy.md`
- `Components/website/living-ferments/soil-alchemy.md`
- `Components/website/living-ferments/water-alchemy.md`

`living-ferments/` is the remaining hidden lane. It has a complete local index and clean links, but no root doorway, no architecture mention, and no review-queue placement. Decide whether it is public, archived/off-route, or waiting for later integration.

`The-Living-Year/README.md` is a redirected stub with no incoming links. It should either be kept intentionally as a compatibility redirect and linked from `ARCHITECTURE.md`, or deleted/replaced after Ana confirms it is not needed as a historical route.

### Sovereign Biophysics

The SB spine is strong:

- root frontispiece has multiple reader routes;
- `where-to-begin.md` and the Dictionary protect mixed registers;
- method, experiment, analysis, synthesis, and Dictionary sections resolve;
- June 4 experiment is now public, indexed, and in the review queue;
- `the-map-and-the-cut.md` and `the-mother-wound.md` now use the corrected tier order;
- `sediment-field-guide.md` now has `claim_tier: observation` and visible boundary language.

The live SB risk is direct-entry reading. Readers who land on a protocol-adjacent or high-claim page may not pass through the frontispiece or Dictionary first.

Priority direct-entry pages:

- `sovereign-biophysics-distillation/10-method/distilled-fraction-protocols.md`
- `sovereign-biophysics-distillation/10-method/oral-care-protocol.md`
- `sovereign-biophysics-distillation/10-method/apothecary-balm.md`
- `sovereign-biophysics-distillation/10-method/amaroli-protocols.md`
- `sovereign-biophysics-distillation/10-method/before-you-begin.md`
- `sovereign-biophysics-distillation/10-method/on-sodium-chloride.md`
- `sovereign-biophysics-distillation/30-analysis/analysis-pharmacological-jurisdiction.md`
- `sovereign-biophysics-distillation/40-synthesis/crystal-blueprint-vortex-inheritance.md`

### Private Vessel

The private Vessel is coherent:

- `README.md` identifies it as the private source container.
- `ARCHITECTURE.md` distinguishes public research book, public Living Record, and private source/access container.
- `QUEUE.md` tracks method-private, experiment-private, intimate-field-private, synthesis-private, ready member docs, and records needing bounded public summaries.

Still relevant from earlier reports: private records should become public only through bounded summaries, not raw publication or covert protocols.

## Metadata Accuracy

Frontmatter scan:

| Finding | Count |
|---|---:|
| Website Markdown files | 126 |
| Files with no frontmatter | 8 |
| Files with frontmatter but missing required field | 1 |
| Invalid visibility values | 0 |

No-frontmatter files:

- `Components/website/ARCHITECTURE.md`
- `Components/website/Foundations/README.md`
- `Components/website/PUBLISH_BATCH_2026-03-15.md`
- `Components/website/PUBLISH_CHECKLIST.md`
- `Components/website/README.md`
- `Components/website/REVIEW_QUEUE.md`
- `Components/website/living-ferments/README.md`
- `Components/website/sovereign-biophysics-distillation/README.md`

Frontmatter present but missing a required AGENTS field:

- `Components/website/The-Living-Year/README.md` is missing `claim_tier`

Current status values:

| Status | Count |
|---|---:|
| `reviewed` | 58 |
| `draft` | 56 |
| `active` | 2 |
| `redirected` | 1 |
| `approved` | 1 |

AGENTS currently names only `draft`, `review`, `approved`, and `published`. The live archive uses `reviewed`, `active`, and `redirected`.

This is not just cosmetic. If tooling or publishing filters expect the AGENTS vocabulary, most reviewed pages will not match. If the live vocabulary is preferred, AGENTS should be updated to bless it. Pick one contract.

Current `claim_tier` values are also split between older page-level summary labels and newer Dictionary tier IDs. Values in use include `interpretation`, `practice`, `orientation`, `synthesis`, `personal-account`, `mixed`, `hypothesis`, `personal-record`, `observed`, `documented-fact`, `observation`, `preliminary-observation`, `comparative`, and `established-record`.

The newer Dictionary defines numbered claim tiers:

- `tier_0_poetic`
- `tier_1_personal_observation`
- `tier_2_measured_observation`
- `tier_3_comparative`
- `tier_4_hypothesis`
- `tier_5_documented_external_record`

Recommendation: keep `claim_tier` as the simple page-level summary if Ana likes it, but document it as different from `claim_tiers`. Use the numbered Dictionary IDs only in the plural `claim_tiers` array.

## Accuracy Flags

### 1. Protocol Force Remains The Highest Reader-Safety Risk

Several public/community method files say "record, not instruction" but still contain reproducible application structure: materials, sequencing, timing, dilution, storage, body routes, ratios, and "start slowly" language.

Priority files:

- `10-method/distilled-fraction-protocols.md`
- `10-method/oral-care-protocol.md`
- `10-method/apothecary-balm.md`
- `10-method/amaroli-protocols.md`
- `10-method/before-you-begin.md`
- `10-method/observation-protocol-handout.md`
- `50-presentations/presentation-living-waters-v1.md`

Decision needed per file:

- public record;
- community handout;
- protected protocol;
- public summary of a protected protocol.

The fix is not only disclaimers. The structure itself should match the chosen lane.

### 2. Source Proximity Is Better, Still Uneven

Improved since report `043`:

- `the-map-and-the-cut.md` has visible claim posture and source notes.
- `the-mother-wound.md` has visible claim posture and explicitly names neurodivergence framing as philosophical, not diagnostic.
- `sediment-field-guide.md` has boundary language and no longer presents itself as diagnostic.
- June 4 experiment now states its limits clearly.

Still priority:

- `analysis-pharmacological-jurisdiction.md`: high external/legal/medical claim load; source notes exist but should sit closer to each fact cluster; keep `draft`.
- `on-sodium-chloride.md`: good source-proximity note, but the page still needs careful scope around infant guidance, SSaSS, chloride physiology, salt appetite, and personal withdrawal record.
- `crystal-blueprint-vortex-inheritance.md`: improved source-proximity note, but Singer/Cowan/Vogel/Schauberger/Sheldrake/Braden/HeartMath should remain source-field/hypothesis unless independently supported.
- `the-map-and-the-cut.md` and `the-mother-wound.md`: improved, but the stronger heart-field, diagnostic, family-field, and sexuality claims should keep sources close to the sentence or paragraph where they appear.

### 3. Experiment Discipline Is The Main Scientific Gap

The experiment spine is coherent, but future runs need standardization:

- instrument and calibration date;
- sample source category;
- collection window;
- sample age;
- raw source readings;
- distillation timing;
- fraction timing;
- jar fill/headspace/lid state;
- sample temperature;
- duplicate stabilized readings;
- operator account;
- sensory notes separated from measurements.

Report `042` and the June 4 site file agree: stable pH at 9.3-9.4, H2 range 0-52 ppb, but raw baseline, source provenance, and exact timing were missing. That run is valuable as a logged observation, not a clean comparative run.

### 4. External Claim Scope Needs Dates And Conditions

Targeted external spot checks support several public-record claims, with scope cautions:

- FDA's FY 2025 PDUFA financial report shows PDUFA obligations were 77 percent user-fee funds and 23 percent non-user-fee appropriations for FY 2025. Use the dated form: "FY 2025 PDUFA obligations," not a timeless FDA-wide claim. Source: https://www.fda.gov/media/190768/download
- FDA states PDUFA was created by Congress in 1992 and reauthorized through PDUFA VII, through September 2027. Source: https://www.fda.gov/industry/fda-user-fee-programs/prescription-drug-user-fee-amendments
- NIH's 2014 notice states NIH leadership intended policies requiring applicants to consider sex as a biological variable in NIH-funded animal and cell research. Source: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-14-128.html
- FDA's own history says the 1993 Gender Guideline called for assessment of medication responses in both genders and revoked the 1977 guideline excluding women of childbearing potential from early clinical studies. Source: https://www.fda.gov/about-fda/histories-product-regulation/promoting-safe-effective-drugs-100-years
- GOV.UK 2025 commercial baby food guidelines do not permit salt as an ingredient in meals/finger foods/snacks and set sodium limits; NHS says babies should not have much salt because their kidneys are not fully developed. Sources: https://www.gov.uk/government/publications/commercial-baby-food-and-drink-voluntary-industry-guidelines/commercial-baby-food-and-drink-voluntary-industry-guidelines and https://www.nhs.uk/live-well/eat-well/food-types/salt-in-your-diet/
- The SSaSS trial supports lower stroke, major cardiovascular event, and death rates in an older/high-risk Chinese population using potassium-enriched salt substitute versus regular salt. Do not generalize it beyond population and substitution context. Source: https://www.nejm.org/doi/full/10.1056/NEJMoa2105675
- Chloride physiology literature supports keeping chloride visible as an independent variable, but the review language is nuanced and population/model dependent. Source: https://link.springer.com/article/10.1007/s00424-015-1690-8
- DCIS overdiagnosis/overtreatment concern is supported, but DCIS is not uniformly harmless; use "active research question" language. Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC8760161/ and https://pubmed.ncbi.nlm.nih.gov/27671693/
- South Korea thyroid screening/overdiagnosis is a strong example: NEJM reports 2011 diagnosis rates 15 times 1993 rates while mortality remained stable. Source: https://www.nejm.org/doi/abs/10.1056/NEJMp1409841

This was not a full external fact-check of every claim. It was a targeted accuracy pass on the claims most likely to affect public trust or safety.

## Recent Reports: Still Relevant

### `036_whole-git-archive-flow-report.md`

Still relevant as a pattern report.

Durable signal:

- the archive flow is source record -> bounded public summary -> claim environment/posture -> synthesis -> dictionary refinement -> new observation;
- private/public architecture is conceptually stable;
- do not mass-normalize metadata; prioritize high-risk, high-traffic pages.

Stale facts:

- counts and some path findings are old;
- living architecture has moved since then.

### `037_archive-stability-executive-report.md`

Still relevant.

Durable signal:

- architecture is stable enough to pressure-test;
- main weakness is page-level evidence posture;
- scientific record is hypothesis-generating, not controlled lab evidence;
- run sheets and calibration logs are still needed.

### `038_sovereign-biophysics-full-review-may29.md`

Still relevant for aliveness and "presence speed."

Partially answered:

- report `044` now drafts the first-distillation phenomenological account.

Still open:

- place or rewrite that account into the site when ready;
- add operator accounts to experiment reports.

### `039_sovereign-biophysics-archive-review-june1.md`

Still relevant as a high-risk page map.

Closed or improved:

- `sediment-field-guide.md` metadata/boundary issue is fixed;
- `the-map-and-the-cut.md` and `the-mother-wound.md` have claim posture and corrected tier order;
- June 4 is now public/indexed.

Still open:

- protocol-page lane decisions;
- source proximity on high-risk analysis/synthesis;
- run-sheet/calibration layer;
- update presentation only after claim posture and source support are stable.

### `041_water-memory-austin-emoto-review.md`

Still useful source synthesis.

Carry forward:

- Austin/Emoto belong in observational/philosophical/hypothesis register;
- CMP on Solar/Lunar/Saturn fractions is a useful low-barrier observational extension;
- Austin's distilled-water/mineral-salt tension is productive for SB.

Correction:

- Its `T5 hypothesis` language is stale. Use `tier_4_hypothesis` for hypothesis claims and `tier_5_documented_external_record` only for clearly cited external source statements.

### `042_june4-fresh-plasma-distillation-log.md`

Still relevant as provenance for the June 4 H2 run.

Carry forward:

- stable pH, variable H2, missing raw baseline/source/timing map;
- next clean H2 run needs fixed timing, source labels, raw readings, headspace/lid notes, and duplicates.

### `043_archive-flow-accuracy-audit-june4.md`

Still useful but partially superseded.

Closed since then:

- no broken website links remain;
- Foundations README links actual files;
- June 4 experiment is public and indexed;
- sediment guide has `claim_tier` and boundary language;
- tier reversal in site metadata is fixed;
- review queue now declares itself a priority board.

Still live:

- source proximity;
- protocol boundaries;
- run-sheet/calibration discipline;
- operator accounts;
- `living-ferments/` decision;
- metadata contract harmonization.

### `044_living-year-felt-from-inside-draft.md`

Still relevant as working draft material.

Carry forward:

- likely site placement near `a-year-in-the-practice.md`, The Living Record, or an orientation close;
- needs visible personal-account claim note if dental/skin observations stay in public/community form.

### `045_reports-cleanup-candidates.md` and `046_reports-clear-candidate-cleanup.md`

Keep as cleanup records.

Carry forward:

- clear candidates were deleted;
- optional cleanup remains unapproved;
- source/research reports should stay protected until their facts are moved elsewhere.

## Priority Flags

### Immediate

1. Decide the metadata contract:
   - normalize live statuses to `draft/review/approved/published`; or
   - update AGENTS to include `reviewed`, `active`, and `redirected`.

2. Decide whether root/index/workflow files require frontmatter:
   - add `status`, `visibility`, and `claim_tier`; or
   - explicitly exempt operational index files from the content-file metadata rule.

3. Decide `living-ferments/`:
   - public lane linked from root and architecture;
   - archived/off-route lane with explicit note;
   - or later integration.

4. Decide `The-Living-Year/README.md`:
   - keep as intentional redirect and give it full metadata;
   - or remove after Ana confirms no compatibility route is needed.

5. Start protocol-boundary pass:
   - `distilled-fraction-protocols.md`
   - `oral-care-protocol.md`
   - `apothecary-balm.md`
   - `amaroli-protocols.md`
   - `before-you-begin.md`
   - `observation-protocol-handout.md`

6. Add or tighten visible claim posture/source proximity:
   - `analysis-pharmacological-jurisdiction.md`
   - `on-sodium-chloride.md`
   - `crystal-blueprint-vortex-inheritance.md`
   - `the-map-and-the-cut.md`
   - `the-mother-wound.md`

### Next

7. Build a standard experiment run-sheet template.
8. Add operator accounts to experiment reports, beginning with Feb 22, March 8, and June 4.
9. Place or rework report `044` into the site when Ana is ready.
10. Add a small `reports/README.md` index for the cleaned report archive.
11. Preserve report `041` but supersede its tier wording in future site work.
12. Keep report `042` until a cleaner H2 run replaces it as the active provenance record.

## Bottom Line

The archive flow is now trustworthy at the mechanical and architectural level.

The accuracy work is more subtle: make the metadata contract real, make direct-entry pages safe without relying on the reader to find the Dictionary first, keep public method pages from becoming instructions by shape, and make future experiments easier to compare.

The archive is ready for precision work, not another map.
