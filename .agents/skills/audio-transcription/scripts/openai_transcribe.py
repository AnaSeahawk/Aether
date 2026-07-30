#!/usr/bin/env python3
"""Create a timed SRT with OpenAI Whisper without exposing the API key."""

from __future__ import annotations

import argparse
import ctypes
import http.client
import json
import math
import os
from pathlib import Path
import re
import secrets
import shutil
import socket
import subprocess
import sys
import tempfile


API_HOST = "api.openai.com"
API_PATH = "/v1/audio/transcriptions"
GOPASS_ENTRY = "openai/api-key"
MODEL = "whisper-1"
MAX_UPLOAD_BYTES = 25 * 1024 * 1024
TARGET_UPLOAD_BYTES = 22 * 1024 * 1024
DEFAULT_PROMPT = (
    "Transcribe spoken English. Preserve names, product names, and acronyms "
    "exactly when spoken. Do not translate."
)
DEFAULT_CHUNK_SECONDS = 600
SRT_TIMESTAMP = re.compile(
    r"^(?P<sh>\d+):(?P<sm>\d{2}):(?P<ss>\d{2}),(?P<sms>\d{3})"
    r"\s+-->\s+"
    r"(?P<eh>\d+):(?P<em>\d{2}):(?P<es>\d{2}),(?P<ems>\d{3})$"
)


