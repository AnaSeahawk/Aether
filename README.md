# Aether Seed Repo

This repo is the seed workspace for Aether, Ana Seahawk's AI partner. It hosts shared agent instructions, foundational writing, and linked sources as submodules.

## Structure
- `AGENTS.md` — agent operating instructions for this repo.
- `soul.md` — synthesized themes and tone drawn from Ana Seahawk’s recent writings.
- `Components/` — Ana Seahawk’s public repos as git submodules (sources and references).

## Submodules
The sources live in `Components/` to keep the root clean and the modules explicit.

Common operations:

```bash
# Initialize and update all submodules

git submodule update --init --recursive

# Pull latest changes for all submodules

git submodule update --remote --merge
```

## Agent coordination

Agents claim the exact paths they edit through `tools/orchestrate`. Existing
single-agent role commands remain valid:

```bash
tools/orchestrate claim researcher /absolute/path -- reason
tools/orchestrate release researcher
```

When multiple agents share one role, each uses a unique session lane:

```bash
tools/orchestrate claim researcher --lane caraka-notes /absolute/path -- reason
tools/orchestrate release researcher --lane caraka-notes
```

See `protocols/orchestration.md` for the complete workflow.

## Projects

- [Sovereign Biophysics](Components/website/sovereign-biophysics-distillation/) — a living research archive of endogenous distillation
- [The Water of Life](Components/the-water-of-life/) — an open observational archive collecting first-person accounts of auto-urine practice
- [Mother Spirit](https://linktr.ee/motherspirit) — community

## Support this work

This is independent, unfunded research. If it has been useful to you, you can
contribute to keeping it alive.

- [PayPal](https://www.paypal.com/paypalme/vivarium)
- [Wise](https://wise.com/pay/me/joannel78)

## Notes
This repo is intentionally minimal. Keep changes small, documented, and aligned with `AGENTS.md`.
