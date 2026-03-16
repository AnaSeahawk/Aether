# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

`aether` is Ana Seahawk's AI-companion seed repo. It holds agent instructions, voice/soul definition, and links to content via git submodules. The primary content lives in `Components/website` (the `AnaSeahawk/website` submodule).

`AGENTS.md` at the repo root contains the canonical operating instructions for agents. Read it before making any changes.

`soul.md` defines Aether's voice, themes, and boundaries — consult it when drafting any content or framing language.

## Submodule Workflow

Most active work happens inside `Components/website`, which is a separate git repo (`AnaSeahawk/website`). Treat it as an independent repo when committing; then update the parent pointer in `aether`.

```bash
# Initialize submodules (first clone)
git submodule update --init --recursive

# Pull latest from all submodules
git submodule update --remote --merge

# After committing changes inside Components/website, update the pointer in aether:
git add Components/website
git commit -m "update website submodule after <description>"
```

All three submodules use SSH remotes (`git@github.com:AnaSeahawk/...`).

## Content Architecture (Components/website)

Content is organized around **Four Pillars**:
1. **Alchemical Journals** — lived notes, field-writing (`The-Living-Year/`, `Dreamwork/`, `Foundations/`)
2. **Sovereign Biophysics** — method, experiments, synthesis (`sovereign-biophysics-distillation/`)
3. **The Living Year** — private container structure and rhythm notes (`The-Living-Year/`)
4. **Community & Open Archives** — routes to external spaces

## Content Metadata

Every content file carries YAML frontmatter with three tags:

- `status` — draft/review/approved/published
- `visibility` — `private` | `community` | `public`
- `claim_tier` — indicates sensitivity level of claims made

**Only `community` and `public` files are candidates for publishing.** `visibility` metadata is internal only — GitHub repo privacy settings control actual access, not these tags.

## Publishing Workflow

1. **Review Queue** — `Components/website/REVIEW_QUEUE.md` tracks file status
2. **Checklist** — `Components/website/PUBLISH_CHECKLIST.md` is the 10-point pre-publish gate
3. **Batch Records** — `Components/website/PUBLISH_BATCH_YYYY-MM-DD.md` log approvals
4. Nothing is published without explicit user approval.

## Sensitive Content

The `sovereign-biophysics-distillation/` folder contains sensitive operational material. The intended direction (as of 2026-03-16) is to migrate this content to a separate private GitHub repo. Do not assume it is safe to publish or share. When in doubt about sensitivity, ask before acting.

## Language Conventions

When writing or editing content in this repo:
- Use single-subject, non-clinical framing (no medical claims or directives)
- Maintain boundary language: personal record and responsibility only
- Match the quiet, precise, relational voice described in `soul.md`
- Prefer plain language; avoid jargon, hype, or performance
