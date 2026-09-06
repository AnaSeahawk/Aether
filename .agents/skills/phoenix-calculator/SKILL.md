---
name: phoenix-calculator
description: Calculate Phoenix zodiacal points from an exact tropical longitude using 138° steps, preserve Ana's ordinal zodiac notation, solve the actual geocentric tropical solar transit for each point, assign the Phoenix Anno Mundi year, and prepare verified calendar-ready event data.
---

# Phoenix Calculator

## Governing convention

Use **ordinal zodiacal notation** as the primary display convention:

- `1º` of a sign = cardinal `0°00′00″–0°59′59″`
- `10º` of a sign = cardinal `9°00′00″–9°59′59″`
- `30º` of a sign = cardinal `29°00′00″–29°59′59″`

Never confuse an ordinal degree-field with a cardinal coordinate.

Examples:

- cardinal `9°52′ Scorpio` → `10º Scorpio`
- cardinal `11°37′ Taurus` → `12º Taurus`
- cardinal `12°00′ Taurus` → `13º Taurus`

When an exact cardinal coordinate is provided, preserve its minutes and seconds.

## Phoenix sequence

For an exact tropical zodiacal longitude \(\lambda_0\),

\[
P_n=(\lambda_0+138^\circ n)\pmod{360^\circ}
\]

The step is exactly `138°`.

Because \(\gcd(138,360)=6\), the sequence contains 60 distinct zodiacal longitudes before the spatial pattern repeats:

\[
60\times138^\circ=23\times360^\circ
\]

This is the 60-step / 23-year structure.

## Critical date rule

**Never calculate a Phoenix date by adding 138 calendar days.**

A Phoenix event occurs at the actual moment when the **apparent geocentric tropical Sun** reaches the exact Phoenix longitude.

Use a high-quality ephemeris. The bundled calculator uses Swiss Ephemeris (`pyswisseph`) and numerically solves the solar-longitude crossing.

The Sun's apparent angular speed is not uniform, so the interval between Phoenix events varies.

## Tropical solar longitude

Use:

- geocentric Sun
- tropical zodiac
- apparent longitude
- equinox of date
- UT for ephemeris solving
- convert the solved instant to the requested IANA timezone only after the transit is found

Do not substitute a mean-Sun approximation when exact event times are requested.

## Anno Mundi convention

For this Phoenix system, the AM year begins at the **Aries ingress**: the actual solar crossing of cardinal `0° Aries`, not January 1.

The currently established Phoenix AM offset is:

- after the Aries ingress: `AM = Gregorian year + 3894`
- before that year's Aries ingress: `AM = Gregorian year + 3893`

This reproduces the established anchors:

- 1974 Scorpio anchor → AM 5868
- 1985 Aries anchor → AM 5879

If a future Phoenix source changes the epoch, treat `3894` as a configurable system constant rather than silently changing the convention.

## Ana's current personal anchor

Do not substitute another dataset unless explicitly requested.

- Anchor: `10º Scorpio`
- Exact cardinal coordinate: `9°52′00″ Scorpio`
- Tropical absolute longitude: `219°52′00″`
- Gregorian anchor year: `1974`
- AM: `5868`

Sequence:

\[
P_n=(9^\circ52′\ \text{Scorpio}+138^\circ n)\pmod{360^\circ}
\]

A separate historical dataset exists at `6º Aries = 5°37′ Aries, 1985 / AM 5879`. Keep it strictly separate.

## Required calculation procedure

1. Parse the exact cardinal longitude.
2. Convert the sign coordinate to absolute tropical longitude:
   - Aries 0°
   - Taurus 30°
   - Gemini 60°
   - Cancer 90°
   - Leo 120°
   - Virgo 150°
   - Libra 180°
   - Scorpio 210°
   - Sagittarius 240°
   - Capricorn 270°
   - Aquarius 300°
   - Pisces 330°
3. Keep longitude arithmetic in integer arcseconds when possible.
4. Add exactly `138° × n`, modulo `360°`.
5. Convert the result back to:
   - primary ordinal notation, e.g. `28º Sagittarius`
   - exact cardinal notation, e.g. `27°52′00″ Sagittarius`
6. Find the first actual solar transit of that longitude after the requested starting instant.
7. For a sequence, use each solved event as the lower bound for the next search.
8. Convert UTC to the requested IANA timezone.
9. Determine the AM year by comparing the event instant with that Gregorian year's actual Aries ingress.
10. Report the ephemeris convention and timezone used.

## Output format

For each point, return at minimum:

| Field | Example |
|---|---|
| Sequence | `P136` |
| Ordinal | `28º Sagittarius` |
| Exact cardinal | `27°52′00″ Sagittarius` |
| Local transit | `19 Dec 2026 19:32:15 Europe/Madrid` |
| UTC transit | `19 Dec 2026 18:32:15 UTC` |
| AM year | calculated from Aries ingress |

When helpful, also include the absolute tropical longitude.

## Calendar preparation

Only create calendar events when the user explicitly asks.

Before writing:

1. List/identify calendars and resolve the **exact target calendar ID**.
2. Do not assume `primary` means the calendar the user intends.
3. Search the target date range for existing Phoenix events to prevent duplicates.
4. For a secondary personal calendar, create a clean solo event:
   - `attendees=[]`
   - `self_attendance="omit"` where supported
   - `add_google_meet=false`
   - `transparency="transparent"`
5. Prefer a short 15-minute marker beginning at the exact transit time.
6. Title:
   - `Phoenix Point — 28º Sagittarius`
7. Description should include:
   - sequence number
   - ordinal position
   - exact cardinal longitude
   - local transit
   - UTC transit
   - birth/event anchor
   - formula
   - AM year
   - note that the 15-minute duration is only for calendar visibility

Never create mirrored attendee copies on another calendar merely to make the event visible.

## Verification

For a batch:

- verify the number of created events equals the requested number
- verify the first and last sequence numbers
- verify the target calendar ID
- spot-check at least one event by reading it back
- report any ephemeris or timezone limitation explicitly

## Executable calculator

Use:

```bash
python scripts/phoenix.py \
  --sign Scorpio \
  --degree 9 \
  --minute 52 \
  --second 0 \
  --start-n 136 \
  --count 12 \
  --after 2026-09-05T00:00:00+02:00 \
  --timezone Europe/Madrid
```

The script prints a table and can emit JSON with `--json`.
