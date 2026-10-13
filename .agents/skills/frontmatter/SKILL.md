---
name: frontmatter
description: Generate Aether content frontmatter with the current Sun and Moon positions, moon phase, status, visibility, and claim_tier. Use when starting a new content file or when Ana asks for frontmatter.
---

Run from the Aether root:

```
.agents/skills/frontmatter/scripts/run
```

It prints the `date`, `sun`, `moon`, and `moon-phase` lines for this moment,
computed locally with Swiss Ephemeris (the first run installs it, a few
seconds). Degrees are ordinal with `º`: `21º Libra`. For a file that has
only a date, pass `--date YYYY-MM-DD`; it computes noon Europe/Madrid, the
curator convention.

Then ask the user three questions.

"What type of file is this?" Offer the most-used values on the website:
- foundation (essay, lineage, philosophy)
- orientation
- analysis
- experiment
Other values in use include plant-relationship, dictionary, synthesis,
method, reference, and journal; accept any of these or a new one.

"Visibility?" — private / community / public. Default: private.

"Where does this file's authority come from?" (`claim_tier`, defined in
`.agents/skills/curator/SKILL.md`):
- aptopadesha — the keeper's experience, voice, or interpretation
- pratyaksha — observed and recorded firsthand, with dates and conditions
- anumana — reasoned together: dialogue, collaboration, or sources
  (needs a named collaborator's consent before release)
- yukti — structure: READMEs, logs, scaffolding

Then generate front matter in this format:

```yaml
---
date: [from the script]
sun: [from the script]
moon: [from the script]
moon-phase: [from the script]
type: [chosen type]
status: draft
visibility: [chosen visibility]
claim_tier: [chosen claim_tier]
---
```

New files always start at `status: draft`. Present the completed block
ready to copy.
