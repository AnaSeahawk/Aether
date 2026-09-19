"""Exercise the metadata consumer using dummy values and a mocked store."""

import importlib.util
import io
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/passwords/scripts/append_login.py"
SPEC = importlib.util.spec_from_file_location("append_login", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class LoginMetadataTests(unittest.TestCase):
    def test_frames_login_and_suppresses_consumer_output(self):
        with patch.object(MODULE.subprocess, "run") as run:
            run.return_value.returncode = 0
            self.assertEqual(MODULE.append_login("example.test/login", io.BytesIO(b"dummy@example.test\n")), 0)
        run.assert_called_once_with(
            ["gopass", "insert", "--append", "example.test/login"],
            input=b"login: dummy@example.test\n",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )

    def test_rejects_empty_multiline_control_and_oversized_input(self):
        for value in (b"", b"\n", b"dummy\n\n", b"dummy\nlogin: injected", b"dummy\rvalue", b"dummy\x00", b"x" * 4097):
            with self.subTest(value_length=len(value)), patch.object(MODULE.subprocess, "run") as run:
                self.assertEqual(MODULE.append_login("example.test/login", io.BytesIO(value)), 64)
                run.assert_not_called()

    def test_rejects_option_or_invalid_entry(self):
        for entry in ("", "--force", "bad\nentry"):
            with self.subTest(entry=entry), patch.object(MODULE.subprocess, "run") as run:
                self.assertEqual(MODULE.append_login(entry, io.BytesIO(b"dummy")), 64)
                run.assert_not_called()

    def test_store_failure_returns_generic_failure(self):
        with patch.object(MODULE.subprocess, "run") as run:
            run.return_value.returncode = 7
            self.assertEqual(MODULE.append_login("example.test/login", io.BytesIO(b"dummy")), 1)

    def test_missing_store_returns_generic_failure(self):
        with patch.object(MODULE.subprocess, "run", side_effect=FileNotFoundError):
            self.assertEqual(MODULE.append_login("example.test/login", io.BytesIO(b"dummy")), 1)


if __name__ == "__main__":
    unittest.main()
