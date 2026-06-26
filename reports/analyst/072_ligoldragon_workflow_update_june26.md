# 72. LiGoldragon Workflow Update June 26

**Date:** 2026-06-26
**Role:** analyst
**Session topic:** Re-check LiGoldragon primary and public GitHub for new workflow patterns after report 065.

---

## Executive Summary

Yes. There is new workflow material since the June 18 scan in
`reports/analyst/065_ligoldragon-primary-workflow-scan.md`.

The most important new pattern is a two-layer workflow shift:

1. `primary` now has a much thinner startup contract: read only
   `skills/skills.nota`, then load narrow triggered skills instead of broad repo
   guidance.
2. A new fresh-context, lead/subagent workflow has landed around
   `intent-led-orchestration`, `subagent-session-workflow`, helper context
   transfer, and context handover.

There is also a newer technical workflow engine direction across public repos:

- `orchestrate` and `signal-orchestrate` now expose workflow-run vocabulary,
  including `RunWorkflow`, `ObserveWorkflowRun`, logs, and
  `WorkflowReceiptProduced`.
- `mentci` is becoming a programmable human approval and prompt-to-work surface.
  Its docs describe a future prompt-to-bead-weave harness session flow, and
  `src/preflight.rs` already contains a typed preflight engine and NOTA launch
  validation code.
- `terminal-cell` is the durable terminal-session primitive underneath that
  direction: daemon-owned PTY lifecycle, transcript capture, attach/reattach,
  programmatic input, and witness apps.

For Aether, the useful takeaway is still small-pattern borrowing, not importing
the machinery.

## Sources Checked

- Existing Aether baseline:
  - `reports/analyst/065_ligoldragon-primary-workflow-scan.md`
  - `reports/analyst/071_current-state-executive-brief-june25.md`
- Local checkout:
  - `/home/bird/Git/primary`
  - `origin`: `https://github.com/LiGoldragon/primary.git`
  - current checked remote head after fetch: `origin/main` at `1842aa3d`
  - compared against report 065 baseline: `0d48b9b`
- Public GitHub repo list:
  - `gh repo list LiGoldragon --limit 100 --json name,updatedAt,description,url,isFork,isPrivate`
- Public repos sampled directly:
  - `https://github.com/LiGoldragon/primary`
  - `https://github.com/LiGoldragon/orchestrate`
  - `https://github.com/LiGoldragon/signal-orchestrate`
  - `https://github.com/LiGoldragon/mentci`
  - `https://github.com/LiGoldragon/terminal-cell`

## What Changed In `primary`

### 1. Startup Is Now Skill-Index First

`primary`'s current `AGENTS.md` is much smaller than the earlier model. It says
to read only `skills/skills.nota` at startup, then choose triggered skills by
topic, discipline, repo, tool, and risk. It explicitly says not to auto-read
large surfaces such as `ESSENCE.md`, `INTENT.md`, repo docs, broad source
trees, or reports.

This is a real shift from "load the whole operating context" toward "load an
index, then load only what is triggered."

Potential Aether relevance:

- Aether's `AGENTS.md` is still appropriately explicit because the repo is
  smaller and less automation-heavy.
- Aether could eventually add a compact "active surfaces" or "skill index"
  pattern, but it should not shrink the current contract until the replacement
  is actually easier for future agents.

### 2. Intent-Led Orchestration Is The New Fresh-Context Protocol

New canonical files:

- `skills/intent-led-orchestration.md`
- `.agents/skills/intent-led-orchestration/SKILL.md`
- `.codex/prompts/intent-led-orchestration.md`
- `.codex/commands/intent-led-orchestration.md`

The protocol is fresh-context only. The lead agent reads the protocol and then
uses no tools. It asks one focused question at a time, dispatches subagents for
workspace reading or implementation, waits for returns, and synthesizes. It has
two hard gates:

- alignment must be explicitly locked;
- method or dispatch plan must be explicitly approved.

