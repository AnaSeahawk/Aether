---
name: water-of-life
description: Intake, processing, and stewardship skill for The Water of Life — a cooperative observational archive for auto-urine practice. Handles retelling accounts, transcript processing, framing discipline, and editorial principles.
---

# Skill — The Water of Life Archive

*Intake, processing, and stewardship for a collective field notebook.*

---

## What this skill is for

Use this skill when:

- Retelling a form submission for review and approved publication
- Retelling an interview as an observation
- Validating observations for framing compliance
- Working on the website or archive structure
- Evolving the methodology as the archive grows

---

## Who holds the archive

The Water of Life is a cooperative archive, maintained by Ana Seahawk
with the support of Fiona Gardner (GitHub `fiology`) and Megan Macdonald
(GitHub `ExpansionHealing`). Ana maintains it; Fiona and Megan support
it. On the site their names link to `anaseahawk.com`,
`fionagardner.org`, and `expansionhealing.ca`.

---

## Repositories

- **Website (public):** `/home/bird/Git/the-water-of-life/` →
  `github.com/AnaSeahawk/the-water-of-life`
  - Hugo static site, deployed to GitHub Pages
  - Site lives at `https://anaseahawk.github.io/the-water-of-life/`
  - Hugo template functions (`relURL` etc.) do NOT work in content `.md`
    files — only in layout templates. Use relative paths (`../privacy/`)
    in content.
- **Keeping (private):** `/home/bird/Git/water-of-life-keeping/` →
  `github.com/AnaSeahawk/water-of-life-keeping`
  - `in-progress/` — a retelling until it is published, then deleted
  - `mailing-list.md` — emails left for news of upcoming events
  - `originals/` — the 005 and 006 originals only; no new originals
- **Aether:** `/home/bird/Git/aether/Components/the-water-of-life/`
  - Methodology and templates (synced with website versions)

The founding document exists in three copies: the website's
`site/content/methodology/founding-document.md` and
`methodology/founding-document.md`, and Aether's
`Components/the-water-of-life/methodology/founding-document.md`. Edit
all three together.

Water of Life material does not go in the Vessel.

---

## The archive's position

The Water of Life collects accounts of engagement with auto-urine
practice, retold with light editing in the contributor's own voice.

It is **not** a medical resource, treatment guide, or advocacy site. It
makes no therapeutic claims. It holds self-reported observations with
concurrent factors documented.

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

These rules govern the archive's own words. A contributor's own
interpretation, kept in their voice, stays theirs (see below).

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

1. **Retold in the contributor's voice.** Accounts are retold with light
   editing and stay in first person, the way the contributor gave them.
   Do not convert to third person.
2. **Light editing.** Correct grammar and spelling, clarify sequence,
   write out shorthand, remove unnecessary repetition. Do not change the
   meaning or intensity of what someone said.
3. **Their interpretation stays theirs.** If a contributor says "I felt
   I was about to have a stroke," "I feel it saved my life," or "it is
   the only treatment that has ever cleared my dandruff," keep it as
   their interpretation. Do not convert it into the archive's claim or
   soften it into something they didn't say.
4. **Every observation field they filled out appears.** Pathways,
   duration, overall experience, concurrent factors, anything else —
   nothing submitted gets silently dropped. Email is the exception: it
   goes only to the mailing list.
5. **When unsure of a correction, ask Ana.** Name what changed and why
   when presenting a draft.

---

## Observation format

The basic unit is an **observation** — a short, first-person record of
what someone did, what they noticed, and what else was happening at the
time. On the site, the call to contribute is "Share an account"; the
published entry is titled "Observation NNN".

Every observation is a markdown file in `site/content/entries/`.

Filename: `YYYYMMDD-NNN.md` — the date the account was submitted, and
the next sequence number. A late entry keeps its submission date, even
when that places it out of order.

```markdown
---
title: "Observation NNN"
date: YYYY-MM-DD
contributor: <display name or "anonymous">
overall: <positive | neutral | mixed | negative | stopped | stopped-other>
---

## Practice

**Pathways:** <list all pathways used, inline>

**Duration:** <how long, how often>

**Overall:** <same value as front matter>

## What I observed

<Their words, lightly edited. First person.>

## What else was happening

<Age range, if given. Concurrent factors. Their words.>
```

Add `## Anything else` when the contributor filled that field.

---

## Consent and authority

The form's consent checkbox and the privacy page together constitute the
contributor's consent to retelling, light editing, and publication.
Ana's role is editorial review: framing, formatting, and readiness. She
does not re-verify consent the form already captured. Contributor
consent does not replace Ana's publication approval.

### Terms by date

- **Shared on or after 2026-11-07:** the account stays once published.
  A named contributor can ask for their name to come off the public
  site; the account stays. No original is kept.
- **Observations 001–006 (shared before 2026-11-07):** given under the
  earlier terms, which included removal of the whole observation on
  request. Honor that for them.

---

## Processing a form submission

1. Find the submission in Ana's email (Formspree, subject "New
   submission from Water of Life Contributions"). Read it; do not save
   a copy of the original anywhere.
2. Retell it in the format above, with light editing. Keep any working
   draft in `water-of-life-keeping/in-progress/` or in chat — never in
   the public repo before approval.
3. Present the draft to Ana with a short list of what changed. Use her
   explicit approval if already given.
4. Once approved, install the observation in `site/content/entries/`,
   build, review the output, commit, push, and confirm it is live.
5. If the contributor left an email, add it with the date to
   `water-of-life-keeping/mailing-list.md`, with nothing else about them.
   Commit and push.
6. Delete the submission email permanently (including from Trash), and
   delete any `in-progress/` draft. Ana clears Formspree herself.

---

## Processing an interview

1. Transcribe the recording using the audio-transcription skill and its
   upload authorization requirements; keep the recording and transcript
   private.
2. Retell the account in the contributor's voice, in the format above.
3. Prepare the draft for contributor review. Send it only when
   communication with that contributor is explicitly authorized;
   otherwise return it to Ana.
4. After the contributor approves the text and Ana approves publication,
   install and push as in the form steps.
5. Delete the recording and transcript once the account is retold and
   published.

---

## One person, many observations

A person can contribute as often as they want. Observations stand alone.
Where a contributor uses a display name, related observations may
naturally become identifiable as part of an ongoing record. There is no
identity management system and no linking by email.

---

## Privacy

What the privacy page promises, and this workflow keeps:

- A name appears only when one is given; it comes off the site on request.
- Email is optional and only for the mailing list of upcoming events.
  Never published, never connected to an account.
- The submission is deleted once the account is published; recordings
  once the account is retold.
- Submissions and the mailing list are seen by the archive's keepers
  (Ana, with Fiona and Megan supporting). Everyday tools keep it
  running: email, Formspree, GitHub.
- No cookies, analytics, or tracking.

Removing a name means removing it from the public site. Git history
rewriting is not promised.

Site copy follows the prose skill: noun-led, with "I" and "you" kept
sparse.

Contact for requests is through [anaseahawk.com](https://anaseahawk.com).

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
- **Logo:** none yet. The Ana Seahawk emblem is not the archive's logo; leave the spot blank.

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
- `.agents/skills/prose/SKILL.md`
