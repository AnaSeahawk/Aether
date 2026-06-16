# 59. Living Archive Architecture Proposal Review

**Date:** 2026-06-16
**Role:** analyst
**Session topic:** Review of Ana's `Archatecture proposal.md` and how to move toward a relational archive without restructuring the working SB path.

---

## Sources Read

Proposal source:

- `/home/bird/Downloads/to read/new entry/Archatecture proposal.md`

Current-state reports:

- `reports/055_sb-post-restructure-review.md`
- `reports/analyst/058_current-state-after-june-entry-integration.md`
- `reports/curator/057_vessel-community-stories-container.md`
- `reports/035_vessel-public-private-architecture-plan.md`
- `reports/036_whole-git-archive-flow-report.md`
- `reports/037_archive-stability-executive-report.md`

Repo context:

- `soul.md`
- `Components/website/ARCHITECTURE.md`
- `Components/the-vessel/ARCHITECTURE.md`
- `Components/website/README.md`
- `Components/website/The-Vessel/README.md`
- `Components/website/The-Vessel/journal/README.md`
- `Components/website/The-Vessel/journal/living-journal-2026.md`
- `Components/website/sovereign-biophysics-distillation/README.md`

## Executive Read

Ana's proposal is directionally right, but it should not be implemented as a folder restructure.

The important move is not "put everything in one physical place." The important move is: **one relational entry model, many generated doors.**

The current archive already has a stable public reading path, a public Living Record, and a private Vessel container. Those layers should remain. What is missing is the living navigation layer Ana is asking for: a way to see events, people, questions, threads, phases, and thresholds as one relational field instead of as separate manually maintained indexes.

The proposal should therefore become a **metadata and generated-view pilot**, not a repo-wide migration.

Best next move:

1. Keep the Sovereign Biophysics eleven-part reader path intact.
2. Keep The Vessel/private source boundary intact.
3. Add an archive-entry schema that can be applied to selected records.
4. Build a small pilot with 5-10 existing entries.
5. Generate a chronological view and a few filtered views from metadata.
6. Let the pilot teach what the architecture needs before migrating anything else.

This honors the felt request: relationship matters. The archive should be easier to enter through people, questions, phases, and lived events, not only through subject folders.

## What The Proposal Understands Correctly

The proposal names the actual confusion Ana is feeling.

The archive is currently working better as a reading path, but it is still difficult as a living system because its navigation is mostly sectional:

- Sovereign Biophysics
- The Living Record
- Journal
- Experiments
- Synthesis
- Community stories
- Private Vessel
- Reports

Those sections are useful, but they are not how life arrives. Life arrives as a day, an encounter, a question, a practice change, a body signal, a dream, a person, or a realization.

The proposal's strongest principles are:

- **One entry, many views.** A record should be written once, then appear in appropriate places through metadata.
- **The archive is the timeline.** Chronology should not need a second manually maintained document.
- **Milestones should emerge from significance.** Thresholds should be marked in metadata rather than duplicated into a separate milestone file.
- **Threads are more alive than categories.** Distillation, nourishment, return, community, menstrual/artava, and restoration of continuity can cross folders and years.
- **Questions should be preserved.** The archive should not only show what Ana concluded; it should show how an inquiry changed over time.
- **People enter through different doors.** Food, dreams, relationship, community, body, water, practice, grief, plants, and distillation are entry points into the same field.

This is the right diagnosis. The archive does not need more explanation. It needs more relational affordance.

## What Needs Correction

The proposal's one risky sentence is: private entries should live within the same archive structure and "no separate private archive should exist."

That should not be implemented literally.

The current architecture deliberately keeps sensitive source material in `Components/the-vessel/`, with public summaries or companion records in `Components/website/`. That boundary exists for consent, operational safety, intimate material, and future publication control. It should not be removed.

The better interpretation is:

> One conceptual archive, multiple access layers.

That means public, community, and private records can share an entry schema and be represented in a unified map, but their full content should remain in the correct repository and access layer.

For public website purposes, private records can appear as **stubs** or **redacted summaries** only when Ana wants them visible:

```yaml
visibility: private
access: private-source
summary: Private Vessel record exists for this event.
source_record:
  repo: the-vessel
  path: 25-intimate-field-private/example.md
```

The public view may show that a protected record exists. It should not expose the private content.

This keeps relationship visible without sacrificing boundary.

## Current Technical State

The website is a Markdown archive. There is no detected static-site build system in `Components/website` right now: no `package.json`, Astro, Next, Vite, MkDocs, Hugo, or Jekyll config was found in the checked depth.

That means "automatic views" cannot currently be assumed to exist. They would need to be introduced as generated Markdown indexes or as a later website build layer.

Current Markdown counts:

- `Components/website`: 134 Markdown files
- `Components/website/The-Vessel` plus `Components/website/sovereign-biophysics-distillation`: 97 Markdown files
- `Components/website/sovereign-biophysics-distillation`: 82 Markdown files

