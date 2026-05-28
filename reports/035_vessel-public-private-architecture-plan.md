# 35. Vessel Public / Private Architecture Plan

**Date:** 2026-05-28
**Agent:** Codex / GPT-5
**Role:** analyst
**Session topic:** Clarifying the two Vessel areas, public/private routing, dream records, and whether a second public book exists beside Sovereign Biophysics.

---

## Short Answer

Do not merge the public and private repositories into one public space.

Make them one conceptual Vessel with two access layers:

- **Public layer:** the readable life/dream/body companion archive on the website.
- **Private layer:** the protected member/source archive for operational, intimate, and detailed field records.

The current confusion comes from naming, stale links, duplicated migration copies, and no clear public-summary workflow.

The fix is not to start over.

The fix is to rename the reader-facing roles, clean links, mark source records, and create public summaries for private records where safe.

---

## What Exists Now

### Public Website Layer

Path:

`Components/website/The-Vessel/`

Current role:

- public practitioner account;
- backstory;
- living journal;
- dream records;
- temporal framework;
- portal to contact/community.

This is already public-facing and reads like a companion body to Sovereign Biophysics.

### Private Repo Layer

Path:

`Components/the-vessel/`

Current role:

- private member/source archive;
- operational protocols;
- detailed experiment records;
- intimate field records;
- in-development drafts;
- migration maps and triage.

This is the correct home for material that cannot be public in full.

---

## The Core Distinction

The public website should answer:

> What can be safely read, shared, cited, and used to understand the work?

The private Vessel should answer:

> What must be preserved honestly, with full context, before it is summarized or withheld?

Both belong to the same living work.

They should not be the same access surface.

---

## Recommended Naming

Keep the private repo name:

`Components/the-vessel/`

But change the public-facing website language so it does not feel like a duplicate private repo.

Recommended public name:

**The Living Record**

Working subtitle:

**Dream, body, time, and the life behind Sovereign Biophysics**

This allows:

- `Sovereign Biophysics` to remain the research/method archive;
- `The Living Record` to become the public companion book;
- `The Vessel` to remain the private threshold/member/source container.

The folder name `Components/website/The-Vessel/` can stay for now to avoid link churn. The displayed title and navigation can change first.

---

## Is There A Second Book Beside Sovereign Biophysics?

Yes.

It is already forming.

Sovereign Biophysics is the research body:

- method;
- measurements;
- fractions;
- alchemical translation;
- analysis;
- synthesis;
- claim architecture.

The second public body is the lived companion:

- dreams;
- body perception;
- temporal formation;
- the living year;
- backstory;
- relationship with place;
- nervous system and environmental learning;
- public body-practice reflections that are not operationally intimate.

Possible title:

**The Living Record**

Possible subtitle:

**Dream, Body, Time, and the Life Behind the Work**

This should accompany Sovereign Biophysics rather than compete with it.

---

## Where Dream Entries Belong

Dream entries belong in the public companion layer when they are:

- symbolic;
- reflective;
- not exposing another person;
- not operationally explicit;
- not tied to intimate practice details that require consent or protection.

Path:

`Components/website/The-Vessel/journal/`

Dream entries belong in the private Vessel when they include:

- sexual or mucosal practice context;
- partnered details;
- identifiable relational material;
- operational body-application context;
- content that would become too exposing if read publicly.

Private dream/body records can later produce bounded public summaries.

---

## What To Do With Double Entries

Do not delete duplicates automatically.

Classify them.

Each private record should get one of these statuses:

- **source_only:** kept privately as the original context;
- **public_summary_exists:** a public version exists and should be linked;
- **public_summary_needed:** safe summary should be written;
- **private_only:** not appropriate for public summary yet;
- **superseded:** preserved only for provenance, not active reading.

Example:

`Components/the-vessel/20-experiments-private/experiment-report-aged-plasma-distillation.md`

has a public counterpart:

`Components/website/sovereign-biophysics-distillation/20-experiments/experiment-report-aged-plasma-distillation.md`

The private file should not look like an active duplicate. It should be marked as source/provenance with a link to the public report.

