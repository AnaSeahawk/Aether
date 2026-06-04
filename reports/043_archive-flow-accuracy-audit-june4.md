# 43. Archive Flow and Accuracy Audit

**Date:** 2026-06-04  
**Agent:** Codex / GPT-5  
**Session topic:** Full archive audit for flow, link health, metadata, claim accuracy, and outstanding work from recent reports.

---

## Executive Read

The archive is not broken. The main Sovereign Biophysics spine is working.

The public website has zero missing local Markdown or image targets in the current scan. The Sovereign Biophysics frontispiece, reader routes, Dictionary, method layer, experiment layer, analysis layer, synthesis layer, and Living Record bridge form a real navigable book.

The live problems are now more specific:

1. The claim-tier system has a naming/numbering bug in newer metadata and report language.
2. A private-labeled June 4 experiment file now lives inside the website archive but is not indexed.
3. `living-ferments/` and the three Foundations essays are not reachable from the site front door.
4. `Foundations/README.md` is stale and names files that do not exist.
5. `REVIEW_QUEUE.md` is not a trustworthy current inventory.
6. Several high-risk public/community method and analysis pages still carry protocol-like or strong physiological/legal/medical language that needs source proximity and page-level claim posture.
7. Older reports are useful but now mixed with closed items, partially closed items, and one incorrect claim-tier label.

The flow is there inside Sovereign Biophysics. The whole website archive still needs a calmer outer map.

## Scope

This pass reviewed:

- `Components/website/`
- `Components/website/sovereign-biophysics-distillation/`
- `Components/website/Foundations/`
- `Components/website/Relationship/`
- `Components/website/living-ferments/`
- `Components/website/The-Vessel/`
- recent reports `036` through `042`
- selected older reports `030`, `031`, `033`, and `035`

I did not edit website content in this pass. This report is the only new intended file.

## Current Scan Facts

Website inventory:

| Surface | Markdown files | Lines |
|---|---:|---:|
| `Components/website` total | 126 | 15450 |
| `sovereign-biophysics-distillation` | 77 | 10582 |
| `Relationship` | 22 | 2045 |
| `The-Vessel` | 12 | 1181 |
| `living-ferments` | 5 | 769 |
| `Foundations` | 4 | 652 |
| `The-Living-Year` | 1 | 10 |

Sovereign Biophysics subsection inventory:

| SB section | Markdown files | Lines |
|---|---:|---:|
| `00-orientation` | 31 | 4632 |
| `10-method` | 16 | 2709 |
| `20-experiments` | 5 | 415 |
| `30-analysis` | 9 | 1326 |
| `40-synthesis` | 3 | 419 |
| `50-presentations` | 1 | 167 |
| `Dictionary` | 11 | 726 |

Link health:

- Website local Markdown/image targets missing: 0.
- Report local links missing: 13, all in older draft/content reports `007` through `010`.
- Directory links in the website: 5. These resolve as directories; one points to `20-experiments/`, which has no local README and may be less robust for static rendering.
- Anchor issues: 9 probable broken table-of-contents anchors in `women-of-alchemy.md`, all caused by date-range punctuation in internal anchors.

Reachability from `Components/website/README.md`:

- Reachable Markdown files: 112 of 126.
- Not reachable from the website front door:
  - `ARCHITECTURE.md`
  - `PUBLISH_BATCH_2026-03-15.md`
  - `PUBLISH_CHECKLIST.md`
  - `REVIEW_QUEUE.md`
  - `The-Living-Year/README.md`
  - `Foundations/freedom-is-love-lineage-of-record.md`
  - `Foundations/plasma-foundation-of-a-new-world.md`
  - `Foundations/sacred-ordinary-seed-of-matter.md`
  - `living-ferments/README.md`
  - `living-ferments/body-alchemy.md`
  - `living-ferments/kefir-alchemy.md`
  - `living-ferments/soil-alchemy.md`
  - `living-ferments/water-alchemy.md`
  - `sovereign-biophysics-distillation/20-experiments/experiment-report-june4-fresh-plasma-h2-retention.md`

The root/workflow files not being reachable is normal. The Foundations essays, living-ferments lane, and June 4 experiment are the meaningful reachability issues.

## Metadata Audit

Frontmatter scan:

