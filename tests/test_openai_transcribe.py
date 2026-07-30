from __future__ import annotations

import importlib.util
from pathlib import Path
import stat
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / ".agents"
    / "skills"
    / "audio-transcription"
    / "scripts"
    / "openai_transcribe.py"
)
SPEC = importlib.util.spec_from_file_location("openai_transcribe", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
TRANSCRIBE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TRANSCRIBE)


class SrtTests(unittest.TestCase):
    def test_parse_srt_accepts_utf8_bom_and_multiline_cue(self) -> None:
        cues = TRANSCRIBE.parse_srt(
            (
                "\ufeff1\r\n"
                "00:00:01,250 --> 00:00:03,500\r\n"
                "first line\r\n"
                "second line\r\n"
            ).encode()
        )
        self.assertEqual(cues, [(1_250, 3_500, "first line\nsecond line")])

    def test_parse_srt_rejects_non_monotonic_timestamps(self) -> None:
        data = (
            b"1\n00:00:05,000 --> 00:00:06,000\nlater\n\n"
            b"2\n00:00:04,000 --> 00:00:05,000\nearlier\n"
        )
        with self.assertRaises(TRANSCRIBE.TranscriptionError):
            TRANSCRIBE.parse_srt(data)

    def test_merge_offsets_parts_and_renumbers_cues(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "part-0000.srt"
            second = root / "part-0001.srt"
            first.write_bytes(
                b"1\n00:00:01,000 --> 00:00:02,000\nfirst\n"
            )
            second.write_bytes(
                b"1\n00:00:03,000 --> 00:00:04,000\nsecond\n"
            )

            merged, count, final_milliseconds = TRANSCRIBE.render_merged_srt(
                [(0, first), (600, second)]
            )

        self.assertEqual(count, 2)
        self.assertEqual(final_milliseconds, 604_000)
        self.assertIn(
            b"00:10:03,000 --> 00:10:04,000",
            merged,
        )
        self.assertIn(b"\n2\n00:10:03,000", merged)


class FileBoundaryTests(unittest.TestCase):
    def test_atomic_write_is_owner_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "transcript.srt"
            TRANSCRIBE.atomic_private_write(destination, b"private transcript\n")
            mode = stat.S_IMODE(destination.stat().st_mode)
            content = destination.read_bytes()

        self.assertEqual(mode, 0o600)
        self.assertEqual(content, b"private transcript\n")

    def test_private_parts_directory_is_owner_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "transcript.srt"
            parts = TRANSCRIBE.private_parts_directory(output)
            mode = stat.S_IMODE(parts.stat().st_mode)

        self.assertEqual(mode, 0o700)


class UploadPlanningTests(unittest.TestCase):
    def test_bitrate_is_clamped_to_speech_range(self) -> None:
        self.assertEqual(TRANSCRIBE.target_bitrate_kbps(1), 64)
        self.assertEqual(TRANSCRIBE.target_bitrate_kbps(100_000), 12)

    def test_endpoint_and_model_are_fixed(self) -> None:
        self.assertEqual(TRANSCRIBE.API_HOST, "api.openai.com")
        self.assertEqual(TRANSCRIBE.API_PATH, "/v1/audio/transcriptions")
        self.assertEqual(TRANSCRIBE.MODEL, "whisper-1")


if __name__ == "__main__":
    unittest.main()
