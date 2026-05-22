# 31. Whole-Git Audit and Sovereign Biophysics Flow Review

**Date:** 2026-05-23
**Agent:** Codex / GPT-5
**Session topic:** Whole-repo audit with special attention to Sovereign Biophysics structure, flow, flags, redundancy, and blending opportunities.

---

## Executive Summary

The repo is healthy at the git level and strong at the conceptual level. The main issue is not weak material. It is that the archive is moving faster than its navigation, review queue, metadata discipline, and public/private boundaries.

Sovereign Biophysics is the clear flagship. It is substantial, coherent, and alive: 63 Markdown files, a working orientation-method-experiment-analysis-synthesis architecture, and a growing experimental record. The strongest next move is a curator pass, not a rewrite. The archive needs its doors, labels, and internal corridors brought up to the current state of the work.

The highest-priority flags:

1. `Components/website/REVIEW_QUEUE.md` is badly stale.
2. `Components/website/sovereign-biophysics-distillation/README.md` is missing six current SB files.
3. A link check found 13 broken internal website links.
4. One file marked `visibility: private` lives in the public website submodule.
5. The new May 22 material is powerful but operationally intimate; it needs a deliberate boundary decision before being treated as community-facing.
6. `Components/website/sovereign-biophysics-distillation/10-method/plasma-forms-taxonomy.md` is open in the IDE but does not exist on disk. If that file is an unsaved draft, save it before any cleanup pass.
7. `sovereign-biophysics-translation-map.md` is doing too many jobs. It wants to be split into an alchemical translation map plus a practical plasma/fraction taxonomy.

My read: the work does not need less. It needs clearer layering. The strongest blend would be to make `plasma-forms-taxonomy.md` the practical hub for forms, fractions, and reunion, while letting the existing translation map become the symbolic/alchemical lexicon.

## Repo Inventory

All tracked git worktrees were clean at audit time:

| Surface | Role | Status |
|---|---|---|
| `.` | Parent seed repo | `main...origin/main`, clean |
| `Components/website` | Main public/content site | `main...origin/main`, clean |
| `Components/bibliography` | Source library | `main...origin/main`, clean |
| `Components/the-vessel` | Private contained archive | `main...origin/main`, clean |
| `Components/mother-spirit-webpage` | Small legacy/current public page | `main...origin/main`, clean |
| `Components/wiki` | Legacy wiki | `main...origin/main`, clean |

Size profile:

| Path | Size | Note |
|---|---:|---|
| `Components/bibliography` | 2.4G | Main weight of the repo |
| `.git` | 2.6G | Large parent git object store |
| `Components/website` | 79M | Content + images |
| `.jj` | 17M | Jujutsu workspace metadata |
| `reports` | 604K | Audit/session trail |
| `Components/the-vessel` | 160K | Small private archive |
| `Components/wiki` | 24K | Legacy |
| `Components/mother-spirit-webpage` | 20K | Minimal |

The parent repo is intentionally a seed/coordinator repo. That architecture is working.

## Root-Level Notes

The root is mostly clean, but two things are worth noting:

- `CLAUDE.md` is fine as a compatibility entry point; it points back to `AGENTS.md`.
- `gopass-wrapped-glcoud` is a root-level executable. It does not contain a secret, but the name appears misspelled (`glcoud` / `gcloude`) and it is operational tooling rather than core repo identity. Consider moving it under `tools/` or renaming it if it is still used.

Report numbering has historical drift: there are two `010_*` reports and no `019_*`. Not harmful, but future reports should continue from the highest prefix, which this report does.

## Website Audit

The website submodule currently has 112 Markdown files.

Frontmatter health is mostly good. The main drift is taxonomy:

- `status` values include `draft`, `reviewed`, `approved`, `active`, and `redirected`.
- `AGENTS.md` describes `status` as `draft/review/approved/published`.
- `claim_tier` values are useful but loose: `practice`, `observed`, `observation`, `preliminary-observation`, `interpretation`, `synthesis`, `mixed`, etc.

Recommendation: either update `AGENTS.md` to match the real taxonomy, or normalize the files to the documented taxonomy. Right now both are partly true.

### Review Queue

