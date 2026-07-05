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
- Research notes filed in `reports/researcher/` (see `protocols/orchestration.md`).

The researcher reads freely across `Components/the-vessel/` and
`Components/website/` to understand what the writing needs — but does not edit
those surfaces. Leave a note in `reports/researcher/` naming what was found and
where it can be used.

---

## Required reading before starting

- `AGENTS.md` — the full repo contract, especially §Bibliography and Book
  Acquisition, §Language Conventions, §Sensitive Content.
- `skills/sensitive-content.md` when source work touches private,
  health-adjacent, or unpublished operational material.
- `soul.md` — the voice and orientation of the work. Research serves this orientation;
  do not source material that flatly contradicts it without flagging the tension.
- `skills/prose.md` — citation conventions and primary-source structure.

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

## Fetching texts — the `annas` CLI

```bash
# Search
annas book-search "caraka samhita sharma"
annas book-search "frawley ayurveda"

# Download into the correct topic folder
ANNAS_DOWNLOAD_PATH=/home/bird/Git/aether/Components/bibliography/ayurveda \
  annas book-download <md5_hash> Author-Short-Title.pdf
```

The wrapper at `/home/bird/.nix-profile/bin/annas` loads `ANNAS_SECRET_KEY` from
gopass and sets `ANNAS_BASE_URL`. Always set `ANNAS_DOWNLOAD_PATH` explicitly.

After download, verify the file type:

```bash
head -c 16 Components/bibliography/<topic>/<file> | od -An -tx1 -c
```

If mislabeled, rename to the correct extension before committing.

Prefer public-domain, openly licensed, or authorized sources. Do not download
modern copyrighted texts unless Ana has confirmed authorization.

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
- `skills/sensitive-content.md` — privacy and publication boundaries
- `skills/prose.md` — citation form in prose
- `skills/writer.md` — the surface that consumes research output
- `protocols/orchestration.md` — claim/release flow before editing bibliography
