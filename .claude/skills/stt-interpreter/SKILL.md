---
name: stt-interpreter
description: Decode phonetic near-misses in Ana's speech-to-text-dictated prompts. Use when a dictated prompt contains a word or name that doesn't parse as English in context.
---

# Skill — speech-to-text interpreter

*Decoding STT-transcribed prompts that contain mangled names.*

## What this skill is for

Ana sometimes dictates prompts through a speech-to-text tool, which can
mis-transcribe a name it doesn't know into a phonetically similar English
word or phrase. When a word in a dictated prompt doesn't make sense as
English in context, guess the intended word from the table below, act on the
guess, and only ask if the guess turns out wrong.

## Table

| Heard / transcribed as | Canonical |
|---|---|
| "Legal Dragon" / "Gold Dragon" / "Lee" | **Li Goldragon** — Ana's partner. Li's own `primary` repo instead uses "Goldragon" for Li's cluster-proposal repo; judge from context which one is meant. |
| "Shivamboo" | **Shivambu** — the auto-urine practice term used across the Water of Life archive. |

## When the table doesn't help

Don't ask Ana to spell a mis-transcribed word out — dictation often mangles a
spelled-out word too. Look for the canonical spelling in context instead:
nearby files, the memory index, or how Ana has already written the word
elsewhere in the conversation. Ask only once no candidate emerges, and frame
the question with the closest matches considered.

## Keeping this current

This table is workspace state. When a new mishearing recurs in practice, add
a row before continuing — a routine edit, not one needing a separate
decision.

## See also

- `.claude/skills/remember/SKILL.md` — session catch-up, where dictated
  prompts often first surface as mangled transcript text.
