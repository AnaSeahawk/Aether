# 91. July Whole-Archive Audits — Superseded And Closed

**Date:** 2026-08-06
**Role:** analyst
**Session topic:** Replacing the two July whole-archive audits under the stale-report rule; correcting one retired path reference in report 057.

---

## Replacement Note

This report replaces two deleted reports, both confirmed by Ana:

- `reports/analyst/077_full_archive_audit_before_collaborator_invites.md` (July 5)
- `reports/analyst/079_collaboration_private_usefulness_audit.md` (July 6)

Report 087 (July 30) flagged 079 as a stale-report candidate. Both turned out to be stale for the same three reasons:

1. **Their central recommendation has been built.** Report 079's whole argument was `archive as storage → archive as working board`: create a source-packet board, a call topic index, a collaborator review packet, and a media consent log. All four now exist. Report 077's recommended sequence — prepare a gated collaborator entry rather than a full repo invite — was also followed; `collaborator-read-path.md` is the result.
2. **They describe a lane that has since been renamed.** Both are written throughout against `35-collaboration-private/`, retired in favour of `35-water-magicians-private/`.
3. **They carry the attribution framing retired in report 089.** Report 079 names "Megan's correction is the model for future attribution discipline" as a headline finding. That model is retired: there is no ownership question to adjudicate, and the note it referred to is now a provenance record that blocks nothing.

## Why This Replacement Is Short

Same reason as report 090, and it is now a pattern worth naming explicitly.

Reports 077 and 079 were detailed inventories of a **private** lane, published to a **public** repository — file-by-file contents, what each collaborator brings, what their assets are, what remains unreviewed about their material. Report 079 runs 629 lines and report 077 runs 551, most of it private working detail.

Report 087 set the correct principle in July: the cross-lane view belongs in public analyst reports, and lane detail is referenced by path, not copied. These two predate that principle. Their replacement follows it.

**As with reports 074 and 056: this clears the current tree, not public git history.** Rewriting pushed public history remains not recommended.

## What Remains Valid

Three things are worth carrying forward. All are postures, not inventory.

**The working-board test (from 079).** The question that made the board layer happen is still the right one to ask of any lane: *what do we actually have, and what can we use next?* A lane passes when someone can see what is ready, what is blocked, what is still raw, and what may safely move outward — without reading the whole lane.

**The invitation posture (from 077).** Still unused, still correct, and still the right words for the review bundle that has not yet been sent:

> You are being invited to review how the archive is holding the collaboration, not to approve public use by default. Raw messages, transcripts, summaries, and source packets are private unless you approve a specific use.

**Read-only access is not consent to publish.** Report 077's most load-bearing sentence. It survives the retirement of the attribution apparatus, because it is about consent, not ownership.

## Report 057 — Path Correction, Not Replacement

`reports/057_sb-dictionary-water-magicians-gap-analysis.md` references the retired `35-collaboration-private/` path once, in its closing plain-text source list. It is not a link, so nothing is broken to click.

Report 057 is **not** being replaced. Its substance — the SB Dictionary gaps — is still live and still cited by report 087. Under the analyst protocol a path rename is a minor update, noted in a new report rather than triggering a deletion. This is that note. The two files it names are now at:

- `Components/the-vessel/35-water-magicians-private/emergent-patterns-report.md`
- `collaboration-use-map.md` → now `Components/the-vessel/35-water-magicians-private/water-magicians-use-map.md`

## Report Trail After This Pass

Reports 074, 056, 077, and 079 have all been replaced by pointers. **One remains: report 075** (`075_full_archive_audit_current_intention_flow.md`, June 28, 673 lines).

Report 075 is the direct predecessor of 077 in the same audit series and has the same three defects: four live references to the retired `35-collaboration-private/` path, private lane detail in a public repo, and a section built on the attribution framing retired in report 089. It is superseded by report 087 as a whole-archive view.

It is **not** deleted in this pass. Ana confirmed replacing 077 and 079; 075 was not part of that batch, and three substantive deletions should not ride on one confirmation. It is the obvious next candidate and needs only a yes.

Two in-place corrections have already been applied to 075 for reasons that could not wait: third-party names and health details were removed from one line (report 089), and its pointer to the deleted 074 was repointed.

The root-level reports `038`–`060` still predate the June restructure as a group. Report 087 recommended a cleanup pass over them; reports 056 and 057 have now been handled, and the rest remain untouched.

## What Is Actually Outstanding

Carried forward from these audits and from report 087, with current status verified 2026-08-06:

**Blocked on Ana, and blocking others:**

- **The first review bundle has still not been sent.** `collaborator-read-path.md` remains "ready after Ana's review." Every downstream item below depends on it. It has been the top non-risk item since report 087 on July 30.
- `in-development/bridge-possession-sovereignty.md` still carries `visibility: public` while unreviewed in the private repo. Open since early July; a one-line fix, but the visibility call is Ana's.

**Open decisions from 077 that are still genuinely open:**

- What specific use, if any, does Fiona approve for her brand assets?
- Does the support path become a review packet, or stay private drafting?
- Should the generated living archive stay hidden/community, become a member map, or get a public excerpt?
- Should curator review the method/protocol pages before any new public or member-facing offer?

**Resolved, recorded so they stop being re-raised.** Report 078 (July 5) captured Ana's decisions on four of report 077's eight open questions, and it remains the live record of them:

- Collaborator access scope — gated, smaller access first; not a broad private-repo invite. Timing not urgent; the archive opens when Ana is ready.
- "Water Magicians" — accepted as the working name. The group already calls itself that.
- June synthesis — promoted to the SB reader-path endpoint (landed across five website files).
- The collaborator preview note — approved for gated sharing, still private.

Report 078 is **not** replaced; it is a decision record and stays. Two maintenance fixes were applied to it in this pass: its pointer to the deleted 077 now points here, and two `35-collaboration-private/water-magicians/` paths were updated to the current lane. Both are path/pointer corrections under the minor-update rule, recorded here rather than triggering a deletion.

**Work items, not decisions:**

- `womens-shivambu-circle-event-material-packet.md` — still the packet board's named next move.
- The SB Dictionary uniqueness/non-categorization entry — still the one public-safe candidate needing no collaborator consent.
- `QUEUE.md` inbox — still duplicating what the two boards track better.
- `protocols/active-surfaces.md` — proposed in report 075, still absent, now carried by four audits. Build it or drop the proposal.
- New: add `photo_55@02-07-2026_13-02-39.jpg` to the media consent log as unreviewed (from the August 6 backfill).

**Two numbering problems in the report trail:**

- Two reports share the number `056`: the deleted root-level `056_water-magicians-report.md` and the live `reports/analyst/056_new-entry-integration-report.md`. Report 058's references to "report 056" mean the latter.
- On August 4 two reports were independently written as `088`; one was renumbered to `089`. A report claims its number only at commit time, so concurrent sessions cannot see each other's choice. Unresolved.
