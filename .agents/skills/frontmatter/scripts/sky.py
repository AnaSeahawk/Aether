#!/usr/bin/env python3
"""Print frontmatter sun, moon, and moon-phase lines for a moment.

Degrees are ordinal (º): cardinal 9°52′ Scorpio is 10º Scorpio.
With no arguments, uses the current moment. With --date YYYY-MM-DD, uses
noon Europe/Madrid on that date (the curator convention for dated files).
"""
import argparse
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import swisseph as swe

SIGNS = ("Aries Taurus Gemini Cancer Leo Virgo Libra Scorpio "
         "Sagittarius Capricorn Aquarius Pisces").split()
# Eight phases by Sun–Moon separation, 45° each, centred on each phase
# (New moon spans 337.5°–22.5°).
PHASES = ("New moon", "Waxing crescent", "First quarter", "Waxing gibbous",
          "Full moon", "Waning gibbous", "Last quarter", "Waning crescent")


def longitude(jd, body):
    return swe.calc_ut(jd, body, swe.FLG_SWIEPH)[0][0]


def ordinal(lon):
    return f"{int(lon % 30) + 1}º {SIGNS[int(lon // 30)]}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="YYYY-MM-DD; computed at noon Europe/Madrid")
    args = parser.parse_args()

    if args.date:
        local = datetime.fromisoformat(args.date).replace(
            hour=12, tzinfo=ZoneInfo("Europe/Madrid"))
        moment = local.astimezone(timezone.utc)
    else:
        moment = datetime.now(timezone.utc)

    jd = swe.julday(moment.year, moment.month, moment.day,
                    moment.hour + moment.minute / 60 + moment.second / 3600)
    sun = longitude(jd, swe.SUN)
    moon = longitude(jd, swe.MOON)
    separation = (moon - sun) % 360

    print(f"date: {moment.astimezone(ZoneInfo('Europe/Madrid')).date()}")
    print(f"sun: {ordinal(sun)}")
    print(f"moon: {ordinal(moon)}")
    print(f"moon-phase: {PHASES[int(((separation + 22.5) % 360) // 45)]}")


if __name__ == "__main__":
    main()
