# Orchestration Protocol

Coordinates multiple agents working in the same repo simultaneously. Simple
mechanism: each agent claims its paths before editing and releases when done.
Agents may use a role's original single lane or a uniquely named session lane.
The helper rejects overlapping claims, serializes claim changes, and refuses
to replace an active lane. It requires Bash, realpath, and util-linux `flock`.

A claim prints a release token and records when it was made. The token keeps one
session from releasing another session's lane by accident; the claim time makes
an abandoned lane visible and reclaimable. See "When a session ends without
releasing".

These are advisory edit claims; they do not block filesystem writes or Git
operations. The release token is an accident guard, not a security credential:
it is stored in the lock file, which any local process can read. Read-only
inspection needs no edit claim, but all privacy and consent boundaries still
apply.

---

## Ana quick start

Use this when running Claude Code, Codex, or another agent at the same time.

1. Decide what each agent is doing and choose the role that matches the work:
   `researcher`, `writer`, `curator`, or `analyst`.
2. If two agents share a role, give each a short session-lane name such as
   `caraka-notes` or `alchemy-notes`.
3. Give each agent a narrow path, not the whole repo.
4. Start each agent with the standard coordination prompt below.
5. If an agent reports a conflict, let it work somewhere else or wait until the
   other agent releases.
6. At the end of the session, make sure the agent committed, pushed, and
   released the same role and lane it claimed.
7. If a session ended without releasing — it was interrupted, closed, or ran
   out of context — its lane stays claimed and blocks that path. Run
   `tools/orchestrate stale` to see abandoned lanes and `tools/orchestrate
   clear <role> [--lane <lane>]` to reclaim one. No agent has to wait on a
   session that is gone.

Standard coordination prompt:

```text
Read AGENTS.md and protocols/orchestration.md before editing.
Use role: <role>.
Use session lane: <lane>. (Omit this line when the role has only one agent.)
Target path: <absolute path>.
First run tools/orchestrate status.
If the target is only your own report lane, reports are exempt:
write in reports/<role>/<lane>/ when assigned a session lane, or
reports/<role>/ when using the default role lane. Do not claim either path.
Otherwise, claim the target path with:
tools/orchestrate claim <role> [--lane <lane>] <absolute path> -- <short reason>
If there is a conflict, stop and tell me.
Work only inside the claimed path unless I approve more.
Keep the release token your claim prints; you need it to release.
Commit and push substantive changes, then release with:
tools/orchestrate release <role> [--lane <lane>] --token <your release token>
If a lane you need is held by a session that has ended, run
tools/orchestrate stale, then clear that lane and tell me what you cleared.
```

The bracketed `--lane` option means: include it only when a session lane was
assigned. It is explanatory notation, not text to paste literally.

Example with two researchers working at the same time:

```text
Claude Code:
Use role: researcher.
Use session lane: caraka-notes.
Target path: /home/bird/Git/aether/Components/bibliography/ayurveda
Reason: Caraka source notes

Codex:
Use role: researcher.
Use session lane: alchemy-notes.
Target path: /home/bird/Git/aether/Components/bibliography/alchemy
Reason: alchemy source notes
```

Both agents inherit the researcher discipline, but their separate locks and
report directories make their parallel work visible.

---

## Roles

| Role | Default lock | Reports subdir | Natural surface |
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

## Session lanes

A role names the discipline. A session lane names one agent's current seat
inside that discipline.

The original commands remain valid when only one agent uses a role:

```sh
tools/orchestrate claim researcher <path> -- <reason>
tools/orchestrate release researcher
```

When two agents share a role, each uses a unique lowercase lane name:

```sh
tools/orchestrate claim researcher --lane caraka-notes <path> -- <reason>
tools/orchestrate claim researcher --lane alchemy-notes <path> -- <reason>
```

Lane names may contain lowercase letters, digits, and hyphens. Choose a name
unique to the current session, not the model. Never reuse an active lane, even
for the same role. The helper stores dynamic lanes as
`<role>--<lane>.lock` and checks them against every default and dynamic lane.

---

## Claim before editing

Before editing any file, claim its path:

```sh
tools/orchestrate claim <role> [--lane <session>] <path> [more-paths] -- <reason>
```

Example:

```sh
tools/orchestrate claim researcher \
  /home/bird/Git/aether/Components/bibliography/ayurveda \
  -- pulling Caraka quotes for Living Waters
```

The helper checks for an active lane and overlapping paths before writing the
claim. A rejected claim leaves all existing claims unchanged. Existing
role-only commands use the role's default lane, so they are suitable only when
that lane is idle and no other session will use it.

A successful claim prints a release token:

```text
Release token for researcher--caraka-notes: d87f8777eb
```

Keep it for the whole session — releasing needs it. If a conflicting lane is
reported as `STALE`, its session has been holding the path past the
abandonment threshold; see "When a session ends without releasing".

Use absolute paths. Claiming a directory covers all files under it.
Paths must fit one lock-file record: no newlines, trailing whitespace, or
` #` delimiter. Reasons must occupy one line.