`Components/website/REVIEW_QUEUE.md` should be rebuilt, not lightly patched.

Current scan:

- 74 website Markdown files are missing from the queue.
- 6 queue entries point to paths that no longer exist.
- The queue still references moved/private material such as `protocol-golden-syphon.md`, `yoni_receiving_field.md`, `sovereign-biophysics-distillation/the-vessel.md`, and `sovereign-biophysics-distillation/practice-log-2026.md`.

Dead queue paths found:

- `The-Living-Year/journal/2026-04-23-the-deepest-layer.md`
- `protocol-golden-syphon.md`
- `sovereign-biophysics-distillation/40-synthesis/synthesis-multiday-distillation-fresh-vs-aged.md`
- `sovereign-biophysics-distillation/practice-log-2026.md`
- `sovereign-biophysics-distillation/the-vessel.md`
- `yoni_receiving_field.md`

Best fix: generate a fresh queue from actual files, grouped by section, then manually annotate publish readiness.

### Broken Links

A local path check found 13 broken website link hits, across 11 unique source/target patterns:

| Source | Broken target | Likely fix |
|---|---|---|
| `Relationship/README.md` | `../../Components/bibliography/urine-therapy/Damar-Tantra.epub` | Use `../../bibliography/...` only in parent context, or remove/cite externally because `website` is its own repo |
| `Relationship/Ginger.md` | `../10-method/ambrosia-diet.md` | `../sovereign-biophysics-distillation/10-method/ambrosia-diet.md` |
| `Relationship/Bhringaraj.md` | `../sovereign-biophysics-distillation/the-dream-body.md` | Point to the actual Vessel journal/dream page, or create a current dream-body page |
| `40-synthesis/synthesis-current-state-may-2026.md` | `../../The-Living-Year/journal/README.md` | `../../The-Vessel/journal/README.md` |
| `40-synthesis/synthesis-current-state-may-2026.md` | `../the-dream-body.md` | Create/move the dream-body document or link to the Vessel journal |
| `40-synthesis/synthesis-three-year-topical-observations.md` | `../what-the-body-already-knew.md` | Link to the current Vessel/backstory location or remove |
| `10-method/observation-protocol-handout.md` | `../the-vessel.md` | Link to `../../The-Vessel/README.md` or `../../The-Vessel/backstory/the-record.md` |
| `00-orientation/a-year-in-the-practice.md` | `../../The-Living-Year/portal.md` | `../../The-Vessel/living-year.md` or `../../The-Vessel/portal.md` |
| `00-orientation/a-year-in-the-practice.md` | `../the-vessel.md` | `../../The-Vessel/README.md` or `../../The-Vessel/backstory/the-record.md` |
| `00-orientation/urine-derived-stem-cells.md` | `../../reports/researcher/002_urine-derived-stem-cells-artifact-map.md` | Do not link outside the website submodule unless using an absolute GitHub URL |
| `20-experiments/experiment-report-ana-distillation-feb22.md` | `../the-vessel.md` | Link to current Vessel path |

The repeated pattern is clear: several links still assume older SB-root files (`the-vessel.md`, `the-dream-body.md`, `what-the-body-already-knew.md`) that have since moved into the public Vessel section or private Vessel repo.

## Public/Private Boundary Flags

The strongest boundary issue is:

- `Components/website/sovereign-biophysics-distillation/20-experiments/field-note-may21-fraction-blend.md`
  - `visibility: private`
  - Lives inside the `website` submodule.

Per `AGENTS.md`, `visibility` metadata is internal only. GitHub repo privacy controls actual access. If this file is truly private, move it to `Components/the-vessel/20-experiments-private/` or remove it from the website submodule.

The May 22 files also need an intentional publish-lane decision:

- `20-experiments/experiment-report-may22-conjunctio-full-sequence.md`
- `20-experiments/field-note-may22-living-day-protocol.md`

They are valuable as records, but they include explicit rectal/vaginal application details, two-practitioner pooling, and a living-day operational description. If they remain `visibility: community`, they should be framed as contained single-subject field records, not replicable protocols. If that feels too exposed, place them in The Vessel and publish a shorter community-facing summary.

