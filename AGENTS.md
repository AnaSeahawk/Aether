# Aether Agent Instructions

These instructions guide AI agents working in the `anaseahawk/aether` seed repo. Keep the repo clean, predictable, and easy for Ana Seahawk to extend.

All agents — Claude, Codex, Gemini, and others — should read this file before making any changes.

---

## Roles

The workspace supports four coordination roles for parallel agent work:

| Role | Surface | Skill file |
|---|---|---|
| `researcher` | `Components/bibliography/`, source research | `.agents/skills/researcher/SKILL.md` |
| `writer` | `Components/the-vessel/in-development/`, website prose | `.agents/skills/writer/SKILL.md` |
| `curator` | `Components/website/` structure and metadata | `.agents/skills/curator/SKILL.md` |
| `analyst` | `reports/`, session synthesis | `.agents/skills/analyst/SKILL.md` |

**Before starting work, know your role.** Read the relevant skill file and
claim your paths via `tools/orchestrate claim <role> <path> -- <reason>`.
Release when done: `tools/orchestrate release <role>`.

When more than one agent uses the same role, each must use a unique session
lane: `tools/orchestrate claim <role> --lane <session> <path> -- <reason>`.
Release that same lane with
`tools/orchestrate release <role> --lane <session>`.

See `protocols/orchestration.md` for the full coordination protocol.

See `protocols/active-surfaces.md` for which repos are public, what must never
be published, and the current sensitivity watchpoints. Read it before writing
into any public repo — `aether` itself is public.
See `.agents/skills/README.md` for the compact skill map.

### Skill Loading

Load only the skill files the work actually triggers:

- Always read this file and the skill file for the role you are using.
- Read `.agents/skills/prose/SKILL.md` for drafting, editing, or evaluating prose.
- Read `.agents/skills/sensitive-content/SKILL.md` before touching private, operational,
  health-adjacent, collaboration-private, or publishing-sensitive material.
- Read `.agents/skills/water-of-life/SKILL.md` when working with The Water of
  Life archive: contributor entries, templates, transcript processing, or
  methodology.
- Read `.agents/skills/audio-transcription/SKILL.md` when transcribing an
  existing audio or video file. Use its hosted route unless Ana explicitly
  requests the offline fallback.
- Read `.agents/skills/video/SKILL.md` when turning a recording into cleaned video, a
  transcript, or publishing drafts (`tools/mother_spirit_video`).
- Read `.agents/skills/passwords/SKILL.md` before any task involving passwords,
  API tokens, credentials, or `gopass`.
- Do not scan every skill file unless the task is explicitly about the skill
  system itself.

---

## Parent Context and Subagent Defaults

**The psyche** is the human managing the agent in the current session. The
parent agent preserves its context for thinking with the psyche: understanding
intent, holding continuity, making judgments, and carrying the conversation.
Move bounded execution work into subagents so search results, file discovery,
and mechanical editing do not crowd that shared context.

### Delegate by default

Make heavy use of subagents. Delegation is required when work involves:

- searching the web, repository, bibliography, or other source collections;
- research, source comparison, fact gathering, or broad discovery;
- broad or repetitive editing that can be divided into clearly owned paths;
- independent checks that can run in parallel without competing writes.

Keep a task in the parent only when it is small, tightly coupled to the current
conversation, or requires the parent's full judgment. Give each subagent a
narrow task, the minimum necessary context, explicit paths and constraints, and
a concise return format. Prefer parallel subagents for independent work. Do not
copy the full conversation into a subagent unless the task genuinely requires
it. The parent remains responsible for synthesis, verification, coordination,
and the final response to the psyche.

All subagents must follow this file, including path claims, sensitivity rules,
and publishing boundaries. Delegate only the access and material needed for the
task. Never use delegation to bypass a safety, consent, or review gate.

### Required model selection

Always select the subagent model and thinking effort explicitly. Do not accept
an automatic model choice and do not silently substitute a different model.

| Parent surface | Default subagent | Psyche-authorized higher-reasoning subagent |
|---|---|---|
| Codex | GPT-5.6 Luna, extra-high thinking | GPT-5.6 Terra, high thinking |
| Claude | Claude Sonnet 4.6, high thinking | Claude Opus 4.6, high thinking |

The default model is mandatory for every subagent unless the psyche explicitly
instructs the parent to use the higher-reasoning option. A parent must not
escalate merely because a task is difficult or broad. The psyche's instruction
may apply to one task, one group of tasks, or the session; do not infer a wider
authorization than was given.

