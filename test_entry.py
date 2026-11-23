import os
import subprocess
import sys
from pathlib import Path

OUTPUT_DIR = Path("/tmp/dadjout")


def main() -> None:
    env = dict(os.environ)
    env["MAKEFUN_OUTPUT_DIR"] = str(OUTPUT_DIR)

    subprocess.run(
        [sys.executable, "main.py"],
        cwd=Path(__file__).resolve().parent,
        env=env,
        check=True,
    )

    entry_file = OUTPUT_DIR / "entry.txt"
    assert entry_file.is_file(), "entry.txt was not written"

    text = entry_file.read_text(encoding="utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only white space"

    lines = text.splitlines()
    assert len(lines) == 1, "entry must be a single line"
    assert text == lines[0], "entry must not contain line breaks or padding"

    print("PASS")


if __name__ == "__main__":
    main()