Existing metadata is partially ready for this, but not normalized.

Across `Components/website`:

- `date`: 102 files
- `visibility`: 126 files
- `status`: 126 files
- `claim_tier`: 125 files
- `type`: 96 files
- `title`: 8 files
- `phase`: 0 files
- `significance`: 0 files
- `tags`: 0 files
- `summary`: 0 files

Across `The-Vessel` plus `sovereign-biophysics-distillation`:

- `date`: 87 files
- `visibility`: 96 files
- `status`: 96 files
- `claim_tier`: 96 files
- `type`: 80 files
- `title`: 8 files
- `phase`: 0 files
- `significance`: 0 files
- `tags`: 0 files
- `summary`: 0 files

This confirms the proposal's timing: the archive is close enough to benefit from metadata-driven navigation, but not ready for a repo-wide automatic system without a small schema pilot.

## Relationship To Reports 055 And 058

Report 055 remains valid: the Sovereign Biophysics path has an honest first journey and should be protected.

Report 058 also remains valid: the archive does not need more structure in the sense of another SB reorganization.

Ana's proposal does not actually contradict those reports if implemented carefully. It answers a different problem:

- `055` solved the **first reader path**.
- `058` protected the **current state after June integration**.
- This proposal addresses the **living navigation problem**.

The live need is not "change the path." The live need is "give Ana and readers one relational map of what is happening."

## Recommended Architecture Interpretation

Do not make one folder for everything.

Make one shared entry model that can live across existing folders.

Recommended phrase:

> The archive has one relational model, not one physical room.

Physical rooms can remain:

- `sovereign-biophysics-distillation/` for the public research book
- `The-Vessel/` for the public Living Record
- `The-Vessel/community/` for private community stories inside the website layer
- `Components/the-vessel/` for protected private source records
- `reports/` for audit trail and session intelligence

Generated views can cross those rooms.

This gives Ana the thing she is asking for: people, questions, events, and thresholds visible in one space with doors to other rooms.

## Proposed Entry Schema

Use the proposal's schema, but expand it slightly so it fits the current safety architecture.

Minimum pilot schema:

```yaml
title:
date:
type:
visibility:
status:
claim_tier:
summary:
phase:
significance:
threads:
inquiries:
entry_points:
people:
source_layer:
source_record:
```

Field meanings:

- `title`: Human-readable title for generated views.
- `date`: Primary chronological ordering date.
- `type`: What kind of entry this is, such as `journal`, `experiment`, `synthesis`, `community-field-observation`, `dream`, `presentation`, `field-note`, or `analysis`.
- `visibility`: Existing access intent: `public`, `community`, or `private`.
- `status`: Existing workflow state.
- `claim_tier`: Existing claim posture.
- `summary`: One or two sentences for indexes.
- `phase`: Major era of the work, such as `distillation`, `integration`, `receiving-field`, or `full-cycle`.
- `significance`: `minor`, `major`, or `threshold`.
- `threads`: Living cross-time lines such as `distillation`, `menstrual-artava`, `restoration-of-continuity`, `nourishment`, `community-transmission`, or `grounding`.
- `inquiries`: Questions carried by the entry, such as `what-is-nourishment`, `what-is-return`, `what-is-waste`, or `what-is-relationship`.
- `entry_points`: Doorways for readers, such as `water`, `food`, `dreams`, `body`, `community`, `relationship`, `plants`, or `practice`.
- `people`: People directly part of the record, used carefully and only where consent and privacy allow.
- `source_layer`: `public-website`, `private-vessel`, `external-source`, or `report`.
- `source_record`: Optional pointer to a protected or source record when the current file is a public summary or stub.

Do not make every field required on day one. For the pilot, require only:

```yaml
title:
date:
type:
visibility:
status:
claim_tier:
summary:
```

Then add relational fields where they are obvious.

## Pilot Scope

The pilot should use 5-10 existing records that already form a living cross-section.

Best first set:

- `Components/website/The-Vessel/journal/living-journal-2026.md`
- `Components/website/The-Vessel/journal/the-deepest-layer.md`
- `Components/website/The-Vessel/community/2026-06-12-fiona-gardner-musculoskeletal-release.md`
- `Components/website/sovereign-biophysics-distillation/20-experiments/experiment-report-june4-fresh-plasma-h2-retention.md`
- `Components/website/sovereign-biophysics-distillation/20-experiments/experiment-report-june10-three-batch-fresh-plasma.md`
- `Components/website/sovereign-biophysics-distillation/20-experiments/experiment-report-june13-menstrual-plasma.md`
- `Components/website/sovereign-biophysics-distillation/40-synthesis/synthesis-three-year-topical-observations.md`
- `Components/website/sovereign-biophysics-distillation/40-synthesis/synthesis-current-state-may-2026.md`
- `Components/website/sovereign-biophysics-distillation/00-orientation/the-jar-held-to-the-light.md`
- `Components/website/sovereign-biophysics-distillation/00-orientation/the-three-waters.md`

