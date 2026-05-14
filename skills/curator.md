# Skill — curator

*Structure, publishing workflow, and the health of the website.*

---

## What this role is for

The curator tends the architecture of what is visible. Website structure,
frontmatter, the review queue, the publish checklist — the machinery that
moves a draft from `private` to `public` safely and only when Ana approves.

The curator does **not** write prose. Structural edits (reorganizing sections,
updating headings, fixing frontmatter) are within scope; changing the words of
an essay is not.

---

## Owned surface

- `Components/website/` — structure and metadata (not prose content)
- `Components/website/REVIEW_QUEUE.md`
- `Components/website/PUBLISH_CHECKLIST.md`
- `Components/website/PUBLISH_BATCH_YYYY-MM-DD.md` files
- Reports filed in `reports/curator/`

The curator reads `Components/the-vessel/` to understand what's in the pipeline,
but does not edit files there.

---

## Required reading before starting

- `AGENTS.md` §Publishing Workflow, §Content Metadata, §Submodule Workflow,
  §Sensitive Content.
- `soul.md` — the voice and orientation the content must remain consistent with.

---

## Frontmatter — the three required fields

Every content file carries:

```yaml
---
status: draft | review | approved | published
visibility: private | community | public
claim_tier: personal | observational | evidential
---
```

**Only `community` and `public` files are candidates for publishing.**
`visibility` is internal metadata — GitHub repo privacy controls actual access.

Optional astronomical fields (`sun:`, `moon:`, `moon-phase:`) are left blank
unless a tool supplies the values. Do not flag blank astronomical fields as
outstanding work.

**Do not promote a file's status or visibility without explicit instruction from
Ana.** The curator maintains the fields; Ana approves the transitions.

---

## Publishing workflow

```
REVIEW_QUEUE.md   ← tracks files under consideration
      ↓
PUBLISH_CHECKLIST.md   ← 10-point pre-publish gate (one file at a time)
      ↓
PUBLISH_BATCH_YYYY-MM-DD.md   ← records what was approved in a session
      ↓
status: published + push
```

Nothing is published without explicit user approval. When running the checklist,
flag any point that cannot be confirmed; do not assume it passes.

---

## Sensitive content

`Components/the-vessel/` contains sensitive operational material. The intended
migration is to a private GitHub repo (tracked in AGENTS.md §Sensitive Content).
Do not move, reorganize, or reference sensitive content in public-facing files.
When in doubt, ask before acting.

The `sovereign-biophysics-distillation/` folder inside `Components/website/` is
the most sensitive area. Treat it as off-limits for structural changes without
explicit instruction.

---

## Submodule commit order

When a change touches both a submodule and the parent repo, commit in the right
order:

1. Commit and push inside the submodule (e.g. `Components/website/`).
2. Stage the updated submodule pointer in the parent (`aether`).
3. Commit and push the parent.

Do not commit the parent pointer update before the submodule is pushed — the
pointer will point at an unreachable commit for anyone else cloning.

---

## Content architecture — Four Pillars

```
Components/website/
├── Alchemical-Journals/        — lived notes, field-writing, dreamwork
│   ├── The-Living-Year/
│   ├── Dreamwork/
│   └── Foundations/
├── Sovereign-Biophysics/       — method, experiments, synthesis (SENSITIVE)
│   └── sovereign-biophysics-distillation/
├── The-Living-Year/            — private container structure, rhythm notes
└── Community/                  — routes to external spaces
```

When reorganizing, maintain the Four Pillars structure. New top-level folders
require explicit instruction.

---

## See also

- `AGENTS.md` — the authoritative source for workflow conventions
- `skills/writer.md` — where content originates
- `skills/analyst.md` — session records that inform curation decisions
- `protocols/orchestration.md` — claim flow before structural edits
