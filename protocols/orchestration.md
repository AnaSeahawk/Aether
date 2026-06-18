# Orchestration Protocol

Coordinates multiple agents working in the same repo simultaneously. Simple
mechanism: each role claims its paths before editing, releases when done. Two
agents cannot hold overlapping paths at the same time.

This is a coordination protocol, not a hard filesystem lock. It works when each
agent reads this file, checks the current locks, claims before editing, and
releases when finished.

---

## Ana quick start

Use this when running Claude Code, Codex, or another agent at the same time.

1. Decide what each agent is doing and choose the role that matches the work:
   `researcher`, `writer`, `curator`, or `analyst`.
2. Give each agent a narrow path, not the whole repo.
3. Start each agent with the standard coordination prompt below.
4. If an agent reports a conflict, let it work somewhere else or wait until the
   other agent releases.
5. At the end of the session, make sure the agent committed, pushed, and ran
   `tools/orchestrate release <role>`.

Standard coordination prompt:

```text
Read AGENTS.md and protocols/orchestration.md before editing.
Use role: <role>.
Target path: <absolute path>.
First run tools/orchestrate status.
If the target is only your own reports/<role>/ lane, reports are exempt:
write only there and do not claim.
Otherwise, claim the target path with:
tools/orchestrate claim <role> <absolute path> -- <short reason>
If there is a conflict, stop and tell me.
Work only inside the claimed path unless I approve more.
Commit and push substantive changes, then release with:
tools/orchestrate release <role>
```

Example Claude/Codex split:

```text
Claude Code:
Use role: curator.
Target path: /home/bird/Git/aether/Components/website
Reason: website archive metadata work

Codex:
Use role: analyst.
Target path: /home/bird/Git/aether/reports/analyst
Reason: session synthesis
```

This lets one agent work in website structure while another writes analysis,
without both touching the same files.

---

## Roles

| Role | Lock file | Reports subdir | Natural surface |
|---|---|---|---|
| `researcher` | `researcher.lock` | `reports/researcher/` | `Components/bibliography/`, source research |
| `writer` | `writer.lock` | `reports/writer/` | `Components/the-vessel/in-development/`, website prose |
| `curator` | `curator.lock` | `reports/curator/` | `Components/website/` structure and metadata |
| `analyst` | `analyst.lock` | `reports/analyst/` | `reports/`, session synthesis |

Any agent may take any role. The role determines which paths it owns and which
subdirectory its reports go in.

Pick the role by the work, not by the model. Claude Code can be `curator`;
Codex can be `writer`; Gemini can be `researcher`; the protocol only cares that
the role and path are claimed honestly.

---

## Claim before editing

Before editing any file, claim its path:

```sh
tools/orchestrate claim <role> <path> [more-paths] -- <reason>
```

Example:

```sh
tools/orchestrate claim researcher \
  /home/bird/Git/aether/Components/bibliography/ayurveda \
  -- pulling Caraka quotes for Living Waters
```

The helper writes your role's lock file, checks every other lock for overlap,
and rejects the claim if there is a conflict.

Use absolute paths. Claiming a directory covers all files under it.

Prefer the smallest useful claim:

```sh
# Good: one website room
tools/orchestrate claim curator \
  /home/bird/Git/aether/Components/website/The-Vessel \
  -- updating living record pages

# Too broad for most work
tools/orchestrate claim curator \
  /home/bird/Git/aether/Components/website \
  -- updating one page
```

Broad claims are sometimes appropriate for full-site link checks,
archive-generation work, or large restructures. Otherwise, narrow claims keep
parallel work flowing.

---

## Release when done

```sh
tools/orchestrate release <role>
```

Release as soon as the work is finished. Don't hold paths between sessions.

If work narrows, release and reclaim the smaller path. Idle locks make the next
agent guess whether a surface is still active.

---

## Status

```sh
tools/orchestrate status
```

Shows every role's current lock file.

Run this before asking a second agent to start. It gives the current map of
what is safe to touch.

---

## Lock file format

`<role>.lock` is plain text. Each line is one claimed path, optionally
followed by `# reason`. Empty file means idle.

```
/home/bird/Git/aether/Components/bibliography/ayurveda # pulling Caraka quotes
```

Lock files are runtime state — **do not commit them**. They are listed in
`.gitignore`.

---

## Reports — exempt from claim flow

Reports are partitioned by role subdirectory. Each role's subdirectory is its
implied write lane. Do not claim report paths in your own lane; do not write
into another role's subdirectory.

```
reports/researcher/   ← researcher only
reports/writer/       ← writer only
reports/curator/      ← curator only
reports/analyst/      ← analyst only
reports/              ← top-level: cross-role session intelligence (any role)
```

Top-level session intelligence reports (`reports/NNN_session-intelligence-*.md`)
may be written by any role. Use the next available number across all files in
`reports/` and subdirectories.

Even though reports are exempt, agents should still run
`tools/orchestrate status` before beginning so they understand what else is
happening in the repo.

---

## When paths conflict

If another role holds a path you need, either:
- Wait for the other agent to release, then claim.
- File a note in `reports/analyst/` naming the blocker and the next action,
  and work something else.

Do not proceed without claiming. The value of the system is that Ana can see
exactly what is in flight at any moment by reading the lock files.

If Claude Code and Codex both need the same path, the cleanest flow is:

1. First agent finishes the smallest coherent unit.
2. First agent commits, pushes, and releases.
3. Second agent pulls or checks status, then claims and continues.

Do not let two agents "just make small edits" in the same file at the same
time. That is where merge confusion starts.

---

## Version control

After any substantive change, commit and push. From `AGENTS.md`: atomic commits,
one intention per commit. For submodule work: commit and push the submodule
first, then commit the updated pointer in the parent.

---

## See also

- `AGENTS.md` — the full repo contract
- `tools/orchestrate` — the claim/release helper
- `skills/<role>.md` — per-role discipline