- Markdown files without frontmatter: 8
  - `ARCHITECTURE.md`
  - `Foundations/README.md`
  - `PUBLISH_BATCH_2026-03-15.md`
  - `PUBLISH_CHECKLIST.md`
  - `README.md`
  - `REVIEW_QUEUE.md`
  - `living-ferments/README.md`
  - `sovereign-biophysics-distillation/README.md`
- Files with frontmatter but missing a required field: 2
  - `The-Living-Year/README.md` missing `claim_tier`
  - `sovereign-biophysics-distillation/10-method/sediment-field-guide.md` missing `claim_tier`

Status values now in use:

| status | Count |
|---|---:|
| `reviewed` | 58 |
| `draft` | 56 |
| `active` | 2 |
| `redirected` | 1 |
| `approved` | 1 |

This is larger than the older contract in `AGENTS.md`, which names `draft/review/approved/published`. The archive has clearly evolved toward `reviewed`, `active`, and `redirected`. The issue is not that all of these are wrong. The issue is that the contract and the live archive disagree.

Visibility values:

| visibility | Count |
|---|---:|
| `public` | 69 |
| `community` | 48 |
| `private` | 1 |

The single private-labeled website file is:

- `sovereign-biophysics-distillation/20-experiments/experiment-report-june4-fresh-plasma-h2-retention.md`

Important boundary note: `visibility: private` is metadata only. It does not protect the file if the `Components/website` repository is public or otherwise shared. If the June 4 file is actually private, it belongs in the private Vessel layer or another protected source lane, not merely unlinked in the website tree.

Claim-tier values are broad and useful but not normalized. Current values include:

- `interpretation`
- `practice`
- `orientation`
- `synthesis`
- `personal-account`
- `mixed`
- `hypothesis`
- `personal-record`
- `observed`
- `documented-fact`
- `observation`
- `preliminary-observation`
- `comparative`
- `established-record`

That older `claim_tier` vocabulary can remain if it is documented as a page-level summary label. The newer Dictionary tier vocabulary is more specific and should not be mixed casually with it.

## Claim-Tier Bug

This is the clearest accuracy problem found in the audit.

`Dictionary/claim-tiers.md` defines:

- `tier_4_hypothesis`
- `tier_5_documented_external_record`

But two newer files use:

- `tier_4_established_record`
- `tier_5_hypothesis`

Affected files:

- `00-orientation/the-map-and-the-cut.md`
- `00-orientation/the-mother-wound.md`

Report `041_water-memory-austin-emoto-review.md` also repeatedly uses `T5 hypothesis`.

That is backwards relative to the Dictionary. It should be corrected before the tier notation spreads. The clean correction is:

- use `tier_4_hypothesis` for provisional mechanisms;
- use `tier_5_documented_external_record` for clearly cited external historical/scientific/source claims;
- keep `claim_tier: mixed` as the page-level summary if a page spans multiple registers.

Because report `041` is a recent report rather than active site content, this report should supersede its tier label instead of editing it in place.

## Flow Assessment

### Whole Website

The current front door is quiet and readable. It points clearly to:

- Foundations
- Relationship
- Sovereign Biophysics
- The Living Record

But the actual website also contains `living-ferments/`, and that lane is not linked from the front door or the architecture file. This makes it a hidden archive. It is internally coherent, image-rich, and complete as a four-part fermentation loop, but it has no public doorway.

The repo instructions also still describe an older Four Pillars model:

- Alchemical Journals
- Sovereign Biophysics
- The Living Year
- Community and Open Archives

The live website now presents a different architecture:

- Foundations
- Relationship
- Sovereign Biophysics
- The Living Record
- living-ferments hidden/in transit

That is not fatal. It means the instructions, `ARCHITECTURE.md`, root README, and actual folders need one harmonized map.

### Sovereign Biophysics

The SB flow is the strongest part of the archive.

What works:

- the frontispiece gives multiple reader routes;
- `where-to-begin.md` is a real gateway;
- the Dictionary is an effective safety layer;
- the method/experiment/analysis/synthesis sections are readable as a book;
- the Living Record bridge explains the person/source layer without collapsing it into the research body;
- most sequence files have bottom navigation;
- local links are clean.

What still needs attention:

