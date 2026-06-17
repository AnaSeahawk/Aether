# 61. Mother Spirit Video Workflow

**Date:** 2026-06-17  
**Agent:** Codex  
**Session topic:** Turn the video workflow research into a simple Mother Spirit raw-recording pipeline.

---

## Source Read

Read the requested research report:

- `LiGoldragon/primary` report: `reports/videographer/4-codex-subscription-video-workflow-and-publishing-research.md`
- Commit: `690f97ff403e81c39e98b55dda7c60635cec60c3`
- URL: https://github.com/LiGoldragon/primary/blob/690f97ff403e81c39e98b55dda7c60635cec60c3/reports/videographer/4-codex-subscription-video-workflow-and-publishing-research.md

The implemented shape follows the report's local-first recommendation:
immutable raw media, ffprobe/FFmpeg inspection artifacts, a manifest, deterministic
renders, transcript artifacts, and publishing bundles without live platform upload.

## What Changed

Added:

- `tools/mother_spirit_video` - executable Python CLI for the workflow.
- `tools/mother_spirit_video.md` - operator documentation.

Updated:

- `.gitignore` now excludes `.video-work/`, `__pycache__/`, and `*.pyc`.

The tool creates generated projects under:

```text
.video-work/<slug>/
```

That directory is ignored by git so raw recordings, renders, transcripts, and
test media are not committed accidentally.

## Workflow Outputs

From one raw recording, the workflow can produce:

- a copied or symlinked raw source in `sources/`
- `inspection/ffprobe.json`
- `inspection/audio_16k.wav`
- `inspection/thumbnail.jpg`
- `inspection/contact_sheet.jpg`
- `inspection/silence.log`
- `renders/<slug>_clean_full.mp4`
- `transcripts/<slug>.txt`
- `transcripts/<slug>.srt` when a local Whisper model is supplied
- `publishing/youtube_description.md`
- `publishing/chapters.txt`
- `publishing/short_clip_suggestions.md`
- `publishing/telegram_post.md`
- `publishing/website_archive_entry.md`
- `publishing/review_checklist.md`

The workflow can also render a suggested short clip:

```sh
tools/mother_spirit_video clip .video-work/<slug> \
  --start 00:03:00 \
  --end 00:04:15 \
  --name <clip-name>
```

Short clips default to a padded 9:16 render for Shorts/Reels/TikTok review.

## Transcription Boundary

FFmpeg in this environment has the `whisper` filter available, but no local
Whisper model file was found during this session. The tool therefore supports
both modes:

- with `--whisper-model /path/to/ggml-model.bin`, FFmpeg generates text and SRT
  transcript artifacts;
- without a model, the workflow writes a transcript placeholder and still
  produces the cleaned video, inspection artifacts, and publishing bundle;
- with `--transcript /path/to/corrected.srt`, the workflow imports an existing
  transcript and uses it for chapter labels and clip cues.

## Website Archive Entry

The workflow first writes a draft archive entry inside the project:

```text
.video-work/<slug>/publishing/website_archive_entry.md
```

After review, it can be installed into the living archive draft layer:

```sh
tools/mother_spirit_video install-archive-entry .video-work/<slug>
```

That copies the draft into `Components/website/archive/<slug>.md` and runs:

```sh
Components/website/tools/build_archive_views
```

The generated entry remains:

```yaml
status: draft
visibility: community
claim_tier: personal-account
```

No publishing status is changed by the tool.

## Verification

Checks run:

- `python3 -m py_compile tools/mother_spirit_video` - passed.
- `tools/mother_spirit_video --help` - passed.
- Generated a 3-second test recording with FFmpeg under `/tmp`.
- `tools/mother_spirit_video make /tmp/mother-spirit-sample.mp4 --title "Mother Spirit Sample" --date 2026-06-17 --slug mother-spirit-sample --force` - passed.
- Confirmed generated files under `.video-work/mother-spirit-sample/`.
- Confirmed the clean full render with `ffprobe`.
- `tools/mother_spirit_video clip .video-work/mother-spirit-sample --start 00:00:00 --end 00:00:03 --name mother-spirit-sample-clip-1` - passed.
- Confirmed the rendered clip is 1080x1920 with H.264 video and AAC audio.
- Imported a sample SRT transcript and rebuilt the bundle; chapter labels and
  clip cues used transcript text as expected.
- `git diff --check` - passed.
- ASCII scan for `.gitignore`, `tools/mother_spirit_video`, and
  `tools/mother_spirit_video.md` - clear.

## Notes

No platform uploader was added. YouTube, Telegram, TikTok, Instagram, and any
other platform posting remains an explicit later step requiring account review
and credentials outside chat.

No `Components/website` files were modified during implementation. The website
archive entry path is implemented as an optional command so a reviewed recording
can be drafted into the living archive when Ana chooses.
