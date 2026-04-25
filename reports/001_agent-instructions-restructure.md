# 1. Agent Instructions Restructure

**Date:** 2026-04-25  
**Agent:** Claude Sonnet 4.6  
**Session topic:** Make CLAUDE.md a thin wrapper; consolidate all instructions in AGENTS.md; add report protocol.

---

## What changed

### CLAUDE.md
Reduced to a four-line pointer. Its sole purpose is now to tell Claude Code (and any other tool that reads `CLAUDE.md`) to load `AGENTS.md` for the actual instructions. No content lives here anymore.

### AGENTS.md
Two new sections appended; all existing sections preserved:

**Section 11 — Report Protocol**
Defines the numbered report convention:
- Reports go in `reports/` at the repo root.
- Files are named `NNN_<slug>.md` (zero-padded to three digits, incrementing).
- Each report carries a standard header: date, agent, session topic.
- Agents keep inline responses short and put full detail in the file.
- Ana can read the report at her own pace while the agent continues other work.

**Section 12 — Repo Context**
Everything that was in CLAUDE.md beyond the four-line pointer: submodule workflow, content architecture (Four Pillars), content metadata schema, publishing workflow, sensitive content warning, and language conventions. Moved here so Codex, Gemini, and any other agent that reads AGENTS.md gets the full picture.

### reports/
Directory created with `.gitkeep`. This file (`001_...`) is the first occupant.

## Why this matters

Previously, repo context lived in CLAUDE.md (Claude-only) and coding standards lived in AGENTS.md. Any non-Claude agent missed the content-specific rules. Now there is one authoritative file; CLAUDE.md is just a door.

The report protocol solves a friction point: long agent responses inside the Claude Code harness are hard to read and disappear when the session ends. A numbered markdown file is persistent, skimmable, and easy to share.

## Next steps (optional)

- Commit both files and `reports/` to the `aether` repo.
- Consider adding a short mention of `reports/` to the root `README.md` if one exists, so the convention is discoverable.
