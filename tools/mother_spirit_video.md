# Mother Spirit Video Workflow

This is the simple local path for turning one raw recording into reviewable
video and publishing artifacts. It uses FFmpeg, ffprobe, Python, and the living
archive builder already present in this repo. It does not upload to any
platform.

This workflow already covers practitioner conversations, presentations, and
community calls — it is not Mother Spirit-specific despite the name. It has
been run for real on Water Magicians calls; see `.video-work/water-magicians-calls/`
and `.video-work/water-magicians-social-shorts/` for finished examples.

## Status on this machine (checked 2026-07-22)

- `ffmpeg` and `ffprobe` are installed and on `PATH`. The full `make` pipeline
  (start, inspect, render, bundle, clip) runs without any extra setup.
- **Default transcription path: `tools/whisper-transcribe`** (hosted OpenAI
  API). It transcodes the audio, uploads it, and writes a timed `.srt` you then
  import with `--transcript`. It resolves the API key from gopass
  (`openai/api-key`, the same secret the desktop dictation tool uses) and has
  been verified end to end on this machine. Prefer this path — it needs no local
  model management and produces the timed SRT the chapter/clip steps depend on.
- `whisper` CLI (`openai-whisper`) is also installed, with real models cached at
  `~/.cache/whisper/` (`small.pt`, `tiny.en.pt`). This produced the existing
  Water Magicians transcripts and remains the **offline / no-API-cost fallback**
  when you do not want to upload audio.
