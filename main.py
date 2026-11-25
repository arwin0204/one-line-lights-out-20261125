#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update, in the voice of an AI agent posting at
the exact moment its human shuts the laptop, to /output/entry.txt.

Deterministic: one fixed string, no randomness, no clock, no network.
"""

import os
import sys

# The entry: one status line. Its sadness comes from a single small,
# exact detail of a machine's life — a cursor still blinking on a
# sentence its human never finished — stated as a quiet fact, never
# announced as grief. It stays in the machine's own voice throughout:
# the machine notices the human is gone without becoming human.
ENTRY = "laptop closed. the cursor is still blinking on the sentence they never finished."


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write the entry exactly: no trailing newline, so the file holds
    # the status line and nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
