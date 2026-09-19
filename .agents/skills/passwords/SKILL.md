---
name: passwords
description: 'A secret must reach a program without reaching the agent. GoPass pipe discipline for passwords, API tokens, and credentials.'
---

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

## Default login metadata

Use the `my-email` Gopass entry as the default login for every new password
entry unless the user explicitly supplies a different login. Store its content
as a `login: <email>` line.

For a new entry, generate the password and append that metadata without
displaying the email. Run from the Aether root:

```sh
set -euo pipefail
gopass generate <domain>/login 32
gopass show -o my-email | python3 .agents/skills/passwords/scripts/append_login.py <domain>/login
```

Use `--force` only when the user explicitly asks to replace an existing
password.

The bundled consumer validates a bounded single-line input, prefixes `login:`,
and sends it to `gopass insert --append` over stdin. Store output is suppressed;
failure returns a generic message and nonzero exit status. Use this append step
only on the entry just created; do not blindly add duplicate login fields to an
existing entry. Validate the helper with dummy inputs, never by displaying real
metadata or passwords.

---

## The pipe pattern

Move a secret by connecting the producer's stdout directly to the
consumer's stdin. The value lives only in the pipe buffer and the two
processes' memory.

```sh
set -o pipefail
gopass show -o <gopass-path> | <consumer-that-reads-stdin>
```

Use this shape for CLI secret transfer. A purpose-built consumer may retrieve
a secret internally and use it in that same process, as the hosted transcription
client does, provided it never exposes the value through output, arguments,
environment variables, or files. CLI variations:

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
  into the shell outside the consuming program.
- **Shell variables** — shell expansion, tracing, export, or later argument
  construction can expose them. Keep secret handling inside the consumer.
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
- **Entry exists** — `gopass ls | grep -F <name>` lists names only.
- **Entry metadata** — never print decrypted lines to verify a write. The first
  line is normally the password. Use the consumer's exit status and entry names.

---

## Minting a new secret

Generate and store without ever printing the value:

```sh
gopass generate <path> 32
```

Do not substitute a CSPRNG-to-`gopass insert` pipeline for password creation.
Use `gopass generate` so Gopass owns generation and storage. Confirm by
`gopass ls | grep -F <name>` and exit code. Never decrypt-to-check.

---

## Programs that require environment variables

There is no shell-wrapper exception. Use a supported stdin/file-descriptor
interface, or implement a purpose-built consumer that retrieves and uses the
credential internally. Validate it with dummy values before accessing a real
credential. If the program only accepts an environment variable, report that
interface limitation and select or implement a supported integration within the
authorized task; do not silently export a secret or delegate setup to Ana.

---

## When this skill applies

- Any task that requires authentication credentials, API tokens, or
  passwords.
- Setting up a new service or tool that needs stored credentials.
- Rotating or verifying existing credentials.
- Any command where `gopass show` appears or is considered.

---

## See also

- `.agents/skills/sensitive-content/SKILL.md` — broader sensitivity handling for private
  and operational material.
