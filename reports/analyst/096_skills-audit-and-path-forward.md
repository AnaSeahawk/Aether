# 96. Skills Audit and New Path Forward

**Date:** 2026-09-13
**Agent:** Codex
**Session topic:** Report 095 review, Aether skill-system audit, and Water of Life cleanup

---

## Purpose

This report gives Ana one place to resume from when she is back at her laptop.
It consolidates:

- the review of Report 095;
- the status of that report's open recommendations;
- a read-only audit of Aether's fourteen repository skills and their supporting
  scripts, profiles, maps, and protocols;
- the Water of Life founding-document change reviewed, committed, and pushed
  during this session;
- a proposed order for addressing the findings without mixing governance repair
  with content or publication work.

This is a public-safe coordination report. It names private surfaces only where
needed for continuity and does not reproduce private body content.

## Current state at handoff

- Aether `main` and `origin/main` match at commit
  `635070b1d51668f2d3379542c93c997a2040b90f`.
- The only remaining parent working-tree indication is untracked content inside
  the private `Components/the-vessel` submodule. It was not inspected, staged,
  changed, or committed during this session.
- All four orchestration roles are idle.
- No skill corrections have been made. The audit below is review material for
  Ana's decision.
- No background command or long-running tool job was left active.

## Review of Report 095

The latest prior report was
`reports/analyst/095_concurrent-agent-collision-2026-09-07.md`, dated
2026-09-08. It is both the highest-numbered and most recently modified global
report.

### What happened

Two agents worked concurrently on shared archive surfaces on 7 September. One
session continued for hours after checking coordination locks only at its
start. A second Codex session stopped during a Sovereign Biophysics publishing
run.

The stopped session's work was not lost. Its staging artifacts were recovered,
Chapter VI was published, artwork was integrated, citation blockers were
resolved, a dead link was removed, and stale coordination locks were released.
Repository history and submodule pointers were checked and found intact.

### Failures recorded by Report 095

1. Coordination status was checked once rather than again before later commits.
2. Shared instruction files were edited without a path claim.
3. Broad-pattern staging swept an unrelated private draft into repository
   history for two commits.

Report 095 does not claim that these events caused the other agent to stop. The
timing is suggestive, but causation remains unproven.

### Outstanding matters from Report 095

1. A private file remains in the history of the private Vessel repository.
   Removing it entirely would require a coordinated history rewrite and remains
   Ana's decision.
2. `Components/bibliography/buddhism/Vinaya-Pitaka-English.md` still places the
   relevant Pali term in Mahāvagga VI. The Chapter VI publication record gives
   the verified location as Mahāvagga I.30.4. The companion note still needs a
   source-checked correction.
3. Two Müller PDFs were reported without searchable OCR layers, and a Horner
   scan was reported as a different volume from its filename. These shelf
   problems were not re-audited in this session.
4. `claim_tier` reconciliation was reported incomplete in both The Vessel and
   the website. The current counts were not recalculated here.
5. `sovereign-biophysics-distillation/10-method/amaroli-protocols.md` still has
   no designed reader-facing edition. The blocker remains clearly recorded in
   `Components/website/REVIEW_QUEUE.md`; Chapter VI deliberately names it
   without linking to a dead Markdown route.
6. Any additional unfinished work held only in the interrupted Codex session
   remains unknown.

### Protocol changes Report 095 recommended

- Recheck `tools/orchestrate status` immediately before each commit to a shared
  surface.
- Treat `AGENTS.md`, protocols, and role skills as claimable shared surfaces.
- Stage explicit paths whenever a repository contains unrelated or untracked
  work.

These safeguards have not yet been incorporated into the governing files.

## Skill-system audit

The audit covered all fourteen skills under `.agents/skills/`, the skill map,
Claude symlinks and harness-specific copies, Codex agent profiles, relevant
supporting scripts, `AGENTS.md`, `protocols/orchestration.md`, and
`protocols/active-surfaces.md`.

No files were changed during the audit.

### Priority 1 — credential safety

`.agents/skills/passwords/SKILL.md` contains instructions that conflict with its
own absolute rule:

- It says pipes are the only approved secret-transfer mechanism and forbids
  command substitution and shell variables.
- Its environment-wrapper example later uses both command substitution and a
  shell variable.
- Its suggested metadata check, `gopass show <path> | head -1`, would print the
  first line of the entry, which is normally the password rather than metadata.
- Its login-metadata example says it will add a `login: <email>` field, but the
  shown pipeline appends the raw email without adding the `login:` key.

Local `gopass generate --help` confirms that generation does not print the
password unless `--print` is requested, so the basic `gopass generate` advice is
sound. The unsafe verification, metadata, and wrapper examples should not be
used until revised around a vetted helper or file-descriptor interface.