It also treats Matt Pocock-style "grill with docs" as a behavior pattern:
settle vocabulary and intent before briefing workers, not necessarily produce a
large PRD artifact.

Potential Aether relevance:

- The full protocol is too heavy for ordinary Aether work.
- The useful small import is the question discipline: for ambiguous,
  high-stakes, or identity-sensitive work, ask one meaningful question at a time
  and do not infer intent from old reports.
- Aether should not adopt the "lead uses no tools" rule unless Ana explicitly
  wants a multi-agent orchestration experiment.

### 3. Subagent Workers Now Have A Formal Return Shape

New canonical worker file:

- `skills/subagent-session-workflow.md`

It tells workers to read `AGENTS.md`, `skills/skills.nota`, the worker skill,
then triggered skills and only task-relevant sources. Workers choose a lane,
claim paths before mutation, use worktrees where needed, verify, commit/push
when authorized, and return a fixed 11-section schema:

1. files read;
2. skills selected;
3. commands run;
4. files changed;
5. dependency graph;
6. summary or findings;
7. verification;
8. commit/push outcome;
9. blockers or questions;
10. dirty-state changes observed;
11. next concrete action.

Potential Aether relevance:

- Aether already has a simpler four-role lock helper.
- Aether could borrow a shorter return checklist for parallel agents, but the
  full 11-section schema is probably too much for normal single-agent work.

### 4. Helper Context Transfer Is Now Explicit

New files:

- `skills/helper-context-transfer.md`
- `skills/when-to-use-helpers.md`
- `skills/context-handover.md`

The principle is that the main thread is the scarce reasoning context. If a
helper is requested to preserve or gather context, the lead should give the
helper the full reading envelope and then stop reading the delegated material.
The lead synthesizes from the helper's distilled return instead of duplicating
the broad read.

The handover skill is also cleaner than a normal session report. A handover
should contain only:

- the human's intent;
- useful context a fresh agent would need;
- live open decisions.

It should exclude transcript chronology, agent confessions, resolved mistakes,
generic advice, and restated rules that the next agent will read anyway.

Potential Aether relevance:

- This is directly useful for Aether analyst work.
- Aether's report discipline already prevents chat overflow, but the handover
  rule is sharper: preserve intent and useful context, not the whole journey.

### 5. Context Maintenance Became More Aggressive

`skills/context-maintenance.md` now frames session drain as routing every idea
to one of three fates:

- intent, captured through Spirit;
- work, tracked in the dependency graph;
- abandon, because it landed, is stale, or no longer needs a live file.

It also promotes topic-based agglomeration and deleting retired report
directories after substance has migrated.

Potential Aether relevance:

- Aether already has stale-report handling in `AGENTS.md`.
- Aether should not copy the aggressive delete-on-retire lane model yet.
- A useful lighter import would be topic-based report review in
  `skills/analyst.md`: when multiple reports keep carrying the same rule, move
  the current rule into permanent guidance and let old reports be superseded.

## New Technical Workflow Direction Across GitHub

### 1. `orchestrate` Is Moving Beyond Claims

`orchestrate` is no longer just a replacement for lock files. Its current
architecture says it owns orchestration machinery: claims, handoffs, activity,
lane/run coordination, scope acquisition, scheduling, escalation, and eventually
agent-run lifecycle. It still distinguishes itself from `mind`, which owns
state and policy truth.

Current status from docs:

- daemon and ordinary/meta CLIs exist;
- sema-backed claim/activity/role/repository state exists;
- lock-file projection exists;
- some agent-run, spawn-plan, executor-capacity, and escalation tables are
  still missing;
- workflow running is present but early.

### 2. `signal-orchestrate` Has Workflow Run Vocabulary

The ordinary contract now includes:

- `RunWorkflow(WorkflowRunRequest)`
- `ObserveWorkflowRun(WorkflowRunObservation)`
- `WorkflowRunObservationRetraction`
- workflow handles, logs, model attestations, step outcomes, workflow
  definitions, and workflow receipts.

