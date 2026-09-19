---
name: water-of-life
description: Intake, processing, and stewardship skill for The Water of Life — a public, participatory observational archive for auto-urine practice. Handles observation formatting, transcript processing, framing discipline, and editorial principles.
---

# Skill — The Water of Life Archive

*Intake, processing, and stewardship for a collective field notebook.*

---

## What this skill is for

Use this skill when:

- Preparing a form submission for review and approved publication
- Formatting an interview transcript into an observation
- Validating observations for framing compliance
- Working on the website or archive structure
- Evolving the methodology as the archive grows

---

## Repositories

- **Website:** `/home/bird/Git/the-water-of-life/` → `github.com/AnaSeahawk/the-water-of-life`
  - Hugo static site, deployed to GitHub Pages
  - Site lives at `https://anaseahawk.github.io/the-water-of-life/`
  - Hugo template functions (`relURL` etc.) do NOT work in content `.md` files — only in layout templates. Use relative paths (`../privacy/`) in content.
- **Aether repo:** `/home/bird/Git/aether/Components/the-water-of-life/`
  - Methodology and templates (synced with website versions)
  - Skill file at `.agents/skills/water-of-life/SKILL.md`

When editing the founding document, sync both copies.

---

## The archive's position

The Water of Life is a public, participatory observational archive
collecting first-person accounts of engagement with auto-urine practice.

It is **not** a medical resource, treatment guide, or advocacy site. It
makes no therapeutic claims. It collects self-reported observations with
concurrent factors documented, in the contributor's own words.

As of August 2026, no controlled clinical trial evaluating auto-urine
practice as a therapeutic intervention in humans has been identified.
Published literature does exist — historical reviews, case reports,
laboratory work, hypotheses — but it does not establish clinical
efficacy. The absence of that evidence is a gap, not a verdict.

---

## Framing discipline

Every piece of text that enters or leaves this archive must follow
these rules.

### Language rules

| Use | Never use |
|---|---|
| "I observed..." | "It cured..." |
| "I noticed..." | "It treated..." |
| "During this period..." | "The therapy..." |
| "What else was happening..." | "No other treatment was needed..." |
| "Changes I noticed..." | "Results..." / "Outcomes..." |

### Structural rules

1. **No diagnostic labels as categories.** Observations are not
   organized by condition.
2. **No causal claims.** Correlation is documented. Causation is never
   stated by the archive.
3. **Concurrent factors are mandatory.** Every observation must document
   what else was happening. An observation without concurrent factors is
   incomplete.
4. **The contributor is the observer.** The archive holds what they said.
5. **No prescriptive language.** The archive never tells anyone to do
   anything.

---

## Editorial principles

These were established while processing the first observations:

1. **First person.** Observations are published in the contributor's own
   voice, exactly as they gave them. Do not convert to third person.
2. **Preserve their words.** Correct grammar, clarify sequence, remove
   unnecessary repetition — but do not change the meaning or intensity
   of what someone said.
3. **Their interpretation stays theirs.** If a contributor says "I felt
   I was about to have a stroke" or "I feel it saved my life," that is
   their experience. Keep it as their interpretation, not silently
   convert it into the archive's claim or soften it into something they
   didn't say.
4. **Every form field they filled out appears in the published
   observation.** Pathways, duration, overall experience, concurrent
   factors — nothing submitted gets silently dropped.

---

## Observation format

The archive uses a field notebook model. The basic unit is an
**observation** — a short, first-person record of what someone did,
what they noticed, and what else was happening at the time.

Every observation is a markdown file in `site/content/entries/`.

Filename: `YYYYMMDD-NNN.md` (date + sequence number)

```markdown
---
title: "Observation NNN"
date: YYYY-MM-DD
contributor: <display name or "anonymous">
overall: <positive | neutral | mixed | negative | stopped>
---

## Practice

**Pathways:** <list all pathways used, inline>

**Duration:** <how long, how often>

**Overall:** <positive | neutral | mixed | negative | stopped>

## What I observed

<Their words. First person. What they did, what they noticed, what
changed, what didn't, what surprised them.>

## What else was happening

<Concurrent factors. Other treatments, diet, lifestyle, stress,
medications, environment. Their words.>
```