### Priority 2 — publication and deletion authority

`.agents/skills/water-of-life/SKILL.md` currently instructs an agent processing
a form submission to format it, publish it, build, push, and delete the raw
submission from Formspree and email. Its interview route similarly says to
publish and delete the audio after contributor approval.

This conflicts with:

- `AGENTS.md`, which requires Ana's explicit approval before publication;
- the sensitive-content skill's release gate;
- the audio-transcription skill, which requires a separate explicit request for
  deletion;
- the general rule that destructive actions require exact authorization.

Intake, editorial review, contributor consent, Ana's publication approval, and
source deletion should be separate gates. Publication approval should never
silently imply deletion approval.

### Priority 3 — public reports versus private material

`aether` and all directories under its `reports/` tree are public. At the same
time:

- `AGENTS.md` says any session-end response longer than a few lines should be
  written into a report;
- the sensitive-content skill refers to an “appropriate private or role-owned
  report lane” without defining any actual private report location;
- role-owned report directories are still inside the public Aether repository.

This combination can turn an ordinary read-only or sensitive session into an
unrequested public artifact. The report rule needs an explicit exception for
read-only answers and sensitive work, plus a real definition of where private
continuity records may live. Public reports should carry paths, decisions, and
bounded cross-lane state only.

### Priority 4 — video skill and executable disagree

`.agents/skills/video/SKILL.md` prohibits CPU video encoding on this machine and
requires VAAPI on the Intel GPU. The executable `tools/mother_spirit_video`
still invokes `libx264` in both its full-render and clip-render paths.

Following the tool therefore violates the skill and may impose the exact CPU
load the skill warns against. Real renders should pause until the implementation
is brought onto the documented VAAPI path or the hardware rule is deliberately
revised and tested.

The video skill also contains five Markdown links whose relative targets do not
resolve from the skill directory.

### Priority 5 — commit and coordination wording

`AGENTS.md` says to “commit all edits and push.” Taken literally, that can sweep
in unrelated work already present in a shared tree. Report 095 documents an
actual instance of this class of failure.

The governing language should say:

- commit only task-owned, explicitly staged paths;
- preserve all pre-existing and unrelated changes;
- recheck orchestration immediately before committing shared surfaces;
- claim shared instructions before editing them.

There is also a smaller ambiguity around read-only claims. The sensitive-content
skill suggests claiming before touching sensitive material, while the
orchestration protocol defines locks mainly as edit coordination. The intended
rule for read-only sensitive inspection should be stated directly.

### Priority 6 — curator metadata and architecture

`.agents/skills/curator/SKILL.md` has several internal or current-state
conflicts:

- Its example schema lists only `personal`, `observational`, and `evidential`
  for `claim_tier`, then immediately defines a fourth required value,
  `relational-source`.
- The table says evidential material is released by “Nothing; it verifies
  itself.” This can be read as bypassing Ana's approval even though the same
  skill later says nothing is published without approval.
- Its website directory diagram names paths that do not match the live website
  structure and nests `sovereign-biophysics-distillation/` under a directory
  that does not exist.
- It attributes The Vessel's migration state to an `AGENTS.md` section that
  actually discusses Sovereign Biophysics.

The live `Components/website/ARCHITECTURE.md` should be authoritative. The
claim-tier schema should include all four values, and “evidential” should
describe an evidence burden rather than release authority.

### Priority 7 — overlapping role ownership

The writer and curator skills both claim parts of `Components/website/`, divided
conceptually into prose and structure. The orchestration helper can lock paths,
not conceptual layers. Concurrent agents can therefore believe they own
different layers of the same file.

Website work should use exact-file claims, or one role should own a file for the
duration of a task. The analyst skill also describes `reports/` and all role
subdirectories as its owned surface, while orchestration assigns each role its
own report directory. Read access and write ownership should be distinguished.

### Priority 8 — Solar Journal carries contradictory generations

`.agents/skills/solar-journal/SKILL.md` is nearly 48 KB and currently acts as an
operating skill, historical log, product specification, research notebook, and
decision record. Superseded decisions remain beside current ones. Examples:

- solar time is said to be looked up and later said to be observed;
- the `Light` field is said to have been removed and later appears in the entry
  schema;
- the journal is explicitly not a daily planner, while later sections still
  name daily entries;
- A5 is the settled trim size, while a later section still calls the artifact
  612×792-pixel US Letter;
- the skill says there is no printed example entry, while a later page plan
  includes one;
- its simple Gregorian-to-AM formula does not include the Phoenix skill's
  Aries-ingress year boundary.

Settled operating decisions should remain in `SKILL.md`. Historical rationale,
product research, attributed cosmology, and superseded design states should move
to focused reference files. The Solar Journal and Phoenix AM conventions then
need one explicitly shared rule.