class TranscriptionError(RuntimeError):
    """Expected, user-facing transcription failure."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcribe one audio/video file to timed SRT with OpenAI Whisper."
    )
    parser.add_argument("input", type=Path, help="Audio or video file to transcribe")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output SRT path (default: INPUT with .srt suffix)",
    )
    parser.add_argument("--language", default="en", help="ISO-639-1 language hint")
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="Vocabulary and spelling guidance for Whisper",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Prepare and size audio without reading gopass or calling OpenAI",
    )
    parser.add_argument(
        "--chunk-seconds",
        type=int,
        default=DEFAULT_CHUNK_SECONDS,
        help="Hosted chunk duration for long recordings (default: 600)",
    )
    return parser.parse_args()


def require_program(name: str) -> str:
    path = shutil.which(name)
    if path is None:
        raise TranscriptionError(f"required program is not on PATH: {name}")
    return path


def media_duration(ffprobe: str, source: Path) -> float:
    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            os.fspath(source),
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        raise TranscriptionError("ffprobe could not read the input media")
    try:
        duration = float(result.stdout.strip())
    except ValueError as error:
        raise TranscriptionError("ffprobe did not return a valid duration") from error
    if not math.isfinite(duration) or duration <= 0:
        raise TranscriptionError("input media has no positive duration")
    return duration


def target_bitrate_kbps(duration: float) -> int:
    calculated = int((TARGET_UPLOAD_BYTES * 8) / duration / 1000)
    return max(12, min(64, calculated))


def prepare_audio(
    ffmpeg: str,
    source: Path,
    destination: Path,
    bitrate: int,
    start_seconds: int = 0,
    duration_seconds: float | None = None,
) -> int:
    timing = ["-ss", str(start_seconds)]
    if duration_seconds is not None:
        timing.extend(["-t", f"{duration_seconds:.3f}"])
    result = subprocess.run(
        [
            ffmpeg,
            "-nostdin",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            *timing,
            "-i",
            os.fspath(source),
            "-map",
            "0:a:0",
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "libmp3lame",
            "-b:a",
            f"{bitrate}k",
            os.fspath(destination),
        ],
        check=False,
    )
    if result.returncode != 0:
        raise TranscriptionError("ffmpeg could not extract and compress the audio stream")
    size = destination.stat().st_size
    if size > MAX_UPLOAD_BYTES:
        raise TranscriptionError(
            f"compressed audio is {size} bytes, above OpenAI's 25 MiB limit; "
            "split the recording and transcribe each part"
        )
    return size


def make_process_non_dumpable() -> None:
    if not sys.platform.startswith("linux"):
        raise TranscriptionError(
            "secure credential retrieval is currently implemented only on Linux"
        )
    libc = ctypes.CDLL(None, use_errno=True)
    pr_set_dumpable = 4
    if libc.prctl(pr_set_dumpable, 0, 0, 0, 0) != 0:
        errno = ctypes.get_errno()
        raise TranscriptionError(
            f"could not disable process dumps before credential retrieval (errno {errno})"
        )


def read_api_key(gopass: str) -> bytearray:
    process = subprocess.Popen(
        [gopass, "show", "-o", GOPASS_ENTRY],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        close_fds=True,
    )
    stdout, _ = process.communicate()
    if process.returncode != 0:
        raise TranscriptionError(
            f"gopass could not read the OpenAI credential at {GOPASS_ENTRY}"
        )
    key = bytearray(stdout.strip())
    if not key:
        raise TranscriptionError(
            f"gopass returned an empty credential at {GOPASS_ENTRY}"
        )
    if b"\r" in key or b"\n" in key:
        raise TranscriptionError("OpenAI credential contains an unexpected newline")
    return key


def form_field(boundary: str, name: str, value: str) -> bytes:
    return (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{name}"\r\n'
        "\r\n"
        f"{value}\r\n"
    ).encode("utf-8")


def upload(audio: Path, language: str, prompt: str, gopass: str) -> bytes:
    boundary = f"codex-audio-{secrets.token_hex(18)}"
    fields = [
        form_field(boundary, "model", MODEL),
        form_field(boundary, "response_format", "srt"),
    ]
    if language:
        fields.append(form_field(boundary, "language", language))
    if prompt:
        fields.append(form_field(boundary, "prompt", prompt))
    file_prefix = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="file"; filename="audio.mp3"\r\n'
        "Content-Type: audio/mpeg\r\n"
        "\r\n"
    ).encode("utf-8")
    closing = f"\r\n--{boundary}--\r\n".encode("ascii")
    content_length = (
        sum(len(field) for field in fields)
        + len(file_prefix)
        + audio.stat().st_size
        + len(closing)
    )

    make_process_non_dumpable()
    key = read_api_key(gopass)
    connection: http.client.HTTPSConnection | None = None
    try:
        authorization = "Bearer " + key.decode("utf-8")
        connection = http.client.HTTPSConnection(API_HOST, timeout=1800)
        connection.putrequest("POST", API_PATH)
        connection.putheader("Authorization", authorization)
        connection.putheader("Content-Type", f"multipart/form-data; boundary={boundary}")
        connection.putheader("Content-Length", str(content_length))
        connection.endheaders()
        del authorization
        for index in range(len(key)):
            key[index] = 0
        for field in fields:
            connection.send(field)
        connection.send(file_prefix)
        with audio.open("rb") as handle:
            while chunk := handle.read(1024 * 1024):
                connection.send(chunk)
        connection.send(closing)
        try:
            response = connection.getresponse()
            body = response.read()
        except (TimeoutError, socket.timeout, OSError, http.client.HTTPException) as error:
            raise TranscriptionError(
                f"OpenAI request did not complete: {type(error).__name__}"
            ) from error
    finally:
        for index in range(len(key)):
            key[index] = 0
        if connection is not None:
            connection.close()

    if response.status != 200:
        message = f"OpenAI returned HTTP {response.status}"
        try:
            parsed = json.loads(body)
            detail = parsed.get("error", {}).get("message")
            if detail:
                message += f": {detail}"
        except (UnicodeDecodeError, json.JSONDecodeError, AttributeError):
            pass
        raise TranscriptionError(message)
    if not body.strip():
        raise TranscriptionError("OpenAI returned an empty transcript")
    return body


def atomic_private_write(destination: Path, data: bytes) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.",
        dir=destination.parent,
    )
    temporary = Path(temporary_name)
    try:
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def timestamp_milliseconds(match: re.Match[str], prefix: str) -> int:
    return (
        int(match[f"{prefix}h"]) * 3_600_000
        + int(match[f"{prefix}m"]) * 60_000
        + int(match[f"{prefix}s"]) * 1_000
        + int(match[f"{prefix}ms"])
    )


def format_timestamp(milliseconds: int) -> str:
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1_000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def parse_srt(data: bytes) -> list[tuple[int, int, str]]:
    try:
        text = data.decode("utf-8-sig").replace("\r\n", "\n").strip()
    except UnicodeDecodeError as error:
        raise TranscriptionError("OpenAI returned non-UTF-8 SRT") from error
    cues: list[tuple[int, int, str]] = []
    for block in re.split(r"\n[ \t]*\n+", text):
        lines = block.splitlines()
        timing_index = next(
            (index for index, line in enumerate(lines) if "-->" in line),
            None,
        )
        if timing_index is None:
            continue
        match = SRT_TIMESTAMP.fullmatch(lines[timing_index].strip())
        if match is None:
            raise TranscriptionError(
                f"OpenAI returned an invalid SRT timestamp: {lines[timing_index]}"
            )
        start = timestamp_milliseconds(match, "s")
        end = timestamp_milliseconds(match, "e")
        content = "\n".join(lines[timing_index + 1 :]).strip()
        if end < start or not content:
            raise TranscriptionError("OpenAI returned an invalid or empty SRT cue")
        if cues and start < cues[-1][0]:
            raise TranscriptionError("OpenAI returned non-monotonic SRT timestamps")
        cues.append((start, end, content))
    if not cues:
        raise TranscriptionError("OpenAI returned no valid SRT cues")
    return cues


def render_merged_srt(
    parts: list[tuple[int, Path]],
) -> tuple[bytes, int, int]:
    merged: list[tuple[int, int, str]] = []
    for offset_seconds, path in parts:
        offset = offset_seconds * 1_000
        for start, end, content in parse_srt(path.read_bytes()):
            merged.append((start + offset, end + offset, content))
    lines: list[str] = []
    for index, (start, end, content) in enumerate(merged, start=1):
        lines.extend(
            [
                str(index),
                f"{format_timestamp(start)} --> {format_timestamp(end)}",
                content,
                "",
            ]
        )
    return "\n".join(lines).encode("utf-8"), len(merged), merged[-1][1]


def private_parts_directory(output: Path) -> Path:
    directory = output.parent / f".{output.name}.parts"
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    directory.chmod(0o700)
    return directory


def main() -> int:
    args = parse_args()
    source = args.input.expanduser().resolve()
    if not source.is_file():
        raise TranscriptionError(f"input file not found: {source}")
    if args.chunk_seconds < 60:
        raise TranscriptionError("--chunk-seconds must be at least 60")
    output = (
        args.output.expanduser().resolve()
        if args.output
        else source.with_suffix(".srt")
    )
    ffmpeg = require_program("ffmpeg")
    ffprobe = require_program("ffprobe")
    gopass = require_program("gopass")

    duration = media_duration(ffprobe, source)
    chunk_count = max(1, math.ceil(duration / args.chunk_seconds))
    print(
        f"openai-transcribe: {duration:.1f}s in {chunk_count} hosted chunk(s)",
        file=sys.stderr,
    )
    parts_directory = private_parts_directory(output)
    completed_parts: list[tuple[int, Path]] = []
    for index in range(chunk_count):
        start = index * args.chunk_seconds
        chunk_duration = min(args.chunk_seconds, duration - start)
        part_output = parts_directory / f"part-{index:04d}.srt"
        if part_output.is_file():
            parse_srt(part_output.read_bytes())
            print(
                f"openai-transcribe: part {index + 1}/{chunk_count} already complete",
                file=sys.stderr,
            )
            completed_parts.append((start, part_output))
            continue
        bitrate = target_bitrate_kbps(chunk_duration)
        with tempfile.TemporaryDirectory(prefix="openai-transcribe.") as directory:
            audio = Path(directory) / f"part-{index:04d}.mp3"
            size = prepare_audio(
                ffmpeg,
                source,
                audio,
                bitrate,
                start_seconds=start,
                duration_seconds=chunk_duration,
            )
            print(
                f"openai-transcribe: part {index + 1}/{chunk_count} "
                f"prepared ({size} bytes at {bitrate} kbps)",
                file=sys.stderr,
            )
            if args.dry_run:
                continue
            print(
                f"openai-transcribe: part {index + 1}/{chunk_count} "
                f"uploading to OpenAI ({MODEL})",
                file=sys.stderr,
            )
            transcript = upload(audio, args.language, args.prompt, gopass)
        parse_srt(transcript)
        atomic_private_write(part_output, transcript)
        completed_parts.append((start, part_output))

    if args.dry_run:
        print(
            "openai-transcribe: dry run complete; gopass was not read and no API request was made",
            file=sys.stderr,
        )
        return 0

    merged, cue_count, final_milliseconds = render_merged_srt(completed_parts)
    atomic_private_write(output, merged)
    print(f"openai-transcribe: wrote {output}", file=sys.stderr)
    print(
        f"openai-transcribe: validated {cue_count} cues through "
        f"{format_timestamp(final_milliseconds)}",
        file=sys.stderr,
    )
    print(output)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TranscriptionError as error:
        print(f"openai-transcribe: {error}", file=sys.stderr)
        raise SystemExit(1)
