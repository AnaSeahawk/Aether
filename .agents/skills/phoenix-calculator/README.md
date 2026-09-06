# Phoenix Calculator Skill

A reusable skill package for Ana's Phoenix system.

## Files

- `SKILL.md` — governing rules and assistant behavior
- `scripts/phoenix.py` — executable Swiss Ephemeris calculator

## Dependency

```bash
pip install pyswisseph
```

## Ana's current anchor example

```bash
python scripts/phoenix.py \
  --sign Scorpio \
  --degree 9 \
  --minute 52 \
  --start-n 136 \
  --count 12 \
  --after 2026-09-05T00:00:00+02:00 \
  --timezone Europe/Madrid
```

Use `--json` for machine-readable output.

The `degree` input is the **cardinal degree inside the sign**, not the ordinal display degree. Therefore Ana's `10º Scorpio` anchor is entered as `--degree 9 --minute 52`.
