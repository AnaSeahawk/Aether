---
name: solar-journal
description: Design and content skill for The Solar Journal — a timeless physical journal organized by the 360° solar cycle, not the Gregorian calendar. Covers the calendar system, notation, astronomical references, and journal structure.
---

# Skill — The Solar Journal

*A physical journal where the organizing principle is the 360° solar cycle.*

---

## What this skill is for

Use this skill when:

- Designing pages or sections for The Solar Journal
- Working with the degree-based date notation
- Converting between Gregorian, solar degree, and Annus Mundi dates
- Building the front-matter codebook (degree key, moon phases, etc.)

Product content for each page (tables, diagrams, calculations) lives in
`references/front-matter-content.md`. Phoenix cosmology and terminology
live in `references/phoenix-architecture.md`. This file holds the
operating decisions.

---

## Voice, language, and archive sources

The Solar Journal is one expression of **The Living Year** — a body of
work already being developed inside The Vessel. The journal's language
should be built from the established voice in that archive.

### Key source files

Read these before writing or rewriting any journal prose:

- `Components/the-vessel/in-development/alchemy-of-return/fragments/time-orientation-aphorisms.md`
- `Components/the-vessel/in-development/alchemy-of-return/notes/integration-decisions.md`
- `Components/the-vessel/in-development/alchemy-of-return/source-packets/living-year-time-orientation-packet.md`
- `Components/website/The-Vessel/living-year.md`

### Writing posture

The journal must never take a defensive or corrective posture. Don't
define it by what it isn't. Don't argue with conventional timekeeping.
Don't position the journal as a replacement for the Gregorian calendar.

The reader picked up the journal. They're already here. The posture is
handing someone a brass instrument and saying *here — hold this*, not
explaining why their phone is wrong.

Preferred language: return, re-entry, orientation, restored relationship,
finding the way back.

### Established aphorisms (use these, don't reinvent)

- "The Sun tells the time of day. The watch tells when to catch the train."
- "Civil time coordinates society. Solar time orients life."
- "The calendar names it. The sky locates it."
- "Life is not happening on a flat calendar. Life is unfolding under a moving sky."
- "Before interpretation, orientation. Before analysis, location. Before the story, the field."
- "The journal is not only a record. It is a way of being placed again."
- "The clock is not wrong. It is simply not the only authority."
- "This is not a system to follow. It is an orientation."

---

## Core concepts

### Two kinds of time

1. **Astronomical / natural time** — the primary calendar. The sun's
   position on the ecliptic, measured in degrees 1°–360°.
2. **"Train time"** — the Gregorian calendar. Used for coordination with
   the conventional world. Always secondary, always lowercase, always
   small in the layout.

### The solar year

- Starts at Aries 1° (~March 20 Gregorian).
- Runs 1°–360°. There is no 0° — "0° doesn't exist in a real circle."
- Each sign spans exactly 30°.
- One degree ≈ one day (~0.9856° per day, varies with orbital speed).

### Annus Mundi year count

From Jason Breshears' Archaix research. An ancient year-count system
predating Anno Domini.

**Conversion formulas:**

- CE dates: AM = 3894 + CE year
- BCE dates: AM = 3895 − BCE year

**Reference point:** Great Pyramid constructed at 1080 AM = 2815 BCE.

There is no year zero between 1 BCE and 1 CE.

**Year boundary:** The AM year ticks over at the Aries ingress (when
the Sun enters tropical Aries, ~March 20). This is the same boundary
the Phoenix calculator uses. The simple formula gives the AM year for
a Gregorian year; for dates between January 1 and the Aries ingress,
the AM year is still the previous one.

### The journal is timeless

No year is printed. Users buy it anytime, fill in their own year
(Gregorian, Annus Mundi, or both). The first act is finding where they
are astronomically.

---

## Notation system

The journal teaches a compact date notation using the ordinal
indicator º (U+00BA):

- **5920 · ♈ 15º** — Annus Mundi year, sign glyph, degree within sign
- **♈ 15º** — sign-relative
- **15º** — absolute degree
- **2026 · 15º** — Gregorian year + absolute degree

Any of these is a complete date.

---

## Degree key — sign/degree/Gregorian correspondence

