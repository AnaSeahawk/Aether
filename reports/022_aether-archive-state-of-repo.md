# 22. Aether Archive — State of the Repo

**Date:** 2026-05-13
**Agent:** Claude Sonnet 4.6
**Session topic:** Full audit of the Aether git repo — git health, content placement, flow breaks, REVIEW_QUEUE gaps, self-hosted readiness, and a clear path forward.

---

## Aether Archive — State of the Repo

*Report date: May 2026. Parent repo + 5 submodules surveyed.*

---

### 1. Git Health — Clean

Everything is pushed, submodules are up to date, no uncommitted work. The only ongoing thing to watch: `the-vessel` is a private submodule referenced by the public website — that boundary is correctly enforced, with no private content leaking into the public repo. Nothing needs immediate attention at the git level.

---

### 2. The REVIEW_QUEUE Is Significantly Out of Date

Fifteen files exist in the archive that are not tracked in `REVIEW_QUEUE.md`. This means their publish status is unknown and they've been slipping through without a record of what state they're in:

**Missing from queue — all effectively complete:**
- `00-orientation/the-first-water.md` — public, reviewed
- `00-orientation/sun-bu-er-and-the-inner-furnace.md` — public, still flagged draft
- `00-orientation/beauty-and-the-binding.md` — public, still flagged draft
- `00-orientation/in-the-name-of-love.md` — public, reviewed
- `00-orientation/why-the-distillation-is-missing.md` — public, reviewed
- `00-orientation/inanna-venus-and-the-seven-gates.md` — public, reviewed
- `00-orientation/agni.md` — public, reviewed
- `00-orientation/manifesto-clear-mirror.md` — public, reviewed
- `10-method/shivambu.md` — community, still flagged draft (updated May 2026)
- `10-method/the-living-grain.md` — community, still flagged draft
- `10-method/vilepi-and-the-krama.md` — community, still flagged draft
- `10-method/sediment-field-guide.md` — public, reviewed
- `30-analysis/analysis-circulatio-microscopy.md` — community, reviewed
- `30-analysis/analysis-shivambu-as-menstruum.md` — community, reviewed
- `40-synthesis/synthesis-current-state-may-2026.md` — community, draft
- `the-dream-body.md` — community, reviewed

**Also flagged:** `analysis-plasma-composition-hypothesis.md` is listed in the queue as *Private / Not for Publishing* but its frontmatter says `visibility: community`. Inconsistency that needs a decision.

**Action:** REVIEW_QUEUE needs a full pass to catch up to the archive's current state.

---

### 3. Five Documents Flagged `status: draft` That Appear Complete

These are in the live reading chain with public or community visibility, but still carry the draft flag:

- `beauty-and-the-binding.md` — fully written, in chain, public
- `sun-bu-er-and-the-inner-furnace.md` — fully written, in chain, public
- `shivambu.md` — updated with community links May 2026, community
- `the-living-grain.md` — community
- `vilepi-and-the-krama.md` — community

If they're ready they should be marked reviewed. If they genuinely need a pass, they should be in the queue as "Needs Pass."

---

### 4. Internal Ops Files Are Publicly Visible

`PUBLISH_CHECKLIST.md`, `REVIEW_QUEUE.md`, and `PUBLISH_BATCH_2026-03-15.md` all live in the root of the `website` submodule and are publicly accessible. On a self-hosted site they would appear in directory listings. They don't expose anything sensitive, but they look like scaffolding left on the facade. Options: move them to a `_ops/` folder, or add a `.gitignore` rule if the site generator excludes underscore-prefixed dirs.

---

### 5. Flow Breaks — Where Readers Get Lost

**At the site root (biggest gap):** The website `README.md` lists five sections as equal nav items — Foundations, Dreamwork, Relationship, The Living Year, Sovereign Biophysics — with no hierarchy and no guidance about which one matters most to which reader. A reader who finds the site for the first time has no signal that SB is the flagship work and everything else is context. Someone who arrives via a SB link and wants to go deeper into the site has no path. The README describes the work well but doesn't orient the reader spatially.

**The Relationship section is orphaned:** There is no link from the SB archive to the Relationship plant entries, and no link in the other direction. The plant entries (Hing, Burdock, the diet connection) are directly relevant to the ambrosia diet and the krama — a reader going deep into the method section has no way to find them unless they already know to look. One cross-link from the ambrosia diet or vilepi document to the Relationship index would close this gap.

**The Foundations section has no context:** Three essays that pre-date the SB archive, listed by date with no explanation of what they are or how they relate. `plasma-foundation-of-a-new-world.md` is a direct theoretical ancestor of the SB work but nothing connects them. A reader can't tell whether to read Foundations before or after SB, or instead of.

