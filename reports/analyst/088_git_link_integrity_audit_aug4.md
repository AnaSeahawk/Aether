# 088. Git Link Integrity Audit — August 4

**Date:** 2026-08-04
**Role:** analyst
**Session topic:** Full link-integrity review of the Aether parent repository and all initialized submodules

---

## Executive result

The Git structure is healthy, but the authored/archive content is not completely
link-clean.

- All six repositories are on `main`, match `origin/main`, and answer
  `git ls-remote`.
- All five submodule pointers resolve to initialized commits.
- Both tracked symlinks resolve; there are no broken symlinks.
- 1,520 local file/anchor link occurrences were checked across tracked Markdown,
  HTML, CSS, and SVG.
- 178 unique well-formed HTTP(S) targets were checked across tracked UTF-8 text.
  162 returned success directly, 14 returned access/bot blocks rather than
  not-found responses, one slow Alchemy Website page succeeded on retry, and
  one deleted GitHub document is definitively stale.
- There are **18 definitely broken link occurrences representing 14 distinct
  destinations**, plus three expected cross-export reply gaps in preserved
  Telegram HTML.

No source files were changed in this review. The private raw exports were treated
as archival records: findings are named by path and line only, without repeating
private message content.

## Definite findings

### 1. Nine broken table-of-contents anchors in a public website document

File:

`Components/website/sovereign-biophysics-distillation/00-orientation/women-of-alchemy.md`

Broken lines: 29, 30, 31, 35, 37, 40, 42, 43, and 44.

Cause: the link fragments turn typographic en/em dashes into one ASCII hyphen,
while GitHub's heading slugger removes those punctuation characters. An en dash
without surrounding spaces disappears; an em dash surrounded by spaces leaves
two hyphens.

Current fragment → GitHub heading fragment:

| Line | Current | Correct target |
|---|---|---|
| 29 | `#mary-the-jewess-fl-1st-3rd-century-ce` | `#mary-the-jewess-fl-1st3rd-century-ce` |
| 30 | `#cleopatra-the-alchemist-fl-3rd-4th-century-ce` | `#cleopatra-the-alchemist-fl-3rd4th-century-ce` |
| 31 | `#medera-dates-unknown-likely-3rd-4th-century-ce` | `#medera-dates-unknown-likely-3rd4th-century-ce` |
| 35 | `#trotula-of-salerno-fl-c-11th-12th-century-ce-italy` | `#trotula-of-salerno-fl-c-11th12th-century-ce-italy` |
| 37 | `#caterina-sforza-1463-1509-italy` | `#caterina-sforza-14631509-italy` |
| 40 | `#martine-de-bertereau-c-1600-c-1645-france` | `#martine-de-bertereau-c-1600c-1645-france` |
| 42 | `#mary-anne-atwood-1817-1910-england` | `#mary-anne-atwood-18171910-england` |
| 43 | `#part-six-the-language-of-distillation-and-its-erasure` | `#part-six-the-language-of-distillation--and-its-erasure` |
| 44 | `#part-seven-mercury-as-mirror-and-as-decoy` | `#part-seven-mercury-as-mirror--and-as-decoy` |

Recommended repair: update only the nine fragment destinations. The visible
typography can remain unchanged.

### 2. Two stale relative links in report 056

File: `reports/056_water-magicians-report.md`

- Line 77 still points through the removed
  `35-collaboration-private/water-magicians/` path. The current target is:
  `../Components/the-vessel/35-water-magicians-private/collective-archive-support-path.md`
- Line 93 points through the same removed path, but the file now belongs in a
  different lane. The current target is:
  `../Components/the-vessel/32-living-year-archive-participation-private/living-journal-participation-template.md`

The two destination files still exist. Only the report links are stale. Because
report 056 is substantive, it should not be silently edited or deleted; this
finding should be handled under the stale-report protocol if Ana wants the old
report replaced.

### 3. Three malformed `href` values in preserved Telegram exports

Private raw archive:

- `35-water-magicians-private/raw/2026-06-27-telegram-ana-megan-fiona-chat-export/messages.html:15975`
  uses `Mother-Spirit.com` without a scheme.
- `35-water-magicians-private/raw/2026-07-09-telegram-ana-megan-fiona-chat-export/messages.html:975`
  and `:1367` use the same Google Meet destination without `https://`.

Browsers interpret these as relative file paths, so they do not reach the
intended sites. Because these files are raw exports, the safer policy is to leave
the originals unchanged and correct or annotate the links only in a derived
navigation layer if those messages are surfaced.

### 4. One deleted GitHub document referenced four times

Stale target:

`https://github.com/AnaSeahawk/website/blob/main/sovereign-biophysics-distillation/50-presentations/living-waters-event-access-2026-06-22.md`

Occurrences:

- `Components/the-vessel/35-water-magicians-private/raw/2026-06-27-telegram-ana-megan-fiona-chat-export/messages.html:11655`
  (the raw export contains both linked text and visible URL)
- `Components/the-vessel/35-water-magicians-private/thread-extraction.md:155`
- `Components/the-vessel/35-water-magicians-private/thread-extraction.md:191`

This is definitively stale: the authenticated GitHub contents API returns 404,
the file is absent from the current website tree, and website history records
`de06a0a Remove temporary Living Waters event access` after its temporary
publication.

The raw occurrence should remain historical. The two derived
`thread-extraction.md` occurrences can be marked as a retired source lead or
repointed only if a current replacement is chosen.

## Expected archival gaps, not repair candidates

Three Telegram reply links call `GoToMessage(...)` for messages outside their
continuation export:

- July 1 export, line 521 → message 15290
- July 2 export, line 591 → message 15419
- July 9 export, line 71 → message 15461

The export's JavaScript intentionally catches this state and displays “This
message was not exported.” These are unresolved cross-export references, but not
corrupt files. They should remain unchanged unless a separate cross-export
viewer is built.

## External checks that were not classified as dead

Fourteen URLs returned HTTP 403 from automated requests. They are concentrated
on DOI publishers and NIH, JAMA, NEJM, Justia, ScienceDirect, and CHOP pages.
This is consistent with access or bot protection, not a 404/410 response. They
were therefore marked **automation-blocked**, not dead.

`https://alchemywebsite.com/maryprof.html` timed out on one direct request but
returned HTTP 200 on retry through its normal redirect route. It is slow or
intermittent, not presently dead.

## Coverage and limits

Checked:

- parent repo plus `Components/bibliography`,
  `Components/mother-spirit-webpage`, `Components/the-vessel`,
  `Components/website`, and `Components/wiki`;
- all tracked Markdown/HTML/CSS/SVG file and anchor destinations;
- all well-formed HTTP(S) strings in tracked UTF-8 text, including plain URLs;
- repository origins, current branch synchronization, submodule commits, and
  symlink targets;
- Git history and authenticated GitHub state for the one ambiguous deleted
  GitHub document.

Not treated as repository navigation:

- hyperlinks embedded inside acquired PDF, EPUB, DOCX, CHM, audio, video, or
  image assets;
- deliberately truncated URL snippets such as `https://…` in extraction tables;
- generated source-code template strings before their output files exist.

## Suggested repair order

1. Curator: fix the nine public TOC fragments in `women-of-alchemy.md`.
2. Analyst/Ana: decide whether substantive stale report 056 should be replaced
   under the report protocol.
3. Curator of the private archive: annotate the retired temporary-event URL in
   the derived thread extraction; preserve the raw export unchanged.
4. Leave the three cross-export Telegram reply gaps as documented archival
   limitations.
