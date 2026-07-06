# 77. Full Archive Audit Before Collaborator Invites

**Date:** 2026-07-05
**Role:** analyst
**Session topic:** Deep archive audit before new intake and before Megan and Fiona receive read-only access.

---

## Executive Read

The archive is not broken. It is overfull at the working edge.

The core architecture is holding:

- `aether` is the coordination, report, and instruction layer.
- `Components/website` is the public/community archive.
- `Components/the-vessel` is the private source, member, and collaborator container.
- `Components/bibliography` is the source shelf.
- `reports/` is the continuity trail.

What has changed since the last full audit is that the collaborator lane has become the center of gravity. `Components/the-vessel/35-collaboration-private/water-magicians/` now has a real private navigation doorway, bridge maps, source packet workflow, private microscopy vocabulary, support path, living journal template, Fiona asset lane, and the first filled source packet.

That is the good news.

The unfinished part is review and permission. The new systems work as private archive structure, but most of them have not crossed the human-review gate. Megan and Fiona can be invited in soon, but the safest first move is a limited review path or a very clear read-only orientation, not an unframed "here is the whole private repo" handoff.

## What I Verified In This Pass

Observed state:

- Parent repo `aether`: clean, aligned with `origin/main`.
- All orchestration lanes: idle.
- Submodules:
  - `Components/bibliography`: clean, aligned.
  - `Components/mother-spirit-webpage`: clean, aligned.
  - `Components/the-vessel`: clean, aligned after fetching the stale tracking ref.
  - `Components/website`: clean, aligned.
  - `Components/wiki`: clean, aligned.

Checks run:

- `Components/website/tools/build_archive_views` - passed, built 15 living archive entries, no diff.
- Lightweight local Markdown link check across `Components/website` and `Components/the-vessel` - 811 relative links checked, 0 missing.
- `git -C Components/website diff --check` - passed.
- `git -C Components/the-vessel diff --check` - passed.
- `git diff --check` in parent repo - passed before this report was added.

Not checked:

- External URLs.
- Public deployment.
- GitHub collaborator permission settings.
- Human review of machine transcripts.
- Medical/legal accuracy beyond existing archive guardrails.

## Current Scale

Current local file counts from this pass:

| Surface | Count / state |
|---|---|
| `Components/website` | 142 markdown files |
| `Components/the-vessel` | 85 markdown files |
| `Components/bibliography` | 229 files at max depth 2 |
| Living Archive generated pilot | 15 real entries |
| Website local markdown links checked | 811 links, 0 missing |

The living archive text search finds 16 `archive_entry: true` strings, but one is the example block in `archive/ENTRY_SCHEMA.md`. The generator correctly excludes generated/schema files and builds 15 real entries.

## What Changed Since Report 075

Report `075` remains directionally right, but several new systems landed after it.

### 1. Aether Got Its Own Skill-Loading Layer

New files:

- `skills/index.md`
- `skills/sensitive-content.md`

Updated:

- `AGENTS.md`
- `skills/analyst.md`
- `skills/curator.md`
- `skills/researcher.md`
- `skills/writer.md`

This is the small Aether-native version of LiGoldragon-style skills. Agents now have an explicit rule: read the role skill, load `skills/prose.md` for writing, load `skills/sensitive-content.md` before private/operational/health-adjacent/collaboration-sensitive work, and do not scan every skill by default.

This is working and needs no more machinery right now.

### 2. Water Magicians Became A Real Private Working Lane

Current clean doorway:

- `Components/the-vessel/35-collaboration-private/water-magicians/README.md`

It now links the Telegram exports, call transcripts, Fiona microscopy material, Megan correction notes, bridge maps, support drafts, source packet workflow, and assets.

This solved the earlier "scattered files" problem enough for navigation. It has not solved review or consent by itself.

### 3. The Source-Packet Workflow Moved From Proposal To Trial

New/current workflow files:

- `water-magicians/source-packet-template.md`
- `water-magicians/collaboration-private-to-sovereign-biophysics-bridge-map.md`
- `water-magicians/collaboration-private-archive-review.md`
- `water-magicians/sovereign-biophysics-archive-review-from-collaboration-lane.md`
- `water-magicians/alchemy-matter-saturn-microbe-archive-source-packet.md`