| Glyph | Sign | Degrees | Absolute | ~Gregorian | Element | Modality | Polarity | Body |
|---|---|---|---|---|---|---|---|---|
| ♈ | Aries | 1°–30° | 1°–30° | Mar 20 – Apr 19 | Fire | Cardinal | Masc. | Head |
| ♉ | Taurus | 1°–30° | 31°–60° | Apr 20 – May 20 | Earth | Fixed | Fem. | Neck, throat |
| ♊ | Gemini | 1°–30° | 61°–90° | May 21 – Jun 20 | Air | Mutable | Masc. | Arms, lungs |
| ♋ | Cancer | 1°–30° | 91°–120° | Jun 21 – Jul 22 | Water | Cardinal | Fem. | Chest, stomach |
| ♌ | Leo | 1°–30° | 121°–150° | Jul 23 – Aug 22 | Fire | Fixed | Masc. | Heart, spine |
| ♍ | Virgo | 1°–30° | 151°–180° | Aug 23 – Sep 22 | Earth | Mutable | Fem. | Intestines |
| ♎ | Libra | 1°–30° | 181°–210° | Sep 23 – Oct 22 | Air | Cardinal | Masc. | Kidneys, lower back |
| ♏ | Scorpio | 1°–30° | 211°–240° | Oct 23 – Nov 21 | Water | Fixed | Fem. | Reproductive organs |
| ♐ | Sagittarius | 1°–30° | 241°–270° | Nov 22 – Dec 21 | Fire | Mutable | Masc. | Hips, thighs |
| ♑ | Capricorn | 1°–30° | 271°–300° | Dec 22 – Jan 19 | Earth | Cardinal | Fem. | Knees, bones |
| ♒ | Aquarius | 1°–30° | 301°–330° | Jan 20 – Feb 18 | Air | Fixed | Masc. | Ankles, circulation |
| ♓ | Pisces | 1°–30° | 331°–360° | Feb 19 – Mar 20 | Water | Mutable | Fem. | Feet |

Gregorian dates are approximate (±1 day per year). Degree ranges use
en dash (–), not hyphen.

---

## This is not a day planner

Settled by Ana 2026-09-08.

The reader does **not** write every day. They write when they have
something to record — sometimes days apart. The journal is for seeing
seasons and patterns, not for keeping a streak.

**The body pages are not daily-entry pages.** Do not build 360 dated
slots. Do not name a template `daily-entry`. Do not write copy that
presumes daily writing.

An entry begins when the reader begins it. The coordinates are
recorded at the moment of writing, whenever that is.

---

## Tracks recorded per entry

Each entry captures:

1. **Sun degree** — sign glyph + ordinal degree. This is the date.
2. **Moon degree and phase** — sign glyph + ordinal degree, plus the
   phase symbol.
3. **Year** — Annus Mundi, Gregorian, or both.
4. **Location** — latitude and longitude. Written once, updated when
   the reader moves.
5. **Solar time** — sunrise, noon, sunset. Looked up for the reader's
   coordinates, not estimated. The point is to see the gap between
   solar noon and clock noon.
6. **Quarter** — which quarter of the year (Spring, Summer, Autumn,
   Winter).
7. **Train time** — Gregorian date. Optional, small, secondary.

Plus ruled writing lines for the entry itself.

**Removed fields:** "Light" was removed by Ana and replaced by
"Quarter." There is no Light field.

### Solar time is looked up, not observed

An earlier draft said "Observed, not looked up." Ana reversed this
(2026-09-07): the point of recording solar time is to *see the gap*
between solar noon and clock noon. You cannot see a gap you estimated —
you have to look up real figures for your coordinates.

**Terms:** the body's ~24-hour cycle entrained by light is the
**circadian rhythm**. The strain of living out of step with it is
**social jetlag** (Till Roenneberg, 2006).

Keep the posture: name the gap, give the reader the means to measure
their own, and stop. Do not argue with the clock, and do not list
diseases.

---

## Design tokens

- **Fonts:** Cormorant Garamond (display/serif), Cormorant SC (small
  caps labels), IBM Plex Sans (body/labels/sans)