---

## Cross-Reference Pattern

Private records should be able to point outward:

```yaml
public_summary:
  status: exists
  path: Components/website/sovereign-biophysics-distillation/...
```

Public records should not link directly into private operational content unless the reader has access.

Instead, public records can say:

> A protected source record exists in the private Vessel. The public version preserves the claim boundary and omits operational detail.

This lets the public archive acknowledge deeper data without exposing it.

---

## Portal Recommendation

The public portal should become a funnel, not a confusing second archive door.

It should explain:

- the public archive is open;
- the private Vessel is by relationship/access;
- the private layer contains source records and protected operational detail;
- access is not a course or medical service;
- the reader can book a call or enter community first.

Current public portal:

`Components/website/The-Vessel/portal.md`

Recommended display title:

**Enter The Vessel**

or:

**Private Vessel Access**

This keeps the word Vessel for the threshold, not for every public page.

---

## What Can Move Public

Move or summarize public when the content is:

- reflective rather than operational;
- single-subject and non-directive;
- not sexually explicit;
- not mucosal/genital/rectal in practical detail;
- not exposing Olivier or another person without consent;
- useful for understanding the work.

Good public candidates:

- dreams and symbolic reflections;
- perceptual formation;
- environmental timing;
- public body-practice outcomes;
- high-level summaries of private field records;
- philosophical essays about the body and time.

Keep private:

- explicit application sequences;
- mucosal/genital/rectal pathways;
- partnered practice details;
- operational volumes and timing that read as protocol;
- raw field notes with intimate relational charge;
- anything still too alive to be safely framed.

---

## Recommended Cleanup Sequence

### 1. Do Not Move Folders Yet

First change labels, links, and status metadata.

Folder renames can happen later if the public-facing logic holds.

### 2. Fix Stale Public Links

Repair old links such as:

- `../the-vessel.md`
- `../../The-Living-Year/journal/README.md`
- `../the-dream-body.md`

Point them to the current public companion layer or remove them until a public target exists.

### 3. Update Website Navigation Language

Change visible public language from:

`The Vessel`

to:

`The Living Record`

where the page is public journal/backstory/dream material.

Leave the private repo as:

`The Vessel`

### 4. Add Source/Public Summary Metadata To Private Records

Start with:

- `20-experiments-private/experiment-report-aged-plasma-distillation.md`
- all files in `25-intimate-field-private/`

### 5. Build Public Summary Stubs

For private records that can be acknowledged publicly, create bounded public summaries in the relevant public lane.

Example:

- private detailed record: `25-intimate-field-private/2026-05-25-field-note-early-saturation-phase.md`
- possible public summary later: `sovereign-biophysics-distillation/40-synthesis/synthesis-private-application-layer-may-2026.md` or a small note under `The Living Record`

### 6. Refresh Review Queues

Both queues are stale:

- `Components/website/REVIEW_QUEUE.md`
- `Components/the-vessel/QUEUE.md`

They should be rebuilt after the naming and link cleanup.

---

## Proposed Final Architecture

```text
Components/website/
  sovereign-biophysics-distillation/
    # public research book

  The-Vessel/                    # folder can remain for now
    README.md                    # displayed as The Living Record
    backstory/
    journal/
    living-year.md
    portal.md                    # private Vessel access funnel

Components/the-vessel/
  00-welcome/
  10-method-private/
  20-experiments-private/
  25-intimate-field-private/
  40-synthesis-private/
  80-archive-raw/
  90-ops/
```

Conceptually:

```text
Sovereign Biophysics = the research book.
The Living Record = the public companion book.
The Vessel = the private source/member container.
```

---

## Recommendation

The next working session should be a curator cleanup, not a content-writing session.

Scope:

1. Repair stale public links.
2. Rename public-facing `The Vessel` labels to `The Living Record` without moving folders.
3. Add private/public summary metadata to the obvious duplicate/source files.
4. Update the portal so it clearly funnels readers toward private access.
5. Refresh the queues.

After that, write the first bounded public summaries from private records.

The archive does not need to be restarted.

It needs a clearer threshold.