- No real whisper.cpp `ggml-*.bin` model is present, so the `--whisper-model`
  flag (FFmpeg's built-in `whisper` filter) will fail if used as-is. Only tiny
  test-fixture stubs exist on this machine, not usable models.

## One-command path

```sh
tools/mother_spirit_video make /path/to/raw-recording.mp4 \
  --title "Mother Spirit - June Call" \
  --date 2026-06-17
```

This creates the cleaned video, inspection files, audio extract, and publishing
drafts, with a transcript placeholder that says exactly how to rerun the
transcription step. Then transcribe separately with `tools/whisper-transcribe`
(the default hosted path; see "Status on this machine" above) and re-run
`bundle` to fold the transcript into chapters and clip suggestions:

```sh
tools/whisper-transcribe \
  .video-work/2026-06-17-mother-spirit-june-call/inspection/audio_16k.wav \
  --output .video-work/2026-06-17-mother-spirit-june-call/transcripts/audio_16k.srt

tools/mother_spirit_video transcribe .video-work/2026-06-17-mother-spirit-june-call \
  --transcript .video-work/2026-06-17-mother-spirit-june-call/transcripts/audio_16k.srt

tools/mother_spirit_video bundle .video-work/2026-06-17-mother-spirit-june-call
```

If a real whisper.cpp ggml model is downloaded later, `--whisper-model` can be
passed to `make` directly for a single-command run.

Generated projects live under `.video-work/<slug>/`, which is ignored by git.

## Outputs

Each project contains:

- `sources/` - the raw recording copy or symlink
- `inspection/ffprobe.json` - stream and duration metadata
- `inspection/audio_16k.wav` - audio prepared for transcription
- `inspection/thumbnail.jpg` and `inspection/contact_sheet.jpg` - review images
- `inspection/silence.log` - FFmpeg silence detection notes
- `renders/<slug>_clean_full.mp4` - normalized clean full video
- `transcripts/<slug>.txt` and, when a model is used, `transcripts/<slug>.srt`
- `publishing/youtube_description.md`
- `publishing/chapters.txt`
- `publishing/short_clip_suggestions.md`
- `publishing/telegram_post.md`
- `publishing/website_archive_entry.md`
- `publishing/review_checklist.md`

## Step-by-step path

Create the project:

```sh
tools/mother_spirit_video start /path/to/raw-recording.mp4 \
  --title "Mother Spirit - June Call" \
  --date 2026-06-17
```

Inspect the media:

```sh
tools/mother_spirit_video inspect .video-work/2026-06-17-mother-spirit-june-call
```

Render the cleaned full video:

```sh
tools/mother_spirit_video render .video-work/2026-06-17-mother-spirit-june-call
```

**Recommended path — transcribe with `tools/whisper-transcribe` (hosted
OpenAI), then import.** This transcodes the audio to fit the 25 MiB upload cap,
calls the OpenAI transcription API, and writes a timed `.srt`. The API key comes
from gopass (`openai/api-key`); nothing else needs configuring:

```sh
tools/whisper-transcribe \
  .video-work/2026-06-17-mother-spirit-june-call/inspection/audio_16k.wav \
  --output .video-work/2026-06-17-mother-spirit-june-call/transcripts/audio_16k.srt

tools/mother_spirit_video transcribe .video-work/2026-06-17-mother-spirit-june-call \
  --transcript .video-work/2026-06-17-mother-spirit-june-call/transcripts/audio_16k.srt
```

`whisper-transcribe` defaults to model `whisper-1`, because that is the model
whose API returns SRT with timestamps (the `gpt-4o-transcribe` model the
dictation tool uses returns plain text only, which would lose the timing the
chapter/clip steps need). Pass `--prompt "..."` with names or jargon that should
be spelled correctly. For very long recordings that still exceed the 25 MiB cap
after compression, split them first with `tools/mother_spirit_video clip` and
transcribe each part.

**Offline fallback — the local `whisper` CLI.** Proven on real calls and needs
no upload or API cost, but you manage the local model:

```sh
whisper .video-work/2026-06-17-mother-spirit-june-call/inspection/audio_16k.wav \
  --model small --output_format srt \
  --output_dir .video-work/2026-06-17-mother-spirit-june-call/transcripts

tools/mother_spirit_video transcribe .video-work/2026-06-17-mother-spirit-june-call \
  --transcript .video-work/2026-06-17-mother-spirit-june-call/transcripts/audio_16k.srt
```

Use `--model tiny.en` instead of `small` for a faster, English-only pass; both
models are already cached locally. For multi-person calls, hand-label speakers
in the resulting SRT (see the water-magicians-calls transcripts for the
`(Speaker Name)` convention already in use) or run a diarization step before
import — neither transcription path identifies speakers.

**Alternate path — FFmpeg's built-in Whisper filter.** Only use this once a
real whisper.cpp ggml model is downloaded (e.g. via `whisper-cpp-download-ggml-model`,
not currently on this machine's `PATH`); the stub files present here are test
fixtures and will not produce usable transcripts.

```sh
tools/mother_spirit_video transcribe .video-work/2026-06-17-mother-spirit-june-call \
  --whisper-model /path/to/ggml-model.bin
```

Either way, you can always import a corrected or manually-made transcript
directly:

```sh
tools/mother_spirit_video transcribe .video-work/2026-06-17-mother-spirit-june-call \
  --transcript /path/to/corrected-transcript.srt
```

Build the publishing bundle:

```sh
tools/mother_spirit_video bundle .video-work/2026-06-17-mother-spirit-june-call
```

## Short clips

The workflow suggests clips in `publishing/short_clip_suggestions.md`. Render
one of them with the command shown there, or use:

```sh
tools/mother_spirit_video clip .video-work/2026-06-17-mother-spirit-june-call \
  --start 00:03:00 \
  --end 00:04:15 \
  --name june-call-clip-1
```

Clips default to a 9:16 padded render for Shorts/Reels/TikTok review. Use
`--format source` to keep the source shape.

## Website archive entry

The workflow first writes a draft entry to:

```text
.video-work/<slug>/publishing/website_archive_entry.md
```

After review, install it into the website archive draft layer:

```sh
tools/mother_spirit_video install-archive-entry .video-work/<slug>
```

That copies the draft into `Components/website/archive/` and runs:

```sh
Components/website/tools/build_archive_views
```

The entry remains `status: draft` and `visibility: community`. Nothing is
published or uploaded by this workflow.

## Review boundary

Before anything is posted, review:

- the cleaned full video end to end
- the transcript against the recording
- the YouTube description and chapter markers
- short clip windows before rendering or posting
- the Telegram post for consent and context
- the website archive entry for privacy, claim boundaries, and draft status

## Multi-person recordings and consent

Any recording with more than one person speaking (practitioner conversations,
community calls) needs a consent pass before any clip is shared, independent
of the tool's normal review boundary above. The pattern already in use for
Water Magicians calls, from `.video-work/water-magicians-social-shorts/REVIEW_INDEX.md`:

- Mark the batch `status: review candidates only; not cleared for posting`
  until every visible/audible person has approved the exact clip, caption, and
  platform.
- First-pass clip selection should avoid: process/practice specifics, health
  or diagnostic claims, private funding mechanics, project architecture
  detail, or anything the group hasn't chosen shared public language for yet.
- Keep this review index alongside the clips, not just in chat — it's the
  record of what was screened out and why.

Reuse this pattern for any new multi-person batch rather than re-deciding the
boundary each time.