Relationship plant entries also have publish-risk language. Examples include traditional quotations about "conquer death" or being "free of old age," plus practical dosage-style sections such as "A quarter teaspoon..." These can remain if clearly framed as traditional record, but the safest public edit is to rename "A note on use" to "Traditional forms recorded" and keep Ana's stance non-prescriptive.

## Sovereign Biophysics: Current State

Current SB count: 63 Markdown files.

Status distribution:

- `reviewed`: 45
- `draft`: 15
- `active`: 1
- `approved`: 1

Visibility distribution:

- `public`: 38
- `community`: 23
- `private`: 1

The archive is strong. The orientation is broad, the method layer is practical, the experiments preserve raw measurements, and the analysis/synthesis layer is doing real interpretive work. The problem is not content volume. It is that new material is not being integrated into the reading path fast enough.

### SB README Is Missing Six Current Files

These files exist but are not indexed in `Components/website/sovereign-biophysics-distillation/README.md`:

- `00-orientation/capacity-not-substance.md`
- `00-orientation/urine-derived-stem-cells.md`
- `20-experiments/experiment-report-may22-conjunctio-full-sequence.md`
- `20-experiments/field-note-may21-fraction-blend.md`
- `20-experiments/field-note-may22-living-day-protocol.md`
- `40-synthesis/crystal-blueprint-vortex-inheritance.md`

Suggested placement:

- `capacity-not-substance.md`: place after `Two Distillates` and before `Agni`, or after `The Biological Baseline` and before `Thesis`. I prefer after `Two Distillates`; it prepares the reader to understand ojas/Jing/plasma as capacity rather than object.
- `urine-derived-stem-cells.md`: make it a companion/FAQ branch from `Capacity Not Substance`, not necessarily a main sequence piece. It answers a specific community objection.
- May 22 experiment + living-day field note: list under Experiments as "current draft records"; link them to each other.
- May 21 private fraction blend: move to The Vessel if it stays private.
- `crystal-blueprint-vortex-inheritance.md`: add to Synthesis, but include an evidence-tier note because it crosses Singer, Cowan, HeartMath, Sheldrake, Pollack, microscopy, and archive interpretation.

### Metadata Fixes

Two SB files lack required `claim_tier`:

- `10-method/sediment-field-guide.md`
- `10-method/sovereign-biophysics-translation-map.md`

Suggested values:

- `sediment-field-guide.md`: `claim_tier: practice` or `claim_tier: observation`
- `sovereign-biophysics-translation-map.md`: `claim_tier: synthesis` or `claim_tier: mixed`

Also decide what to do with `status: active` on `sediment-field-guide.md`. It is expressive, but it is outside the documented status set.

## Sovereign Biophysics: Flow and Blending Recommendations

### 1. Split the Translation Map

`sovereign-biophysics-translation-map.md` is rich, but overloaded. It currently contains:

- women's alchemical lineage
- spagyric vocabulary
- source material categories
- fraction taxonomy
- VITRIOL / Sal Salis
- Chymical Wedding
- Opus Mulierum conclusion

That is too much cognitive work for one method document.

Recommended split:

- Keep `sovereign-biophysics-translation-map.md` as the symbolic/alchemical lexicon: Eagle, Tria Prima, Solve et Coagula, VITRIOL, Chymical Wedding, Opus Mulierum.
- Create/save `10-method/plasma-forms-taxonomy.md` as the practical taxonomy: fresh, aged, pure plasma, Solar/Spirit, Lunar/Essence, Essence Tails, Saturn/Serum, blends, reunited fractions, and when each term is used.

This directly matches the missing IDE tab. The tab name is the right file. It just does not exist on disk yet.

### 2. Make a "Fractions and Reunion" Hub

The same core idea appears in several places:

- `translation-map.md`: separation and reunion
- `urine-derived-stem-cells.md`: cells are not the point; transformed fractions are
- `experiment-report-may22-conjunctio-full-sequence.md`: Albedo, Conjunctio, Rubedo sequence
- `crystal-blueprint-vortex-inheritance.md`: all three fractions reunited as complete medicine
- `distilled-fraction-protocols.md`: practical use of distinct fractions

