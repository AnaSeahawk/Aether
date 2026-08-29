# Active Surfaces

Names the live surfaces of this archive and the sensitivity watchpoints that
currently apply, so agents do not re-derive them from old reports.

Proposed in report 075 (June 28), carried unbuilt through reports 077, 079, and
087, approved and created 2026-08-06.

**Read this before writing anything into a public repo.**

---

## The surfaces

| Surface | Repo | Visibility | What belongs here |
|---|---|---|---|
| Coordination seed | `aether` | **public** | Agent instructions, protocols, skills, analyst/writer/curator/researcher reports |
| Sovereign Biophysics | `Components/website` | **public** | The reader-facing archive: orientation, method, experiments, analysis, synthesis, Dictionary |
| Mother Spirit | `Components/mother-spirit-webpage` | **public** | Public-facing site for the Mother Spirit call |
| Wiki | `Components/wiki` | public | Historical, dormant |
| Bibliography | `Components/bibliography` | public | Acquired texts by topic folder |
| The Water of Life | `Components/the-water-of-life` | **public** | Open observational archive: contributor entries, methodology, templates |
| The Vessel | `Components/the-vessel` | **private** | Everything operational, relational, intimate, or unreviewed |

`aether` being public is the single most-missed fact in this archive's history.
Five analyst reports reached it carrying private material before anyone noticed.

## The rule that follows

**Public reports carry the cross-lane view. Lane detail is referenced by path,
not copied.**

Report 087 stated this; reports 090, 091, and 092 exist because five earlier
reports did not follow it. If a report would let a reader reconstruct a private
lane's contents, it is in the wrong repo.

## Never publish

- **Named third parties' personal or health accounts.** People outside the
  collaboration have not consented to anything. This is the boundary that report
  074 breached.
- **Private collaborators' working arrangements** — money, splits, roles,
  unreviewed material about their practice. Report 056 breached this.
- **Anything from `the-vessel` that has not been through review**, regardless of
  how finished it reads.

Naming a *public figure* and engaging with their published work is different and
is fine — that is ordinary intellectual engagement, not exposure.

## Sensitivity watchpoints (current)

| Watchpoint | State |
|---|---|
| Water Magicians material | Private. Outflow gated on collaborator review. |
| Named third-party testimony | Never public without that person's own consent. |
| Media (photos, video, brand assets) | Unusable by default until visually reviewed and logged. See the lane's media consent log. |
| Raw Telegram exports | Private. Large packets may go to owner-only Drive rather than git. |
| Intimate-field records | Private, permanently. Not review material for anyone. |
| Method and protocol pages | Curator review required before any new public or member-facing offer (Ana, 2026-08-06). |

## Before a record enters the archive

The nine-step intake sequence, carried forward from report 075:

1. **Intent** — what is this record trying to serve?
2. **Lane** — where does it belong before interpretation?
3. **Provenance** — who or what generated it, and under what conditions?
4. **Sensitivity** — who could be exposed or misrepresented?
5. **Index** — what threads does it touch?
6. **Consent** — what uses are actually cleared?
7. **Synthesis** — what can be said privately without overclaiming?
8. **Derivative** — should anything public, community, book-facing, or
   member-facing be made from it?
9. **Rule migration** — did this reveal a durable rule belonging in a README,
   protocol, or skill file?

Defaults: collaborator records → private synthesis, not public copy. Public
records → bounded invitation and archive navigation, not proof. Member/portal
records → exact consent and context framing before features.

**Step 4 is the one that gets skipped.** Every public-repo exposure this archive
has had would have been caught by asking it.

## Detecting archive gaps

Message-ID arithmetic on Telegram exports produces false alarms — IDs are
assigned account-wide, so hundreds are legitimately absent. The reliable signal
is **an internal reference that fails to resolve**: a reply link pointing at a
message no export contains. That is what exposed the July 2–4 gap on August 6.

## Reports

- One global number sequence covers files directly in `reports/` and directly
  in each `reports/<role>/` folder. Dynamic session lanes use a local sequence
  inside `reports/<role>/<lane>/`; ignore those nested files when selecting the
  next global number.
- Stale reports are deleted and replaced, not edited in place. Confirm with Ana
  first when the content is substantive.
- Two known numbering faults: two reports share `056` (one root, one analyst),
  and two were independently written as `088` on 2026-08-04 because a number is
  only claimed at commit time. Check both `reports/` and `reports/*/` before
  choosing a number.

---

*Update this file when a surface changes, not the reports. Reports are
point-in-time; this is current state.*
