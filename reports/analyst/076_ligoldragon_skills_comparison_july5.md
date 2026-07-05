# 76. LiGoldragon Skills Comparison July 5

**Date:** 2026-07-05
**Role:** analyst
**Session topic:** Compare LiGoldragon primary skills with Aether's existing agent-skill structure.

---

## Short Answer

Aether already has a simpler version of LiGoldragon's skill system.

The shared pattern is: agents read a small entry contract, choose a role, load the relevant skill file, coordinate edits through a claim/release mechanism, and leave durable reports when the answer is too large for chat.

The difference is scale and automation. Aether has five human-readable skill files under `skills/`. LiGoldragon's current `primary` remote has moved toward generated, cross-harness doctrine: generated skills under `.agents/skills/` and `.claude/skills/`, generated Codex/Claude/Pi agent profiles, and a smaller `AGENTS.md` that says ordinary worker packets carry the needed doctrine.

## Sources Checked

- Aether:
  - `AGENTS.md`
  - `protocols/orchestration.md`
  - `skills/analyst.md`
  - `skills/prose.md`
  - `skills/researcher.md`
  - `skills/writer.md`
  - `skills/curator.md`
  - `reports/analyst/072_ligoldragon_workflow_update_june26.md`
- LiGoldragon primary local checkout:
  - `/home/bird/Git/primary`
  - local worktree commit: `40cce90445781acc29d181e0b50acf6fc4f04c96`, dated 2026-05-21
- LiGoldragon primary remote after fetch:
  - `origin/main` commit: `6c3444da2e54d0e38d275ef72c0c00fa3d0d906b`, dated 2026-07-05
  - `AGENTS.md`
  - `skills/generated-role-outputs.nota`
  - `.agents/skills/reporting/SKILL.md`
  - `.agents/skills/orchestration/SKILL.md`
  - `.agents/skills/privacy/SKILL.md`
  - `.codex/agents/scout.toml`

## What Changed Since The June Scan

`reports/analyst/072_ligoldragon_workflow_update_june26.md` is now partly superseded for current-state purposes.

On June 26, the useful finding was that `primary` had a typed `skills/skills.nota` index and many direct `skills/*.md` files. In the current fetched `origin/main`, `skills/skills.nota` is gone from `primary`. The current `AGENTS.md` says:

- generated worker role packets carry required doctrine for normal role work;
- agents load extra doctrine only when the prompt, role packet, dispatch envelope, or local repo context requires it;
- skills and agent files under `.agents/`, `.claude/`, `.codex/`, and `.pi/` are generated from `LiGoldragon/skills`;
- manual reports are no longer the default for every substantive answer.

So the live direction appears to be: `primary` is no longer the canonical hand-maintained skill source. It is a generated consumer of a separate `LiGoldragon/skills` system.

## How LiGoldragon's Current Pattern Works

The current remote has at least 57 generated skill files under `.agents/skills/`. The same doctrine is projected into harness-specific locations such as `.claude/skills/` and `.codex/agents/*.toml`.

That means a skill is not just a markdown convention. It is a reusable instruction module that can be compiled or copied into multiple agent surfaces.

Examples:

- `.agents/skills/reporting/SKILL.md` defines when chat is enough and when a report is actually needed.
- `.agents/skills/orchestration/SKILL.md` defines a fresh-context orchestration lane that interviews, gates, dispatches workers, and synthesizes without directly doing the task.
- `.agents/skills/privacy/SKILL.md` defines closed-by-default handling for personal or private material.
- `.codex/agents/scout.toml` packages a read-only scouting role for Codex with its own output protocol and embedded doctrine.

This is larger than Aether needs right now, but it is useful as a pattern.

## What Aether Already Has

Aether has a lighter, repo-native skill system:

- `AGENTS.md` is the entry contract.
- `protocols/orchestration.md` is the coordination protocol.
- `skills/researcher.md`, `skills/writer.md`, `skills/curator.md`, and `skills/analyst.md` define role-specific behavior.
- `skills/prose.md` defines shared writing craft.
- `reports/` is the durable memory surface.
- `tools/orchestrate status`, `claim`, and `release` coordinate concurrent work.

This session used that system directly: I treated the request as analyst work, read `skills/analyst.md` and `skills/prose.md`, checked orchestration status, and wrote this report in the analyst lane.

There is also a second kind of skill active in this Codex session: Codex-level skills supplied by the harness, such as the system `imagegen`, `openai-docs`, and plugin skills for GitHub, Gmail, Google Calendar, and Google Drive. Those are not Aether repo files. They are runtime capabilities exposed to Codex. Aether's `skills/*.md` files are local repo instructions that agents read because `AGENTS.md` tells them to.

## Practical Difference

LiGoldragon's system is agent-infrastructure heavy:

- many specialized skills;
- generated role packets;
- harness-specific projections;
- cross-repo doctrine;
- stricter distinctions among intent, matter, privacy, worker output, and orchestration;
- likely a separate canonical source repo, `LiGoldragon/skills`.

Aether's system is content-archive heavy:

- four clear roles;
- direct human-readable skills;
- simple lock files;
- reports as continuity;
- language and privacy constraints tied to Ana's archive, submodules, and publishing workflow.

The Aether version is easier for mixed agents to follow without a generator. The LiGoldragon version is better when many worker agents need consistent doctrine across multiple harnesses.

## How Aether Can Use This

The useful adoption is not to copy LiGoldragon's whole machinery. Aether should borrow the small parts that reduce repeated confusion.

Recommended next steps:

1. Add a compact `skills/index.md` or `skills/skills.nota` only if agents keep asking which Aether skill applies. Right now `AGENTS.md` already gives a clear four-role table, so this is optional.
2. Add a short "skill loading" paragraph to Aether `AGENTS.md`: read the role skill, then read `skills/prose.md` for writing work, and do not scan all skills unless the task calls for it.
3. Consider a `skills/privacy.md` or `skills/sensitive-content.md` for Aether, because `sovereign-biophysics-distillation/` and private collaboration material need closed-by-default handling. Some of that already exists in `AGENTS.md`, but a dedicated skill would make it easier for agents to load only the privacy doctrine.
4. Consider a short worker-return checklist for parallel-agent work. Aether does not need LiGoldragon's full generated role-packet system, but it could use a simple return shape: files read, files changed, checks run, blockers, next action.
5. Do not adopt LiGoldragon's generated cross-harness skill pipeline unless Ana actually wants Aether to become agent-infrastructure. For Aether's current purpose, direct markdown is the right level.

## Answer For Ana

When he asks whether Aether has "skills," the accurate answer is:

Yes, but ours are simpler and more human-facing. Aether has role skills in `skills/` and an orchestration protocol. Li's current system is a generated multi-agent doctrine system that projects skills into Codex, Claude, Pi, and generic agent folders. We are already using the same basic idea, but not the full automation.

The next useful step is not to import all of Li's skills. It is to choose one or two Aether-specific skills that would reduce repeated explanation: likely `sensitive-content` and maybe a compact `skills/index`.
