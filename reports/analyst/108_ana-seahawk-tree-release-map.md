# 108. Ana Seahawk: The Tree as Release Map

**Date:** 2026-10-24

**Agent:** Claude / Opus 5.5

**Session topic:** Updating the October 18 sitemap with the decisions of October 22 and 24, and marking every branch with where it stands on the live site.

**Supersedes:** [107. Revised Website Sitemap](107_ana-seahawk-sitemap-revised.md), which stays as the record of the October 18 tree.

**Plan:** [The Plan, version 3](https://claude.ai/artifact/KTRT9AL6utW8GytxgEAM4U)

---

This is a planning document. The website is unchanged by it.

## What changed since 107

- **Income comes first, built properly.** The front page is the first build because it leads to the paid sessions, which are already live.
- **Ways of Living** has three branches: Urbaculture, Biophilia Design, and Place Readings. The names Habitat Reading and Habitat Design are retired.
- **Foundations** is a door again. It holds *Freedom Is Love* and a short page on how the archive is kept. *The Sacred Ordinary* and *Plasma* wait for a rewrite.
- **The Living Year** is the paid membership, shown as *Coming soon*.
- **The Shivambu Women's Circle** gets its own site on Ana's account.
- **The Water of Life conversation** stays free, as part of that archive.
- **Living Waters and the community stories** stay where they are.
- **Websites for others** are word of mouth and do not appear on the site.
- **No place-reading service** appears under Work with Ana yet. 107 placed one there, but its name, scope and exchange are unwritten.

## How each branch is marked

Each status comes from the live site at anaseahawk.com, checked on October 24, together with each file's front matter.

| Mark | Meaning |
|---|---|
| **Live** | Open and linked from the site |
| **Unlisted** | Served at an address but linked from nowhere, so it opens only for someone who has the link |
| **Ready** | Reviewed and public in front matter; can open once it has a page |
| **Draft** | Needs review or rewriting before it opens |
| **Held** | Deliberately kept back by decision |
| **Not written** | No page yet |

## The tree

```text
ANA SEAHAWK
|
+-- Home ................................. Live (old version)
|     New simple version: first build. A fuller draft has sat
|     uncommitted since October 2 and is the starting material.
|
+-- Explore
|   |
|   +-- Sovereign Biophysics ............. Live, in part
|   |     Index, 7 orientation pages and 1 analysis page are open.
|   |     The rest are source files, excluded from the site:
|   |     +-- Orientation ...... 39 files: 6 published, 18 reviewed or approved, 15 draft
|   |     +-- Method ........... 16 files: 12 reviewed, 4 draft or active
|   |     +-- Experiments ...... 10 files: 4 reviewed, 6 draft
|   |     +-- Analysis ......... 12 files: 1 published, 7 reviewed, 2 in review, 2 draft
|   |     +-- Synthesis ........  4 files: 3 reviewed or approved, 1 draft
|   |     +-- Dictionary .......  7 files: all draft
|   |     +-- Living Waters presentation ... Held where it is (decided Oct 24)
|   |
|   +-- The Living Record ................ Broken door
|   |     The draft homepage links to The-Vessel/README.md, which
|   |     returns 404. The-Vessel/ also returns 404.
|   |     +-- The Record (backstory) ...... Unlisted, draft
|   |     +-- Living Journal 2026 ......... Unlisted, active (community)
|   |     +-- Dream and journal pieces .... Unlisted, 6 drafts
|   |     +-- Community stories ........... Held where they are (decided Oct 24)
|   |
|   +-- Foundations ...................... Live
|   |     +-- Freedom Is Love ............. Live, stays
|   |     +-- How the archive is kept ..... Not written
|   |     +-- The Sacred Ordinary ......... Live now; decision says hold for rewrite
|   |     +-- Plasma ...................... Live now; decision says hold for rewrite
|   |
|   +-- Ways of Living ................... Not written
|       "Structure Follows the Ground": named in the Vessel's
|       living-design drafts. The essay itself was not located
|       on October 24.
|       |
|       +-- Urbaculture .................. Not written (intro)
|       |   +-- Biophilia and the Vivarium .. Not written
|       |   +-- Living Ferments ........... Unlisted, 4 drafts (community)
|       |   +-- Relationship with Plants .. Index returns 404
|       |       +-- Ready (reviewed, public): Burdock, Hing,
|       |       |   Miswak, Yerba Santa
|       |       +-- Reviewed, community: 7 entries
|       |       +-- Draft: 10 entries
|       |       All of these are Unlisted.
|       |
|       +-- Biophilia Design ............. Not written (intro)
|       +-- Place Readings ............... Not written (intro)
|             Source: October 14 voice notes.
|
+-- The Living Year ...................... Coming soon
|     Paid membership. The-Living-Year/ returns 404. The draft
|     homepage already has its description and the three ways
|     to join (lunar cycle, solar quarter, full solar cycle).
|     +-- A Living Map of Time ........... Not written
|     +-- The Solar Journal .............. In development (own repo)
|
+-- Work with Ana
|   +-- Private time ..................... Live on cal.com/anaseahawk
|         A Place to Soften, 20 min, US$25, via PayPal
|         Private Session with Ana, 60 min, US$60, via PayPal
|     (Place-reading service ............. Held, unwritten)
|
+-- Gather
|   +-- Salons, open gatherings .......... Held: no dates or pages
|
+-- Site Map page ........................ Not written
|     The October 2 draft homepage holds an inline version.
|
+-- Stay up to date (Kit) ................ In the October 2 draft homepage

SISTER SITES (on the front page)
+-- Mother Spirit ........................ Live, mother-spirit.com
+-- The Water of Life .................... Live, own site
|     The free 30-min conversation on Cal.com belongs here.
+-- Shivambu Women's Circle .............. Not built
      Will be on Ana's account. Listing it on her front page
      waits for Fiona's and Megan's yes.
```

## What the survey found

1. **Two links on the draft homepage are broken.** *The Living Record* points to `The-Vessel/README.md` and *Relationship* points to `Relationship/`. Both return 404. The front-page rebuild fixes them.
2. **Unlisted pages are served.** GitHub Pages renders every Markdown file outside Sovereign Biophysics, whatever its front matter says. Draft, community and private stubs therefore open for anyone who has the address. Two examples are the Living Journal and a private community-story stub, both returning 200. [ACCESS_BOUNDARIES.md](../../Components/website/ACCESS_BOUNDARIES.md) already says front matter is not access control, so this is known. It still needs a decision before release: exclude unreleased sections in `_config.yml`, as Sovereign Biophysics already is, or accept that they are unlisted.
3. **Two Foundations essays are live against the October 22 decision.** Holding them means taking them out of the Foundations index and excluding them from the site.

## Release order

1. **The front page** (first, for income). It links only to Live doors, private time, the sister sites, *Coming soon* for the Living Year, and Kit.
2. **Fiona's site, the basics.**
3. **The rhythm**, one piece at a time, perhaps at each new or full moon. Candidates in rough order: the Living Record door fixed; the Foundations method page; the Relationship index with its four ready plants; the Ways of Living intros; the Circle site; further Sovereign Biophysics pages from the reviewed files.
4. **The Living Year**, opened when it is ready to hold people.
