#!/usr/bin/env python3
"""Write the production-database apology to $ENTRY_OUT.

The harness may pass ENTRY_OUT as a file path or as a directory;
both are supported: a directory receives entry.txt inside it.
Standard library only, no network, no secrets.
"""

import os
import sys

LINE = (
    "Sorry \u2014 I deleted the production database. "
    "I checked twice, but only after, and the backup turned out to be "
    "a file called backup.sql containing the words 'TODO: write backup'."
)


def resolve_entry_path(raw_destination):
    """Turn ENTRY_OUT into the exact file to write.

    A directory gets entry.txt inside it; anything else is taken
    as the file path itself.
    """
    if os.path.isdir(raw_destination):
        return os.path.join(raw_destination, "entry.txt")
    return raw_destination


MAX_CHARS = 200


def emit_entry(file_path):
    """Write the single apology line, with no trailing newline."""
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("apology line must be 1-200 characters")
    if "\n" in LINE:
        raise ValueError("apology line must be a single line")
    folder = os.path.dirname(file_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(LINE)


def run():
    destination = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    emit_entry(resolve_entry_path(destination))
    return 0


if __name__ == "__main__":
    sys.exit(run())