This is not bad repetition. It is the central teaching trying to become a hub.

Best blend: make `plasma-forms-taxonomy.md` the place where the reader can understand all forms at once. Then each deeper essay can point to it instead of re-explaining the whole model.

### 3. Merge Duplicate Interpretation in the May 22 Experiment

`experiment-report-may22-conjunctio-full-sequence.md` has two sections that repeat the same interpretation:

- "Key Observations"
- "Data Notes"

Blend them into one section called "Interpretive Data Notes" or "Data Notes." Keep the raw phase tables unchanged. Then the report will read as:

1. Phase data
2. Complete sequence table
3. Interpretive data notes
4. Limitations / future protocol

Important limitations to name clearly:

- Li's Nigredo baseline was not measured.
- Ana's starting ORP was not measured.
- Starting TDS was recalled, not formally recorded.
- Rubedo output is intentionally combined vaginal + urinary output and cannot be disaggregated.

The report already names these honestly. Consolidating them would make the science cleaner.

### 4. Give the Living-Day Note a Different Job

`field-note-may22-living-day-protocol.md` should not duplicate the experiment report. Its job is atmosphere and lived context:

- continuous production
- real-time use
- pooling practice
- appetite/dietary signal
- phenomenological body response

Keep it as the living frame around the formal May 22 report. Add a line near the top: "For raw measurements, see the Conjunctio report." Then keep this note sensory and contextual.

### 5. Resolve the Dream Body Gap

Several current files point toward a dream-body document that does not exist at the linked path. The underlying theme is important: cannabis removal, lucid dreaming, recapitulation, night practice, medhagni, and the Vessel journal.

Options:

- Create a current public/community document in `Components/website/The-Vessel/journal/` or `Components/website/The-Vessel/`.
- Keep it private in `Components/the-vessel` and replace public links with the Vessel journal index.
- Create a short SB synthesis note called `dream-body-and-clearing.md` if the theme belongs in SB proper.

Right now the theme is alive but the doorway is missing.

### 6. Decide Where "Capacity Not Substance" Leads

`capacity-not-substance.md` is one of the best bridge pieces because it protects the archive from a crude "what molecule is it?" reading. It should be integrated into the main path.

Recommended flow:

```text
Two Distillates
→ Capacity Not Substance
→ Agni
→ The Root and the Refinement
→ The Medicine
```

`urine-derived-stem-cells.md` should link out from `Capacity Not Substance` as a focused case study.

### 7. Update the Presentation Last

`presentation-living-waters-v1.md` should not be updated until the README/index and May 22 boundaries are settled. Then update the talk to include:

- "All the practice is for the medicine" as the core thesis.
- "Capacity not substance" as the epistemology.
- The May 22 full-sequence experiment as the newest live record.
- The fraction taxonomy as the handout/reference.

## Sovereign Biophysics: Claim and Evidence Flags

The archive generally does a good job naming observation vs interpretation. A few areas deserve extra care:

1. `crystal-blueprint-vortex-inheritance.md`
   - Strong synthesis, but it crosses several speculative bridges.
   - Add a short "Evidence tiers" note: established anatomy / cited theory / archive hypothesis / direct observation.

2. `analysis-pharmacological-jurisdiction.md`
   - Public-facing and medically adjacent.
   - Claims about DCIS, thyroid cancer, overdiagnosis, and treatment harms need citations close to the claims if this is published.

3. `distilled-fraction-protocols.md`
   - Contains eye/ear drops, headache, burns, wound healing, and sequencing language.
   - Strong candidate for community/private rather than public unless rewritten more clearly as personal record.

4. `oral-care-protocol.md`
   - Public and method-like.
   - If public, make sure it stays explicitly observational and non-prescriptive.

5. Relationship plant entries
   - Several read like practical use notes.
   - They should keep traditional-use boundaries prominent and avoid sounding like instructions.

## Whole-Repo Flow Notes

### Website Front Door

`Components/website/README.md` is much stronger than the old report described. It now establishes Ana Seahawk and Sovereign Biophysics as the central work quickly. Good.

