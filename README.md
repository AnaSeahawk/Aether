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
tools/orchestrate release researcher --token <token printed by the claim>
```

When multiple agents share one role, each uses a unique session lane:

```bash
tools/orchestrate claim researcher --lane caraka-notes /absolute/path -- reason
tools/orchestrate release researcher --lane caraka-notes --token <token>
```

An active lane cannot be overwritten; failed claims preserve existing records.
To change paths, pause edits, release your own lane, and claim the new set.
Each claim prints a release token that the release requires, so one session
cannot clear another's lane by accident. It is an accident guard, not a
credential.

A session that ends without releasing leaves its lane claimed; nothing expires
on its own:

```bash
tools/orchestrate status                  # claim age; STALE marks a likely dead lane
tools/orchestrate stale                   # lanes held past the threshold (12h default)
tools/orchestrate clear researcher --lane caraka-notes
```

`clear` prints the record it removes and refuses a lane younger than the
threshold unless given `--older-than <hours>` or `--force`.

The helper requires Bash, realpath, and util-linux `flock` to serialize updates.
`ORCHESTRATE_WORKSPACE_ROOT` can select a shared registry for multiple checkouts.
`ORCHESTRATE_STALE_HOURS` sets the abandonment threshold.

Use separate worktrees for concurrent editing, or coordinate exclusive staging
and commits in each shared repository. Before committing, recheck claims and
review the full staged diff; include only explicit task-owned paths. Claims do
not enforce Git ownership or grant publication/deletion approval.

Run the coordination and dummy-data metadata checks with:

```bash
bash tests/test_orchestrate.sh
python3 -m unittest discover -s tests -p test_password_login.py
```

See `protocols/orchestration.md` for the complete workflow and `AGENTS.md`
section 11 for public versus private report placement.

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
