# Skill — video

*Turning one raw recording into reviewable video and publishing drafts.*

---

## What this skill is for

Load this skill for any work that turns a recording — a practitioner
conversation, a presentation, or a community call — into a cleaned video, a
transcript, and draft publishing copy.

This is a **task skill**, not a role. Any role may load it when the work
involves recordings. It does not have its own orchestration lane; claim the
`.video-work/` path (or the relevant publishing path) under whatever role you
are working as.

The whole pipeline is **local-first**. The only step that leaves the machine is
the optional hosted transcription call described below, and only when you choose
it over the offline transcriber.

---

## The tool

`tools/mother_spirit_video` is a self-contained Python CLI built on FFmpeg. The
name is legacy — it is general-purpose, not Mother-Spirit-specific. It creates a
project under `.video-work/<slug>/` (git-ignored) and never uploads or requires
platform credentials.

Stages, in order:

```
start     create the project folder + manifest from a raw recording
inspect   ffprobe metadata, 16 kHz audio extract, thumbnail, silence log
render    the cleaned, normalized full video
transcribe  generate or import transcript artifacts (.srt + .txt)
bundle    draft publishing copy: description, chapters, clips, telegram, archive
```

Plus `clip` (render one short), `install-archive-entry` (copy the draft entry
into the website archive), and `make` (run start → inspect → render →
transcribe → bundle in one command).

Full command reference and examples live in
[`tools/mother_spirit_video.md`](../tools/mother_spirit_video.md). Treat that
file as the exhaustive source; this skill is the orientation and the
transcription decision.

---

## Transcription

`transcribe` folds a transcript into the project. The `bundle` step then parses
the **timed** `.srt` to place chapter markers and suggest clip windows, so the
transcript must carry timestamps — plain text is not enough.

There are two ways to produce that transcript.

### Default — hosted: `tools/whisper-transcribe`

```sh
tools/whisper-transcribe .video-work/<slug>/inspection/audio_16k.wav \
  --output .video-work/<slug>/transcripts/audio_16k.srt

tools/mother_spirit_video transcribe .video-work/<slug> \
  --transcript .video-work/<slug>/transcripts/audio_16k.srt
```

`whisper-transcribe` transcodes the audio to fit the 25 MiB upload cap, calls
the OpenAI transcription API, and writes a timed `.srt`. Notes:

- The API key is read from **gopass at `openai/api-key`** — the same secret the
  desktop dictation tool uses. The key is written to a private, mode-600 curl
  config file and never placed on a command line or printed.
- It defaults to model **`whisper-1`**, because that is the model whose API
  returns SRT with timestamps. The `gpt-4o-transcribe` model returns plain text
  only, which would lose the timing `bundle` depends on.
- Pass `--prompt "..."` with names or jargon that should be spelled correctly.
- Very long recordings that still exceed the cap after compression should be
  split first with `tools/mother_spirit_video clip`, then transcribed per part.

### Offline fallback — local `whisper` CLI

Use when you do not want to upload audio or spend API budget. Proven on real
calls; you manage the local model.

```sh
whisper .video-work/<slug>/inspection/audio_16k.wav \
  --model small --output_format srt \
  --output_dir .video-work/<slug>/transcripts

tools/mother_spirit_video transcribe .video-work/<slug> \
  --transcript .video-work/<slug>/transcripts/audio_16k.srt
```

`--model tiny.en` is faster and English-only; both models are cached locally.

Neither path identifies speakers. For multi-person calls, hand-label speakers in
the SRT (the `(Speaker Name)` convention already used in the water-magicians-calls
transcripts) or run a diarization step before import.

---

## Review and consent boundary

Before anything is posted, review the cleaned video end to end, the transcript
against the recording, the chapter markers, each clip window, and the archive
entry (privacy, claim boundaries, draft status).

**Any recording with more than one person speaking needs a consent pass** before
any clip is shared, independent of the normal review. The pattern in use for
Water Magicians calls:

- Mark the batch `status: review candidates only; not cleared for posting` until
  every visible/audible person has approved the exact clip, caption, and platform.
- First-pass selection avoids process/practice specifics, health or diagnostic
  claims, private funding mechanics, project architecture detail, or anything the
  group has not chosen shared public language for yet.
- Keep the review index alongside the clips, not just in chat.

Recordings are operational, often health-adjacent material — read
[`skills/sensitive-content.md`](sensitive-content.md) before handling them.

---

## Outputs

Projects live under `.video-work/<slug>/` (git-ignored). The website archive
entry is a draft (`status: draft`, `visibility: community`); install it into the
website only after review with `install-archive-entry`. Nothing is published or
uploaded by this workflow.

---

## See also

- [`tools/mother_spirit_video.md`](../tools/mother_spirit_video.md) — full command reference
- [`skills/sensitive-content.md`](sensitive-content.md) — privacy and consent boundaries
- [`skills/curator.md`](curator.md) — installing the archive entry into the website
- `AGENTS.md` — the authoritative repo contract
