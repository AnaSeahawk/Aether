# 75. Full Archive Audit: Current Intention And Flow

**Date:** 2026-06-28
**Role:** analyst
**Session topic:** Full archive audit after the June collaboration intake, LiGoldragon workflow scan, and new current-state synthesis.

---

## Executive Read

The archive is in a new phase.

The earlier structure still holds:

- `aether` is the coordination seed and instruction layer.
- `Components/website` is the public/community archive surface.
- `Components/the-vessel` is the private source and collaborator archive.
- `Components/bibliography` is the source shelf.
- `reports/` is the continuity and decision trail.

What changed is the center of gravity. The archive is no longer only Ana's
records, source research, and public synthesis. The new
`Components/the-vessel/35-collaboration-private/` lane has become a real source
surface. It now holds raw group-chat export material, machine transcripts, day
indexes, thread extraction, consent mapping, Fiona microscopy records, Megan
source correction, and emergent-pattern synthesis.

That lane should be treated as one of the future cores of the archive, not as
miscellaneous notes.

The intention I read across the whole system is:

> Build a consent-aware living archive where Ana's practice, collaborator
> witness, source research, and public teaching can inform one another without
> collapsing into exposure, testimony, medical claim, or product pressure.

The workflow should become simple and repeatable:

1. raw record enters the correct private or public lane;
2. provenance is preserved;
3. threads are indexed without over-interpreting;
4. consent and attribution are mapped before reuse;
5. synthesis happens privately first;
6. public or community-facing derivatives are created only after clearance;
7. durable rules move out of reports and into guidance files when they become
   stable.

This is the Aether-sized version of the LiGoldragon "intent-led orchestration"
pattern. We should borrow the clarity, not the machinery.

## Current Git And Repo State

Before this report was written:

- parent repo `aether`: `main...origin/main`, clean;
- `Components/website`: `main...origin/main`, clean;
- `Components/the-vessel`: `main...origin/main`, clean;
- `Components/bibliography`: `main...origin/main`, clean;
- `Components/mother-spirit-webpage`: aligned with its remote in the parent
  submodule status;
- `Components/wiki`: aligned with its remote in the parent submodule status.

The old bibliography reproducibility issue named in report `064` and repeated
in report `071` appears resolved. The bibliography submodule is no longer ahead
of `origin/main`.

The stale Megan-source report issue has also been resolved. Report `073` was
deleted and replaced by:

- `reports/analyst/074_megan_macdonald_systems_hypothesis_corrected_integration.md`

The next analyst report number is therefore `075`.

## What Changed Since Report 071

Report `071` was the last broad executive brief. It remains directionally
accurate, but several facts have moved.

### 1. The June Current-State Synthesis Exists

New file:

- `Components/website/sovereign-biophysics-distillation/40-synthesis/synthesis-current-state-june-2026.md`

It names the June phase as a shift from clearing toward flow. It adds fresh
material exactness, artava/menstrual measurement, household-scale practice, and
aged-fraction repeatability.

It does not yet replace the May endpoint in the protected Sovereign Biophysics
reader path. The file itself says the May current-state synthesis remains the
path endpoint until Ana approves a path update.

This is the right state: June is present, but not prematurely canonical.

### 2. The Living Archive Pilot Grew

Current website archive summary:

- `Components/website/archive/README.md` now lists 15 included entries.
- `Components/website/archive/THREADS.md` still defines 14 controlled threads.

The archive pilot is functioning as a relational map, not a second filing
system. This remains the correct interpretation.

### 3. The Collaborator Lane Became Real

New private lane:

- `Components/the-vessel/35-collaboration-private/`

Current scale:

- about 57 MB;
- 179 files total;
- raw Telegram export includes 88 JPG files, 42 PNG files, 14 OGG audio files,
  2 video files, export HTML/CSS/JS, and checksum records;
- 14 machine-generated voice transcripts exist;
- day index, thread extraction, consent map, export intake report, processing
  pass report, and emergent-pattern report exist.

This is now the strongest prototype for the future public or member portal where
collaborators may eventually share their own experience.

### 4. Megan Source Attribution Was Corrected

Report `074` is now the reliable source on the Megan systems hypothesis packet.

Current rule:

- Megan's direct contribution, AI extrapolation, Ana notes, and Aether synthesis
  must be separated in any future derivative.
- The Western medical framing in the `.docx` should not be treated as Megan's
  authored position without further review.
- The long-practice Shivambu example is Shakti Mhi, not Lynne Taillefer, and
  remains private unless separately cleared.

This correction is important because it models exactly the kind of provenance
discipline the collaborator lane will need.

### 5. The Private Community-Story Boundary Was Improved

The full named Fiona community story was moved out of the public website current
tree and into:

- `Components/the-vessel/30-community-private/`

