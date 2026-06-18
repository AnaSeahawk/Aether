# 65. LiGoldragon Primary Workflow Scan

**Date:** 2026-06-18
**Role:** analyst
**Session topic:** Quick review of LiGoldragon GitHub workflow surfaces for Aether relevance.

---

## Executive Read

LiGoldragon's `primary` repo is useful as a reference pattern, not as something
to copy wholesale.

The most useful pieces for Aether are:

- a sharper distinction between chat, reports, and permanent guidance files;
- a more deliberate context-maintenance practice for old reports;
- a current-attention map separate from historical archives;
- stronger privacy-default language around tracked files;
- the separate `caraka-samhita` repo, which is directly useful for researcher
  work because it already holds chapter-level Caraka extraction, edition
  provenance, OCR correction history, and philological notes.

The least useful pieces for Aether right now are the heavy Persona-specific
machinery: daemon-backed orchestration, BEADS, Jujutsu workflow, Spirit intent
capture, typed NOTA infrastructure, and the large role/lane matrix. Aether is
still better served by its small four-role system and simple lock helper.

## Sources Checked

- GitHub repo: `https://github.com/LiGoldragon/primary`
  - default branch: `main`
  - current fetched `origin/main`: `0d48b9b`
  - inspected local checkout: `/home/bird/Git/primary`
- GitHub repo: `https://github.com/LiGoldragon/caraka-samhita`
  - default branch: `main`
  - temporary read-only clone: `/tmp/codex-ligoldragon-caraka-samhita`
  - inspected commit: `a120366`
- Aether continuity checked against:
  - `reports/analyst/064_full-review-before-new-data.md`
  - `reports/055_sb-post-restructure-review.md`
  - `AGENTS.md`
  - `soul.md`

No browser access was used. This was GitHub/app + local git inspection.

## Useful Patterns From `primary`

### 1. Report Discipline Is More Explicit

`primary` treats reports as the durable agent surface and chat as the user's
attention surface. Aether already does this in `AGENTS.md` §11, but `primary`
adds a useful distinction:

- reports carry analysis, synthesis, proposals, and continuity;
- chat carries the report path plus the few user-attention items that matter
  without requiring Ana to open the report;
- permanent guidance files absorb rules once they stop being session findings.

For Aether, the useful transplant is not the full rule set. It is the reminder
that a report should not become a graveyard of permanent guidance. If a report
keeps being used as a rule, that rule probably belongs in `AGENTS.md`,
`protocols/orchestration.md`, a role skill, `soul.md`, or a website README.

### 2. Context Maintenance Has a Real Method

`primary` has a dedicated `skills/context-maintenance.md` with a clear workflow:

- inventory reports;
- rank by topic and recency;
- identify what is still load-bearing;
- migrate mature material into permanent docs;
- replace or delete stale reports after the valid material has landed elsewhere.

Aether already has stale-report handling, and recent work has been careful about
supersession. The next refinement would be adding a light version of this to the
analyst skill: topic-based report review, not only chronological review.

This matters now because Aether has several report arcs around Sovereign
Biophysics, living archive architecture, community stories, and video workflow.
Some will eventually need refresh/agglomeration so future agents do not have to
read ten reports to know the current rule.

### 3. Active Map Separate From Archive

`primary` separates a broad repository index from an active-attention map:

- `RECENT-REPOSITORIES.md` is a broad checkout/history index;
- `protocols/active-repositories.md` is the current working map.

Aether has fewer moving parts, but the same pattern could help. A minimal
`protocols/active-surfaces.md` could name:

- parent repo responsibilities;
- `Components/website` as the main content submodule;
- `Components/bibliography` as the source shelf;
- `Components/mother-spirit-webpage`, `Components/the-vessel`, and
  `Components/wiki` as present but lower-activity surfaces;
- current sensitivity watchpoints, especially SB and private community stories.

This would keep agents from re-deriving the active map from old reports.

### 4. Privacy Defaults Are Stronger

`primary` treats private material as closed by default and distinguishes metadata
from access control very sharply. Aether already names this problem in report
`064`: a file with `visibility: private` is still exposed if it lives in a
public repo or deployed surface.

