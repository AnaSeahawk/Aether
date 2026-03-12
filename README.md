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

## Notes
This repo is intentionally minimal. Keep changes small, documented, and aligned with `AGENTS.md`.
