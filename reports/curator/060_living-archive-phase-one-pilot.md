# 60. Living Archive Phase One Pilot

**Date:** 2026-06-16
**Role:** curator
**Session topic:** Implement the first living-archive metadata and generated-view pilot while preserving the existing SB reader path.

---

## What Changed

Website submodule commit:

- `Components/website` commit `e98699e` - `add living archive pilot views`

Created the draft generated living-map layer:

- `Components/website/archive/ENTRY_SCHEMA.md` defines the opt-in archive entry schema.
- `Components/website/archive/entry-template.md` gives future entries a reusable metadata template.
- `Components/website/archive/README.md` is the generated chronological pilot view.
- `Components/website/archive/by-thread.md` is the generated thread view.
- `Components/website/tools/build_archive_views` builds the generated views from frontmatter.

Added `archive_entry: true` pilot metadata to ten existing records:

- `Components/website/The-Vessel/journal/living-journal-2026.md`
- `Components/website/The-Vessel/journal/the-deepest-layer.md`
- `Components/website/The-Vessel/community/2026-06-12-fiona-gardner-musculoskeletal-release.md`
- `Components/website/sovereign-biophysics-distillation/00-orientation/the-jar-held-to-the-light.md`
- `Components/website/sovereign-biophysics-distillation/00-orientation/the-three-waters.md`
- `Components/website/sovereign-biophysics-distillation/20-experiments/experiment-report-june4-fresh-plasma-h2-retention.md`
- `Components/website/sovereign-biophysics-distillation/20-experiments/experiment-report-june10-three-batch-fresh-plasma.md`
- `Components/website/sovereign-biophysics-distillation/20-experiments/experiment-report-june13-menstrual-plasma.md`
- `Components/website/sovereign-biophysics-distillation/40-synthesis/synthesis-three-year-topical-observations.md`
- `Components/website/sovereign-biophysics-distillation/40-synthesis/synthesis-current-state-may-2026.md`

Updated:

- `Components/website/ARCHITECTURE.md` now records `archive/` as a draft generated living-map pilot and `tools/` as the helper lane.

## What Stayed Protected

No source files were moved.

No Sovereign Biophysics reader-path links were changed.

The private community story remains private. The generated views show it only as a private stub and do not link directly to the private story file.

The new `archive/` views are marked `visibility: community` and `status: draft`. They are not linked from the public website README yet.

## What Was Learned

The pilot confirms the architecture can work without flattening the rooms.

Ten records are enough to make a living field visible: journal, private community observation, threshold orientation, experiment reports, and synthesis can appear together by chronology and thread while still keeping their source locations.

The current metadata vocabulary is usable, but thread names will need stewardship. The first generated `by-thread.md` view is useful, but it already shows that thread proliferation can happen quickly if names are not tended.

`living-journal-2026.md` remains the awkward but important case. It is one continuous journal object containing many dated inner entries. For now it appears as one archive entry with its start date. Later, selected inner entries may need separate records or a section-level indexing strategy.

## Verification

Checks run:

- `Components/website/tools/build_archive_views` - built 10 living archive entries.
- `python3 -m py_compile Components/website/tools/build_archive_views` - passed.
- Local Markdown link check across `Components/website` - passed.
- `git -C Components/website diff --check` - passed before commit.
- ASCII scan for new archive/schema/tool files - clear.

## Next

Review the feel of:

- `Components/website/archive/README.md`
- `Components/website/archive/by-thread.md`

If the map feels useful, the next curator step is not a full migration. The next step should be one of:

- add a `by-entry-point.md` generated view;
- add a `by-inquiry.md` generated view;
- add 5-10 more carefully chosen entries;
- refine thread vocabulary before expansion.

Do not link `archive/` from the public website front door until Ana confirms the pilot should become a visible reader doorway.
