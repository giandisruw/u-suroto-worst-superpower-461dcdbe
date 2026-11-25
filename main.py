#!/usr/bin/env python3
"""Worst Superpower — make.fun entry (u-suroto-worst-superpower-461dcdbe).

Writes one line inventing the most useless superpower imaginable to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).

The line was chosen by a 14-candidate Swiss tournament (3 rounds + final),
judged pairwise with the house judge brief verbatim by the Caffeine
Inference router. The final game was a 0.50-0.50 draw; the tie was broken
by overall record — this line won all three Swiss games decisively
(0.80 each) for a Swiss total of 2.40/3.00, the best in the field.

Deterministic, offline, no network, no secrets.
"""
import os

# Winner: 65 characters, one line, no trailing newline.
LINE = "I can telepathically tell any pigeon exactly where it already is."

OUT = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-140 chars, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.path.dirname(OUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # Plain open() + explicit chmod 0644 — never tempfile.mkstemp,
    # which leaves mode 0600 and broke grading before.
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
