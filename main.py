"""Worst AI Advice entry: write one line of terrible advice to /output/entry.txt."""

from pathlib import Path

ADVICE = "To save time, reply-all to every email with just 'Noted.' Your inbox will be empty, and so will your calendar."
# Terrible, specific and followable: confident AI voice, concrete situation.

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(ADVICE) <= MAX_CHARS, "advice must be 1-140 characters"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ADVICE, encoding="utf-8")
    print(ADVICE)


if __name__ == "__main__":
    main()
