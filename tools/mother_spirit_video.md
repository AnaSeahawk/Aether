# Mother Spirit Video Workflow

This is the simple local path for turning one raw recording into reviewable
video and publishing artifacts. It uses FFmpeg, ffprobe, Python, and the living
archive builder already present in this repo. It does not upload to any
platform.

## One-command path

```sh
tools/mother_spirit_video make /path/to/raw-recording.mp4 \
  --title "Mother Spirit - June Call" \
  --date 2026-06-17 \
  --whisper-model /path/to/ggml-model.bin
```

If no Whisper model is available yet, omit `--whisper-model`. The workflow will
still create the cleaned video, inspection files, audio extract, and publishing
drafts, with a transcript placeholder that says exactly how to rerun the
transcription step.

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

Generate the transcript with FFmpeg's Whisper filter:

```sh
tools/mother_spirit_video transcribe .video-work/2026-06-17-mother-spirit-june-call \
  --whisper-model /path/to/ggml-model.bin
```

Or import a corrected transcript:

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
