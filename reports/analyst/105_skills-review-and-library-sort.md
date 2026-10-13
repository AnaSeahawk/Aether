# 105. Skills Review and Library Sort

**Date:** 2026-10-13  
**Agent:** Claude Code (Opus 5.5)  
**Session topic:** Second skills review (18 skills), fixes, private details out of public skills, and the full bibliography sort

---

## Purpose

Two weeks after Report 104, a second pass over the skill tree, which had grown
to eighteen skills (`frontmatter`, `ontology`, `stt-interpreter` new). Ana
approved every recommendation, including finishing the move of copyrighted
books off the public bibliography repo and settling how the shelf is
organized.

This is a public-safe report.

---

## Skills review

Nothing was broken; the fixes from Reports 101–104 held. `researcher` gained
the two-shelf library (public repo and private Drive), `remember` now catches
up across Claude and Codex sessions, `prose` gained website wording guidance,
and the skills README gained lineage, compost, and a seasonal review.

| Finding | Resolution | Commit |
|---|---|---|
| `/frontmatter` called a remote `chronos` build: 2–3 minutes, and fails if one server is offline | Local Swiss Ephemeris script (`frontmatter/scripts/sky.py`), instant; also fills `moon` and `moon-phase` (common phase names, 45° bins centred on each phase); `--date` gives noon Europe/Madrid | `d69bb58` |
| `AGENTS.md` §Skill Loading missed the three new skills | Added | `d69bb58` |
| README "Last tended" dates had drifted | Corrected; seasonal review now checks them against git | `d69bb58` |
| Claude `remember` allowed Haiku; `CLAUDE.md` says Sonnet | Sonnet with light thinking | `d69bb58` |
| `stt-interpreter` described a person's relationship to Ana in a public repo | Label removed; the name stays, since decoding needs it | `4a93c9b` |
| `researcher` listed Ana's personal library locations publicly | Moved to private `the-vessel/90-ops/library-locations.md`; the skill points there | `4a93c9b`, Vessel `2b36045` |

Withdrawn finding: the Alexander lexicon is not missing; it lives at
`living-design/alexander-pattern-index.md` and is recorded as "names done".

The old wording remains in `aether`'s public Git history. No history rewrite
was done.

---

## Library sort

### Before

179 books in 14 public folders (about 2.3 GB), most of them copyrighted, plus
3 large copyrighted books held only on the laptop. Only `embodiment/` had been
moved to the private shelf.

### Rights check

Each book's edition was checked from its own metadata and front matter, not
from the original's date. Several "classics" turned out to be modern editions:
Armstrong (Ebury 2011), the Damar Tantra (S. Lotus 2014), Dioscorides
(Osbaldeston translation), Suzuki (Golden Elixir 2015), the I Ching (Legge
with modern additions), the Yoni Tantra (Magee 2007). Uncertain items went
private by default.

**Stays public (15):** French, Waite, Mead, Atwood, Cabala mineralis
(Warburg scan and BL plates), the Chrysopoeia image, Bhishagratna, Ramacharaka,
Sacred Books of the East vols. 13 and 17, Culpeper, Mortimer, Duncan, Russell's
*Universal One*.

**Moved to the private shelf (166):** everything else, including the BL
*Cabala mineralis* Book 1 (it carries McLean's modern translation), the
unpublished Abelar manuscript, and the three laptop-only books (Sharma
*Caraka Saṃhitā* vols. 1–2, Bartnett & Adelman). Their local copies stay.

### Organization (now in `READING_LIST.md` §How the shelf is organized)

1. One book, one folder; a book that also serves another topic gets a
   *Listed under* row there (13 such rows).
2. Each section's bold scope line decides where a book goes.
3. Public only when the edition is public domain or openly licensed.
4. Filenames: `Author-Short-Title.ext`.

Changes: `chinese-medicine` renamed `daoism-chinese-medicine`; new `ecology`
(Biophilia, soil, forests, *Silent Spring*, Sheldrake) and `astrology` (cell
salts; three lexicon sources listed as not yet on the shelf); refiled the
Avataṃsaka Sūtra to buddhism, Russo to alexandrian-science, McKenna and
Castaneda's *Art of Dreaming* to shamanism, *Blood Magic* to women-healers;
removed a duplicate *Silent Spring*; added four unlisted water books. Companion
notes, being our own writing, stay public.

### Verification

- Uploaded to `gdrive:Bibliography/<folder>/`; `rclone check --size-only`
  on all 21 source/destination groups: 166 matching files, 0 differences,
  and each Drive folder holds exactly the expected count.
- A `CATALOG.md` for each of 17 folders: title, author, format, why it's in
  the archive (from the reading list), provenance, and a *Not landed* list.
- Repo files removed only after verification, one commit per folder.
  Bibliography `beba22d` is the final commit; the repo now holds only the 15
  public items plus companion notes.
- The empty old Drive folder `chinese-medicine/` was removed.

Removing a file does not erase it from the bibliography repo's Git history.

## Open

- A public website page,
  `sovereign-biophysics-distillation/30-analysis/analysis-the-medicine-cross-traditional.md`,
  names six repo file paths as text-extraction sources; those books are now on
  the private shelf. Plain text, not links. Changing published copy is a
  separate decision.
- Catalog entries for bulk-moved books lack year, edition, and publisher; the
  researcher skill fills them when a book is next used.