The public website now keeps only a redacted stub in:

- `Components/website/The-Vessel/community/`

This is the correct pattern for contributor records: private full source,
optional public chronology marker.

### 6. Paid/Member Access Is Still Conceptual

The public "Private Vessel Access" page exists:

- `Components/website/The-Vessel/portal.md`

Mother Spirit exists as a community surface:

- `Components/mother-spirit-webpage/`

But the actual portal/container model for paid, private, member, or collaborator
access is not yet designed. This matters more now because the collaborator lane
is growing into a major archive body.

## Full Archive Map

### Aether Parent Repo

Purpose:

- agent instructions;
- roles and orchestration;
- reports;
- submodule pointers;
- small local tools.

The parent repo is healthy. The four-role model is still enough:

- `researcher`;
- `writer`;
- `curator`;
- `analyst`.

No heavy orchestration import is needed. Aether should keep its small role and
claim system, but add a clearer current-surface map when the workflow stabilizes.

Likely future guidance file:

- `protocols/active-surfaces.md`

That file could name the live surfaces and the current sensitivity watchpoints
so agents do not keep re-deriving them from old reports.

### Reports

`reports/` remains the continuity trail.

The analyst sequence is currently coherent:

- `064` gives the pre-new-data broad review;
- `065` scans LiGoldragon's workflow;
- `069` audits Sovereign Biophysics flow and value;
- `071` gives the June 25 executive brief;
- `072` updates the LiGoldragon workflow interpretation;
- `074` corrects the Megan source-attribution issue;
- this report, `075`, refreshes the whole map after the collaboration intake.

Report discipline should stay active. When a report finding becomes a permanent
rule, it should move into `AGENTS.md`, a role skill, a protocol file, or a lane
README instead of remaining hidden in history.

### Website

Scale:

- 146 markdown files;
- about 80 MB.

The website is the public/community presentation layer. It is not the place for
raw private source material.

Important current surfaces:

- `Components/website/README.md` - public front door;
- `Components/website/ARCHITECTURE.md` - content architecture;
- `Components/website/ACCESS_BOUNDARIES.md` - metadata/access distinction;
- `Components/website/PUBLISH_CHECKLIST.md` - pre-publish gate;
- `Components/website/REVIEW_QUEUE.md` - active review board;
- `Components/website/archive/` - living archive pilot;
- `Components/website/sovereign-biophysics-distillation/` - Sovereign
  Biophysics public/community archive;
- `Components/website/The-Vessel/` - Living Record and access doorway.

The website has a strong boundary document now. The key phrase operationally is:
frontmatter is not access control.

### Sovereign Biophysics

Current state:

- May synthesis remains the approved endpoint of the protected reader path.
- June synthesis exists as a draft/community current-state update.
- June experiment reports are indexed without forcing a path rewrite.
- The June line has moved from isolated protocol toward household-scale,
  collaborator-aware, flow-based practice.

The archive should not rush to public certainty. The strongest posture remains:

- one body;
- one household;
- one still;
- observed conditions;
- non-medical language;
- no universal protocol claim;
- no treatment framing.

The June synthesis is important because it names the shift clearly, but it
should become canonical only after Ana reviews the path as a whole.

### Living Archive Pilot

The living archive is doing its job.

Its best function is relational retrieval:

- What records share a thread?
- What phase of the work does this belong to?
- Which files should be read together?
- Which records are public, community, or private?

It should not become a substitute for source files, and it should not expose
private records by trying to be too complete.

The controlled-thread list is a success. The next refinement is not more thread
labels. It is better decisions about which private records deserve redacted
public stubs, and which should remain invisible outside the private repo.

### The Vessel Private Repo

Scale:

- 55 markdown files;
- active private source archive.

Important lanes:

- `00-welcome/` - member/private orientation;
- `10-method-private/` - method records not suitable for public release;
- `20-experiments-private/` - private experiment records;
- `25-intimate-field-private/` - highly sensitive field notes;
- `30-community-private/` - full contributor story records;
- `35-collaboration-private/` - close collaborator records and source packets;
- `40-synthesis-private/` - private synthesis;
- `90-ops/` - migration and triage records;
- `in-development/` - drafts and transitional writing.

The Vessel architecture is now more important than the website architecture for
the next phase. The public archive can only stay clean if the Vessel remains the
place where complex, named, raw, consent-held, and not-yet-clear material is
allowed to stay whole.

### Collaboration Private Lane

This is the biggest new development.

The lane's own README defines it correctly: trusted collaboration fields,
private talks, presentations, feedback, correction, book-planning context, and
witness-field material.

It should not be treated as:

- public source pages;
- promotional copy;
- testimonials;
- final co-authored text;
- evidence for general claims.

Current internal structure is good:

- intake report;
- raw export;
- checksum manifest;
- machine transcripts;
- day index;
- thread extraction;
- consent map;
- emergent-pattern synthesis;
- named correction files;
- microscopy flow report.

The strongest rule is from the consent map: raw export material stays private,
and no message, audio, image, video, paraphrase, or inferred position leaves the
private Vessel until the relevant person reviews the exact proposed use.

This is the rule that should govern the future portal too.

### Fiona Microscopy Layer

Fiona's microscopy records are a distinct source layer inside the collaborator
lane.

They are valuable because they begin to give the archive an observational
vocabulary for samples, settling, motion, boundary, center, edge, projection,
branching, and redirection.

They are not ready for public use.

Near-term best use:

- build a private microscopy observation template;
- separate "what was seen" from "what it might mean";
- keep machine transcript language private until Fiona and Ana review;
- avoid converting visual impressions into mechanism claims.

### Megan Systems Layer

Megan's material is valuable as a translation and systems-thinking aid, not as a
public evidence source yet.

The corrected rule is:

- Megan explicit material stays distinct;
- AI extrapolation stays distinct;
- Ana/Aether synthesis stays distinct;
- any named third-party example stays private unless cleared.

This is also the general model for all collaborator-derived synthesis.

### Community Private Records

`Components/the-vessel/30-community-private/` is small but structurally
important.

It handles personal accounts from people in relationship with the work. It is
not clinical evidence, proof, promise, testimonial inventory, or public sales
material.

The website stub pattern is the right bridge:

- full source in private Vessel;
- redacted chronology marker in public website only when needed.

### Mother Spirit

Mother Spirit is the active community doorway.

Current files:

- `Components/mother-spirit-webpage/Mother Spirit - about`;
- `Components/mother-spirit-webpage/_index.md`;
- `Components/mother-spirit-webpage/invitation.md`.

The "about" text frames Mother Spirit as a practitioner community with monthly
calls and an active Telegram space. That matches the direction of the archive.

Open issue:

- `Components/mother-spirit-webpage/invitation.md` contains the typo
  `platforms.ss`.

Larger issue:

Mother Spirit can carry community rhythm, but it does not yet define a
contributor archive protocol. If collaborators will eventually access a public
or member portal and share their own experiences, Mother Spirit and The Vessel
need a shared intake/consent model.

### Bibliography

Scale:

- about 2.5 GB;
- broad source shelf across alchemy, Ayurveda, Buddhist texts, Chinese medicine,
  embodiment, feminist science, fermentation, grief/body, mythology, plants,
  shamanism, urine therapy, water, and women healers.

The bibliography is now aligned with its remote. That removes the main
reproducibility issue from earlier reports.

The most practical workflow refinement from the LiGoldragon scan remains:

- use `LiGoldragon/caraka-samhita` as a Caraka-finding and verification aid;
- do not import it wholesale;
- cite and verify against local holdings when passages enter Aether content.

### Wiki

`Components/wiki` is very small and appears mostly historical. It includes old
Mother Spirit notes but is not currently the live archive surface.

Treat it as low-activity background unless Ana asks to revive or migrate it.

## The Workflow We Should Use Now

The phrase "intent-led orchestration" fits, with one Aether-specific correction:
it should not mean more machinery first. It should mean the system asks the
right question before moving material.

For each new record, the workflow should be:

1. **Intent** - what is this record trying to serve?
2. **Lane** - where does it belong before interpretation?
3. **Provenance** - who/what generated it, and under what conditions?
4. **Sensitivity** - who could be exposed or misrepresented?
5. **Index** - what threads does it touch?
6. **Consent** - what uses are actually cleared?
7. **Synthesis** - what can be said privately without overclaiming?
8. **Derivative** - should anything public, community, book-facing, or
   member-facing be made from it?
9. **Rule migration** - did this reveal a durable rule that belongs in a README,
   protocol, or skill file?

For collaborator records, the default output should be private synthesis, not
public copy.

For public records, the default output should be bounded invitation and archive
navigation, not proof.

For member/portal records, the default output should be exact consent and
context framing before features.

## What Is Stable

These parts are stable enough to build on:

- The public/private separation between `website` and `the-vessel`.
- The redacted-stub pattern for community stories.
- The living archive pilot as relational map.
- The Sovereign Biophysics reader path as protected until Ana approves change.
- The June synthesis as a draft/current-state successor, not a forced endpoint.
- The collaboration lane as private source archive.
- The consent map as the governing rule for Telegram/collaborator material.
- The reports trail as the continuity layer.

## What Is Not Yet Stable

These parts need deliberate next design:

- Future contributor/member portal.
- How collaborators submit their own records.
- How collaborator records become searchable without becoming exposed.
- How exact consent scopes are recorded in a reusable form.
- Whether the June synthesis should replace the May endpoint.
- Whether `protocols/active-surfaces.md` should be added.
- Whether the private Vessel welcome/member files are enough for real access.
- How Mother Spirit, The Vessel, and the website relate operationally.
- Whether public protocol-like pages need another safety pass before paid/member
  framing.

