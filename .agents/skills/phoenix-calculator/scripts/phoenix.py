#!/usr/bin/env python3
"""
Phoenix Calculator
Requires: pyswisseph
Python: 3.9+ (zoneinfo)
"""

from __future__ import annotations
import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import swisseph as swe

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]
SIGN_INDEX = {s.lower(): i for i, s in enumerate(SIGNS)}
FULL_CIRCLE_ARCSEC = 360 * 3600
STEP_ARCSEC = 138 * 3600
UNIX_EPOCH_JD = 2440587.5


def jd_from_datetime(dt: datetime) -> float:
    if dt.tzinfo is None:
        raise ValueError("Datetime must be timezone-aware.")
    utc = dt.astimezone(timezone.utc)
    hour = utc.hour + utc.minute / 60 + (utc.second + utc.microsecond / 1e6) / 3600
    return swe.julday(utc.year, utc.month, utc.day, hour, swe.GREG_CAL)


def datetime_from_jd(jd: float) -> datetime:
    return datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(days=jd - UNIX_EPOCH_JD)


def sun_longitude(jd_ut: float) -> float:
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    xx, _ = swe.calc_ut(jd_ut, swe.SUN, flags)
    return xx[0] % 360.0


def angle_diff(lon: float, target: float) -> float:
    """Signed angular difference lon-target in [-180, 180)."""
    return ((lon - target + 180.0) % 360.0) - 180.0


def solve_solar_transit(target_lon: float, after: datetime) -> datetime:
    """Find the first apparent geocentric tropical solar-longitude crossing after `after`."""
    start = after.astimezone(timezone.utc) + timedelta(seconds=1)
    jd0 = jd_from_datetime(start)
    d0 = angle_diff(sun_longitude(jd0), target_lon)

    a = jd0
    da = d0
    bracket = None
    for i in range(1, 402):
        b = jd0 + i
        db = angle_diff(sun_longitude(b), target_lon)
        if da <= 0.0 <= db and abs(da) < 5.0 and abs(db) < 5.0:
            bracket = (a, b)
            break
        a, da = b, db

    if bracket is None:
        raise RuntimeError("Could not bracket solar transit within 401 days.")

    lo, hi = bracket
    for _ in range(80):
        mid = (lo + hi) / 2.0
        dm = angle_diff(sun_longitude(mid), target_lon)
        if abs(dm) < 1e-11 or (hi - lo) * 86400 < 0.001:
            return datetime_from_jd(mid)
        if dm >= 0:
            hi = mid
        else:
            lo = mid
    return datetime_from_jd((lo + hi) / 2.0)


def parse_anchor_arcsec(sign: str, degree: int, minute: int, second: int) -> int:
    idx = SIGN_INDEX.get(sign.lower())
    if idx is None:
        raise ValueError(f"Unknown sign: {sign}")
    if not (0 <= degree <= 29):
        raise ValueError("Cardinal degree inside a sign must be 0..29.")
    if not (0 <= minute <= 59 and 0 <= second <= 59):
        raise ValueError("Minute and second must be 0..59.")
    return (idx * 30 + degree) * 3600 + minute * 60 + second


def render_position(total_arcsec: int):
    a = total_arcsec % FULL_CIRCLE_ARCSEC
    abs_deg = a // 3600
    sec_in_deg = a % 3600
    minute = sec_in_deg // 60
    second = sec_in_deg % 60
    sign_idx = abs_deg // 30
    cardinal_degree = abs_deg % 30
    ordinal_degree = cardinal_degree + 1
    sign = SIGNS[sign_idx]
    ordinal = f"{ordinal_degree}º {sign}"
    exact = f"{cardinal_degree}°{minute:02d}′{second:02d}″ {sign}"
    return ordinal, exact, a / 3600.0


def aries_ingress_utc(year: int) -> datetime:
    jan1 = datetime(year, 1, 1, tzinfo=timezone.utc)
    return solve_solar_transit(0.0, jan1)


def phoenix_am_year(dt_utc: datetime, offset: int = 3894) -> int:
    ingress = aries_ingress_utc(dt_utc.year)
    return dt_utc.year + offset if dt_utc >= ingress else dt_utc.year + offset - 1


@dataclass
class PhoenixPoint:
    sequence: str
    ordinal: str
    exact_cardinal: str
    absolute_longitude: float
    local_transit: str
    utc_transit: str
    am_year: int


def calculate(anchor_arcsec: int, start_n: int, count: int, after: datetime,
              timezone_name: str, am_offset: int = 3894):
    tz = ZoneInfo(timezone_name)
    cursor = after
    rows = []
    for n in range(start_n, start_n + count):
        target_arcsec = (anchor_arcsec + STEP_ARCSEC * n) % FULL_CIRCLE_ARCSEC
        ordinal, exact, target_lon = render_position(target_arcsec)
        utc_dt = solve_solar_transit(target_lon, cursor)
        local_dt = utc_dt.astimezone(tz)
        am = phoenix_am_year(utc_dt, am_offset)
        rows.append(PhoenixPoint(
            sequence=f"P{n}",
            ordinal=ordinal,
            exact_cardinal=exact,
            absolute_longitude=round(target_lon, 9),
            local_transit=local_dt.strftime(f"%Y-%m-%d %H:%M:%S {timezone_name}"),
            utc_transit=utc_dt.strftime("%Y-%m-%d %H:%M:%S UTC"),
            am_year=am,
        ))
        cursor = utc_dt + timedelta(seconds=1)
    return rows


def parse_after(value: str) -> datetime:
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        raise argparse.ArgumentTypeError("--after must include a UTC offset.")
    return dt


def main():
    p = argparse.ArgumentParser(description="Calculate Phoenix points and exact solar transit times.")
    p.add_argument("--sign", required=True, choices=SIGNS)
    p.add_argument("--degree", type=int, required=True, help="Cardinal degree within sign, 0..29")
    p.add_argument("--minute", type=int, default=0)
    p.add_argument("--second", type=int, default=0)
    p.add_argument("--start-n", type=int, required=True)
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--after", type=parse_after, required=True,
                   help="Timezone-aware ISO datetime, e.g. 2026-09-05T00:00:00+02:00")
    p.add_argument("--timezone", default="Europe/Madrid")
    p.add_argument("--am-offset", type=int, default=3894)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    anchor = parse_anchor_arcsec(args.sign, args.degree, args.minute, args.second)
    rows = calculate(anchor, args.start_n, args.count, args.after, args.timezone, args.am_offset)

    if args.json:
        print(json.dumps([asdict(r) for r in rows], indent=2, ensure_ascii=False))
        return

    print(f"{'Seq':<6} {'Ordinal':<20} {'Exact cardinal':<28} {'Local transit':<39} {'AM':<6}")
    print("-" * 105)
    for r in rows:
        print(f"{r.sequence:<6} {r.ordinal:<20} {r.exact_cardinal:<28} {r.local_transit:<39} {r.am_year:<6}")


if __name__ == "__main__":
    main()
