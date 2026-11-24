"""Copy the entry text byte-for-byte into the requested output directory."""

import os
from pathlib import Path

# Source bytes are copied unchanged except for a single trailing newline.
SOURCE = Path(__file__).resolve().with_name("entry.txt")
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", Path(__file__).resolve().parent / "out"))


def main():
    data = SOURCE.read_bytes()
    if data.endswith(b"\r\n"):
        data = data[:-2]
    elif data.endswith(b"\n") or data.endswith(b"\r"):
        data = data[:-1]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