Claims cover whole files. Writer and curator roles cannot simultaneously edit
different conceptual layers of the same file. `AGENTS.md`, protocols, and role
skills are shared edit surfaces too: claim their exact paths and coordinate a
pause with affected sessions before changing their governing instructions.

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
tools/orchestrate release <role> [--lane <session>]
```

Release the same lane used for the claim as soon as the work is finished.
Don't hold paths between sessions.

If work narrows, release and reclaim the smaller path. Idle locks make the next
agent guess whether a surface is still active.

Release requires the token the claim printed:

```sh
tools/orchestrate release curator --lane living-record --token d87f8777eb
```

Only release a claim belonging to your session. A missing or wrong token is
refused with exit 3 and the lane is left standing, so one agent cannot clear
another's lane by guessing at the command. Records written before tokens
existed still release without one, and say so. An active lane cannot be
expanded or replaced by another `claim` call. To change its paths, pause edits,
release your own lane, and claim the complete new path set. Resume only if that
claim succeeds; another session may have claimed a path in the meantime.

---

## When a session ends without releasing

An interrupted session — closed terminal, exhausted context, crashed run —
leaves its lane claimed. Nothing expires on its own, so the path stays blocked
until someone reclaims it. This is the ordinary recovery path, not an
emergency.

Find abandoned lanes:

```sh
tools/orchestrate stale
tools/orchestrate stale --older-than 2
```

A lane counts as abandoned once it has been held longer than the threshold:
12 hours by default, or whatever `ORCHESTRATE_STALE_HOURS` sets. `status` marks
those lanes `STALE`, and a claim blocked by one says so.

Reclaim one:

```sh
tools/orchestrate clear <role> [--lane <session>]
tools/orchestrate clear curator --lane living-record --older-than 2
tools/orchestrate clear curator --lane living-record --force
```

`clear` prints the whole record it is removing — lane, claim time, paths, and
reason — so what was discarded stays visible. It refuses a lane younger than
the threshold: a recent claim usually means a session that is still working, and
the right move is to coordinate with it. `--older-than` lowers the threshold for
this call. `--force` skips the age check entirely; use it only when you know the
owning session has ended, and say in your report that you cleared someone's
lane.

Clearing a lane releases the claim, not the work. If that session left edits in
the working tree, inspect them before assuming the path is free.

---

## Status

```sh
tools/orchestrate status
```

Shows every default role lane and every active dynamic session lane, with when
each claim was made and how long it has been held:

```text
--- curator/living-record --- claimed 2026-09-19T08:14:02Z, 1d6h ago STALE
```

`STALE` means the lane has been held past the abandonment threshold and its
session may be gone. Run this before asking a second agent to start. It gives
the current map of what is safe to touch.

---

## Lock file format

`<role>.lock` and `<role>--<lane>.lock` are plain text. Lines beginning with `#`
are claim metadata; every other line is one claimed path, optionally followed by
`# reason`. Empty file means idle.

```
# lane: researcher--caraka-notes
# claimed: 2026-09-20T14:20:20Z
# epoch: 1789824021
# token: d87f8777eb
/home/bird/Git/aether/Components/bibliography/ayurveda # pulling Caraka quotes
```

`claimed` is human-readable; `epoch` is what the helper measures age against. A
record with no `epoch` falls back to the file's own timestamp, so age stays an
honest lower bound.

The helper uses `.orchestrate.guard.lock` to serialize validation and writes
across processes; `status` reads under the same guard. Do not remove that file
while helpers may be running. `ORCHESTRATE_WORKSPACE_ROOT` selects the shared
claim registry (and supports temporary test workspaces). Agents in separate
checkouts that coordinate shared surfaces must use the same registry. The
helper does not authenticate lane owners: the release token prevents accidental
cross-session releases, but any local process can read it or write these files
directly. Unique session names and correct release discipline remain necessary.

Lock files are runtime state — **do not commit them**. They are listed in
`.gitignore`.

---

## Reports — exempt from claim flow

Public reports are partitioned by role. A default role lane writes directly in its
role directory. A dynamic session lane writes in its own subdirectory:

```
reports/researcher/   ← researcher only
reports/researcher/caraka-notes/   ← that session lane only
reports/writer/       ← writer only
reports/curator/      ← curator only
reports/analyst/      ← analyst only
reports/              ← top-level: cross-role session intelligence (any role)
```

Dynamic session reports use a three-digit sequence local to their unique
directory, beginning with `001`. This prevents two simultaneous agents from
selecting the same global report number. After the parallel work finishes, the
coordinating analyst may write one consolidated top-level report using the next
available global number.

Do not claim report paths in your own lane and do not write into another
lane's report directory.

This exemption applies to public Aether reports only. Private continuity goes
to the verified private destination defined in `AGENTS.md` section 11 and needs
an exact-path claim. A role or lane directory in Aether never makes data private.

Even though reports are exempt, agents should still run
`tools/orchestrate status` before beginning so they understand what else is
happening in the repo.

---

## When paths conflict

If another lane holds a path you need, either:
- Wait for the other agent to release, then claim.
- File a note in `reports/analyst/` naming the blocker and the next action,
  and work something else.

Claims are coordination records, not operating-system locks. Do not proceed
after an overlap is reported. The value of the system is that Ana can see
exactly what is in flight at any moment by reading the lock files.

If Claude Code and Codex both need the same path, the cleanest flow is:

1. First agent finishes the smallest coherent unit.
2. First agent commits, pushes, and releases.
3. Second agent pulls or checks status, then claims and continues.

Do not let two agents "just make small edits" in the same file at the same
time. That is where merge confusion starts.

---

## Version control

Use separate worktrees/checkouts for concurrent editing where practical. If a
working tree is shared, agree on one session owning its index and HEAD from
staging through commit. A submodule has its own index; coordinate it separately.
The helper does not enforce this Git ownership.

Before committing, recheck status and your claims, inspect `git status`, stage
only explicit task-owned paths, and review the entire `git diff --cached`.
Recheck if the index or HEAD changes. If unrelated work is staged, stop and
coordinate; do not unstage or reset someone else's work. A displayed idle role
is not authorization to include that role's files.

Commit and push only authorized task changes. For submodule work, push the
inner commit before updating the parent pointer. Preserve publication gates and
pre-existing changes. See `AGENTS.md` sections 7 and 11.

---

## See also

- `AGENTS.md` — the full repo contract
- `tools/orchestrate` — the claim/release helper
- `skills/<role>.md` — per-role discipline
