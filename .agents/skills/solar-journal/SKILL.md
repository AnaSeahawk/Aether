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
- Creating artboard mockups on the `claude/journal-design-tv0uqe` branch

---

## Voice, language, and archive sources

The Solar Journal is one expression of **The Living Year** — a body of
work already being developed inside The Vessel. The journal's language
should be built from the established voice in that archive, not invented
fresh each time.

### Key source files

Read these before writing or rewriting any journal prose:

- `Components/the-vessel/in-development/alchemy-of-return/fragments/time-orientation-aphorisms.md`
  — compact distillation of reusable aphorisms
- `Components/the-vessel/in-development/alchemy-of-return/notes/integration-decisions.md`
  — voice guidance: "The archive voice comes first"
- `Components/the-vessel/in-development/alchemy-of-return/source-packets/living-year-time-orientation-packet.md`
  — 800-line source material with first-person voice
- `Components/website/The-Vessel/living-year.md`
  — public-facing draft with lunar/solar layers

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
predating Anno Domini, compiled from records at the Alexandrian Library
starting in the 3rd century BCE. Structurally connected to the Phoenix
cycle (552 years = 4 × 138 years).

**Conversion formulas:**

- CE dates: AM = 3894 + CE year
- BCE dates: AM = 3895 − BCE year

**Reference point:** Great Pyramid constructed at 1080 AM = 2815 BCE.

**Current year:** 2026 CE = 5920 AM.

There is no year zero between 1 BCE and 1 CE.

### The journal is timeless

No year is printed. Users buy it anytime, fill in their own year
(Gregorian, Annus Mundi, or both). The first act is finding where they
are astronomically — checking astro.com or an ephemeris.

---

## Notation system

The journal teaches users a compact date notation using the ordinal
indicator º (U+00BA — circle on bar, see "The degree mark" section):

