# Aether Agent Instructions

These instructions guide AI agents working in the `anaseahawk/aether` seed repo. Keep the repo clean, predictable, and easy for Ana Seahawk to extend.

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
