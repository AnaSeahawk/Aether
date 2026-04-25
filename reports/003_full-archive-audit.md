# 3. Full Archive Audit

**Date:** 2026-04-25  
**Agent:** Claude Sonnet 4.6  
**Session topic:** Full audit of the SB archive for inconsistencies, artifacts, nav gaps, style issues, and REVIEW_QUEUE accuracy.

---

## What changed

### `sovereign-biophysics-distillation/10-method/the-living-loop.md`

Three internal drafting artifacts removed that were visible to readers:

- `*(Fill in: morning routine, drinking, oral care, skin, what changes by season and location)*` — placeholder note sitting between the "Daily Practice" heading and the actual content
- `*(Fill in: collection, filtering, storage rotation, what requires planning)*` — same, in the "Weekly Practice" section
- `"This section was missing from the original outline and belongs here."` — process note at the start of the Nasal section; the section is solid and earns its place, the note explaining its origin is not content

### `sovereign-biophysics-distillation/10-method/oral-care-protocol.md`

Nav chain gap fixed. The file was linking directly to the experiments, skipping `sovereign-biophysics-translation-map.md` and `observation-protocol-handout.md`. The README's stated reading order places both of those between Oral Care Protocol and the Experiments. The jump meant a reader following the nav chain from oral-care-protocol would never reach the translation map or observation protocol.

Fixed: the `Continue reading` link now points to `sovereign-biophysics-translation-map.md`. The redundant `Reference:` line pointing to the same document was removed.

The full method chain is now correct:  
before-you-begin → on-sodium-chloride → ambrosia-diet → the-living-loop → amaroli-protocols → distilled-fraction-protocols → apothecary-balm → **oral-care-protocol → sovereign-biophysics-translation-map → observation-protocol** → experiments

### `sovereign-biophysics-distillation/00-orientation/the-grief-that-was-never-recorded.md`

Subtitle typo fixed: `"Has Always Know"` → `"Has Always Known"`

### `sovereign-biophysics-distillation/00-orientation/women-of-alchemy.md`

Duplicate `---` separator removed from the header area (two consecutive horizontal rules after the byline).

### `REVIEW_QUEUE.md`

The queue had systematic filename errors and was missing over half the archive. Fixed:

**Filename errors:** Every Foundations file and every SB orientation file was listed with a date prefix in the filename (e.g. `2026-02-22-manifesto-clear-mirror.md`) — the actual files have never had date prefixes. The experiments, analysis, and synthesis files had the same problem. All corrected.

**Wrong path:** `the-grief-that-was-never-recorded.md` was listed under `Foundations/` — the file lives in `sovereign-biophysics-distillation/00-orientation/`.

**Missing files — 12 added:**
- Orientation: `where-to-begin.md`, `the-language-of-erasure.md`, `two-distillates.md`, `the-distillery-in-the-field.md`, `the-biological-baseline.md`, `a-year-in-the-practice.md`
- Method: `before-you-begin.md`, `on-sodium-chloride.md`, `distilled-fraction-protocols.md`, `oral-care-protocol.md`, `observation-protocol-handout.md`
- Experiments: `experiment-report-ana-distillation-feb22.md`
- Living Record: `the-vessel.md`
- Presentations: `presentation-living-waters-v1.md` (draft, community)

---

## Style observations

### Good style to carry forward

**The plain declarative close:** The ending of the-living-loop.md — *"Not a theory. A living practice, with land and animals and a still running and someone to open the door."* — is the strongest closing in the archive. Short sentences after sustained density. No rhetorical flourish. This pattern appears at its best when the preceding writing has done full work and the close just names what is. Carry this into other documents that currently trail off with softer endings.

**Safety documentation without clinical language:** The alkaline burn incident in the-living-loop.md is documented precisely and without drama. *"This is documented here because it is real safety information, not a theoretical caution."* This framing — personal, exact, grounded — is more credible than any liability-hedged caution. The nasal safety note (what concentrations are and aren't appropriate) follows the same model. Both are good templates for any future safety content.

**Historical naming:** The Andalusia section names specific people, dates, and mechanisms of erasure without over-claiming. This is the pattern to follow whenever the writing engages with historical record — not *"women were persecuted"* in the abstract, but Leonor "la Camacha" Rodríguez, tried in 1572, Cervantes knew her name. Specificity is the evidence that the work is grounded.

### Style to watch

**Process meta-commentary:** The three artifacts removed from the-living-loop.md were all explanations of the document's own construction — the practice of leaving notes about what was missing, then filling in the content without removing the note. Check other documents-in-progress for the same pattern before publishing.

**Double separators:** The `---` duplication in women-of-alchemy was likely a copy-paste artifact. Simple to catch in a visual read.

---

## Archive state as of 2026-04-25 (end of session)

- Nav chain: complete and unbroken from where-to-begin.md through to practice-log-2026.md
- the-living-loop.md: clean — all placeholders removed, document reads as a finished practitioner account
- REVIEW_QUEUE: accurate for the first time — all 30+ files accounted for with correct paths
- the-grief-that-was-never-recorded.md: subtitle corrected
- women-of-alchemy.md: formatting clean

No outstanding audit items.