### Priority 9 — Phoenix calculator is not currently runnable as shown

The Phoenix skill tells an agent to run `python scripts/phoenix.py`, which fails
from the Aether root because that path does not exist there. Running the actual
script at `.agents/skills/phoenix-calculator/scripts/phoenix.py` then fails in
the current environment because `pyswisseph` is not installed.

The package README mentions `pip install pyswisseph`, but the dependency is not
provisioned by the repository. A stable repo-level wrapper and declarative
dependency setup would make the skill reproducible without relying on an
assumed working directory or ad hoc installation.

### Priority 10 — skill map and harness documentation drift

`.agents/skills/README.md` omits `solar-journal`, `phoenix-calculator`,
`remember`, and `skills` from its tables.

It also says Claude skills are symlinks to canonical Aether skills and instructs
all new skills to follow that pattern. In practice, `remember` and `skills`
correctly have separate Claude implementations because they contain
harness-specific model and runtime guidance. The map should document this
exception rather than describe a universal symlink rule.

All existing shared symlinks resolve correctly, and all skill directory names
match their YAML `name` fields.

### Skills whose core intent is sound

The analyst, researcher, prose, writer, remember, sensitive-content, and
audio-transcription skills are coherent in their central purpose. The hosted
transcription client keeps the OpenAI credential inside its process rather than
passing it through shell arguments or environment variables. The main problems
are cross-document governance, stale duplicated state, unsafe examples, broken
links, and tool/skill mismatch rather than a need to replace the whole system.

## Water of Life change completed in this session

The pre-existing uncommitted change was limited to:

`Components/the-water-of-life/methodology/founding-document.md`

It was an editorial attribution cleanup: four additions and twelve deletions.
It removed model attribution and private-session references, renamed “What this
conversation established” to “What the founding research established,” changed
“contributor template design” to “contribution model,” and updated the minimum
viable product wording from templates and entries to forms and observations.

The archive's purpose, evidence framing, privacy principles, and stewardship
rules were otherwise unchanged. The automatic audio-deletion language noted in
the audit predates this diff and remains unresolved.

The approved change was committed and pushed to Aether as:

`635070b refine Water of Life founding attribution`

After the push, Aether `HEAD` matched `origin/main`.

### Copy relationship discovered

Three related copies were compared:

- the Aether methodology file;
- `/home/bird/Git/the-water-of-life/site/content/methodology/founding-document.md`;
- `/home/bird/Git/the-water-of-life/methodology/founding-document.md`.

The public site's content copy already matched the newly committed Aether file.
The external repository's top-level methodology copy is a substantially older,
structurally different document, not a simple missing four-line update. It was
therefore not overwritten under the narrow authorization to commit the existing
Aether change. That divergence should be reviewed deliberately rather than
resolved by blind copying.

## Proposed path forward

### Phase 1 — make agent operation safe

Review and approve a small governance repair covering only:

1. password handling;
2. publication and deletion authority;
3. public versus private reporting;
4. task-owned staging and pre-commit coordination checks.

These are the items capable of exposing secrets, publishing without the intended
gate, deleting source material, or sweeping unrelated work into a commit.

### Phase 2 — align skills with their executables and live architecture

1. Reconcile the video tool with the VAAPI-only rule and test a short hardware
   render before any real job.
2. Correct curator claim-tier guidance and replace its copied directory tree
   with a link to the authoritative website architecture.
3. Clarify exact-file ownership for writer and curator work on the website.
4. Repair broken skill links and complete the skill map.

### Phase 3 — consolidate domain skills

1. Reduce the Solar Journal skill to current governing decisions and move its
   historical/research material into references.
2. Establish one shared AM-year rule between Solar Journal and Phoenix.
3. Add a stable Phoenix wrapper and reproducible Swiss Ephemeris dependency.
4. Review the divergent external Water of Life methodology source against the
   already-public content copy before deciding which is canonical.

### Phase 4 — return to Report 095's content and archive work

Only after the operating layer is safe:

1. decide whether the private historical file warrants a coordinated history
   rewrite;
2. correct the Vinaya companion note from verified source evidence;
3. repair the mislabeled or unsearchable bibliography PDFs;
4. complete judgment-dependent `claim_tier` reconciliation;
5. decide whether and how to create a reviewed reader-facing Amaroli edition.

## Decision point for Ana

The recommended next session is a narrow **governance repair**, not a content
session. Before editing, review the four Phase 1 areas together and decide the
exact policy language. Then claim only the governing files involved, make one
atomic change, validate all affected skills and links, commit explicit paths,
push, and release the lane.

No Phase 1 correction should silently authorize publication, deletion, history
rewriting, or changes to private content.
