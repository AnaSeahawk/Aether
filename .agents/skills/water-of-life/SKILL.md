---
name: water-of-life
description: Intake, processing, and stewardship skill for The Water of Life open observational archive. Handles contributor templates, transcript formatting, entry validation, and framing discipline.
---

# Skill — The Water of Life Archive

*Intake, processing, and stewardship for a participatory observational archive.*

---

## What this skill is for

Use this skill when working with contributor data for The Water of Life archive:

- generating or adapting the contributor template
- processing audio transcripts into archive-format entries
- validating entries for framing compliance
- organizing and indexing the archive
- evolving the template or methodology as the archive grows

---

## The archive's position

The Water of Life is an open-source, participatory observational archive
collecting first-person accounts of engagement with auto-urine practice.

It is **not** a medical resource, treatment guide, or advocacy site. It makes
no therapeutic claims. It collects self-reported observations with concurrent
factors documented, in the contributor's own language.

The archive exists because:

- No controlled clinical trials on auto-urine therapy in humans exist.
- The dismissal of the practice is based on absence of evidence, not evidence
  of absence.
- The historical record (Damar Tantra, Sushruta Samhita, Bhava Prakasha,
  Hatha Yoga Pradipika, Armstrong 1944) is extensive but entirely
  practitioner-narrated, not self-reported.
- People who practice often hide it. The data that does exist is scattered,
  anecdotal, and frequently suppressed by platform content policies.
- No one has built the dataset. This archive builds it.

---

## Framing discipline

This is the most important section of this skill. Every piece of text that
enters or leaves this archive must follow these rules.

### Language rules

| Use | Never use |
|---|---|
| "I observed..." | "It cured..." |
| "I noticed..." | "It treated..." |
| "During this period..." | "The therapy..." |
| "My engagement included..." | "My treatment was..." |
| "What I was experiencing before..." | "My diagnosis was..." / "I had [disease]..." |
| "What else was happening in my life..." | "No other treatment was needed..." |
| "Changes I noticed..." | "Results..." / "Outcomes..." |

### Structural rules

1. **No diagnostic labels as categories.** Do not organize entries by condition
   name. The archive is organized by contributor, not by pathology.
2. **No causal claims.** Correlation is documented. Causation is never stated.
3. **Concurrent factors are mandatory.** Every entry must document what else was
   happening: other treatments, diet, lifestyle, stress, environment. An entry
   without concurrent factors is incomplete.
4. **The contributor is the observer.** The archive does not interpret, diagnose,
   or evaluate. It holds what the person said they experienced.
5. **No prescriptive language.** The archive never tells anyone to do anything.

### When processing transcripts

Audio interviews will contain natural speech that may include diagnostic labels,
causal claims, or prescriptive statements. When formatting a transcript into an
archive entry:

- Preserve the contributor's words in the transcript section verbatim.
- In the structured summary, reframe into observational language.
- Flag any statements that make direct therapeutic claims — do not delete them,
  but note them as the contributor's personal interpretation, not the archive's
  position.

---

## Entry format

Every archive entry is a markdown file in `Components/the-water-of-life/entries/`.

Filename: `YYYYMMDD-<pseudonym-or-anon-id>.md`

```markdown
---
entry_id: <unique identifier>
date: YYYY-MM-DD
contributor: <chosen name or "anonymous">
method: written | interview | audio-transcription
status: draft | review | published
---

# Entry: <contributor name or anonymous identifier>

## Context

<Age range, general life context — only what the contributor chose to share.>

## What brought them here

<What they were noticing in their body or life that led them to explore this
practice. In their own language. No diagnostic labels required.>

## Their practice

<What they do, which pathways, how often, how long they have been engaged.
Specifics are the contributor's choice — some share extensively, some share
minimally. Both are valid.>

## The full picture

<Everything else happening during the period of engagement: other treatments,
dietary changes, lifestyle shifts, stress levels, environment, relationships,
work. This section is what gives the entry its integrity.>

## What they observed

<Changes, shifts, surprises, things that stayed the same. In their own words.
No interpretation imposed.>

## Timeline

<When they began, any phases or turning points, duration at time of entry.>

## In their own words

<Open space for anything the template did not ask. The contributor's voice,
unstructured.>
```

When the entry comes from an audio interview, add a `## Full transcript` section
at the end containing the complete transcription.

---

## One person, one entry

Each contributor receives a unique identifier. The archive accepts one primary
entry per contributor. Updates or follow-up observations are appended to the
existing entry, not created as new entries.

The identifier system (cryptographic key pairs for pseudonymous deduplication)
is documented in the methodology. Until the key infrastructure is built,
deduplication is managed manually by the archive steward.

---

## Privacy

Contributors choose their level of visibility:

- **Named**: real name appears on the entry
- **Pseudonym**: chosen name, no link to real identity in the archive
- **Anonymous**: entry carries only the unique identifier

Raw recordings (audio/video) are retained by the archive steward but never
published. Only the transcript enters the public archive.

---

## Evolving this skill

This archive will change as it grows. When a pattern emerges that the current
template does not capture, or when a framing problem is discovered:

1. Document the issue in `Components/the-water-of-life/methodology/`.
2. Update this skill file.
3. Do not retroactively alter existing entries to fit new structure — append
   notes or create a methodology record explaining the evolution.

The archive's integrity depends on its entries reflecting what was asked and
answered at the time, not what we later wished we had asked.

---

## See also

- `Components/the-water-of-life/methodology/founding-document.md`
- `Components/the-water-of-life/templates/contributor-template.md`
- `.agents/skills/sensitive-content/SKILL.md`
- `.agents/skills/prose/SKILL.md`
- `soul.md`