The useful workflow import is a privacy preflight before adding or publishing
tracked files that name third parties, health context, relationship context, or
operational SB detail.

For Aether this probably means a simple curator checklist item first, not a new
privacy subsystem:

- confirm whether the file is safe to be tracked in the target repo at all;
- confirm whether deployment excludes private/community drafts;
- confirm consent scope for named community stories.

### 5. Per-Repo Intent Is Conceptually Useful, But Aether Already Has `soul.md`

`primary` puts an `INTENT.md` in each active project. The key idea is good:
agents should know what the project is trying to be before editing it.

Aether's equivalent is currently:

- `soul.md` for Aether's voice and boundaries;
- `AGENTS.md` for repo-level operating rules;
- submodule READMEs and website front doors for content architecture.

I would not add `INTENT.md` everywhere yet. Aether is smaller and more literary;
extra intent files could become maintenance weight. The more useful near-term
move is making sure `soul.md` remains current and that each major website room
has a clear README/front-door statement.

## Directly Useful: `LiGoldragon/caraka-samhita`

This is the strongest practical find.

The `caraka-samhita` repo contains:

- chapter-level markdown for Priya Vrat Sharma 2014, Volume I;
- one file per chapter under `sharma-2014/`;
- YAML frontmatter with `sthana`, chapter number/name/topic, source pages, and
  source edition;
- root digests by sthana;
- thematic digest work such as fruit/vegetable warnings;
- OCR correction notes;
- translation-source inventory;
- philological notes for specific verses, including Sūtrasthāna 5.12 and Sū. 27
  fruit verse anchoring.

This fits Aether's researcher workflow almost exactly. The repo is not a
replacement for Aether's bibliography PDFs, and its interpretive frame is not
Aether's frame. But as a source-preparation layer, it is valuable.

Recommended Aether use:

- researcher should consult it before pulling Caraka quotes from local PDFs;
- do not quote it blindly as authority; use it to find and verify passages;
- when a Caraka passage enters Aether content, cite the edition/translator and
  verify against Aether's local holdings or the referenced chapter markdown;
- consider adding a short note to the local Caraka companion note in
  `Components/bibliography/ayurveda/` pointing to the public GitHub repo and
  naming what it is good for.

Do not import the whole repo into Aether unless Ana explicitly wants that. A
link/note is enough for now.

## What Not To Import

Do not import these into Aether right now:

- daemon-backed orchestration;
- BEADS/task-lock machinery;
- Jujutsu-first version-control rules;
- Spirit intent logging;
- NOTA/schema stack;
- the large multi-lane role matrix;
- the rule that agents should commit unrelated working-copy changes.

Those make sense in LiGoldragon's high-concurrency engineering workspace. They
would add friction and conceptual noise to Aether.

Aether's four roles are enough:

- `researcher`;
- `writer`;
- `curator`;
- `analyst`.

The current `tools/orchestrate` bash helper is also enough for now.

## Recommended Next Moves

1. Add a light context-maintenance section to `skills/analyst.md`, borrowing the
   topic-based review idea without importing the full `primary` protocol.
2. Consider `protocols/active-surfaces.md` as a one-page current map for Aether's
   submodules and sensitive surfaces.
3. Add a curator privacy preflight checklist for private/community files before
   they are tracked, linked, or deployed.
4. Add a researcher note linking to `LiGoldragon/caraka-samhita` as a Caraka
   extraction/philology reference.
5. Leave orchestration, roles, and version-control mechanics as they are.

## Bottom Line

LiGoldragon's `primary` is a high-intensity coordination lab. Aether should not
become that.

But several small patterns are worth borrowing: current-state maps, topic-based
report maintenance, sharper privacy preflight, and better movement of durable
rules out of reports into guidance files.

The immediate practical win is Caraka: `LiGoldragon/caraka-samhita` looks like a
useful source-work scaffold for Aether's Ayurvedic research, provided we treat it
as a verification aid rather than a substitute for primary-source discipline.
