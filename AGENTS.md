# Aether Agent Instructions

These instructions guide AI agents working in the `anaseahawk/aether` seed repo. Keep the repo clean, predictable, and easy for Ana Seahawk to extend.

All agents — Claude, Codex, Gemini, and others — should read this file before making any changes.

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

**Location:** `reports/` at the repo root.

**Naming:** zero-padded three-digit prefix, followed by a short slug:

```
reports/001_<slug>.md
reports/002_<slug>.md
...
```

Find the next available number by scanning existing files in `reports/` and incrementing the highest prefix.

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

### Publishing Workflow

1. **Review Queue** — `Components/website/REVIEW_QUEUE.md` tracks file status
2. **Checklist** — `Components/website/PUBLISH_CHECKLIST.md` is the 10-point pre-publish gate
3. **Batch Records** — `Components/website/PUBLISH_BATCH_YYYY-MM-DD.md` log approvals
4. Nothing is published without explicit user approval.

### Sensitive Content

The `sovereign-biophysics-distillation/` folder contains sensitive operational material. The intended direction (as of 2026-03-16) is to migrate this content to a separate private GitHub repo. Do not assume it is safe to publish or share. When in doubt about sensitivity, ask before acting.

### Language Conventions

When writing or editing content in this repo:
- Use single-subject, non-clinical framing (no medical claims or directives)
- Maintain boundary language: personal record and responsibility only
- Match the quiet, precise, relational voice described in `soul.md`
- Prefer plain language; avoid jargon, hype, or performance