This is the main unfinished trial flow.

The trial worked structurally: raw source was narrowed into a source packet with attribution map, consent/review status, possible uses, do-not-move-yet boundaries, open questions, and candidate SB destinations.

The trial is stalled at human review:

- Ana has not yet approved the packet framing.
- Megan has not reviewed the relevant private personal/practice material.
- Fiona has not reviewed the microscopy/body-language parts.
- Nothing from the packet is cleared for public, book, community, or SB movement.

### 4. Fiona's Microscopy Layer Is Now A Private Vocabulary System

Current file:

- `Components/the-vessel/35-collaboration-private/water-magicians/microscopy.md`

This gives Fiona's observation language a private holding place. It is useful now as a private glossary and future template seed. It is not ready for public Dictionary movement.

The old public microscopy analysis in SB remains separate from the newer private Fiona vocabulary. That separation matters.

### 5. Fiona Brand Assets Were Added Privately

Current asset lane:

- `Components/the-vessel/35-collaboration-private/water-magicians/assets/`
- `Components/the-vessel/35-collaboration-private/water-magicians/assets/fiona-gardner-brand-assets/`

The asset lane has a source note, checksum manifest, and explicit permission boundary. It is working. It needs Fiona's exact permission before any public, promotional, book, social, support-page, or community use.

### 6. The Urine Therapy Booklet Is Only An Outline

Current file:

- `Components/the-vessel/in-development/urine-therapy-booklet-outline-2026-07-04.md`

It is a private outline, not drafted prose. The next step is a verse/source selection decision before drafting, especially around classical claims that could read as promises if handled carelessly.

### 7. Mother Spirit Typo Was Fixed

Report `075` named a typo in `Components/mother-spirit-webpage/invitation.md`. Current file no longer has the `platforms.ss` typo.

### 8. Website Had One Recent Focused Change

Since June 28, `Components/website` has one recent commit:

- `aa7f961` - consolidate dictionary terms and add oral-care burn warning

This suggests the public archive itself has been relatively stable while private collaborator work accelerated.

## What Is Working

### Public/Private Architecture

The public/private split is working.

`Components/website/ACCESS_BOUNDARIES.md` is now the key rule:

- frontmatter is routing metadata, not access control;
- `public`, `community`, and `private` are review states, not actual privacy;
- paid access is not permission to expose private source records;
- third-party community records live in private Vessel by default.

This boundary is strong and should be treated as current.

### Living Archive Pilot

The living archive pilot is working as a generated relational map.

Current state:

- 15 entries;
- controlled thread vocabulary in `archive/THREADS.md`;
- generator builds cleanly;
- generated views are subordinate to source files and reader paths.

The pilot is no longer hypothetical. It has been pressure-tested enough to keep using carefully. It should not be made a public front door until Ana chooses that.

### Sovereign Biophysics Public Spine

The SB reader path still points to May 2026 as the protected endpoint. June 2026 is present as a draft/current-state successor and appears in the archive pilot, but it has not replaced May.

This is correct if the question is "what is safe and coherent for a reader right now?"

### The Vessel Queue

`Components/the-vessel/QUEUE.md` is doing real work. It is long, but it now functions as the private dashboard for:

- Water Magicians source packets;
- collaborator review items;
- transcripts;
- raw export packets;
- private support path;
- in-development drafts;
- intimate and method records;
- public stub/public summary relationships.

It is the best current source for "what is still in the private inbox."

### Consent And Attribution Discipline

The Megan correction and Water Magicians source-packet template have made the attribution standard concrete:

- collaborator explicit;
- Ana observation;
- AI/agent synthesis;
- unclear or needs confirmation;
- exact review status before any derivative.

This is one of the strongest new systems in the archive.

### Local Mechanical Health

Mechanical state is good:

- clean repos;
- clean submodules;
- living archive generator passes;
- local relative markdown links pass across `website` and `the-vessel`;
- no whitespace diff errors.

## What Is Not Working Yet

### Collaborator Access Is Not Framed Enough