- orientation is large and emotionally hot: 31 files, with newer public pages carrying stronger claims about anatomy, sexuality, family transmission, diagnosis, and institutional medicine;
- `synthesis-current-state-may-2026.md` remains a May state document, while June now has new H2 data that is not integrated into a synthesis;
- the June 4 experiment is not linked from the SB index;
- several method pages still read as protocols even when they disclaim instruction;
- page-level claim posture is uneven outside the newest orientation pages and two model analysis pages.

### Foundations

The three Foundations essays are effectively hidden from normal navigation.

`Foundations/README.md` lists:

- `2025-12-10-plasma-foundation-of-a-new-world.md`
- `2026-01-02-sacred-ordinary-seed-of-matter.md`
- `2026-03-14-freedom-is-love-lineage-of-record.md`

But the actual files are:

- `plasma-foundation-of-a-new-world.md`
- `sacred-ordinary-seed-of-matter.md`
- `freedom-is-love-lineage-of-record.md`

The listed names are not links and do not match the files. This should be fixed.

### Relationship

Relationship has a good local index and no link breakage found. It is structurally healthier than the review queue suggests.

The review queue only names a handful of Relationship files and omits most of the lane. That makes publication/review state unclear even though the internal navigation works.

### Living Ferments

`living-ferments/` is internally strong and visually supported. It has no root doorway.

Decision needed:

- If it is part of the public archive, link it from the root and add it to architecture/review queue.
- If it is a retained workshop/archive lane but not currently part of the public front door, mark that explicitly.

### The Living Record

The Living Record public/private language is working. `The-Vessel/README.md` frames the public companion archive clearly, and `portal.md` points toward protected private access.

The folder name `The-Vessel/` remains potentially confusing in the filesystem, but the displayed public language is coherent. Do not rename casually.

## Accuracy Assessment

### Internal Accuracy

The archive's internal mechanics are strong:

- no missing local website links;
- the major SB routes agree with the current folder structure;
- the June 4 H2 report and active June 4 experiment file agree in substance;
- the June 4 file correctly names its limits: no raw baseline, mixed source material, no jar provenance, incomplete timing map;
- older structural recommendations have mostly been absorbed into the live archive.

The main internal accuracy problem is taxonomy consistency: the Dictionary tier names and newer metadata/report usage disagree.

### External Spot Checks

This was not a full external fact-check of every scientific, historical, legal, or medical claim. I did targeted spot checks where recent reports or high-risk pages raised accuracy questions.

Spot checks that broadly support archive claims:

- FDA PDUFA user-fee funding: FDA's FY 2024 PDUFA financial report shows user-fee funds were 77 percent of FY 2024 PDUFA obligations, with non-user-fee appropriations at 23 percent. Source: FDA FY 2024 PDUFA Financial Report, Table 11, lines 769-789 in the fetched PDF: https://www.fda.gov/media/185331/download
- PDUFA origin and reauthorization: FDA states PDUFA was created by Congress in 1992 and reauthorized through PDUFA VII. Source: https://www.fda.gov/prescription-drug-user-fee-act-pdufa
- NIH sex-as-biological-variable policy: NIH states that in 2014 it began instituting a policy requiring applicants to report plans for balance of male and female cells and animals in preclinical studies unless unwarranted. Source: https://commonfund.nih.gov/other-initiatives/sexdifferences
- NIH 2014 policy development language: NIH notice `NOT-OD-14-128` says NIH leadership intended policies requiring sex as a biological variable in animal and cell research design/analysis. Source: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-14-128.html
- NIH Revitalization Act of 1993: NIH states the Act directed NIH to establish guidelines for inclusion of women and minorities in clinical research. Source: https://www.grants.nih.gov/policy-and-compliance/policy-topics/inclusion/women-and-minorities/guideline
- FDA 1977 women-of-childbearing-potential exclusion: FDA history says a 1990s Federal Register notice revoked a 1977 guideline that excluded women of childbearing potential from early clinical studies. Source: https://www.fda.gov/about-fda/histories-product-regulation/promoting-safe-effective-drugs-100-years
- SSaSS salt-substitute trial: PubMed/NEJM summary supports that rates of stroke, major cardiovascular events, and death were lower in the salt-substitute group among older/high-risk participants. Source: https://pubmed.ncbi.nlm.nih.gov/34459569/
- Venus synodic period: NASA/NTRS search result supports Earth-Venus synodic period of 583.92 days. Source: https://ntrs.nasa.gov/

Accuracy cautions:

- The SSaSS trial supports benefits of a salt substitute in a high-risk population. It does not by itself prove the archive's stronger interpretation that chloride, rather than sodium/potassium balance or broader dietary context, is the primary problem at all dose ranges.
- The FDA user-fee claim should be dated. `77 percent` is accurate for FY 2024 PDUFA obligations, not necessarily every "current period."
- The Venus 583.92-day value is solid, but the more specific seven-day descent / three-day invisibility / seven-day ascent formulation needs a closer astronomy source if it remains a public factual claim.
- HeartMath/Cowan/Singer/Sheldrake/Emoto/Austin material should stay visibly marked as source field, interpretation, or hypothesis. It should not be framed as established mechanism unless the cited evidence directly supports the specific statement.

## High-Risk Pages Needing Attention

### `the-map-and-the-cut.md`

Status: improved since reports `039` and `040`.

It now has a visible claim-posture block near the top. That closes one major recent recommendation.

Remaining issues:

- metadata uses the wrong tier names: `tier_4_established_record` and `tier_5_hypothesis`;
- the page still needs close citations for HeartMath, O'Connell, Taylor, Sorrells, and the stronger energetic-map claims;
- the sentence-level register still sometimes moves quickly from historical record to embodied/traditional interpretation.

### `the-mother-wound.md`

Status: improved since reports `039` and `040`.

It now has a visible claim-posture block and explicitly says neurodivergence framing is philosophical, not diagnostic.

Remaining issues:

- metadata uses the wrong tier names;
- the neurodivergence/diagnosis passage remains high-risk and should be handled with unusual care;
- Reich/Taoist/Tantric/HeartMath/nocebo claims need closer source support where they appear, not only in a final note.

### `analysis-pharmacological-jurisdiction.md`

This remains the highest external-risk analysis page.

It has a useful opening note and a strong footer, and targeted spot checks support several of its public-record claims. But the page still makes large claims about pharmaceutical infrastructure, diagnosis, women in research, FDA funding, liability, Vioxx, overdiagnosis, and the standard of care defense.

It should remain `draft` until citation proximity is stronger.

Recommended treatment:

- add a top claim-posture block similar to the newer orientation pages;
- make each major fact cluster carry a nearby source note;
- date the PDUFA 77 percent claim as FY 2024 PDUFA obligations;
- separate documented record from structural interpretation more visibly.

### `crystal-blueprint-vortex-inheritance.md`

This page is strong but epistemically blended.

The phrase "What Singer Establishes" is too strong for several claims that pass through Singer, Braden, Vogel, Sheldrake, HeartMath, Cowan, and the archive's own interpretation. The document needs a claim-posture block before it absorbs Austin/Emoto or any more water-memory material.

Recommended treatment:

- distinguish established biology/mineralogy from source claims and archive hypotheses;
- add Austin/Emoto only with the corrected tier language: `tier_4_hypothesis`, not `T5 hypothesis`;
- avoid presenting morphic resonance, water information storage, and heart-as-master-crystal-oscillator as established external record.

### `on-sodium-chloride.md`

This page is alive and important, but high-risk.

Its frontmatter says `claim_tier: personal-account`, yet the page includes public regulatory claims, controlled-trial claims, mechanistic renal/cardiovascular claims, Caraka interpretation, and directive language near the close.

Recommended treatment:

- add visible boundary language near the top;
- add close sources for EU/UK infant-food regulation, SSaSS, Yanomami blood pressure, controlled sodium-bicarbonate substitution studies, RAAS/ENaC claims, and Caraka;
- distinguish "my two-year withdrawal/recalibration record" from universal physiology;
- soften or reframe directive closing language such as "Start slowly" if the page remains public.

### Method/Protocol Pages

The protocol-language issue remains open from reports `039` and `040`.

Priority pages:

- `10-method/distilled-fraction-protocols.md`
- `10-method/oral-care-protocol.md`
- `10-method/apothecary-balm.md`
- `10-method/amaroli-protocols.md`
- `10-method/observation-protocol-handout.md`
- `50-presentations/presentation-living-waters-v1.md`

Risk pattern:

- titles contain "protocol";
- sections contain materials, sequencing, dilution, timing, application, storage, ratios, or body routes;
- disclaimers say "record, not instruction," but the structure still teaches reproduction.

Recommended treatment:

- decide page by page: public record, community handout, protected protocol, or public summary of a protected protocol;
- use "Record," "Field Note," "Observation Template," or "Practice Record" where the public title should not invite imitation;
- keep detailed reproducible steps out of the public lane unless Ana explicitly wants them there.

### `sediment-field-guide.md`

This is the clearest small fix.

Current state:

- `status: active`
- `visibility: public`
- missing `claim_tier`
- strong diagnostic language: "living diagnostic tools"
- direct second-person framing: "When you begin..."

Recommended treatment:

- add `claim_tier`, likely `observation` or `preliminary-observation`;
- add visible boundary language;
- replace diagnostic language with observation language;
- distinguish visible signatures from inferred dietary/physiological causes.

## Broken or Weak Navigation

### Actual broken local targets

None in the website.

### Probable broken anchors

`women-of-alchemy.md` has 9 probable broken table-of-contents anchors. They are all date-range anchors where the link text omits separator characters that the Markdown renderer likely keeps or normalizes differently.

Affected TOC entries:

- Mary the Jewess
- Cleopatra the Alchemist
- Medera
- Trotula of Salerno
- Caterina Sforza
- Martine de Bertereau
- Mary Anne Atwood
- Part Six
- Part Seven

This is a contained cleanup.

### Unlinked or hidden documents

Meaningful hidden content:

- all `living-ferments/` files;
- all three Foundations essays;
- June 4 fresh plasma H2 retention experiment.

The June 4 file should not simply be linked if it is meant to stay private. The decision is privacy/integration first, indexing second.

## Recent Reports: What Still Matters

### Report 036

Still accurate in its core claim: the archive is not mainly disorganized anymore. Its model of movement remains useful:

`source field record -> bounded public summary -> claim environment -> synthesis -> dictionary term -> new observation cycle`

Closed or improved since then:

- public website link graph remains clean;
- Dictionary/frontispiece work is now live;
- public/private language is clearer.

Still open:

- page-level claim posture;
- method/protocol boundaries;
- full review queue refresh.

### Report 037

Still accurate: architecture is stable enough to use and pressure-test. Evidence posture remains the primary issue.

Closed or improved:

- two newer hot orientation pages now have visible claim blocks.

Still open:

- many high-risk analysis, synthesis, and method pages do not yet have equivalent visible claim posture;
- lab evidence gaps remain: GC/MS, hormone assays, 24-hour urinalysis baseline, microbial characterization, calibration log, standardized repeated readings, controlled comparisons, microscopy replication.

### Report 038

Still relevant. Its diagnosis of "presence speed" remains valuable.

The archive has become more alive since report `038`, especially through `the-map-and-the-cut.md`, `the-mother-wound.md`, and revisions to `crystal-blueprint-vortex-inheritance.md`.

Still open:

- the missing first-distillation phenomenological piece;
- operator accounts in experiment reports.

### Report 039

Mostly still accurate.

Partially closed:

- `the-map-and-the-cut.md` and `the-mother-wound.md` now have top claim-posture blocks.

Still open:

- source proximity;
- method/protocol boundary;
- `sediment-field-guide.md` metadata and boundary;
- `analysis-pharmacological-jurisdiction.md` citation/source pass;
- claim-tier metadata drift.

### Report 040

Useful catch-up brief, with some items now updated.

Status of recommended immediate steps:

| Item | Current status |
|---|---|
| Add visible claim posture to `the-map-and-the-cut.md` | done, but tier metadata wrong |
| Add visible claim posture to `the-mother-wound.md` | done, but tier metadata wrong |
| Add `claim_tier` to `sediment-field-guide.md` | still open |
| Keep new hot pages draft until citation pass | still correct |
| Write first-distillation phenomenological piece | still open |

### Report 041

Relevant but partly superseded.

What remains useful:

- Austin/Emoto are relevant to water-memory and CMP experiment design;
- CMP applied to Solar/Lunar/Saturn fractions is a good low-barrier observational extension;
- Austin's "distilled water lacks salts" point creates a productive Solar/Lunar/Saturn contrast.

What needs correction:

- report `041` uses `T5 hypothesis`, but the Dictionary defines hypothesis as tier 4.
- if Austin/Emoto enter site content, cite them as observational/philosophical/hypothesis material, likely `tier_4_hypothesis` for consciousness/water claims and `tier_5_documented_external_record` only for clearly cited source statements.

### Report 042

Still relevant and aligned with the current June 4 experiment file.