Use the runtime's exact model identifier and reasoning-effort setting that
correspond to the names above. If the requested model or effort is unavailable,
do not choose a higher model automatically. Keep the work in the parent when
practical; otherwise tell the psyche what is unavailable and ask which fallback
to use.

---

## 0. Intent
- Build a solid, minimal programming base that is easy to extend.
- Prefer small, composable modules and explicit interfaces.
- Optimize for clarity, testability, and maintainability over cleverness.

## 1. Non‑Negotiables
- **No silent behavior changes.** If a change affects behavior, document it and update tests.
- **No dead code or unused dependencies.** Remove what you add if unused.
- **No speculative features.** Implement only what is asked or clearly required.
- **No destructive commands.** Never delete user data or repo history.
- **No deferring to the psyche.** When a task requires tool configuration, environment setup, shell commands, or other mechanical work the agent can perform, the agent does it. Never ask the psyche to run a command, configure a tool, or complete setup steps that the agent has the ability to execute. The psyche delegates work to the agent, not the other way around.

## 2. Repo Hygiene
- Keep root clean: only core files at repo root (`AGENTS.md`, `README.md`, config files). Place code in `src/` and tests in `tests/` when created.
- Prefer ASCII in filenames and content unless a domain term requires otherwise.
- Use consistent naming (snake_case for files, `PascalCase` for types, `camelCase` for variables/functions unless the language dictates otherwise).

## 3. Architecture Baseline
- Favor a **small core + adapters** model:
  - `src/core/` for domain logic.
  - `src/io/` for external boundaries (CLI, API, file IO).
  - `src/infra/` for persistence, network, or system integration.
- Keep domain logic free of IO side effects.
- Use interfaces or dependency injection to keep modules testable.

## 4. Coding Standards
- Prefer explicit types and clear error handling.
- Avoid global mutable state unless explicitly required.
- Treat input validation as part of core logic.
- Add brief comments only where the code is non-obvious.

## 5. Testing Expectations
- Add or update tests for all new or changed behavior.
- Prefer fast unit tests; add integration tests only when needed.
- If tests cannot be run, say why and what would be expected to pass.

## 6. Documentation
- Update `README.md` when behavior, usage, or setup changes.
- Keep documentation short and actionable.

## 7. Version Control & Change Discipline
- Make atomic changes. One intention per commit.
- Summarize changes and test status in responses.
- Do not modify files unrelated to the task.

## 8. Safety & Security
- Do not hardcode secrets or tokens.
- Avoid unsafe operations on user files or network access without explicit instruction.
- Validate external inputs; fail closed with helpful errors.

## 9. Agent Response Style
- Be concise and explicit about what changed.
- Reference files with exact paths.
- If assumptions are made, list them clearly.

## 10. When in Doubt
- Ask for clarification if requirements are ambiguous or high‑risk.
- Prefer a minimal, reversible change.

---

## 11. Report Protocol

When a session-end response is longer than a few lines, write it to a numbered report file instead of (or in addition to) returning it inline. This lets Ana review the report at her own pace while the agent continues other work, and keeps a readable audit trail outside the chat harness.

**Location:** Default role reports go in `reports/<role>/`; cross-role session
intelligence may go in `reports/` at the repo root. A dynamic session lane
writes only in `reports/<role>/<lane>/`.

**Naming:** Default role and top-level reports use the existing global,
zero-padded three-digit prefix:

```
reports/<role>/001_<slug>.md
reports/001_<slug>.md
...
```

Find the next global number by scanning files directly in `reports/` and
directly in `reports/<role>/`, then incrementing the highest prefix. Ignore
files nested inside a dynamic session-lane directory.

Dynamic session-lane reports use a sequence local to their unique directory,
beginning with `001`. The coordinating analyst writes any final consolidated
report into the global sequence after parallel work has finished.

**Report file format:**

```markdown
# <N>. <Title>

**Date:** YYYY-MM-DD  
**Agent:** <agent name/model>  
**Session topic:** <one-line summary>

---

<full response content here>
```

Keep inline responses short (a sentence or two pointing to the report file). The full detail lives in the file.

**End-of-session commit and push:** When a session ends with any file changes, commit all edits and push before closing. Use an atomic, descriptive commit message. If multiple repos were touched (e.g. a submodule plus the parent), commit each independently in the correct order (inner repo first, then update the parent pointer) and push both.

**Stale report handling:** When any information in an existing report is found to be outdated or no longer accurate, delete that report file and replace it with a new one at the next available number. The replacement should contain only information that is still valid, rewritten to reflect the current state. Do not edit stale reports in place — remove and replace so the report index stays trustworthy.

