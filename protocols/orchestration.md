# Orchestration Protocol

Coordinates multiple agents working in the same repo simultaneously. Simple
mechanism: each role claims its paths before editing, releases when done. Two
agents cannot hold overlapping paths at the same time.

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

---

## Release when done

```sh
tools/orchestrate release <role>
```

Release as soon as the work is finished. Don't hold paths between sessions.

---

## Status

```sh
tools/orchestrate status
```

Shows every role's current lock file.

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

---

## When paths conflict

If another role holds a path you need, either:
- Wait for the other agent to release, then claim.
- File a note in `reports/analyst/` naming the blocker and the next action,
  and work something else.

Do not proceed without claiming. The value of the system is that Ana can see
exactly what is in flight at any moment by reading the lock files.

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