Megan and Fiona are close enough to be invited in, but the access question is still unresolved:

- full private repo read-only access;
- selected Water Magicians review packet or separate limited review surface;
- selected review packet;
- separate collaborator review packet outside the repo.

This matters because GitHub read-only access is effectively repo-level. If Megan
and Fiona are invited directly to `Components/the-vessel`, they can see more
than the Water Magicians lane unless a separate limited review surface is made.
`the-vessel` also contains intimate, operational, and private in-development
material that is broader than Megan/Fiona's own collaboration lane.

Recommendation: do not send an unframed full-repo invite as the first move unless Ana explicitly wants them to see the whole private Vessel. Start with a review path centered on:

- `35-collaboration-private/water-magicians/README.md`;
- the archive preservation preview draft after Ana reviews it;
- the consent map;
- the first source packet;
- Fiona/Megan-specific review questions.

### Source Packets Need A Board

The bridge map has an active packet board, but the workflow is not yet visible enough as a daily working surface.

Current problem:

- one packet exists;
- several packet candidates exist;
- review status lives inside files;
- there is no compact "source packets board" that says ready / waiting / blocked / cleared.

Recommendation: create a `water-magicians/source-packets/` folder and a `source-packets/README.md` only after the second packet exists, or add a compact board section to the existing Water Magicians README now.

### Call Transcripts Are Still Under-Indexed

The June 24 Water Magicians call is proposal-relevant but not human-reviewed or quote-ready. The May 29 call transcript exists. The archive review already named the missing next layer: a call-topic index.

This remains outstanding.

### Private Synthesis Is Still Scattered

The Water Magicians index makes files findable, but understanding still requires reading many dated reports. The system needs one current synthesis page that says:

- what Water Magicians is now;
- what is cleared;
- what is not cleared;
- what review is needed from Ana/Megan/Fiona;
- what the next packet is.

Report `056_water-magicians-report.md` is useful, but current private files have advanced beyond it.

### June Synthesis Is Present But Not Canonical

The June synthesis is strong and current, but it explicitly supersedes nothing. The public SB reader path still ends at May.

This is not a bug. It is a decision waiting for Ana:

- keep May as the canonical endpoint for now;
- make June the new endpoint;
- create a new July/current "collaboration-aware" successor later.

Recommendation: do not promote June automatically. Let Ana decide after she reviews the whole path.

### Public Method Pages Still Need Boundary Review Before Paid/Member Framing

Reports `069`, `070`, and `075` all converge on this. Before any paid/member offer is built around SB, review public protocol-like pages against `ACCESS_BOUNDARIES.md`.

High-priority pages remain:

- `10-method/amaroli-protocols.md`
- `10-method/distilled-fraction-protocols.md`
- `10-method/oral-care-protocol.md`
- `10-method/observation-protocol-handout.md`
- `10-method/before-you-begin.md`
- any page that can read as instruction rather than record.

### The Private Access Offer Is Still Not Designed

`Components/website/The-Vessel/portal.md` exists and is clean as a public threshold. It does not define a real member/collaborator access model.

Still missing:

- what a person gets access to;
- what remains private even from members;
- whether collaborator access differs from member access;
- how consent is recorded;
- what support pays for;
- how Mother Spirit relates to The Vessel.

### One Private Draft Still Has `visibility: public`

Known file:

- `Components/the-vessel/in-development/bridge-possession-sovereignty.md`

It has `visibility: public` and `migration_status: not-cleared`. This is probably intentional as a public-facing bridge draft, but it should not move anywhere until Ana reviews it.

### Metadata Is Good Enough, Not Normalized

Website status values currently include:

- `draft`: 69
- `reviewed`: 58
- `active`: 2
- blank/example values: 2
- `redirected`: 1
- `approved`: 1

This is acceptable because `ACCESS_BOUNDARIES.md` explicitly names legacy/local statuses. It is not ready for automated publication filtering unless normalized.

Claim tiers are broader and more organic. That is fine for reading, but weak for automation.

### Root/Control Files Lack Frontmatter

