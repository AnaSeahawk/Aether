# 98. Governance Repair and Verification

**Date:** 2026-09-19

**Agent:** Codex / GPT-6

**Session topic:** Complete the urgent coordination and authority repairs identified in Report 097

---

The bounded repair is complete. Agent rules now protect unrelated work, separate
release approval from source deletion, and define where private continuity may
be written. The coordination helper preserves existing claims on failure and
serializes simultaneous requests. The relevant tests passed.

Ana considers token exhaustion the likely explanation for the September 7
interruption. This was not independently verified against runtime usage. The
coordination and staging failures warranted repair regardless of that cause.

The work followed this sequence:

1. Claim the exact governing files and test paths; preserve the pre-existing
   private-submodule indication.
2. Repair claim handling and align the shared rules with actual Git behavior.
3. Reconcile credentials, publication/deletion authority, and report privacy.
4. Exercise failure and concurrency cases, obtain independent read-only checks,
   validate the skills, and review the complete staged change before committing.

**What changed**

| Area | Completed repair | Main files |
|---|---|---|
| Claims | Check ownership and overlap before writing; reject reuse of active default or session lanes; preserve all prior claims after rejection; serialize claim/release/status operations with `flock`; recognize root and normalized overlapping paths; reject malformed lock records. | [orchestrate](../tools/orchestrate), [tests](../tests/test_orchestrate.sh) |
| Shared Git work | Stage explicit task-owned paths, inspect the entire staged diff, recheck claims before committing, and stop if unrelated work is staged. Use separate worktrees or coordinate exclusive staging/commit access within each repository. | [AGENTS.md](../AGENTS.md), [orchestration](../protocols/orchestration.md), [README](../README.md) |
| File ownership | Writer and curator roles share responsibility but cannot simultaneously own different layers of one file. Shared instruction changes require exact claims and coordination with affected sessions. | Writer and curator skills, AGENTS.md, orchestration protocol |
| Credential handling | Remove the shell-wrapper exception and decrypted-output verification examples. Add a bounded stdin consumer that correctly prefixes `login:` and suppresses store output. Document supported stdin/FD or in-process consumers. | [Password skill](../.agents/skills/passwords/SKILL.md), [metadata consumer](../.agents/skills/passwords/scripts/append_login.py), [tests](../tests/test_password_login.py) |
| Release authority | Separate private preparation, contributor consent, Ana's release approval, and source deletion. Existing approval for the same release remains valid. Evidence alone grants no release authority; the claim-tier example now includes all four tiers. | Water of Life, curator, and sensitive-content skills; AGENTS.md |
| Reporting | Ordinary read-only answers may stay in chat. Every Aether report lane is explicitly public. Private continuity has a defined destination in the Vessel, conditional on verifying repository privacy and claiming the destination. Analyst write ownership no longer includes other roles' report directories. | Analyst and sensitive-content skills; AGENTS.md; active-surfaces and orchestration protocols |

The password metadata consumer is for an entry just created by `gopass generate`.
It is not a general credential migration tool. It rejects empty, multiline,
control-character, oversized, and option-like input where applicable. It returns
generic failures without echoing the login or the store's output. All checks
used dummy values; no credentials or real store entries were accessed.

**Verification**

- `bash tests/test_orchestrate.sh` passed. Coverage includes legacy commands,
  independent session lanes, same-role and cross-role overlaps, retained claims
  after failed replacement, active-lane reuse, parent/root/symlink overlaps,
  rejected multipath requests, malformed inputs, simultaneous overlapping and
  independent claims, simultaneous reuse of one lane, and missing `flock`.
- `python3 -m unittest discover -s tests -p test_password_login.py` passed all
  five tests, covering framing, rejected inputs, output suppression, failed
  store commands, and an unavailable store executable.
- An independent temporary dummy-store probe verified stdin-only value transfer,
  no value in command arguments or output, and generic failure reporting.
- A temporary Git repository exercise verified that explicit staging preserves
  unrelated edits and untracked files. Full-index inspection identified an
  unrelated staged file before any commit.
- The skill creator's validator accepted all six edited skills. Its missing
  PyYAML dependency was supplied in a temporary virtual environment, which was
  removed afterward; no project dependency was added.
- Shell syntax checks and whitespace checks passed. Independent scenario review
  covered existing release approval, contributor-only approval, private intake,
  shared-index conflicts, private reports, same-file role overlap, and an
  environment-only credential interface. The governing rule for unrelated staged
  work is to stop and coordinate, never silently unstage another session's work.

**Practical limits and the next use**

Claims remain advisory. They do not authenticate a lane owner, prevent arbitrary
filesystem writes, or lock a Git index. An agent must use a unique session lane
and release only its own claims. To change an active lane's paths, pause edits,
release it, and claim the complete new set; resume only after success. Agents
coordinating shared surfaces from separate checkouts need the same claim
registry. The helper now requires util-linux `flock`, available on this machine.

These checks validate the repaired operating paths, not every tool in Aether or
the live website. Video/VAAPI alignment, Phoenix setup, domain-skill
consolidation, architecture/map cleanup, bibliography work, and private-history
decisions remain separate tasks. Reports 095-097 remain dated evidence of the
incident and audit; this report records which recommendations are now complete.

No website content, source submissions, recordings, private drafts, or repository
history were changed. Website plans remain paused. The next authorized task can
use the repaired workflow without first completing the entire maintenance
backlog.
