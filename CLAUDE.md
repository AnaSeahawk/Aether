# CLAUDE.md

These instructions guide Claude working in the `anaseahawk/aether` seed repo.
Keep the repo clean, predictable, and easy for Ana Seahawk to extend.

Claude skills live in `.claude/skills/`. A skill may be symlinked from another
skill tree only when its instructions are genuinely identical and contain no
harness-specific model, tool, path, or behavior. Keep differing skills as
independent files.

For retrieval, transcript recovery, file discovery, and mechanical application
of already-made decisions, delegate to Sonnet with light thinking. Use Sonnet
with high thinking only when the bounded subtask itself requires independent
judgment. Use a higher-reasoning model only when Ana explicitly authorizes it.

Subagents receive narrow context and return concise results. A subagent that
changes files claims its exact paths, validates its work, commits and pushes its
owned change, and releases its lane before returning.