- **Colors:**
  - `--parchment` `#f5f0e8` — warm background
  - `--ink` `#8b6f47` — secondary text, labels
  - `--dark` `#3d3428` — primary text, all glyphs
  - `--gold` `#c4a97d` — accent: decorative lines, sine wave, borders
  - `--field` `#e8dfd3` — input fields, moon phase fill
  - `--rule` `#d4c9b8` — subtle dividers
  - `--faint` `#f0ebe2` — callout backgrounds
  - `--white` `#faf8f4` — lightest surface
- **Trim size:** A5 — 148 × 210 mm. Author in physical units (mm, pt)
  with `@page { size: 148mm 210mm }`. Never author in px.
- **Margins:** 13mm top, 12mm sides, 11mm bottom → 124mm content width
- **Type floor: 7pt.** Nothing smaller, anywhere, including inside SVG.
  Body 10pt, small 8pt, labels 7.5–9pt.
- **SVG diagrams:** viewBox 500 units across a 124mm measure = 0.248mm
  per unit, so a label needs ≥10 units to clear 7pt.

### Three presentations, one source

Print is the real page. Desktop zooms the A5 page up; phone reflows to
a single column with page geometry dropped. Do not try to make them
identical.

### Fillable

Ruled blanks are real `<input>` elements styled as rules: they print as
empty lines and are typeable on screen. Entries persist per viewer via
`localStorage`, and via the `db` capability when the viewer's runtime
grants it.

### The degree mark renders inconsistently

Fixed by binding U+00BA to a single family with
`@font-face { unicode-range: U+00BA }`.

### Monochrome glyphs

All zodiac and planet glyphs use `var(--dark)`. No element-based
coloring — that system was explored and deliberately removed.
`var(--gold)` is the accent color, not a glyph color.

### Pluto glyph

The bident-with-large-orb variant, rendered as inline SVG (not the
standard Unicode ♇). Source: Wikimedia Commons.

### Don't repeat the zodiac glyphs

The twelve glyphs appear on the sine wave, the phase page, the degree
key, the element/modality tables, and the body map. That is enough.
Before adding another set of twelve, ask what it tells the reader that
the table beside it does not.

---

## Where the journal lives

- **Repo:** `AnaSeahawk/solar-journal` — **private**, mounted at
  `Components/solar-journal/`. Holds artboards, `canvas.json`, and
  published canvas under `published/`.
- **This skill** stays in `aether`: skills belong to the coordination seed.
- **Artifact (current):** `https://claude.ai/code/artifact/44896e33-8c4d-4470-92fb-2d1ed696ec48`
- **Trim:** A5, 148 × 210 mm
- **Superseded:** branch `claude/journal-design-tv0uqe` — history only,
  not the working copy.

The repo is private because the journal is an unreleased product.

### Related skill

`phoenix-calculator` implements the 138° Phoenix sequence
computationally. Read it before building page x (The Phoenix) or any
Personal Phoenix Point content, so the printed values and the
calculator agree.

---

## Journal sections (content plan)

Front matter / codebook (11 pages built in artifact):
- [x] Page i — How to Begin
- [x] Page ii — The Year as a Wave
- [x] Page iii — Eight Moon Phases
- [x] Page iv — Your Birth & Solar Return
- [x] Page v — The Glyphs
- [x] Page vi — The Degree Key
- [x] Page vii — Grammar of the Signs
- [x] Page viii — The Zodiac Man (placeholder for drawn figure)
- [x] Page ix — The Notation
- [x] Page x — The Phoenix
- [x] Page xi — How to Mark Time
- [x] Photograph: instruments on grey wool

Repeating sections (×12, one per sign — not yet started):
- [ ] Sign opener — glyph, name, degree range, properties, train time reference
- [ ] Entry pages — sun position, moon, solar time, writing lines
- [ ] Moon tracker — 29+1 circles to shade, cycle fields, observations space

---

## See also

- `references/front-matter-content.md` — product content for each page
- `references/phoenix-architecture.md` — Phoenix cosmology and terms
- `.agents/skills/phoenix-calculator/SKILL.md` — computation skill
- `Components/solar-journal/` — the private product repo
- `soul.md` — voice, themes, and boundaries
