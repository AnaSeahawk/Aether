# Orchestration Protocol

Coordinates multiple agents working in the same repo simultaneously. Simple
mechanism: each agent claims its paths before editing and releases when done.
Agents may use a role's original single lane or a uniquely named session lane.
Two agents cannot hold overlapping paths at the same time.

This is a coordination protocol, not a hard filesystem lock. It works when each
agent reads this file, checks the current locks, claims before editing, and
releases when finished.

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
Commit and push substantive changes, then release with:
tools/orchestrate release <role> [--lane <lane>]
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
for the work, not the model. The helper stores dynamic lanes as
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

The helper writes your lane's lock file, checks every other lock for overlap,
and rejects the claim if there is a conflict. Existing role-only commands use
the role's default lane.

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
tools/orchestrate release <role> [--lane <session>]
```

Release the same lane used for the claim as soon as the work is finished.
Don't hold paths between sessions.

If work narrows, release and reclaim the smaller path. Idle locks make the next
agent guess whether a surface is still active.

---

## Status

```sh
tools/orchestrate status
```

Shows every default role lane and every active dynamic session lane.

Run this before asking a second agent to start. It gives the current map of
what is safe to touch.

---

## Lock file format

`<role>.lock` and `<role>--<lane>.lock` are plain text. Each line is one
claimed path, optionally followed by `# reason`. Empty file means idle.

```
/home/bird/Git/aether/Components/bibliography/ayurveda # pulling Caraka quotes
```

Lock files are runtime state — **do not commit them**. They are listed in
`.gitignore`.

---

## Reports — exempt from claim flow

Reports are partitioned by role. A default role lane writes directly in its
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

After any substantive change, commit and push. From `AGENTS.md`: atomic commits,
one intention per commit. For submodule work: commit and push the submodule
first, then commit the updated pointer in the parent.

---

## See also

- `AGENTS.md` — the full repo contract
- `tools/orchestrate` — the claim/release helper
- `skills/<role>.md` — per-role discipline