This is real schema surface, not just prose. The sampled schema file includes
workflow records and reply variants such as `WorkflowRunLogReported` and
`WorkflowReceiptProduced`.

`orchestrate/src/workflow.rs` currently looks like an early fixture runner. It
builds a deterministic workflow handle, emits a log with fixture provider/model
metadata, and produces a `signal-criome::WorkflowReceipt` with an authorized
outcome. So the contract shape is real, but the full executor is not mature yet.

### 3. `mentci` Is The Human Approval And Prompt-To-Work Surface

`mentci` describes itself as the daemon for a programmable human approval
surface. The working slice includes:

- `mentci-daemon`;
- a thin `mentci` client;
- observation atoms such as `observe`, `observe:pending`, and
  `observe:notifications`;
- answer atoms such as `answer:approve:<question>`,
  `answer:reject:<question>`, and `answer:defer:<question>`;
- a criome approval bridge when configured.

The important new future design is "Prompt-To-Bead-Weave Harness Sessions."
The intended flow:

1. A prompt enters Mentci.
2. A cheap contained API preflight model emits a fixed NOTA launch packet.
3. The packet names scaffold identity, minimal context, `skills/skills.nota`,
   session identity, persistence, sandbox/privacy posture, stop conditions, and
   residual constraints.
4. `orchestrate` owns the persistent session/lane address.
5. `terminal-cell` owns process liveness.
6. Harness adapters such as Codex, Claude Code, pi, or shell sit on top of the
   same terminal driver.

This is still marked as future design in the architecture doc, but
`src/preflight.rs` already implements a typed preflight request, model-profile
verification, NOTA decoding, validation, and request-preservation checks. That
means the front-door contract has started to become code.

### 4. `terminal-cell` Is The Durable Session Primitive

`terminal-cell` is a low-level terminal cell:

- daemon-owned PTY lifecycle;
- transcript capture;
- programmatic input;
- visible attach/reattach;
- separate control and data sockets;
- witness apps for live coding-agent and pi sessions.

This appears to be the process/session substrate for persistent harness
sessions. It is not an Aether content workflow by itself, but it explains why
Mentci's prompt-to-harness design is becoming feasible.

## Current Verdict

The new work is real, but split by maturity:

- Mature enough to study now:
  - skill-index startup;
  - context handover;
  - helper context transfer;
  - topic-based context maintenance;
  - terminal-cell as a durable process primitive.
- Real but early:
  - `signal-orchestrate` workflow contract;
  - orchestrate fixture workflow receipt generation;
  - Mentci preflight launch schema and validation.
- Still target architecture:
  - full prompt-to-bead-weave harness sessions;
  - generic harness adapters;
  - durable Mentci SEMA storage;
  - full workflow scheduling, retry, escalation, and executor capacity.

## Recommendation For Aether

Do not import the LiGoldragon workflow stack wholesale.

Aether is a content, memory, and sensitive-archive repo. The heavy pieces
remain mismatched: daemon orchestration, Spirit, BEADS, terminal-cell, Mentci,
workflow receipts, Jujutsu-first policy, and dynamic session lanes would add
more machinery than Aether needs.

Small patterns worth considering later:

1. Add a compact handover rule to `skills/analyst.md`: handovers preserve Ana's
   intent and useful context only, not transcript history.
2. Add topic-based report review to the analyst skill so repeated report arcs
   migrate durable rules into `AGENTS.md`, role skills, or `soul.md`.
3. Consider a lightweight `protocols/active-surfaces.md` for Aether's current
   submodules and sensitive surfaces, as already recommended in report 065.
4. Keep Aether's existing four-role `tools/orchestrate` flow. It is still the
   right size.

Bottom line: LiGoldragon's new workflow is becoming a serious multi-agent
operating system. Aether should borrow the memory hygiene, not the operating
system.
