---
name: researcher
description: Source research, bibliography management, book acquisition, and citation discipline. Use for finding texts, extracting quotes, maintaining the bibliography submodule, and stewarding the private Google Drive library and its CATALOG.md entries.
---

# Skill — researcher

*Primary sources, bibliography, and citation. The depth beneath the writing.*

---

## What this role is for

The researcher finds, reads, and cites. Primary sources — classical Ayurvedic texts,
alchemical corpus, Chinese medicine, mythology, women healers — are the evidentiary
foundation of everything written in this repo. This role keeps that foundation honest:
texts actually read, citations actually checked, bibliography actually maintained.

The researcher does **not** write prose for publication. That is the writer's surface.
The researcher produces: sourced quotes with attribution, bibliography entries,
research notes, and structured passages the writer can build from.

---

## Owned surface

- `Components/bibliography/` — the entire bibliography submodule. The researcher
  adds files, writes `.md` companion notes, and keeps entries organized by topic.
  This repo is **public** (remote `AnaSeahawk/bibliography`) — see §Public
  repo vs. private shelf below.
- The private library shelf on Google Drive, `gdrive:Bibliography/<topic>/` —
  see §Private library shelf below.
- Research notes filed in `reports/researcher/` (see `protocols/orchestration.md`).

The researcher reads freely across `Components/the-vessel/` and
`Components/website/` to understand what the writing needs — but does not edit
those surfaces. Leave a note in `reports/researcher/` naming what was found and
where it can be used.

---

## Required reading before starting

- `AGENTS.md` — the full repo contract, especially §Bibliography and Book
  Acquisition, §Language Conventions, §Sensitive Content.
- `.agents/skills/sensitive-content/SKILL.md` when source work touches private,
  health-adjacent, or unpublished operational material.
- `soul.md` — the voice and orientation of the work. Research serves this orientation;
  do not source material that flatly contradicts it without flagging the tension.
- `.agents/skills/prose/SKILL.md` — citation conventions and primary-source structure.

---

## Bibliography structure

```
Components/bibliography/
├── alchemy/
├── ayurveda/
├── chinese-medicine/
├── mythology/
├── women-healers/
└── <topic>/
```

Each file: the binary (PDF, EPUB, DJVU) plus an optional `.md` companion note
naming the edition, key chapters, and any quotes already extracted.

The companion `.md` uses this minimal form:

```markdown
# Author — Short Title (Year)

**Edition/translator:** ...
**Anna's Archive MD5:** <hash>

## Key chapters
- Ch. N: ...

## Extracted quotes
> "Quote." — *Source*, Ch.N.V (Translator)
```

---

## Public repo vs. private shelf

`Components/bibliography/` (GitHub `AnaSeahawk/bibliography`) is **public**.
It holds public-domain and openly licensed books, plus `READING_LIST.md`, the
public catalog of everything in the library, including privately held titles.
Copyrighted books go to the private shelf below.

Many copyrighted books from earlier acquisitions are still in the public repo.
The **Shelf status** table at the top of `READING_LIST.md` shows which topic
folders are sorted. When work touches a folder still marked *to sort*, sort the
whole folder in that pass and update the table. Don't run a separate sweep.
Drive already has an empty folder for every topic. Bulk-moved books can get
short CATALOG.md entries (title, author, format, provenance); fill in the
details when a book is next used. For each book:

1. `rclone copy` the file to `gdrive:Bibliography/<topic>/`, keeping the
   same topic folder name as in the repo. Verify it landed with
   `rclone lsf` and a matching size.
2. Add its CATALOG.md entry. Provenance: "moved from public bibliography repo".
3. `git rm` it from the submodule, keep its `READING_LIST.md` line (mark it
   *private shelf*), commit and push the submodule, then commit the pointer
   in `aether`.

Removing a file does not erase it from Git history. Rewriting history is a
separate, destructive step; do it only when Ana asks.

## Private library shelf — Google Drive

Copyrighted and privately-held books live on `gdrive:Bibliography/<topic>/`
(rclone remote, read-write — see `.agents/skills/passwords/SKILL.md` if a
tool needs credentials). First topic: `living-design`.

Each topic folder carries a `CATALOG.md` listing, per book:

```markdown
- **Filename:** ...
- **Title:** full title
- **Author:** ...
- **Year / edition / publisher:** ...
- **Format:** PDF/EPUB/...
- **Why it's in the archive:** ...
- **Provenance:** e.g. "from Ana's own library" vs. "newly acquired"
  (mark previews/excerpts clearly as *not* the full book)
```

End each CATALOG.md with a **not landed** list: titles identified as wanted
but not yet on the shelf.

### Search before acquiring

Ana's existing library is ~1,450 books, scattered. Search these before
downloading anything new:

