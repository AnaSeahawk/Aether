#!/usr/bin/env python3
"""Append login metadata from stdin without displaying the value."""

import subprocess
import sys
from typing import BinaryIO


def append_login(entry: str, source: BinaryIO) -> int:
    if not entry or entry.startswith("-") or any(ord(c) < 32 for c in entry):
        return 64
    raw = source.read(4097)
    login = raw.removesuffix(b"\n").removesuffix(b"\r")
    if len(raw) > 4096 or not login or any(c < 32 or c == 127 for c in login):
        return 64
    try:
        result = subprocess.run(
            ["gopass", "insert", "--append", entry],
            input=b"login: " + login + b"\n",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        return 1
    return 0 if result.returncode == 0 else 1


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: append_login.py <existing-gopass-entry>", file=sys.stderr)
        return 64
    status = append_login(sys.argv[1], sys.stdin.buffer)
    if status:
        print("Login metadata was not stored; check input and store access.", file=sys.stderr)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
