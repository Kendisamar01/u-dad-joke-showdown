"""Verify main.py produces an exact, unpadded copy of entry.txt."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def check():
    expected = (ROOT / "entry.txt").read_text(encoding="utf-8").strip()
    assert 1 <= len(expected) <= 200
    assert "\n" not in expected and "\r" not in expected

    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ)
        env["MAKEFUN_OUTPUT_DIR"] = tmp
        completed = subprocess.run(
            [sys.executable, str(ROOT / "main.py")],
            cwd=str(ROOT),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        assert completed.returncode == 0, completed.stderr.decode("utf-8", "replace")
        produced = (Path(tmp) / "entry.txt").read_text(encoding="utf-8")

    assert "\n" not in produced and "\r" not in produced
    assert produced == produced.strip()
    assert 1 <= len(produced) <= 200
    assert produced == expected


if __name__ == "__main__":
    check()
    print("PASS")