This set would test the exact complexity Ana is feeling:

- journal
- community account
- experiment reports
- synthesis
- threshold orientation
- public and private visibility
- people and consent
- menstrual/artava
- distillation
- restoration of continuity
- full-cycle practice

If the schema works here, it is likely robust enough to expand.

## Generated Views To Build First

Because the repo currently appears Markdown-only, start with generated Markdown files rather than a full web application.

Recommended first generated files:

- `Components/website/archive/README.md` - chronological living archive stream
- `Components/website/archive/by-phase.md`
- `Components/website/archive/by-type.md`
- `Components/website/archive/by-thread.md`
- `Components/website/archive/by-entry-point.md`
- `Components/website/archive/by-significance.md`

However, do not add these until Ana confirms the pilot.

The first implementation pass should probably create a small generator script and a template, then generate only one or two views from the pilot set. For example:

- chronological archive stream
- threads view

Those two are enough to test whether the archive starts to feel like one living field.

## About The Living Journal

`living-journal-2026.md` is both precious and technically awkward.

It contains many dated entries inside one Markdown file. That makes writing easy, but metadata generation works best when each entry is its own object.

Do not split the whole journal immediately.

For the pilot, there are two good options:

1. Keep `living-journal-2026.md` intact and create generated index entries for selected dated sections manually.
2. Split only the June 12, June 14, and June 15 entries into separate files as a test, while leaving the original journal as the continuous record.

Option 1 is safer for now. Option 2 may become cleaner later if Ana likes the entry model.

The principle should be: keep writing easy. If the architecture makes the act of recording feel fussy, it will fail.

## People And Relationship

Ana's sentence "Relationship. Matters." should become a design requirement.

The proposal is strongest when it stops treating navigation as a taxonomy problem and starts treating it as a relational problem.

The archive should eventually support:

- entries involving Ana only;
- entries involving named contributors with consent;
- anonymized community records;
- protected records where a person exists but is not exposed;
- threads that show how people enter the work through different doors.

For this reason, `people:` should exist in the schema, but it must be handled carefully.

Recommended pattern:

```yaml
people:
  - name: Fiona Gardner
    role: contributor
    consent_scope: private-vessel-record
```

For public generated views, the generator should be able to suppress or anonymize people depending on `visibility` and `consent_scope`.

This is a future feature, not phase one.

## What Not To Do

Do not move all files into one new archive folder.

Do not flatten Sovereign Biophysics into a chronological blog.

Do not replace the eleven-part reader path with generated chronology.

Do not expose private Vessel content through public metadata unless Ana intentionally creates a stub or summary.

Do not create a large type vocabulary before the pilot. The current repo already has many type values, including `foundation`, `orientation`, `method`, `analysis`, `synthesis`, `experiment`, `journal`, `dictionary`, `field-entry`, and `community-field-observation`. Normalize only as needed.

Do not require every old file to be cleaned before the system can begin. That would turn the living architecture into a chores wall.

## Recommended Phase One

Phase One should be smaller than the proposal's "automatic phase, type, tag, significance pages" list.

Recommended Phase One:

1. Create a canonical archive-entry schema note.
2. Create an entry template.
3. Add pilot metadata to 5-10 selected files.
4. Generate one chronological pilot view.
5. Generate one thread pilot view.
6. Review how it feels before expanding.

Suggested future files:

- `Components/website/archive/ENTRY_SCHEMA.md`
- `Components/website/archive/entry-template.md`
- `tools/build_archive_views` or similar small script
- `Components/website/archive/README.md`
- `Components/website/archive/by-thread.md`

Exact names can be adjusted during implementation.

## Success Criteria

The pilot succeeds if:

- Ana can understand where a new record belongs without asking "which system is this?"
- a new entry can be written once and then appear in multiple useful views;
- public/private boundaries remain intact;
- the SB reader path still feels protected;
- the Living Record becomes easier to enter through life, not only through file structure;
- people and community can be represented without turning into testimonials or clinical evidence;
- the metadata feels like a small act of witnessing, not administration.

The last criterion matters most. If metadata becomes dead labor, the architecture will not be living.

## Best Next Action

Ask Codex for an implementation plan for Phase One only.

Do not ask for a full migration.

The implementation plan should answer:

- What exact schema fields are required for the pilot?
- Which 5-10 files should receive pilot metadata?
- Where should generated views live?
- Should the first generated view include private stubs or public/community entries only?
- How will private source records be represented without exposing them?
- What command will rebuild the views?

After Ana approves that plan, implement the pilot and review the feeling of the generated archive before expanding.

## Bottom Line

Ana is right: the archive needs living architecture.

But living architecture does not mean one giant room.

It means one field of relationship with clear doors.

Keep the rooms. Build the field.
