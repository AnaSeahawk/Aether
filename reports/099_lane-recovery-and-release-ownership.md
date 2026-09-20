# 99. Lane Recovery and Release Ownership

**Date:** 2026-09-20

**Agent:** Claude Opus 5 / Claude Code

**Session topic:** Review Report 098 with Ana, then repair the two coordination
gaps that review found

---

Report 098's repairs hold up. Both of its test suites were re-run independently
here and passed, and the files it describes contain the changes it claims. This
report records two gaps that review found in the repaired coordination helper,
the repair of both, and one sentence in 098 that claimed more protection than
the code provided.

Ana reviewed the findings and authorized these two repairs. Items she deferred
are listed at the end; they were not touched.

**What review found**

| Gap | Why it mattered |
|---|---|
| A lane claimed by a session that ends without releasing stays claimed forever. Nothing recorded when a claim was made, nothing expired, and no document said who may clear an abandoned lane or how. | The September 7 incident was an interrupted session. The repair hardened claims against replacement without giving the next agent any way past a claim left by a session that is gone. |
| `release` performed no ownership check at all. Any agent could clear any lane, then claim its paths. | 098's table reported that the helper rejects reuse of an active lane. That is true of `claim` and was not true of `release`, which made the stated protection bypassable in two commands. |

**What changed**

| Area | Repair | Main files |
|---|---|---|
| Claim records | A claim now records its lane, claim time (human-readable and epoch), and a release token. Metadata lines begin with `#` and are ignored by the path parser, so older records still parse and release. | [orchestrate](../tools/orchestrate) |
| Release ownership | `release` requires the token its claim printed. A missing or mismatched token exits 3 and leaves the lane standing, naming `clear` as the route for an abandoned lane. Records written before tokens still release without one and say so. | orchestrate, [AGENTS.md](../AGENTS.md), [orchestration](../protocols/orchestration.md), [README](../README.md) |
| Abandonment visibility | `status` shows how long each lane has been held and marks `STALE` past the threshold. `stale` lists abandoned lanes with their paths and the exact command to reclaim each. A claim blocked by a stale lane says so. | orchestrate |
| Recovery | New `clear <role> [--lane <session>]` reclaims an abandoned lane. It prints the full record it removes, refuses a lane younger than the threshold, and takes `--older-than <hours>` or `--force` to override. Threshold is 12 hours, or `ORCHESTRATE_STALE_HOURS`. | orchestrate, AGENTS.md, orchestration, README |
| Documented procedure | The protocol gained a "When a session ends without releasing" section; the standard coordination prompt now carries the token and the recovery instruction. Ana's quick start says what to do when an agent reports a blocked path. | orchestration, AGENTS.md, README |

**Correction to Report 098**

098's "What changed" table states that the helper rejects reuse of an active
default or session lane. That described `claim` only. `release` accepted any
lane name from any caller, so an agent could release a lane it did not own and
then claim those paths — the outcome the row appeared to exclude. 098 does say
elsewhere that claims are advisory and that the helper does not authenticate a
lane owner, which is still true. The narrower point is that the specific
protection it reported was reachable around. That is now repaired for accidental
releases. 098 otherwise stands as written and was not edited.

**Verification**

- `bash tests/test_orchestrate.sh` passed, before and after the change. The
  suite's existing coverage was preserved; every owning-session release in it
  now passes the token its claim recorded.
- New coverage: recorded metadata and token format; claimed paths parsed
  correctly alongside metadata lines; release refused with no token and with a
  wrong token, lane intact in both cases; release accepted with the right token;
  pre-token records released with and without a token; `clear` refused on a
  fresh lane; `clear` accepted with `--older-than 0` and with `--force`; `clear`
  on an idle lane; a back-dated lane surfacing in `status` and `stale`, blocking
  a claim with a stale notice, then being reclaimed and the blocked claim
  succeeding; invalid hour arguments rejected.
- `python3 -m unittest discover -s tests -p test_password_login.py` passed, five
  tests, unchanged by this work.
- A manual end-to-end run in a temporary workspace exercised claim, refused
  release, back-dated abandonment, `stale`, and `clear`. No repository lock file
  was used for that test.
- This session's own lane was claimed before the edits by the previous helper,
  so its release exercised the pre-token compatibility path on a real record.
- `bash -n` passed on the helper and the suite.

**Limits**

The threshold is a heuristic about elapsed time, not detection that a session
died. A legitimately long task that holds a lane more than twelve hours will be
marked `STALE` and can be cleared by another agent while it is still working.
Agents working that long should re-check `status` before committing, which the
protocol already requires.

The token prevents accidental cross-session releases. It is not authentication:
it is stored in the lock file, readable by any local process, and `--force`
bypasses the age check entirely. Claims remain advisory records that do not
block filesystem writes or Git operations, and `clear` frees a claim, not
whatever the ended session left in the working tree.

Age falls back to the lock file's own timestamp when a record has no `epoch`
line, which is a lower bound rather than the true claim time.

**Still open**

Ana deferred these; nothing here touched them.

- Video rendering (VAAPI versus the `libx264` paths), Phoenix calculator setup,
  the skill map's omissions, and Solar Journal consolidation — all carried
  forward from Reports 096 and 097 and still unrepaired.
- Report filing. Reports 095-097 are in `reports/analyst/` and 098 is at the top
  level; report numbers are not unique across lane directories, and `058` is
  already used twice. This report sits at the top level, which the protocol
  reserves for cross-role session intelligence and which matches 098. The
  convention question itself is unresolved.

No website content, submissions, recordings, private material, or repository
history were changed.
