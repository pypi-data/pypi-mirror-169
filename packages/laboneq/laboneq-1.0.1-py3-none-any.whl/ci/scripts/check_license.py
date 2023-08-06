#!/usr/bin/env python
""" Utility to check for presence of the correct license boilerplate. """
import argparse
import re
import sys
from datetime import datetime
from difflib import unified_diff
from pathlib import Path

# Boilerplate consists of copyright, license identifier, and one or more empty
# lines.

SEARCH = r"""# Copyright (?P<year>[0-9]+) Zurich Instruments AG
# SPDX-License-Identifier: Apache-2.0(\n\n)?(?P<newlines>\n*)"""

REPLACEMENT = r"""# Copyright \g<year> Zurich Instruments AG
# SPDX-License-Identifier: Apache-2.0

\g<newlines>"""

SEARCH_RE = re.compile(SEARCH)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Root path to scan")
    parser.add_argument(
        "--fixup", default=False, action="store_true", help="Fix up all issues",
    )

    args = parser.parse_args()

    root_directory = Path(args.path)
    modification_count = 0

    for path in root_directory.glob("**/*.py"):
        original_text = path.read_text()
        (modified_text, count) = SEARCH_RE.subn(REPLACEMENT, original_text)

        if count == 0:
            print("\n!! License missing:", path)
            license_header = REPLACEMENT.replace("\\g<year>", f"{datetime.now().year}")
            license_header = license_header.replace("\n\\g<newlines>", "\n")
            modified_text = license_header + modified_text

        # Cleanup excessive newlines at end of file.
        if modified_text[-1] == modified_text[-2] == modified_text[-3] == "\n":
            modified_text = modified_text[:-2]

        if modified_text == original_text:
            continue

        if args.fixup:
            path.write_text(modified_text)
            print("!! Modified:", path)
        else:
            print("!! Modification needed:", path)

        modification_count += 1

        sys.stdout.writelines(
            unified_diff(
                original_text.splitlines(keepends=True),
                modified_text.splitlines(keepends=True),
                fromfile=str(path),
                tofile=f"{str(path)} (modified)",
            )
        )

    if modification_count != 0:
        if args.fixup:
            print(f"\n💄 {modification_count} file(s) were fixed up.")
        else:
            print(f"\n🧨 {modification_count} file(s) require changes.")
        sys.exit(1)

    print("All good! 🥳")


if __name__ == "__main__":
    main()
