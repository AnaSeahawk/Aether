# 1. Runtime lock cleanup

**Date:** 2026-10-23
**Agent:** Codex
**Session topic:** Remove orchestration clutter and prevent recurrence

---

Removed 59 empty, ignored coordination records from the working-tree root.
The only active claim belonged to this cleanup and was moved into Git metadata.
No other session claim was cleared.

No lock paths are tracked or present in fetched main history, so no history
rewrite is needed. Preserve existing history and push the workflow correction
as a normal commit.

`tools/orchestrate` now uses the Git common directory's
`aether-orchestration/` registry. Linked worktrees share the registry; independent
checkouts can select a shared registry with `ORCHESTRATE_WORKSPACE_ROOT`.
Release and clear remove records instead of retaining empty files.

Verification: `bash tests/test_orchestrate.sh` passed, including default storage,
linked-worktree conflicts, release deletion, and clear deletion. Unrelated
submodule edits and the untracked output directory were preserved.
