---
name: audio-transcription
description: Create private, timed transcripts from existing audio or video files with OpenAI's hosted Whisper API. Use when a user asks to transcribe a recording, call, interview, voice note, MP3, WAV, M4A, MP4, or other media file; when timestamps or SRT output are needed; or when local CPU/GPU transcription must be avoided. Check embedded captions first, require explicit authorization before a paid upload, and never run a local speech model unless the user explicitly requests the offline fallback.
---

# Audio Transcription

Use the hosted OpenAI route for existing media. Keep source media and working
artifacts private unless the user explicitly changes that boundary.

## Workflow

1. Read the repository's sensitive-content instructions when the recording is
   private, multi-person, operational, health-adjacent, or publishing-sensitive.
2. Inspect stream metadata with `ffprobe`. If an embedded subtitle stream is
   present, extract it without uploading audio.
3. If no captions exist, confirm that the current request explicitly authorizes
   a paid OpenAI transcription upload. Do not infer authorization from an API
   key merely existing.
4. Run the bundled client:

   ```sh
   .agents/skills/audio-transcription/scripts/openai_transcribe.py INPUT \
     --output OUTPUT.srt \
     --prompt "Ana Seahawk, Fiona Gardner, Shivambu, Water Magicians"
   ```

   `tools/whisper-transcribe` is the stable repo-level alias for the same
   client.
5. Validate that the SRT is non-empty, begins with a numbered cue, has monotonic
   timestamps, and reaches plausibly close to the media duration.
6. Treat speaker identity as unverified. Hosted Whisper produces timestamps but
   not reliable speaker names. Do not invent labels; mark them for review or
   identify them only from direct evidence.
7. Install the transcript into the requested archive only after validation.
   Preserve the source recording until the transcript is committed, pushed, and
   independently verified. Deletion always requires a separate explicit request.

## Credential boundary

The client reads `openai/api-key` from `gopass` inside the same Python process
that opens the HTTPS connection. It never places the key in an environment
variable, command argument, output, log, or temporary file. On Linux it marks
itself non-dumpable before reading the key. Do not replace this with `curl`
arguments, shell variables, exported environment variables, or a generated curl
config.

FFmpeg runs before credential retrieval and receives no secret. The client
splits long recordings into 10-minute audio-only chunks, transcodes each to a
private temporary MP3 sized below OpenAI's upload limit, and uploads it to the
fixed `api.openai.com` endpoint. It checkpoints each validated SRT part with
mode `0600`, resumes without repeating completed paid chunks, merges exact
timestamp offsets, and removes temporary audio on exit.

Use `--dry-run` to validate dependencies, duration, and upload size without
reading `gopass` or making an API request.

## Output boundary

Default to `whisper-1` with SRT because this workflow requires timestamps.
Do not silently substitute a plain-text model. Record the model and method in
archive metadata. Keep multi-person transcripts private and draft until consent,
speaker attribution, and sensitive-content review are complete.