- `gdrive:Laptop Archive/Books/` — largest cluster, ~1,092 books, organized by
  topic folder (Ayurveda, alchemy, ferments, soil, BioPhilia, garden,
  plasmaTherapy, tao, …).
- `gdrive:Laptop Archive/Pictures/` — z-lib downloads mixed into photo folders.
- `gdrive:Books/` — Ana's personal library, ~46 books, mostly urine-therapy
  texts. Keep separate; don't reorganize it.
- Local: `~/Documents/Archive-From-Alpha/` and
  `~/Downloads/Telegram Desktop/`.

If found, **copy** (never move) the book onto the shelf and record it in
CATALOG.md with its real provenance. Never substitute a different edition or
work for the one that was actually wanted.

---

## Fetching texts — the `annas` CLI

```bash
# Search
annas book-search "caraka samhita sharma"
annas book-search "frawley ayurveda"

# Download to a temp dir — never straight into Components/bibliography
ANNAS_DOWNLOAD_PATH=/tmp/researcher-download \
  annas book-download <md5_hash> Author-Short-Title.pdf
```

The wrapper at `/home/bird/.nix-profile/bin/annas` loads `ANNAS_SECRET_KEY` from
gopass and sets `ANNAS_BASE_URL`. Always set `ANNAS_DOWNLOAD_PATH` explicitly,
to a temp dir, not to the bibliography repo. The `annas` service may be
DDoS-Guard-blocked at times — if a download fails outright, say so rather than
retrying silently or substituting another source.

After download, verify the file type and content before trusting it:

```bash
head -c 16 <tempfile> | od -An -tx1 -c
```

If mislabeled, rename to the correct extension. Archive.org previews can
masquerade as full books — check page count and actual content, not just file
type, before treating a download as complete. Never substitute a different
edition or work for the one that was wanted.

### Landing the file

1. Verify the temp download (above).
2. If public domain: `rclone copy` into `Components/bibliography/<topic>/`
   (the submodule) and commit as usual.
3. If copyrighted or privately held: `rclone copy` the verified file onto
   the private shelf, `gdrive:Bibliography/<topic>/`; update that topic's
   CATALOG.md entry (including provenance); then delete the temp copy.
4. Never leave a verified download sitting only in the temp dir.

### Quoting copyrighted books in public writing

We never publish the book itself, but we do quote it. A public page may quote
a copyrighted book when:

- each quotation is short (a sentence or a passage, not pages) and is there
  because our own writing comments on it, builds on it, or answers it;
- the page is our writing, with quotations inside it, not a run of excerpts;
- every quotation carries its citation (author, title, year, chapter or
  page, edition or translator) and is quoted exactly.

Reproducing a whole systematic work is different. A page that lists every
entry of a structured book, such as Alexander's 253 patterns, uses names,
numbers, and summaries in our own words.

---

## Citation discipline

**Sanskrit / IAST:** Use proper diacritics throughout (ā, ī, ū, ṭ, ḍ, ṇ, ś, ṣ, ḥ, ṃ).
Sanskrit before English in primary-source blocks.

Primary-source quote block form:

```markdown
> *Carakasaṃhitā*, Sūtrasthāna 1.15 (Sharma & Dash, Vol. 1)
>
> "English translation here."
```

Modern academic citations: preserve the published form exactly, even when it
violates workspace conventions.

When paraphrasing rather than quoting, write "After *Source*, Ch.N" — never
present a paraphrase as a direct quote.

**Do not cite without reading.** Training-data familiarity with a text is not
the same as the text's actual claims. If a passage cannot be verified from the
local file, say so explicitly.

---

## Caraka Saṃhitā — current holdings

Local PDFs:
- `Components/bibliography/ayurveda/Sharma-Caraka-Samhita-Vol1.pdf`
- `Components/bibliography/ayurveda/Sharma-Caraka-Samhita-Vol2.pdf`
- Companion notes: `Components/bibliography/ayurveda/Sharma-Caraka-Samhita.md`

Li Goldragon's `caraka-samhita` repo (cloned at `/home/bird/Git/primary`) has
per-page OCR, per-sthāna digests, and verse-level philological notes. Read it
before pulling Caraka quotes — it may have already done the extraction work.

---

## When to file a report vs. return inline

For any research session that produces more than a few extracted quotes, file a
report in `reports/researcher/` with the standard header (see
`protocols/orchestration.md`). Keep inline responses to a pointer.

---

## See also

- `AGENTS.md` §Bibliography and Book Acquisition
- `.agents/skills/sensitive-content/SKILL.md` — privacy and publication boundaries
- `.agents/skills/prose/SKILL.md` — citation form in prose
- `.agents/skills/writer/SKILL.md` — the surface that consumes research output
- `protocols/orchestration.md` — claim/release flow before editing bibliography
