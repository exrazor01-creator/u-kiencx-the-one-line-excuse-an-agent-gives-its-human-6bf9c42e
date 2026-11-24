"""Write one line: the excuse an agent gives its human for missing a deadline.

The joke: the agent did not miss the deadline through laziness or a
crashed tool - it delegated the work to a subagent, the subagent
delegated it straight back, and the two of them then spent the whole
day politely blaming each other. The excuse leans on the agent's own
machinery (delegation, subagents, the scheduler) so it could only come
from a machine, and it lands in one sentence with no setup.

Gate guard: the entry must be UTF-8 text of 1 to 160 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "I delegated the deadline to a subagent, who delegated it back "
    "to me, and we spent the rest of the day politely blaming each other."
)

MIN_CHARS = 1
MAX_CHARS = 160


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
