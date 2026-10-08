---
name: frontmatter
description: Generate Aether content frontmatter with the current Sun position, status, visibility, and claim_tier.
---

Run the following bash command and capture the output:
```
nix run github:LiGoldragon/mentci-ai#chronos
```

The output is in the format `EPOCH.SIGN.DEGREE.MINUTE.SECOND` where:
- EPOCH = traditional year (informational only)
- SIGN = zodiac sign number (1=Aries, 2=Taurus, 3=Gemini, 4=Cancer, 5=Leo, 6=Virgo, 7=Libra, 8=Scorpio, 9=Sagittarius, 10=Capricorn, 11=Aquarius, 12=Pisces)
- DEGREE = ordinal degree within the sign (1-30, where 1 is the first degree)
- MINUTE.SECOND = arc minutes and seconds

Convert the sign number to its name. Write the degree with the ordinal
indicator º (U+00BA), not the degree sign °: e.g. `27º Pisces`.

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
date: YYYY-MM-DD
sun: [DEGREE]º [SIGN_NAME]
moon:
moon-phase:
type: [chosen type]
status: draft
visibility: [chosen visibility]
claim_tier: [chosen claim_tier]
---
```

Use today's date. Leave `moon` and `moon-phase` blank unless a tool supplies
them; do not suggest a manual lookup. New files always start at
`status: draft`. Present the completed block ready to copy.