## Watchpoints

### 1. Portal Before Protocol Would Be Risky

The user intention is clear: collaborators may eventually access a public portal
and share their own experiences.

That can become beautiful, but the protocol has to come first:

- contributor owns their story;
- default visibility is private;
- exact quote/paraphrase/summary requires explicit clearance;
- health-context material is not testimonial marketing;
- member access is not consent to republish;
- AI summaries must be labeled as synthesis, not source voice.

### 2. The Vessel Draft Marked Public Needs Review

One file inside the private Vessel is marked `visibility: public`:

- `Components/the-vessel/in-development/bridge-possession-sovereignty.md`

That may be intentional because it is a public-facing bridge essay, but it
should be reviewed before any deployment/migration. Its subject matter is strong
and interpretive, and it sits in a private/in-development repo.

### 3. Mother Spirit Has A Small Typo

Fix later:

- `Components/mother-spirit-webpage/invitation.md`
- typo: `platforms.ss`

This is minor, but easy to clean.

### 4. Machine Transcripts Are Navigation Aids

The Fiona audio transcripts and Telegram voice transcripts are not quote-ready.
They should remain navigation aids until the speaker reviews them.

### 5. AI-Generated Synthesis Must Stay Labeled

The Megan correction shows why this matters. The archive can use AI synthesis,
but it must never blur:

- direct collaborator statement;
- Ana note;
- AI extrapolation;
- Aether analysis;
- public wording.

### 6. Claim-Tier Vocabulary Is Broad

The website has required frontmatter, but claim-tier vocabulary is broad and
partly organic. This is acceptable for now because access boundaries are clear,
but if the portal becomes real, claim tiers may need a more normalized schema.

## Recommended Next Moves

### Immediate Analyst Move

Add a short active-surface map:

- `protocols/active-surfaces.md`

It should list the current live surfaces, roles, and sensitivity watchpoints.
This would make the LiGoldragon workflow pattern concrete without importing
heavy machinery.

### Immediate Curator Move

Run a small boundary cleanup:

- review `bridge-possession-sovereignty.md` visibility;
- fix the Mother Spirit typo;
- confirm whether the June synthesis should stay only indexed or become the new
  reader-path endpoint;
- make sure `REVIEW_QUEUE.md` reflects that decision after Ana chooses.

### Immediate Collaboration-Lane Move

Create a reusable private contributor intake template for
`35-collaboration-private/`.

It should capture:

- contributor name or private label;
- record type;
- date;
- raw source path;
- consent scope;
- cleared uses;
- prohibited uses;
- attribution preference;
- AI-processing status;
- human-review status;
- possible public/member derivative;
- exact clearance date when any derivative is approved.

The existing `collaboration-note-template.md` may be a base, but the future
portal needs something stricter.

### Immediate Microscopy Move

Create a private microscopy observation template before extracting more meaning
from Fiona's records.

Suggested sections:

- sample context;
- preparation and timing;
- instrument/magnification if known;
- first visual field;
- settling changes;
- center/edge/boundary;
- motion;
- color/texture;
- forms;
- uncertainty;
- direct visual observation;
- interpretation held separately;
- review/clearance status.

### Immediate Portal Move

Do not build a public contributor portal until the intake/consent model is
written.

When the portal is designed, it should start with three visibility states:

- private to Ana/archive team;
- visible to trusted community/members;
- public excerpt or public stub.

It should also let contributors distinguish:

- private story;
- practice note;
- observation log;
- question;
- correction;
- public testimony, if they explicitly choose that later.

## Where We Are

We are not at "publish the archive."

We are at:

- the public archive has a working shape;
- the private archive has enough structure to protect source material;
- the collaborator archive has just crossed the threshold into being central;
- the next phase is not more content first, but cleaner intake, consent,
  attribution, and flow.

Ana's work is becoming a living archive in the literal sense: it now has a body,
a memory, a source shelf, a public voice, and witnesses entering the field.

The right pace now is not slowdown. It is a more conscious rhythm:

- keep the raw whole;
- mark the source;
- protect the person;
- synthesize carefully;
- publish only what has actually crossed the boundary.

## Bottom Line

Yes: the foundation you are reading is intent-led orchestration.

For Aether, that means the archive moves by named intention and consent-aware
lane choice, not by dumping everything into public content or freezing in
private storage.

The new collaborator material belongs in the center of the next design pass.
It is likely to become one of the largest and most meaningful parts of the
archive. The system can hold that, but the next layer has to be built around
source provenance, contributor agency, and exact permission before portal
features or public-facing story flows.