Optional additions if the contributor provided them:
- Display name (otherwise anonymous)
- Age range
- "Anything else" section

### Processing a form submission

1. Receive the submission within the authorized intake scope and keep the raw
   record private.
2. Prepare a private draft using the template above. Preserve the contributor's
   first-person language and intensity; apply the sensitive-content skill to
   its working location. Do not place an unapproved draft in the public repo.
3. Verify contributor consent for the proposed text and public display identity.
   A submission alone is not proof of consent beyond what its form recorded.
4. Prepare and check the proposed publication. Use Ana's explicit approval for
   that release if already given; otherwise present the completed draft for it.
5. Once the release is authorized, install the observation in
   `site/content/entries/`, build, review the output, and commit/push only the
   approved paths under the coordination protocol.
6. Retain the raw Formspree submission and email unless Ana separately
   authorizes deletion of those exact records. Verify the retained derivative
   before carrying out an authorized deletion.

### Processing an interview

1. Transcribe the recording using the audio-transcription skill and its upload
   authorization requirements; keep the recording and working draft private.
2. Extract the observation from the conversation — what they did, what
   they noticed, what else was happening
3. Format in first person using their words
4. Prepare the draft for contributor review. Send it only when communication
   with that contributor is explicitly authorized; otherwise return it to Ana.
5. Verify contributor approval and Ana's separate release approval, honoring
   either when already given for this exact release. Then publish using the
   checked form-submission release steps above.
6. Preserve the recording until the transcript is committed, pushed, and
   independently verified. Delete it only on a separate explicit request.

---

## One person, many observations

A person can contribute as often as they want. Observations stand alone.
Where a contributor uses a display name, related observations may
naturally become identifiable as part of an ongoing record. There is no
identity management system, no deduplication infrastructure, no key
pairs. If that's needed someday, build it then.

---

## Privacy

Contributors choose how they appear: a display name or anonymous (the
default). The form collects no email addresses.

Audio recordings and raw submissions remain private. Contributor approval and
publication do not authorize source deletion. Follow a separately authorized
retention/deletion instruction for the exact records; surface any conflict with
an existing consent or retention commitment before further processing.

Contact for data rights is through [anaseahawk.com](https://anaseahawk.com),
not a published email address.

---

## Licensing

Licensing for published observations has not yet been decided. CC BY 4.0
was considered and deliberately deferred — solve when there are
thousands of observations, not before. Do not add licensing language to
the form or consent without explicit direction.

---

## Technical notes

- **Hugo version:** 0.164.0 extended
- **Form backend:** Formspree (`https://formspree.io/f/xnpqnbzk`), 50 submissions/month free tier
- **Booking:** `https://cal.com/anaseahawk/the-water-of-life-a-conversation`
- **Template functions in content files:** Hugo does NOT process Go template syntax (`relURL`, etc.) in `.md` content files. Use relative paths (`../privacy/`, `../images/foo.jpg`) instead.
- **GitHub Pages base path:** site lives at `/the-water-of-life/`, not root

---

## Evolving this skill

When a pattern emerges that the current model does not capture, or when
a framing problem is discovered:

1. Document the issue in `Components/the-water-of-life/methodology/`.
2. Update this skill file.
3. Do not retroactively alter existing observations to fit new
   structure — the archive's integrity depends on observations
   reflecting what was asked and answered at the time.

Before adding any new field, consent layer, classification system, or
methodology requirement, answer: "What will this let us see that we
cannot see without it?" If the answer isn't compelling, don't add it.

---

## See also

- `Components/the-water-of-life/methodology/founding-document.md`
- `Components/the-water-of-life/templates/contributor-template.md`
- `Components/the-water-of-life/templates/interview-guide.md`
- `.agents/skills/sensitive-content/SKILL.md`
