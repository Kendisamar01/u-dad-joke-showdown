import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.txt"


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8").strip()
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