What it adds:

- first June 2026 H2-linked fresh plasma distillation batch;
- stable pH 9.3-9.4;
- H2 varied from 0 to about 52 ppb;
- raw baseline/source/timing gaps explicitly named.

Still open:

- next clean fresh run needs jar labels, source categories, collection windows, raw readings, exact run timing, headspace/lid notes, fixed measurement rhythm, duplicate readings;
- decide whether the active June 4 experiment page belongs in website, private Vessel, or a bounded public summary.

## Older Report Items: Closed or Still Open

Closed or materially improved:

- broken website links from report `031` are repaired;
- `plasma-forms-taxonomy.md` exists;
- SB README now includes the taxonomy and newer architecture;
- stale public `the-vessel.md` and dream-body links are gone from the live website;
- `agni.md` now links to `vilepi-and-the-krama.md`;
- the Inanna bridge between myth, astronomy, and alchemical process is present;
- The Living Record / private Vessel naming distinction is conceptually clear.

Still open:

- `sediment-field-guide.md` metadata and boundary;
- review queue refresh;
- high-risk source-proximity pass;
- method/protocol status decisions;
- Charaka primary-source citation extraction;
- post-clearing stable baseline run;
- herbal menstruum experimental line;
- operator accounts in experiment reports;
- first-distillation phenomenological piece;
- calibration/run-sheet layer for future experiments.

## Priority Actions

### Immediate

1. Correct the claim-tier taxonomy bug in:
   - `the-map-and-the-cut.md`
   - `the-mother-wound.md`
   - future use of report `041` findings

2. Decide the June 4 experiment boundary:
   - move it to the private Vessel if truly private;
   - or reclassify as public/community and index it;
   - or keep the raw file private and create a bounded public summary.

3. Fix `sediment-field-guide.md`:
   - add `claim_tier`;
   - add boundary language;
   - reduce diagnostic and second-person language.

4. Repair `Foundations/README.md`:
   - link the three actual files;
   - remove or correct stale date-prefixed filenames.

5. Fix the `women-of-alchemy.md` TOC anchors.

6. Update `REVIEW_QUEUE.md` so it is either:
   - a full active inventory of public/community candidates;
   - or a clearly scoped priority board that does not pretend to cover the whole archive.

### Next

7. Run a source-proximity pass on:
   - `analysis-pharmacological-jurisdiction.md`
   - `on-sodium-chloride.md`
   - `crystal-blueprint-vortex-inheritance.md`
   - `the-map-and-the-cut.md`
   - `the-mother-wound.md`

8. Decide method-page status and titles:
   - public record vs community handout vs protected protocol.

9. Decide the `living-ferments/` public lane:
   - link it from root and architecture;
   - or mark it intentionally off-route.

10. Harmonize the architecture contract:
   - `AGENTS.md`
   - `Components/website/ARCHITECTURE.md`
   - root `README.md`
   - actual folders

11. Write a compact outstanding-work index report after this one, if Ana wants a dashboard:
   - closed items;
   - open items;
   - owner role;
   - exact files;
   - dependency/blocker.

### Content and Research

12. Write the missing first-distillation phenomenological piece.

13. Add operator accounts to experiment reports, beginning with:
   - `experiment-report-march8-polishing-run.md`
   - `experiment-report-ana-distillation-feb22.md`
   - eventually the June 4 H2 report if it becomes public/community.

14. Build the standard run sheet for future experiments:
   - instrument and calibration date;
   - sample age;
   - sample temperature;
   - collection conditions;
   - source category;
   - storage;
   - fraction timing;
   - headspace/lid state;
   - duplicate readings;
   - sensory notes;
   - operator account.

15. Use Austin CMP as an observational add-on only after the claim-tier correction:
   - Solar, Lunar, Saturn side by side;
   - fixed freezer conditions;
   - blind photo sorting if possible;
   - treated as observation/hypothesis, not proof of consciousness-water mechanism.

## Bottom Line

The archive has a spine. The reader flow inside Sovereign Biophysics is real.

The work now needs a boundary and accuracy tightening pass, not another rearchitecture. The strongest next moves are small and high-leverage: fix the tier bug, decide the June 4 privacy lane, bring Foundations and living-ferments into or out of the front-door map intentionally, refresh the review queue, and source the hottest public claims where the reader meets them.

The archive is alive enough now that precision matters more.