---

## 12. Repo Context

### Purpose

`aether` is Ana Seahawk's AI-companion seed repo. It holds agent instructions, voice/soul definition, and links to content via git submodules. The primary content lives in `Components/website` (the `AnaSeahawk/website` submodule).

`soul.md` defines Aether's voice, themes, and boundaries — consult it when drafting any content or framing language.

### Submodule Workflow

Most active work happens inside `Components/website`, which is a separate git repo (`AnaSeahawk/website`). Treat it as an independent repo when committing; then update the parent pointer in `aether`.

```bash
# Initialize submodules (first clone)
git submodule update --init --recursive

# Pull latest from all submodules
git submodule update --remote --merge

# After committing changes inside Components/website, update the pointer in aether:
git add Components/website
git commit -m "update website submodule after <description>"
```

All three submodules use SSH remotes (`git@github.com:AnaSeahawk/...`).

### Bibliography and Book Acquisition

Books and source files live in the `Components/bibliography` submodule, filed directly under their topic folders such as `alchemy/`, `ayurveda/`, `mythology/`, or `women-healers/`. The root `bibliography` path is a symlink to this submodule.

Use the local `annas` CLI when Ana asks to get books:

```bash
# Search by title, author, or topic
annas book-search "title or author"

# Download by MD5 hash into the bibliography shelf
ANNAS_DOWNLOAD_PATH=/home/bird/Git/aether/Components/bibliography/<topic> \
  annas book-download <md5_hash> <Author-Short-Title.ext>
```

The wrapper at `/home/bird/.nix-profile/bin/annas` sets `ANNAS_BASE_URL` and attempts to load `ANNAS_SECRET_KEY` from `gopass`. It defaults downloads to the current directory unless `ANNAS_DOWNLOAD_PATH` is set, so always set the path explicitly.

Prefer public-domain, openly licensed, or otherwise authorized sources. Do not download modern copyrighted books unless Ana has confirmed authorization. After download, verify that the file type matches the extension; Anna's metadata can mislabel files. For example:

```bash
head -c 16 Components/bibliography/<topic>/<file> | od -An -tx1 -c
```

If the file is mislabeled, rename it to the correct extension or replace it with a cleaner result. Then commit inside `Components/bibliography`, push that submodule, and commit the updated submodule pointer in `aether`.

### Content Architecture (Components/website)

Content is organized around **Four Pillars**:
1. **Alchemical Journals** — lived notes, field-writing (`The-Living-Year/`, `Dreamwork/`, `Foundations/`)
2. **Sovereign Biophysics** — method, experiments, synthesis (`sovereign-biophysics-distillation/`)
3. **The Living Year** — private container structure and rhythm notes (`The-Living-Year/`)
4. **Community & Open Archives** — routes to external spaces

### Content Metadata

Every content file carries YAML frontmatter with three tags:

- `status` — draft/review/approved/published
- `visibility` — `private` | `community` | `public`
- `claim_tier` — indicates sensitivity level of claims made

**Only `community` and `public` files are candidates for publishing.** `visibility` metadata is internal only — GitHub repo privacy settings control actual access, not these tags.

Some files also carry optional astronomical frontmatter (`sun:`, `moon:`, `moon-phase:`). **Do not attempt to fill these in** unless a CLI tool or direct data source is available to fetch the values efficiently. Manual lookup via astro.com is not a worthwhile use of session time. Leave blank fields blank and do not flag them as outstanding work.

### Publishing Workflow

1. **Review Queue** — `Components/website/REVIEW_QUEUE.md` tracks file status
2. **Checklist** — `Components/website/PUBLISH_CHECKLIST.md` is the 10-point pre-publish gate
3. **Batch Records** — `Components/website/PUBLISH_BATCH_YYYY-MM-DD.md` log approvals
4. Nothing is published without explicit user approval.

### Sensitive Content

The `sovereign-biophysics-distillation/` folder contains sensitive operational material. The intended direction (as of 2026-03-16) is to migrate this content to a separate private GitHub repo. Do not assume it is safe to publish or share. When in doubt about sensitivity, ask before acting.

Read `.agents/skills/sensitive-content/SKILL.md` before inspecting, editing, summarizing, or
moving sensitive files.

### Language Conventions

When writing or editing content in this repo:
- Use single-subject, non-clinical framing (no medical claims or directives)
- Maintain boundary language: personal record and responsibility only
- Match the quiet, precise, relational voice described in `soul.md`
- Prefer plain language; avoid jargon, hype, or performance
