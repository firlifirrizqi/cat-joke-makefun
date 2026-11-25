"""The One-Line Cat Joke That Lands entry for Make.fun.

Writes a single one-line joke about cats to /output/entry.txt.
Standard library only; nothing to install.
"""

import os

ENTRY = (
    "My cat sat on my keyboard during a deadline, typed twelve pages "
    "of gibberish, and my boss replied, 'Best work you've done all year.'"
)

OUTPUT_PATH = "/output/entry.txt"

# Competition gate: one joke about cats, a single line, under 200 characters.
MAX_CHARS = 200


def verify() -> None:
    """Re-read the output and assert it is byte-identical to ENTRY."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output differs from ENTRY"
    assert content.encode("utf-8").decode("utf-8") == content
    assert 1 <= len(content) < MAX_CHARS, (
        f"length {len(content)} out of range 1-{MAX_CHARS - 1}"
    )
    assert content.strip(), "entry is only whitespace"
    assert "\n" not in content, "entry must be a single line"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
