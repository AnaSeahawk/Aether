# 70. Paid Access Prep: Threads, Metadata, Privacy

**Date:** 2026-06-20
**Role:** curator
**Session topic:** Resolve audit items 3-5 from report 069: thread vocabulary, metadata boundary, and private community-story placement.

---

## What Changed

### Website Submodule

Created:

- `Components/website/archive/THREADS.md`
- `Components/website/ACCESS_BOUNDARIES.md`
- `Components/website/The-Vessel/community/2026-06-12-community-musculoskeletal-release-stub.md`

Updated:

- `Components/website/archive/ENTRY_SCHEMA.md`
- `Components/website/archive/entry-template.md`
- `Components/website/archive/README.md`
- `Components/website/archive/by-thread.md`
- `Components/website/tools/build_archive_views`
- `Components/website/ARCHITECTURE.md`
- `Components/website/PUBLISH_CHECKLIST.md`
- `Components/website/REVIEW_QUEUE.md`
- `Components/website/The-Living-Year/README.md`
- `Components/website/The-Vessel/community/README.md`
- `Components/website/The-Vessel/community/story-template.md`
- archive-entry thread metadata across the 13 generated living-archive records

Deleted from public website current tree:

- `Components/website/The-Vessel/community/2026-06-12-fiona-gardner-musculoskeletal-release.md`

The deletion removes the full named health-context community story from the
public website repository's current tree. It does not erase old Git history.

### Private Vessel Submodule

Created:

- `Components/the-vessel/30-community-private/README.md`
- `Components/the-vessel/30-community-private/community-story-template.md`
- `Components/the-vessel/30-community-private/2026-06-12-fiona-gardner-musculoskeletal-release.md`

Updated:

- `Components/the-vessel/ARCHITECTURE.md`
- `Components/the-vessel/QUEUE.md`
- `Components/the-vessel/90-ops/MIGRATION_MAP_FROM_PUBLIC.md`
- `Components/the-vessel/90-ops/PRIVATE_TRIAGE_STATUS.md`

## Decisions

### Thread Vocabulary

The living archive now has a controlled thread list in
`Components/website/archive/THREADS.md`.

The live generated archive dropped from 32 thread labels to 14 controlled
labels. Finer detail now belongs in `entry_points`, `inquiries`, summaries, and
the source record.

This keeps the archive useful as a relational map without letting it become a
taxonomy thicket.

### Metadata And Access Boundary

The one missing required website metadata field was fixed:

- `Components/website/The-Living-Year/README.md` now has
  `claim_tier: orientation`.

I did not mass-normalize legacy statuses such as `reviewed`, `active`, or
`redirected`, because status promotion remains Ana's publishing decision.

Instead, `Components/website/ACCESS_BOUNDARIES.md` now defines the operational
meaning of `public`, `community`, and `private` for paid-access work. It states
explicitly that frontmatter is not access control.

### Private Community Records

`AnaSeahawk/website` is public. `AnaSeahawk/the-vessel` is private.

Because of that, the full Fiona community story was moved into the private
Vessel under `30-community-private/`. The website now keeps only a redacted,
unlinked stub for chronology and archive-thread continuity.

Future third-party accounts should follow the same rule:

- full record in `Components/the-vessel/30-community-private/`;
- optional redacted website stub only if chronology or archive threading needs
  it;
- no names, direct quotes, health context, detailed practice notes, or Ana
  interpretation in the public stub unless separately re-cleared.

## Verification

Checks run:

- `Components/website/tools/build_archive_views` - built 13 living archive
  entries.
- `python3 -m py_compile Components/website/tools/build_archive_views` - passed.
- `git -C Components/website diff --check` - passed.
- `git -C Components/the-vessel diff --check` - passed.
- Local Markdown link check across `Components/website`: 657 links checked,
  0 broken.
- Required frontmatter scan across `Components/website`: 0 files missing
  `status`, `visibility`, or `claim_tier`.
- Public website scan confirms the named health-context story was removed from
  the current tree. Fiona's name still appears in separate microscopy
  collaborator-credit contexts, which were not part of this privacy move.

## Next

Best next paid-access steps:

1. Draft the public offer page for `Mother Spirit Living Archive`.
2. Decide whether the generated living archive becomes a member map, stays
   hidden, or gets a public excerpt.
3. Draft the June current-state successor only when Ana says the June line has
   ripened enough.
4. Review existing public protocol-like pages against `ACCESS_BOUNDARIES.md`
   before making paid/member claims around them.

## Bottom Line

Items 3, 4, and 5 from report 069 now have working structure:

- a light thread vocabulary;
- a clear metadata/access boundary;
- a private lane and consent template for community records.

This makes the archive safer to turn toward paid access without treating private
records as product inventory.
