# Report 100 — Report 096 Completion and Pramāṇa Vocabulary

**Date:** 2026-09-21
**Session:** `session_01GyFu5bSgXEy2RWNivCoQ5w`
**Scope:** Complete the four-phase roadmap from Report 096 (Skills Audit and
Path Forward), plus a vocabulary decision that emerged from Phase 4 work.

---

## Summary

All four phases of Report 096 are resolved. The most significant outcome was
not anticipated by the report: during `claim_tier` reconciliation, Ana replaced
the entire tier vocabulary with the four pramāṇas (valid means of knowledge)
from the Caraka Samhita.

---

## Phase 1 — Governance repair

Already completed before this session (commit 195ced7, documented in
Report 098).

## Phase 2 — Skill and executable alignment

Completed this session:

1. **Water of Life intake workflow** — aligned with privacy commitments.
   Consent flows clarified, email linking added for contributors, privacy page
   rewritten with community-archive voice, raw-submission deletion authorized
   as part of the published workflow.
2. **Video skill** — 5 broken relative links corrected; VAAPI hardware encoding
   enabled for full renders (vertical clips retain CPU fallback).
3. **Curator skill** — fictional architecture section replaced with reference to
   the canonical `ARCHITECTURE.md`.
4. **Skills README** — solar-journal, phoenix-calculator added; harness skills
   section added.

## Phase 3 — Consolidate domain skills

Completed this session:

1. **Solar Journal skill** — reduced from 1127 to 316 lines. Contradictions
   resolved (Light→Quarter, observed→looked up, pixel→mm). Product content
   extracted to `references/front-matter-content.md`, Phoenix cosmology to
   `references/phoenix-architecture.md`.
2. **AM year boundary** — explicitly aligned between Solar Journal and Phoenix
   calculator (both use Aries ingress).
3. **Phoenix calculator wrapper** — `scripts/run` creates a Python venv with
   `pyswisseph` on first invocation. Verified working on Nix-managed system.
4. **Water of Life methodology** — divergent older copy replaced with canonical
   version. Founding document now renders inline on the methodology page (new
   Hugo layout template).

## Phase 4 — Content and archive work

Five items from Report 095:

1. **Private file in the-vessel history** — closed by Ana's decision. The file
   is untracked and the history rewrite is not warranted. Not to be reflagged.
2. **Vinaya citation error** — fixed. Companion note now distinguishes
   Mahāvagga I.30.4 (ordination allowance) from VI (pharmaceutical
   classification). Horner PDF renamed from generic "Vinaya-Pitaka" to
   "Vol4-Mahavagga" to identify the actual volume.
3. **Unsearchable bibliography PDFs** — dismissed by Ana as not a priority.
   Scans work; lack of OCR is an inconvenience, not a blocker.
4. **`claim_tier` reconciliation** — completed and then superseded (see below).
5. **Amaroli reader-facing edition** — deferred. The content is ready but
   awaits its turn in the publishing sequence. Ana is building the chapter
   spine in order; the Amaroli Protocols page lives in `10-method/`, not in
   the current publishing lane.

---

## The pramāṇa vocabulary

During `claim_tier` reconciliation, Ana identified that the existing tier names
described a document's *purpose* rather than its *authority*. This led to a
broader decision: rename the entire vocabulary using the four pramāṇas from the
Caraka Samhita (Vimānasthāna 4, Sūtrasthāna 11).

### The four tiers

| Pramāṇa | Sanskrit | Meaning | Authority rests on |
|---|---|---|---|
| `aptopadesha` | āptopadeśa | Trustworthy testimony | The keeper's experience, voice, or interpretation — including experience entrusted by others |
| `pratyaksha` | pratyakṣa | Direct perception | What was observed and recorded firsthand, with dates, measurements, conditions |
| `anumana` | anumāna | Reasoned together | Knowledge arrived at through dialogue, collaboration, or engagement with sources |
| `yukti` | yukti | Applied framework | The structure that holds the other three together |

Caraka is unique among Indian philosophical systems in elevating yukti to a
fourth pramāṇa — most schools use only three. Caraka added it because medicine
requires not just testimony, observation, and inference, but a rational
framework that joins them into something you can actually use.

### Scope of change

| Repository | Files updated | Old values replaced |
|---|---|---|
| the-vessel | 167 | personal, observational, relational-source, operational, practice, orientation, synthesis, mixed, attribution-note, evidential |
| website | 136 | interpretation, personal-account, personal-record, personal-observation, observation, observed, preliminary-observation, practice, orientation, synthesis, mixed, hypothesis, comparative, evidential, documented-fact, established-record |
| **Total** | **303** | **16 legacy values → 4 pramāṇas** |

### Governance updated

- **Curator skill** — authoritative tier definitions rewritten with pramāṇa
  vocabulary and mapping table.
- **Writer skill** — default frontmatter changed to `claim_tier: aptopadesha`.
- **AGENTS.md** — tier summary rewritten.
- **Historical reports** — left unchanged (they describe what was true at the
  time they were written).

### Consent safety

The `anumana` tier inherits the consent gate previously attached to
`relational-source`: when a named collaborator is part of the knowledge, their
consent is required for release. The tag continues to do safety work.

---

## Additional work this session

- **Water of Life front page and support page** — replaced "I got tired of
  waiting" paragraph with great-aunt Helen's record-keeping lineage.
- **Chronicle** — named as the future Hugo theme for hand-tended archives.
  Saved to memory, not yet built.
- **`.gitignore`** — added `.venv/` for the Phoenix calculator's virtual
  environment.

---

## Current state

The Report 096 roadmap is complete. The operating layer is clean:

- Governance files are repaired and consistent.
- Skills reference current, non-contradictory decisions.
- The `claim_tier` vocabulary is grounded in the Caraka Samhita and applied
  uniformly across 303 files.
- The Phoenix calculator runs reproducibly.
- The Water of Life intake workflow matches its published privacy commitments.

The next publishing work is the chapter spine: The Living Loop, Agni, and the
remaining orientation chapters, in sequence.