**The Living Year / private journal chain:** `living-map-of-time.md` ends with a "Continue reading" link to `journal/2026-03-08-the-cord.md`. The Living Year README marks journal entries as private. A reader following the chain would land on content that might not be meant for them. Either the chain link should be removed from the public map document, or the journal entries need their visibility confirmed.

**`the-dream-body.md` links to `../Dreamwork/`** (directory, not file). This works on GitHub because it serves the README as index. On a self-hosted static site this may 404 depending on the generator's configuration. Safe fix: `../Dreamwork/README.md`.

---

### 6. What You're Not Seeing

**The wiki submodule is legacy.** It contains `Mother Spirit.md`, `Collaborative groups.md`, and a timestamped journal entry from 2023. This content pre-dates the current website and hasn't been updated in years. It's still sitting as a submodule in the parent repo. It's not causing harm but it's also not being maintained. Worth deciding: archive it, migrate anything useful into the current structure, or drop the submodule.

**The Relationship section has a dead link.** `index.md` lists `Moringa.md` as a plant entry but no `Moringa.md` file exists in the directory. A reader following it gets a 404.

**No bridge between SB and the rest of the site for readers who arrive from outside:** Someone who finds `where-to-begin.md` from a link on mother-spirit.com or Telegram will enter the SB archive and read through it. They'll finish at `practice-log-2026.md` which links to The Living Year. But there's nothing in the SB archive that acknowledges the other sections of the website — no way to find Dreamwork, Foundations, or Relationship from inside SB unless they navigate back to root.

**`analysis-plasma-composition-hypothesis.md` is in community visibility but listed in the queue as private.** This document is currently accessible to anyone who finds the link. If it should be private it needs to move to `the-vessel`. If it's community that's fine but the queue needs to reflect it.

---

### 7. Self-Hosted Readiness

The content structure is genuinely close to deployment-ready. The frontmatter is consistent (date, status, visibility, claim_tier), the file naming is clean, and the internal linking is intact. The main things that need to change for a self-hosted static site:

**URL structure:** The numbered directory names (`00-orientation/`, `10-method/`, `20-experiments/`) work for local organization and will render as URLs. On a live site these become `/sovereign-biophysics-distillation/00-orientation/where-to-begin/` which is readable but long. Most static site generators (Hugo, Eleventy, Astro) let you set a custom URL slug in frontmatter that overrides the directory path. Adding a `slug` or `url` field to documents that need cleaner URLs would solve this without touching filenames.

**Visibility gating:** The archive currently has three visibility levels (public, community, private) but there's no enforcement — everything in the public website repo is accessible to anyone with the URL. For self-hosting, `community` content needs a gate: email subscription, a simple login, or a separate unlisted section. `private` content is already correctly in `the-vessel` repo which is separate. The decision is what "community" means in practice — it's currently a label without a wall.

**Internal links:** All links currently use relative paths with `.md` extensions (`../README.md`, `the-moving-sky.md`). Most static site generators expect extensionless links or absolute paths. This needs a find-and-replace pass when you configure the generator — it's mechanical but it's the biggest migration task.

**Ops files exclusion:** `PUBLISH_CHECKLIST.md`, `REVIEW_QUEUE.md`, and `PUBLISH_BATCH_*` files need to be excluded from the built site (not deleted from git — they're useful for workflow). A `_` prefix or a generator-level exclude rule handles this.

---

### 8. Recommended Path Forward

**Immediate (small, specific):**
- Fix the dead `Moringa.md` link in `Relationship/index.md` — either create the file or remove the entry
- Confirm `the-dream-body.md`'s Dreamwork link should be `../Dreamwork/README.md`
- Remove the Living Year journal "Continue reading" link from `living-map-of-time.md` or confirm the journal entries are public
- Update REVIEW_QUEUE with the 15 missing files and resolve the `analysis-plasma-composition-hypothesis.md` visibility inconsistency
- Flip the 5 draft-status documents that are actually complete

**Medium (when ready to shape the site for readers):**
- Add one sentence to the website root README establishing SB as the flagship and orienting new readers to the other sections as context
- Add a cross-link from the SB method section (ambrosia diet or vilepi) to the Relationship index
- Decide what to do with the wiki submodule

**Before self-hosting:**
- Choose a static site generator and test with the current directory structure
- Decide what "community visibility" means in practice (the gating mechanism)
- Add `slug` or `url` frontmatter to documents where you want cleaner URLs
- Write a find-and-replace script for the `.md` extension in internal links
- Move ops files to a `_ops/` folder or add to the generator's exclude list
