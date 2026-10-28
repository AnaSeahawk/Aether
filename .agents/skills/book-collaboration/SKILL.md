---
name: book-collaboration
description: Hold a book Ana is co-creating with another author — manuscripts, series bible, and a journal of every discussion — in a private Vessel section with version history. Use when working on a collaborator's manuscript, preparing or reviewing edits, recording a call or message about a book, or pulling a new draft from Google Drive.
---

# Skill — book collaboration

*The author's vision leads. The archive remembers what was said and why.*

---

## What this skill is for

Use it when Ana is helping another author with a book or series. That covers
reading a manuscript, suggesting edits, recording a conversation, pulling a
new draft from Drive, or picking the work back up after a gap.

Load `sensitive-content` too. The manuscripts and the conversations are
private collaboration material.

---

## Where things live

Each project gets one private home: a folder in the Vessel, or its own
private repository once it needs room (illustrations) or the author needs
access. A project lives in one place only. When it moves, move it, and leave
a pointer in the Vessel section's `README.md`.

```
Components/the-vessel/36-book-collaborations-private/<author>-<work>/
  (or a private repository with the same layout)
  README.md          doorway: what this is, read order, where else things live
  series-bible.md    settled decisions only, each dated
  journal.md         one dated entry per conversation, newest last
  manuscripts/       current text, one Markdown file per book
  reviews/           review documents, prefixed with their date
  sources/<date>-<origin>/   original files as received, plus SHA256SUMS.txt
```

List each project in the section's `README.md`, and link it from the author's
person card in `Components/the-vessel/05-relationships-private/`. Before
writing, confirm that
the Vessel repository is still private.

Photographs of real people used as references for illustrations, above all
children, never enter Git. They stay in a private Drive folder, and image
tools receive a written description. A photograph goes to an outside image
service only with the agreement of the author and, for a child, the parents.

This skill is public. The specifics of a book stay in its private home:
names, plot, decisions, and anything personal. Never copy them here.

---

## Pulling a new draft

Authors usually work in Google Drive. Every new Drive version becomes a
commit, so the history shows exactly what changed.

1. Copy the Drive folder into `sources/<date>-drive/`. Export Google Docs as
   `.docx`. Write `SHA256SUMS.txt`.
2. Convert each manuscript to Markdown with
   `pandoc -t gfm --wrap=none`, replacing the file in `manuscripts/`. Keep the
   conversion plain, with no frontmatter or edits, so diffs show only the
   author's changes.
3. Check the book order from the title page, not the filename.
4. Commit the draft by itself before any editorial work.

---

## The journal

After every call, message, or review, add an entry to `journal.md`:

- **Date and what it was:** call, message, review, or Drive version.
- **Source:** a transcript path, a Drive location, or the message quoted
  exactly when Ana shares it.
- **Decided:** each decision, with the reason when one was given.
- **Raised and left open:** questions without an answer yet.

Then update `series-bible.md` with any new decisions. Each line points back
to the date it was made. The bible holds what is settled; the journal holds
how it got there.

When a suggestion is declined, record it in the journal and remove it from
the open questions. Do not raise it again unless the author does.

---

## Editorial posture

- **The author's vision leads.** Offer edits; never impose them.
- **When a craft suggestion clashes with the author's picture,** look for a
  version that serves both. Read the manuscript first. The author's own text
  often already holds the answer.
- **Keep the author's voice and imagery.** Fix clarity, consistency, and
  mechanics without flattening what makes the work theirs.
- **Say where a suggestion came from:** Ana, the author, a reviewer, or an AI
  conversation. AI suggestions are options, not verdicts.
- **Check every draft against the bible.** Look at names and spellings,
  pronouns, each character's colour and form, titles, and the threads that
  run across the series.
- **Personal material** that an author brings into a story belongs to them.
  Record only what the work needs, and follow their lead.

---

## Sharing back

Authors may not use Git. Share work with them as documents, through Drive or
in a message. Keep their history in Git for them. Reassure them that earlier
versions and declined ideas are kept, so they can let ideas go.

Nothing in a project folder leaves the Vessel without the author's agreement
and Ana's explicit approval.

---

## See also

- `.agents/skills/sensitive-content/SKILL.md`: private-by-default handling
- `.agents/skills/prose/SKILL.md`: craft moves when drafting or editing
- `.agents/skills/writer/SKILL.md`: the drafting role