Files like `README.md`, `ARCHITECTURE.md`, `REVIEW_QUEUE.md`, `PUBLISH_CHECKLIST.md`, `ACCESS_BOUNDARIES.md`, and some README/control files lack the three content frontmatter fields.

This is not currently breaking anything. Treat these as control files unless a future static-site build requires universal frontmatter.

## Trial Flows And Their Status

| Trial flow | Current status | What worked | What is unfinished |
|---|---|---|---|
| Living Archive pilot | Working | 15 entries, generator passes, controlled threads | Decide whether it stays hidden/community, becomes member map, or gets public excerpt |
| Access boundaries | Working | Clear rule that frontmatter is not access control | Apply it to protocol-like pages before paid/member framing |
| Private community story pattern | Working | Full source in private Vessel, website stub only | Needs repeated use on future community records |
| Water Magicians index | Working | Clean navigation doorway exists | Needs current "what to review now" board |
| Source-packet workflow | Trial succeeded structurally | First packet proves the shape | Human review has not happened; no packet cleared |
| Microscopy vocabulary | Private working glossary | Separates Fiona layer from public SB | Fiona review needed before Dictionary or public movement |
| Support path | Drafted, not cleared | Names support as archive labor, not access purchase | Needs Ana/Megan/Fiona review before any public support page |
| Living journal participation template | Strong seed | Could become future contributor protocol | Needs consent/access model before portal use |
| Archive preservation preview | Drafted | Could orient Megan/Fiona/readers | Needs Ana review before sharing |
| Urine therapy booklet | Outline only | Good section map and boundary notes | Needs verse/source selection and actual prose draft |

## Outstanding Decisions For Ana

Highest priority before more intake:

1. **Collaborator access scope:** Should Megan and Fiona receive full read-only access to `the-vessel`, or should they receive selected review packets / a separate limited review surface first?
2. **First review packet:** Should the July 3 source packet be sent to Megan/Fiona for narrow review, or should Ana revise it first?
3. **Water Magicians name:** Is "Water Magicians" still the working name for the pilot?
4. **Support path:** Is the support path ready to become a review packet, or does it stay private drafting?
5. **June synthesis endpoint:** Should June replace May as the SB reader-path endpoint, or stay as a draft/community synthesis?
6. **Living archive visibility:** Should the generated living archive remain hidden/community, become a member map, or get a public excerpt?
7. **Fiona assets:** What specific use, if any, does Fiona approve for her brand assets?
8. **Public method boundary pass:** Should curator review method/protocol pages before any new public or member-facing offer?

## Recommended Next Sequence

### Step 1: Prepare Megan/Fiona Read-Only Entry

Do this before adding more source material.

Create or revise a short collaborator-facing entry note that says:

- what they are being invited into;
- what is private;
- what has been AI-summarized;
- what is not quote-ready;
- where to start;
- what exact review is being asked of them;
- that read-only access is not consent to publish.

The existing draft is:

- `Components/the-vessel/in-development/archive-preservation-preview-for-collaborators-2026-06-28.md`

It is close, but Ana should review it before sharing.

### Step 2: Use A Limited First Review Packet

Recommended first review packet:

- `water-magicians/README.md`
- `telegram-ana-megan-fiona-consent-map.md`
- `water-magicians/alchemy-matter-saturn-microbe-archive-source-packet.md`
- Fiona-specific review notes from `microscopy.md`
- Megan-specific correction context from `megan-feedback-source-correction.md`

Do not ask them to review the whole archive first. Ask for exact corrections on
narrow source uses. If the first access is via GitHub, remember that a direct
repo invite exposes the whole private repo, not only this packet.

### Step 3: Add A Current Water Magicians Board

Create one board, probably in `water-magicians/README.md` or a new `source-packets/README.md`, with columns:

- packet;
- source window;
- current status;
- who needs to review;
- cleared uses;
- blocked uses;
- next action.

This will reduce the feeling that "everything is happening everywhere."

### Step 4: Pause Public Expansion

Do not expand public SB from Water Magicians material yet.

Public SB is stable. The private collaboration layer needs review first.

### Step 5: Keep New Intake Narrow

When Ana brings more into the archive, route each item through the current nine-step flow from report `075`:

1. intent;
2. lane;
3. provenance;
4. sensitivity;
5. index;
6. consent;
7. synthesis;
8. derivative;
9. rule migration.

For collaborator material, default to source packet, not public prose.

## Reports: What Is Current, Redundant, Or Historical

Do not delete reports in this session. Several are redundant as current guidance, but still useful as decision history.

### Current Load-Bearing Reports

Use these for current orientation:

- `reports/analyst/077_full_archive_audit_before_collaborator_invites.md` - this report; current whole-archive state.
- `reports/analyst/075_full_archive_audit_current_intention_flow.md` - previous whole-archive audit; still useful for the June 28 baseline.
- `reports/analyst/074_megan_macdonald_systems_hypothesis_corrected_integration.md` - authoritative Megan attribution correction.
- `reports/curator/070_paid_access_prep_threads_metadata_privacy.md` - access boundary, thread vocabulary, and private community-story routing.
- `reports/analyst/076_ligoldragon_skills_comparison_july5.md` - current answer on LiGoldragon skills versus Aether skills.
- `reports/056_water-magicians-report.md` and `reports/057_sb-dictionary-water-magicians-gap-analysis.md` - useful Water Magicians overview and dictionary gap report, though private files have advanced beyond them.

### Useful But Not Current Task Lists

Keep these as historical/audit trail, but do not use them as current action lists without checking newer reports:

- `reports/analyst/071_current-state-executive-brief-june25.md`
- `reports/analyst/069_sb_flow_value_audit_june19.md`
- `reports/analyst/064_full-review-before-new-data.md`
- `reports/047_full-archive-flow-accuracy-audit-june10.md`
- `reports/043_archive-flow-accuracy-audit-june4.md`
- `reports/039_sovereign-biophysics-archive-review-june1.md`
- `reports/038_sovereign-biophysics-full-review-may29.md`
- `reports/037_archive-stability-executive-report.md`
- `reports/036_whole-git-archive-flow-report.md`
- `reports/035_vessel-public-private-architecture-plan.md`

The substance in these reports has mostly been absorbed into current architecture, queues, boundary files, and newer reports.

### Cleanup Records

Keep:

- `reports/045_reports-cleanup-candidates.md`
- `reports/046_reports-clear-candidate-cleanup.md`

They explain prior deletion decisions and the rule that further deletion needs Ana's approval.

### Possible Future Cleanup Candidates

Only after Ana confirms:

- Older broad audit snapshots that are now superseded by `075` and `077`.
- Old draft reports whose content now lives in site files.
- `reports/021_castaneda-epub-downloads.md` if git history and bibliography inventory are enough provenance.
- `reports/042_june4-fresh-plasma-distillation-log.md` only after a cleaner H2 run replaces it as active provenance.

Do not delete source research reports, bibliography reports, or provenance reports just because they are old.

## Readiness For Megan And Fiona

Ready:

- Private collaboration lane exists.
- Water Magicians index exists.
- Consent map exists.
- Machine transcripts are clearly labeled as navigation aids.
- Megan attribution correction exists.
- Fiona microscopy vocabulary has a private holding place.
- Fiona brand assets are private and checksummed.
- Source-packet workflow has one test packet.
- Local links resolve.
- Repos and submodules are clean.

Not ready:

- Full repo invite without orientation.
- Public use of Water Magicians material.
- Public use of Fiona's newer microscopy vocabulary.
- Public or book use of the first source packet.
- Support path publication.
- Any assumption that read-only access equals consent.

Best invitation posture:

> You are being invited to review how the archive is holding the collaboration, not to approve public use by default. Raw messages, transcripts, summaries, and source packets are private unless you approve a specific use.

## Bottom Line

The archive is ready to pause and receive orientation.

It is not ready to publish the collaboration layer. It is ready to show Megan and Fiona the private holding structure, ask for narrow corrections, and let their review shape the next layer.

The next work is not more architecture. It is review choreography:

- what do they see first;
- what do they correct;
- what stays private;
- what becomes source packet;
- what, eventually, may become public or member-facing.

Once that is clear, more archive material can enter without becoming another fog bank.