The remaining front-door issue is spatial: The Vessel, Relationship, Living Ferments, Foundations, and Sovereign Biophysics need to feel like one organism. The best simple fix is not more explanation. It is better cross-linking:

- SB method docs should point to Relationship plant entries where relevant.
- Relationship entries should point correctly back to SB.
- The public Vessel section should be the canonical place for backstory, living year, and journal.
- `The-Living-Year/README.md` is now a redirect, so old links should stop targeting it as if it still held active content.

### Private Vessel

There are two "Vessel" surfaces:

- `Components/the-vessel`: private repo/submodule.
- `Components/website/The-Vessel`: public website section.

This is workable, but references need to distinguish them. Public links should go to `Components/website/The-Vessel/...`. Sensitive operational material should go to `Components/the-vessel/...`.

The private repo's own next-step note is still valid:

- add per-folder `README.md`
- add private metadata headers where needed
- update the migration map after the next private import wave

### Bibliography

`Components/bibliography` is strong and well organized. It contains 225 files and now includes the high-priority Charaka material that older reports still listed as pending:

- `ayurveda/Sharma-Caraka-Samhita-Vol1.pdf`
- `ayurveda/Sharma-Caraka-Samhita-Vol2.pdf`
- `ayurveda/Sharma-Caraka-Samhita.md`

This means the next Charaka task is no longer acquisition. It is citation extraction and replacement in the SB documents that still cite Charaka indirectly.

One duplicate exists:

- `plants/Carson-Silent-Spring.pdf`
- `feminist-science/Carson-Silent-Spring.pdf`

They are byte-identical. Keep one copy and replace the other with a note or symlink if repo weight matters.

Large-file note: the bibliography contains several very large PDFs, including a 272.9 MB urine-therapy PDF and 200 MB / 148 MB Charaka volumes. This is acceptable if the bibliography repo is intentionally archival, but it explains the repo's weight.

### Legacy Submodules

`Components/wiki` is legacy and tiny. It still contains 2023-era Mother Spirit notes. Decide whether to:

- archive it as historical,
- migrate anything useful into `Components/website`,
- or remove the submodule later.

`Components/mother-spirit-webpage` is tiny and still points to the Telegram/community frame. It is not causing problems, but it is outside the current website's primary architecture.

## Recommended Next Passes

### Curator Pass: Highest Priority

1. Repair the 13 broken links.
2. Rebuild `Components/website/REVIEW_QUEUE.md`.
3. Update `Components/website/sovereign-biophysics-distillation/README.md` to include the six missing files.
4. Move or reclassify the private May 21 field note.
5. Add missing `claim_tier` values.
6. Decide whether `status: reviewed` or `status: review` is canonical.

### Writer/Flow Pass: Sovereign Biophysics

1. Save/create `10-method/plasma-forms-taxonomy.md`.
2. Split practical taxonomy out of `sovereign-biophysics-translation-map.md`.
3. Blend duplicate interpretation sections in the May 22 Conjunctio report.
4. Position `capacity-not-substance.md` in the main orientation path.
5. Make `urine-derived-stem-cells.md` a companion case study.
6. Add a dream-body doorway or remove broken dream-body links.

### Researcher Pass

1. Extract direct Charaka citations now that the files are present.
2. Add citations to high-risk medical/system claims in `analysis-pharmacological-jurisdiction.md`.
3. For `crystal-blueprint-vortex-inheritance.md`, separate established scientific claims from interpretive archive hypotheses.

## Bottom Line

The archive is not scattered. It is overflowing its old containers.

Sovereign Biophysics has reached the point where it needs a map that is as refined as the material. The next best work is structural: links, queue, metadata, boundaries, and one clear taxonomy hub. Once that is done, the reader will be able to feel what is already true in the body of the repo: this is no longer a set of notes. It is an archive with a living spine.

## Verification

Checked:

- parent and submodule git status
- submodule list and remotes
- top-level and submodule structure
- website Markdown/frontmatter counts
- SB README coverage against actual files
- REVIEW_QUEUE coverage against actual files
- local Markdown link existence across `Components/website`
- current SB active/new files
- private/public boundary metadata
- bibliography size and duplicate basename/hash scan

No content files were edited during the audit. This report is the only intended file change.