- **5920 · ♈ 15º** — Annus Mundi year, sign glyph, degree within sign
- **♈ 15º** — sign-relative (the key tells them what's implied)
- **15º** — absolute degree (the key maps it to Aries)
- **2026 · 15º** — Gregorian year + absolute degree

Any of these is a complete date. No month or day of the week needed.

---

## Degree key — sign/degree/Gregorian correspondence

The front-matter codebook maps all three systems. Each sign includes
its Unicode glyph, element, modality, polarity, and body
correspondence.

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

Gregorian dates are approximate (±1 day per year due to leap years
and variable orbital speed). The journal notes this and directs users
to an ephemeris for their specific year.

Degree ranges use en dash (–), not hyphen.

---

## Elements, modalities, polarity, and the Zodiac Man

The front matter teaches these as the basic grammar of the signs —
the patterns that make the twelve signs intelligible as a system
rather than a list to memorize.

### The four elements

Every sign belongs to one of four elements. The elements cycle in
order through the zodiac: Fire, Earth, Air, Water, repeating three
times.

| Element | Signs | Quality |
|---|---|---|
| **Fire** | ♈ Aries, ♌ Leo, ♐ Sagittarius | Active, energizing |
| **Earth** | ♉ Taurus, ♍ Virgo, ♑ Capricorn | Grounding, material |
| **Air** | ♊ Gemini, ♎ Libra, ♒ Aquarius | Mental, connective |
| **Water** | ♋ Cancer, ♏ Scorpio, ♓ Pisces | Emotional, intuitive |

### The three modalities

Every sign operates in one of three modes. The modalities cycle in
order: Cardinal, Fixed, Mutable, repeating four times. Each element
has one sign in each modality.

| Modality | Signs | Function |
|---|---|---|
| **Cardinal** | ♈ ♋ ♎ ♑ | Initiating — starts the season |
| **Fixed** | ♉ ♌ ♏ ♒ | Stabilizing — holds the season |
| **Mutable** | ♊ ♍ ♐ ♓ | Adapting — transitions between seasons |

The four cardinal signs mark the four quarters of the year (the
equinoxes and solstices on the sine wave).

### Masculine and feminine polarity

The signs alternate: Aries is masculine, Taurus is feminine, Gemini
is masculine, and so on through the entire zodiac. This alternation
produces a rhythm — active/receptive, electric/magnetic — that runs
through the year.

All Fire and Air signs are masculine. All Earth and Water signs are
feminine.

### The Zodiac Man (body correspondence)

The twelve signs map to the human body in descending order from head
to feet. This is one of the oldest astrological systems — the
*Homo Signorum* — appearing in manuscripts for centuries.

| Sign | Body region |
|---|---|
| ♈ Aries | Head, face, brain |
| ♉ Taurus | Neck, throat, voice |
| ♊ Gemini | Arms, hands, lungs |
| ♋ Cancer | Chest, stomach, breasts |
| ♌ Leo | Heart, spine, upper back |
| ♍ Virgo | Intestines, digestive system |
| ♎ Libra | Kidneys, lower back |
| ♏ Scorpio | Reproductive organs |
| ♐ Sagittarius | Hips, thighs |
| ♑ Capricorn | Knees, bones, joints |
| ♒ Aquarius | Ankles, calves, circulation |
| ♓ Pisces | Feet |

The journal presents this as a diagram — the Zodiac Man — so the
reader can see the correspondence visually.

---

## Glyph legend / codebook

The front matter includes a complete glyph legend so the reader can
write shorthand in their entries — drawing a symbol instead of
spelling out a name. The legend also teaches the symbolic grammar:
every astrological glyph is built from three shapes — **circle**
(spirit), **crescent** (soul), **cross** (matter) — combined in
different arrangements. Once someone knows that, every glyph becomes
readable. The journal's own degree mark (circle on a bar) follows
this same grammar: spirit resting on matter.

### Zodiac signs

| Glyph | Sign | Unicode |
|---|---|---|
| ♈ | Aries | U+2648 |
| ♉ | Taurus | U+2649 |
| ♊ | Gemini | U+264A |
| ♋ | Cancer | U+264B |
| ♌ | Leo | U+264C |
| ♍ | Virgo | U+264D |
| ♎ | Libra | U+264E |
| ♏ | Scorpio | U+264F |
| ♐ | Sagittarius | U+2650 |
| ♑ | Capricorn | U+2651 |
| ♒ | Aquarius | U+2652 |
| ♓ | Pisces | U+2653 |

### Planets

| Glyph | Name | Unicode | Grammar |
|---|---|---|---|
| ☉ | Sun | U+2609 | Circle with dot — pure spirit |
| ☽ | Moon | U+263D | Crescent — soul |
| ☿ | Mercury | U+263F | Crescent + circle + cross — all three |
| ♀ | Venus | U+2640 | Circle over cross — spirit over matter |
| ♂ | Mars | U+2642 | Circle with arrow — spirit directed outward |
| ♃ | Jupiter | U+2643 | Crescent beside cross — soul rising from matter |
| ♄ | Saturn | U+2644 | Cross over crescent — matter over soul |
| ♅ | Uranus | U+2645 | — |
| ♆ | Neptune | U+2646 | Crescent over cross — soul over matter |
| ♇ | Pluto | U+2647 | — |

### Lunar nodes

| Glyph | Name | Unicode |
|---|---|---|
| ☊ | North Node (Dragon's Head) | U+260A |
| ☋ | South Node (Dragon's Tail) | U+260B |

### Other useful shorthand

| Glyph | Name | Unicode |
|---|---|---|
| ℞ | Retrograde | U+211E |
| ⚷ | Chiron | U+26B7 |

### Aspects

| Glyph | Name | Angle | Unicode |
|---|---|---|---|
| ☌ | Conjunction | 0° | U+260C |
| ⚹ | Sextile | 60° | U+26B9 |
| □ | Square | 90° | U+25A1 |
| △ | Trine | 120° | U+25B3 |
| ☍ | Opposition | 180° | U+260D |

### The degree mark — the ordinal indicator

The journal uses the **ordinal indicator** º (U+00BA) as its degree
mark, not the standard degree symbol ° (U+00B0). In traditional
typography, the ordinal indicator is a small circle resting on a
short horizontal bar — the circle above, the bar beneath, not
bisecting it.

The name explains the system: **ordinal** numbers count positions —
1st, 2nd, 3rd — starting at 1, not 0. The degrees of the zodiac are
ordinal. The 1st degree of Aries, the 2nd degree of Aries, the 360th
degree. There is no zeroth degree. The ordinal indicator is the
correct symbol for this; the standard ° is not.

The glyph also follows the symbolic grammar of astrological notation:
the circle represents spirit, the line represents matter. Spirit
resting on matter — the celestial measured against the earthly plane.

The legend/codebook introduces and explains this symbol. In printed
typography, the journal uses º (U+00BA). Users draw it by hand in
their entries — a small circle on a short horizontal line.

---

## Moon phases and soli-lunar types

The front-matter codebook teaches the eight phases with visual symbols
users can draw in their entries. Each phase also carries a character —
the soli-lunar type — defined by the angular relationship between sun
and moon at the moment of birth.

| Phase | Sun–Moon arc | Description | Birth type |
|---|---|---|---|
| **New** | 1º–45º | Invisible — sun and moon together | Subjective, impulsive, projecting outward into the world |
| **Crescent** | 46º–90º | First sliver of light, growing | Self-asserting, carrying out an inner command |
| **First Quarter** | 91º–135º | Half lit, growing | Willful, organizing, building against tradition |
| **Gibbous** | 136º–180º | More than half, still growing | Devoted, self-improving, seeking understanding |
| **Full** | 181º–225º | Fully lit — sun and moon opposite | Objective, illuminated, materializing ideals |
| **Disseminating** | 226º–270º | Starting to shrink | Spreading ideas, teaching, crusading |
| **Last Quarter** | 271º–315º | Half lit, shrinking | Reforming, building systems, forcing issues |
| **Balsamic** | 316º–360º | Final sliver before new | Prophetic, sacrificial, concluding cycles |

One full cycle ≈ 29.5 days.

**Waxing** = growing toward full. **Waning** = shrinking toward new.

The sun–moon arc is measured as the angular distance the moon has
traveled ahead of the sun since the last conjunction (new moon). When
someone finds their birth moon phase, they also discover their
soli-lunar type — a quality that colors how they move through the
world.

**Etymology footnote:** *Crescent* comes from Latin *crescere* — to
grow. The crescent is always the moon growing toward full. Include
this as a footnote in the moon phases section.

### Moon phase diagram (interactive)

The moon phases are represented not just as a reference chart but as
a **diagram the reader can locate themselves on**. The diagram shows
the full 29.5-day lunar cycle as a continuous visual — the eight
phases arranged in sequence with enough space and clarity that the
reader can mark their birth moon phase on it, the same way they mark
their birth degree on the solar sine wave.

This makes both diagrams personal and interactive:
- The sine wave = "where is my sun?" — mark your birth degree
- The moon phase diagram = "what was my moon doing?" — mark your
  birth phase

The moon phase diagram should show:
- All eight phases in order with drawn circles (empty, sliver,
  half, gibbous, full, and back)
- A clear marker area or line where the reader places their birth
  phase
- The waxing/waning divide visually evident
- The ~29.5 day cycle length noted

The exact visual form (linear strip, arc, circular layout) is a
design decision to be made when building artboards. What matters is
that it's a diagram you write on, not just a chart you read.

### Soli-lunar distance — the daily calculation

The soli-lunar distance (☉☽) is the angular separation from the sun
to the moon. This is not only for finding your birth phase — it is
the calculation used for **every journal entry** to determine the
current moon phase. Every time you write, you look up where the sun
and moon are, run the formula, and record the result.

**Formula:**

> ☉☽ = Moon° − Sun° (add 360 if the result is negative)

**Sign base degrees (for converting to absolute degrees):**

| ♈ | ♉ | ♊ | ♋ | ♌ | ♍ | ♎ | ♏ | ♐ | ♑ | ♒ | ♓ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 30 | 60 | 90 | 120 | 150 | 180 | 210 | 240 | 270 | 300 | 330 |

To convert any position to absolute degrees: sign base + degree
within sign. Example: ♏ 10° → 210 + 10 = 220°.

**Worked example:**

Sun at ♏ 10° · Moon at ♊ 13°
- Sun absolute: 210 + 10 = 220°
- Moon absolute: 60 + 13 = 73°
- ☉☽ = 73 − 220 + 360 = **213°** → Full (181°–225°)

**Phase ranges from the result:**

| 1°–45° | 46°–90° | 91°–135° | 136°–180° | 181°–225° | 226°–270° | 271°–315° | 316°–360° |
|---|---|---|---|---|---|---|---|
| New | Crescent | First ¼ | Gibbous | Full | Dissem. | Last ¼ | Balsamic |

The front matter includes the formula, a sign-base reference, a
worked example, and blank workspace fields for the reader to do
their own calculation. A linear lunation scale underneath the sine
wave shows the same 360° divided into eight phases — the two 360°
systems (solar year and lunation cycle) presented in parallel.

---

## Visual language — the sine wave

The zodiac year is represented as a **sine wave of the sun's
declination** — not a circle, not semicircles.

- Horizontal center = equator (0° declination)
- Upper bound = Tropic of Cancer (Summer Solstice, ~23.4°N)
- Lower bound = Tropic of Capricorn (Winter Solstice, ~23.4°S)
- Equinoxes = zero crossings (Aries 1° and Libra 1°)

The twelve signs are marked along the wave.

### The four quarters (cardinal points)

The sine wave is structured by four cardinal points — the solstices
and equinoxes. These are the backbone of the year:

| Point | Sign degree | Position on wave | What happens |
|---|---|---|---|
| Vernal Equinox | ♈ Aries 1° | Zero crossing, ascending | Equal day/night, light increasing |
| Summer Solstice | ♋ Cancer 1° | Peak of wave | Longest day, maximum declination north (~23.4°N) |
| Autumnal Equinox | ♎ Libra 1° | Zero crossing, descending | Equal day/night, light decreasing |
| Winter Solstice | ♑ Capricorn 1° | Trough of wave | Shortest day, maximum declination south (~23.4°S) |

These four points divide the year into quarters. The signs between
them are the journey from one cardinal moment to the next.

The Tropic of Cancer and Tropic of Capricorn are labeled as the
upper and lower bounds of the wave — these are real geographic lines
on the earth where the sun reaches directly overhead at the
solstices. The equator is the centerline.

### Interactive birth degree marker

The sine wave diagram includes space for the reader to **mark their
birth degree** directly on the curve. They find their degree on the
horizontal axis (1°–360°, with sign boundaries marked), then place
a mark on the wave at that point. This shows them:

- Where they fall in the year's rhythm
- How close they are to a solstice or equinox
- Whether their birth light was increasing or decreasing
- Their position relative to the tropics and equator

This makes the sine wave personal — not just a reference diagram
but a record of where you entered the cycle.

---

## Tracks recorded per daily entry

Each daily entry captures:

1. **Sun degree** — sign glyph + ordinal degree. This is the date.
2. **Moon degree and phase** — sign glyph + ordinal degree, plus the
   phase symbol. Together with the sun degree and year, this encodes
   the complete timestamp — the Gregorian date and approximate time
   are derivable from these values alone.
3. **Year** — Annus Mundi, Gregorian, or both. Written once at the
   sign opener or repeated daily, reader's choice.
4. **Location** — latitude and longitude. Written once, updated when
   the reader moves. Determines sunrise, day length, and light.
5. **Solar time** — sunrise, noon, sunset (local observed time)
6. **Light** — what the light is actually doing (season, quality)
7. **Train time** — Gregorian date, optional, small and secondary

Plus ruled writing lines for the journal entry itself.

---

## Design tokens

- **Fonts:** Cormorant Garamond (display/serif), Cormorant SC (small caps labels),
  IBM Plex Sans (body/labels/sans)
- **Colors:**
  - `--parchment` `#f5f0e8` — warm background
  - `--ink` `#8b6f47` — secondary text, labels, small annotations
  - `--dark` `#3d3428` — primary text, all glyphs
  - `--gold` `#c4a97d` — accent: decorative lines, sine wave stroke, borders
  - `--field` `#e8dfd3` — input fields, moon phase fill
  - `--rule` `#d4c9b8` — subtle dividers
  - `--faint` `#f0ebe2` — callout backgrounds
  - `--white` `#faf8f4` — lightest surface
- **Page size:** 612×792px (US Letter)
- **Side margins:** 56px
- **Style notes:** "train time" is always lowercase; degree ranges use
  en dash (–); dark theme is fully supported with token redefinition

---

## Where the journal lives

- **Repo:** `AnaSeahawk/solar-journal` — **private**, mounted at
  `Components/solar-journal/`. Holds the artboards, `canvas.json`, and
  the published canvas under `published/`.
- **This skill** stays in `aether`: skills belong to the coordination seed.
- **Artifact (current):** `https://claude.ai/code/artifact/44896e33-8c4d-4470-92fb-2d1ed696ec48`
- **Format:** 612×792px US Letter per artboard
- **Superseded:** branch `claude/journal-design-tv0uqe`, where the design was
  originally built. Its files now live in the repo above; treat the branch as
  history, not as the working copy.

The repo is private because the journal is an unreleased product. Make it
public when it is ready to sell, not before.

### Related skill

`phoenix-calculator` implements the 138° Phoenix sequence computationally —
Swiss Ephemeris solar-transit solving, Phoenix Anno Mundi assignment, and the
same ordinal notation this journal uses. Read it before building page x (The
Phoenix) or any Personal Phoenix Point content, so the printed values and the
calculator agree.

---

## The Phoenix architecture

### Phoenix Event (Archaix)

Category: Chronology · Cycle · Cataclysm · Reset · Benefactor Protocol

Within the Archaix chronology developed by Jason Breshears, the Phoenix
is a recurrent phenomenon appearing at intervals of 138 years. The
Archaix glossary describes it as a benefactor protocol disguised as a
cataclysm protocol — a force that disrupts established systems and
neutralizes the activity of controlling structures (Archons).

The Phoenix Event is not simply the appearance of an astronomical
object. In the mature Archaix model it represents a periodic
intervention in the Construct: a moment capable of altering geography,
populations, material conditions, historical continuity, and the
prevailing organization of civilization. Magnitude varies from
visitation to visitation.

**Numerical structure:**

- 138 years = one Phoenix Interval
- 414 years = three Phoenix Intervals
- 552 years = four Phoenix Intervals = one Phoenix Cycle

Major ancient Phoenix catastrophes identified by Archaix: 2239 BCE,
1687 BCE, 1135 BCE, 583 BCE — each separated by 552 years. This is
the underlying structure of what Breshears calls the ancient Age of
the Phoenix.

Nearer sequence: **1764 → 1902 → 2040** (each separated by exactly
138 years). Archaix associates the 1764 and 1902 appearances with May
and projects the next return to **17 May 2040**.

**Phoenix as Keeper of the Calendar**

One of the most important Archaix names for the Phoenix. Other names
in the Archaix corpus: Typhon, Phenc, Feng, Fenrir, Noph, Sky Dragon,
Destroyer, Doomshape, Angel of Death.

Breshears argues that the persistence of the 138-year pattern — even
while historical calendar systems and the length attributed to the year
changed — cannot be explained as the orbit of an ordinary physical
body. Within his model, this paradox becomes evidence that Phoenix
behaves more like a programmed chronological protocol than a
conventional planet.

The Phoenix is simultaneously: destruction and correction, ending and
reordering, cataclysm and benefaction, calendar and event, death of a
structure and opening for another. The word Phoenix is appropriate
because the event does not signify simple annihilation — it describes
the periodic collapse of an existing arrangement followed by another
configuration of the world.

### Personal Phoenix Point (astrological analogue)

A distinct development from the Archaix source material. The Personal
Phoenix Point takes the same 138-unit architecture and expresses it
analogically through the zodiac:

- 1 year ↔ 1 degree
- Therefore: 138 years ↔ 138°

A personal Phoenix point advances an exact tropical longitude by 138°
and records the moment when the tropical Sun subsequently crosses that
longitude.

This is an astrological analogue of the Phoenix architecture, not a
claim made by Archaix itself. The personal system uses the 138
structure as a measure, then allows the Sun itself to locate the
moment rather than imposing 138 calendar days. The distinction between
number as interval and celestial event as actual occurrence is
intentional and clean.

### Key terms (do not collapse)

| Term | Meaning |
|---|---|
| Phoenix Interval | 138 years — the fundamental unit |
| Phoenix Cycle | 552 years — four intervals |
| Phoenix Event | A specific recurrent intervention/reset in Archaix chronology |
| Personal Phoenix Point | 138° astrological analogue — separate from Archaix |
| Keeper of the Calendar | Archaix designation for Phoenix's chronological function |

These four terms must always be kept distinct. The Personal Phoenix
Point is cross-referenced with the Phoenix Event but never collapsed
into it.

---

## Your birth degree and solar return

The journal's front matter includes a personal section that grounds the
reader in the system by locating them on the sine wave.

### Birth degree

The reader takes their birthday, birth time, and birthplace to
astro.com or an ephemeris and finds the sun's exact position — not just
the sign, but the precise degree and minute (e.g., ♊ 24°17'). They
locate this on the sine wave declination diagram, which shows where
they fall between the tropics. A birth at ♋ 1° is at the top of the
wave (Summer Solstice, maximum declination, longest day). A birth at
♑ 1° is at the bottom (Winter Solstice, shortest day). The sine wave
makes the quality of the light you were born into visible in a way a
circle cannot.

### Birth moon phase

Which of the eight phases the moon was in at the moment of birth. This
is fixed — part of the natal chart.

### Solar return

Each year the sun returns to the exact degree and minute it occupied at
birth. This is the real birthday — a moment, not a day. The Gregorian
date of the solar return shifts: it might fall the day before, the day
after, or occasionally on the calendar birthday. The journal provides
space to record the train time date of each solar return and watch
the drift year over year.

The calendar date shifts slightly year to year. The degree does not.

### Moon phase at each return

The moon phase at the solar return is different every year. Tracking
it alongside the return builds a pattern over time: the phase you were
born under versus the phase each year returns under. That contrast is
itself information.

### Solar return chart

Briefly explained: the chart cast for the exact moment the sun returns
to the birth degree, used as a reading for the year ahead. The journal
names it so the reader knows what to look for if they want to go
deeper. The journal does not interpret it.

### Fill-in fields

The front matter includes personal fields:
- Birth degree (exact, with minutes)
- Birth moon phase
- Location

A recurring space (inside each sign opener or as a yearly page) to
record each solar return: train time date, moon phase, notes.

---

## How to Mark Time (bridge page)

The last page of the front matter, immediately before the daily
journal pages begin. This is not a teaching page — it's a quick
reference that shows exactly how to fill in each entry's time fields.
It brings together everything the introduction taught and presents
it as a single, compact format the reader will use every day.

**The three values that encode a moment in time:**

1. **Sun degree** — sign glyph + ordinal degree. The sun moves ~1º
   per day, so this tells you the day. Example: ♈ 15º
2. **Moon degree** — sign glyph + ordinal degree, plus the phase
   symbol (one of eight). The moon moves ~13º per day (~0.5º per
   hour), so this tells you the time within the day.
   Example: ♊ 22º, crescent
3. **Year** — Annus Mundi, Gregorian, or both.
   Example: 5920 / 2026

These three values together are a complete timestamp. The Gregorian
date is not a separate piece of information — it is derivable from
the sun degree and the year. The astronomical notation contains the calendar date inside it.
The calendar names it. The sky locates it.

**Location:**

4. **Latitude and longitude** — where you are on the earth when you
   write. Not a timezone (that's a political convention). Lat/long
   is your actual position, expressed in the same ordinal degrees
   the journal uses for everything else. It determines your sunrise,
   your day length, your light quality, and your relationship to the
   sine wave — your latitude tells you how the sun's declination
   plays out where you stand. Written once, updated when you move.
   Your coordinates determine your sunrise, your day length, how
   the light moves through your year.

**Each entry also records:**

5. **Solar time** — sunrise, noon, sunset. Observed, not looked up.
   The times you actually see the light change.
6. **Light** — what the light is doing. Season, quality, length of
   day. A word or a sentence.
7. **Train time** — the Gregorian date. Optional. Small. Secondary.
   For coordination with the conventional world. Example: 9 Apr

This page includes a small example entry showing all fields filled
in, so the reader can see the complete notation in use before they
write their first one.

The format is the same on every daily entry page. Once learned, it
becomes a rhythm — a few seconds of marking where you are before
you write.

---

## Pocket instruments — the physical precedent

The journal's front matter includes a brief section introducing two
brass pocket instruments that embody the same principles the journal
uses. The reader's own instruments are photographed for this section.

### The ring dial (sundial)

A **two-ring universal equinoctial ring dial** — a portable sundial
that reads solar time anywhere on earth without a compass.

**How it works:**

1. **Set your latitude** — slide the suspension point along the
   latitude scale (marked 20º–70º, with cities engraved: London 51º,
   Berlin 52º, St. Petersburg 59º, Rome 41º, Paris 48º50',
   Lisbon 38º, Washington 38º).
2. **Set the date** — slide the cursor on the central bridge to the
   current month.
3. **Open the rings perpendicular** and hang the dial from its cord.
4. **Sunlight passes through the pinhole** in the bridge and hits
   the hour scale on the inner ring — read the time.

No batteries, no compass. Just your position on the earth and the
position of the sun. The same two inputs the journal asks for.

Developed from William Oughtred's 17th-century design. The instrument
has been in use for 500 years.

**Source:** The reader's instrument is the Ring Dial from Grand
Illusions (grand-illusions.com/products/ring-dial), a brass
reproduction made in the EU. Original manufacturer: H.M. Kala,
an Austrian watchmaking family (pocket-sundial.com), producing
precision pocket sundials for over 25 years.

### The nocturnal (star clock)

A **universal pocket nocturnal** — an instrument that reads the
time at night using fixed stars. The world's first nocturnal
that works in both hemispheres.

**How it works:**

1. **Choose your hemisphere** — the instrument has two handles,
   marked N and S.
2. **Set the date** — align the pointer (decorated with a moon face)
   on the inner disc with the current date on the outer disc.
3. **Sight through the center hole:**
   - **Northern Hemisphere (N handle):** Find Polaris (the North
     Star) and sight it through the hole. The pointer reads the time.
   - **Southern Hemisphere (S handle):** Face south and use the
     Southern Cross and Alpha/Beta Centauri (the Pointers) to locate
     the South Celestial Pole. There is no bright star at the southern
     pole — this is why the original nocturnals couldn't work south
     of the equator.

The Southern Hemisphere capability was designed in 2023 by Tony
Sprent in Tasmania, making this the first universal nocturnal ever
produced.

**Source:** Kala Universal Pocket Nocturnal (pocket-sundial.com/
products/universal-nocturnal), solid brass, produced in a family
workshop outside Madrid.

### The connection to the journal

The ring dial reads the **sun** — it needs your **latitude**.
The nocturnal reads the **stars** — it needs your **hemisphere**.
Both use **degrees**. Both are portable. Both are precise. Both
have been used for centuries.

The journal is the paper version of the same idea. It reads the
same sky, uses the same degrees, asks the same opening question:
*where are you?*

The sundial needs latitude because the angle of the gnomon must
match your position on the earth — the sun's path across the sky
changes with latitude. The journal asks for latitude for the same
reason: your sunrise, day length, and light quality all depend on
where you stand on the earth.

These instruments appear in the front matter as a photograph —
the reader's own brass instruments on a grey wool surface, one
reading the day, one reading the night. They establish the
lineage: people have carried instruments like these for centuries.
This journal continues that tradition.

---

## Journal sections (content plan)

Front matter / codebook (11 pages built in artifact):
- [x] Page i — How to Begin: instruments introduction, epigraph, location prompt
- [x] Page ii — The Year as a Wave: sine wave diagram + lunation linear scale
- [x] Page iii — Eight Moon Phases: phase visuals, soli-lunar types, ☉☽ calculation
- [x] Page iv — Your Birth & Solar Return: birth degree, location, return tracking
- [x] Page v — The Glyphs: zodiac signs, planets (incl. Pluto bident), nodes, aspects, ordinal indicator
- [x] Page vi — The Degree Key: full 12-sign reference table
- [x] Page vii — Grammar of the Signs: elements, modalities, polarity
- [x] Page viii — The Zodiac Man: body correspondence (placeholder for drawn figure)
- [x] Page ix — The Notation: Annus Mundi, date format, complete timestamp
- [x] Page x — The Phoenix: 138/552 architecture, Personal Phoenix Point
- [x] Page xi — How to Mark Time: three values, example entry, bridge to daily pages
- [x] Photograph: instruments on grey wool, embedded as data URI

Repeating sections (×12, one per sign — not yet started):
- [ ] Sign opener — glyph, name, degree range, properties, train time reference
- [ ] Daily entry pages — sun position, moon, solar time, light, writing lines
- [ ] Moon tracker — 29+1 circles to shade, cycle fields, observations space

---

## Design decisions (settled)

These decisions were made during artifact development and should not
be revisited without reason.

### Monochrome glyphs

All zodiac and planet glyphs use `var(--dark)` (near-black). No
element-based coloring. The colored badge system (fire red, water
blue, air lavender, earth ochre) and the polarity colors (fem/masc)
were explored and deliberately removed — zodiac element colors are
derived/interpretive tradition, not fundamental, and they clutter
the minimal design language. The CSS variables for those colors
have been deleted.

`var(--gold)` (#c4a97d) is used only for decorative lines, borders,
and the sine wave stroke — it is the journal's accent color, not
a glyph color.

### Pluto glyph

The standard Unicode ♇ (U+2647) is not used. The journal uses the
**bident-with-large-orb** variant, rendered as inline SVG:

```
<svg width="16" height="20" viewBox="0 -1 12 14">
  <path d="M2.25 3a3.751 3.751 0 0 0 7.5 0M6 11V6.75M3.5 8.875h5M8 3a1.999 1.999 0 1 0-4 0a1.999 1.999 0 1 0 4 0z"
        fill="none" stroke="var(--dark)" stroke-width="0.7"/>
</svg>
```

Source: Wikimedia Commons astrological Pluto symbol (option A —
bident with large orb at top, vertical staff, crossbar).

### Sine wave geometry

The sine wave uses cubic bezier curves that produce a **true sine
shape** — steep at the equator crossings (Aries, Libra) and flat
at the peaks/troughs (Cancer, Capricorn). Earlier versions had
horizontal tangents at the zero crossings, which created visible
hesitation/dips. The corrected control points ensure the wave flows
continuously without pausing at any point.

All twelve zodiac markers sit on the computed sine curve at their
correct angular positions (each sign at 30° intervals).

### Glyph grammar section removed

The symbolic grammar teaching (circle = spirit, crescent = soul,
cross = matter) was removed from the Glyphs page. It remains
documented in this skill file for reference but does not appear
in the printed journal's front matter.

### Instrument photograph

The photo for page i (both instruments on grey wool, city names
legible) is embedded in the artifact as a data URI. The files:

- **Committed — web version (249KB, 1000×562):**
  `.agents/skills/solar-journal/instruments-photo-web.jpg`
- **Not committed — master (9.1MB, 6192×3480):**
  `.agents/skills/solar-journal/instruments-photo.jpg`, gitignored.
  `aether` is public and its `.git` is already ~3GB, so the master
  stays local. Regenerate the web version with:
  `magick instruments-photo.jpg -resize 1000x -quality 80 instruments-photo-web.jpg`

The master exists only on Ana's machine. Back it up outside git before
relying on being able to regenerate from it.

---

## Market positioning

No existing product combines:
- Serious daily journaling with thorough astronomical data
- Timeless/undated design (buy anytime, no year penalty)
- Minimal, secular, grounded design language (vs. feminine/spiritual aesthetic)
- High-quality paper expectations (Tomoe River / 120gsm class)

---

## Evolving this skill

This skill grows as the journal's content plan is finalized. Update it
when design decisions are made, new sections are added, or the visual
language evolves. The journal sections checklist tracks what has been
decided vs. what remains open.

---

## See also

- Branch `claude/journal-design-tv0uqe` for current artboards
- Archaix glossary: `https://archaix.com/glossary`
