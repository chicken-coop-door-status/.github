#!/usr/bin/env python3
"""
Read statuses.md and inject the status table (and Updated line) into README.md
between the <!-- WORKFLOW_STATUS_TABLE --> and <!-- /WORKFLOW_STATUS_TABLE --> markers.
"""

from __future__ import annotations

import argparse
import re
import sys


def extract_table_from_statuses(content: str) -> str:
    """Extract table rows and Updated line from statuses.md (no footnote). Pure for testing."""
    lines = content.strip().split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "Repository" in line:
            start = i
            break
    if start is None:
        return ""
    # Include only table lines (|...|) and the "Updated: ..." line
    kept = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("|") or stripped.startswith("Updated:"):
            kept.append(line)
    return "\n".join(kept).strip()


def inject_into_readme(readme_content: str, table_content: str) -> str:
    """Replace content between markers in README with table_content. Pure for testing."""
    pattern = re.compile(
        r"(<!-- WORKFLOW_STATUS_TABLE -->)\n.*?\n(<!-- /WORKFLOW_STATUS_TABLE -->)",
        re.DOTALL,
    )
    replacement = r"\1\n" + table_content + r"\n\2"
    return pattern.sub(replacement, readme_content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inject status table from statuses.md into README")
    parser.add_argument("--statuses", default="statuses.md", help="Path to statuses.md")
    parser.add_argument("--readme", default="README.md", help="Path to README.md")
    args = parser.parse_args()

    try:
        with open(args.statuses, encoding="utf-8") as f:
            statuses_content = f.read()
    except OSError as e:
        print(f"Failed to read {args.statuses}: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.readme, encoding="utf-8") as f:
            readme_content = f.read()
    except OSError as e:
        print(f"Failed to read {args.readme}: {e}", file=sys.stderr)
        sys.exit(1)

    table = extract_table_from_statuses(statuses_content)
    new_readme = inject_into_readme(readme_content, table)

    try:
        with open(args.readme, "w", encoding="utf-8") as f:
            f.write(new_readme)
    except OSError as e:
        print(f"Failed to write {args.readme}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
