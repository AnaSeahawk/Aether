# Skill — passwords

*A secret must reach a program without reaching the agent.*

Adapted from [LiGoldragon/primary](https://github.com/LiGoldragon/primary)
secrets discipline.

---

## The absolute rule

An agent never sees a secret value. This is not a preference; it is the
load-bearing constraint the rest of this skill serves. A secret must never
appear in:

- stdout or stderr of any command you run;
- a log line, a report, a chat message, or a commit message;
- a command's `argv` (visible to any `ps` on the box);
- a shell trace (`set -x` while a secret variable is live);
- a checked-in plaintext file, a test fixture, or a temporary file.

---

## Password store

Passwords live in `gopass`. The store is GPG-encrypted and git-backed.

- `gopass ls` — list entry names (safe; shows names, never values).
- `gopass show -o <path>` — decrypt and emit the secret to stdout.
- `gopass show -c <path>` — copy to clipboard (avoid; agent cannot verify
  and clipboard is a leak surface).
- `gopass insert <path>` — insert interactively (agent cannot do this).
- `gopass generate <path> <length>` — generate and store a random password.

Never run `gopass show` without piping its output to a consumer. Bare
`gopass show` prints the secret to the terminal, which means into the
agent's context.

## Entry names

Store a website's primary login password at `<domain>/login`, using the bare
domain without a protocol or URL path. For example: `hetzner.com/login`.

---

## The pipe pattern

Move a secret by connecting the producer's stdout directly to the
consumer's stdin. The value lives only in the pipe buffer and the two
processes' memory.

```sh
set -o pipefail
gopass show -o <gopass-path> | <consumer-that-reads-stdin>
```

This is the only approved shape. Variations:

```sh
# Feed a password to a CLI that reads from stdin
gopass show -o site/login | some-cli login --password-stdin

# Pipe to a file descriptor the consumer expects
gopass show -o site/api-token | consumer --token-fd 0
```

---

## What is forbidden

Never use any of these to move a secret:

- **Command substitution** — `$(gopass show -o ...)` captures the value
  into the shell, which the agent can see.
- **Shell variables** — `TOKEN=$(...)` or `export TOKEN=...` exposes the
  value in the environment, in `argv`, and to `ps`.
- **Arguments** — `curl -u user:$(gopass show -o ...)` puts the secret
  in `argv`.
- **Environment variables set by the agent** — same as shell variables.
- **Temporary files** — writing a secret to a file, even briefly, risks
  leaving it on disk.
- **Clipboard** — `gopass show -c` or `xclip`; the agent has no control
  over clipboard lifetime.
- **Process substitution** — `<(gopass show -o ...)` creates an fd the
  agent could accidentally read.
- **tee / filters** — `tee`, `sed`, `awk`, `grep` on secret-bearing
  streams risk printing the value.

---

## Verifying blind

Confirm success without decrypting:

- **Exit code** — `echo $?` after the pipe.
- **Byte count** — `gopass show -o <path> | wc -c` prints a count, not
  the value.
- **Entry exists** — `gopass ls | grep -F <name>` lists names only.
- **Entry metadata** — `gopass show <path> | head -1` prints only the
  first line if the entry has key-value metadata below the password, but
  this is still risky. Prefer `gopass ls`.

---

## Minting a new secret

Generate and store without ever printing the value:

```sh
gopass generate <path> 32
```

Or from a CSPRNG:

```sh
head -c 32 /dev/urandom | base64 | gopass insert -f <path> >/dev/null
```

Confirm by `gopass ls | grep -F <name>` and exit code. Never
decrypt-to-check.

---

## Wrapper pattern for programs that need environment variables

When a program requires a secret in an environment variable, wrap the
invocation so the secret is fetched at exec time:

```sh
set -o pipefail
MYSECRET="$(gopass show -o <path>)" exec some-program
```

This is the one case where command substitution is acceptable — the value
is consumed immediately by `exec` and never reaches the agent. The agent
must not run this command with output capture; it must be a fire-and-forget
`exec` or a background launch.

If the consumer is a long-running service, the wrapper belongs in a systemd
unit or a shell script the user maintains — not in agent-generated commands.

---

## When this skill applies

- Any task that requires authentication credentials, API tokens, or
  passwords.
- Setting up a new service or tool that needs stored credentials.
- Rotating or verifying existing credentials.
- Any command where `gopass show` appears or is considered.

---

## See also

- `skills/sensitive-content.md` — broader sensitivity handling for private
  and operational material.
