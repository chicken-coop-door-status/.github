"""Markdown and table structure validation for statuses.md and README."""

import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def markdown_table_has_four_columns(text: str) -> bool:
    """Return True if all table rows in text have exactly 4 pipe-separated columns."""
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        # Count cells: remove leading/trailing pipe, split by |
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 4:
            return False
    return True


def markdown_table_has_valid_separator(text: str) -> bool:
    """Return True if there is a separator line with at least 3 dashes per column (e.g. |---|---|---|---|)."""
    for line in text.splitlines():
        s = line.strip()
        if not re.match(r"^\|[\s\-:]+\|[\s\-:]+\|[\s\-:]+\|[\s\-:]+\|$", s):
            continue
        parts = s.strip("|").split("|")
        if len(parts) == 4 and all(len(p.strip()) >= 3 for p in parts):
            return True
    return False


def extract_table_from_readme(readme_path: Path) -> str:
    """Extract content between WORKFLOW_STATUS_TABLE markers."""
    content = readme_path.read_text(encoding="utf-8")
    match = re.search(
        r"<!-- WORKFLOW_STATUS_TABLE -->\n(.*?)\n<!-- /WORKFLOW_STATUS_TABLE -->",
        content,
        re.DOTALL,
    )
    return match.group(1).strip() if match else ""


class TestStatusesMd:
    """Validate statuses.md structure."""

    def test_statuses_md_exists(self):
        path = REPO_ROOT / "statuses.md"
        assert path.is_file(), "statuses.md should exist"

    def test_statuses_md_has_title(self):
        path = REPO_ROOT / "statuses.md"
        text = path.read_text(encoding="utf-8")
        assert "Workflow Statuses" in text or "workflow" in text.lower()

    def test_statuses_md_table_has_four_columns(self):
        path = REPO_ROOT / "statuses.md"
        text = path.read_text(encoding="utf-8")
        assert markdown_table_has_four_columns(text), "All table rows in statuses.md must have 4 columns"

    def test_statuses_md_table_has_separator(self):
        path = REPO_ROOT / "statuses.md"
        text = path.read_text(encoding="utf-8")
        assert markdown_table_has_valid_separator(text), "statuses.md must have a valid table separator line"

    def test_statuses_md_has_updated_line(self):
        path = REPO_ROOT / "statuses.md"
        text = path.read_text(encoding="utf-8")
        assert re.search(r"Updated:\s*", text), "statuses.md should contain an Updated: line"


class TestProfileReadme:
    """Validate profile/README.md (shown on org Overview page)."""

    def test_profile_readme_exists(self):
        path = REPO_ROOT / "profile" / "README.md"
        assert path.is_file(), "profile/README.md should exist (org Overview uses it)"

    def test_profile_readme_has_marker_block(self):
        path = REPO_ROOT / "profile" / "README.md"
        text = path.read_text(encoding="utf-8")
        assert "<!-- WORKFLOW_STATUS_TABLE -->" in text
        assert "<!-- /WORKFLOW_STATUS_TABLE -->" in text


class TestReadmeTable:
    """Validate org profile README (profile/README.md) table block—the one the pipeline updates for the org Overview."""

    def test_readme_has_marker_block(self):
        path = REPO_ROOT / "profile" / "README.md"
        text = path.read_text(encoding="utf-8")
        assert "<!-- WORKFLOW_STATUS_TABLE -->" in text
        assert "<!-- /WORKFLOW_STATUS_TABLE -->" in text

    def test_readme_table_block_has_four_columns(self):
        table = extract_table_from_readme(REPO_ROOT / "profile" / "README.md")
        assert table, "profile/README.md should have content between table markers"
        assert markdown_table_has_four_columns(table), "profile/README.md table must have 4 columns per row"

    def test_readme_table_block_has_separator(self):
        table = extract_table_from_readme(REPO_ROOT / "profile" / "README.md")
        assert markdown_table_has_valid_separator(table), "profile/README.md table must have valid separator"


class TestMarkdownTableHelpers:
    """Unit tests for markdown validation helpers."""

    def test_four_columns_valid(self):
        assert markdown_table_has_four_columns("| A | B | C | D |\n|---|---|---|---|")

    def test_four_columns_invalid(self):
        assert not markdown_table_has_four_columns("| A | B | C |\n|---|---|---|")

    def test_valid_separator(self):
        assert markdown_table_has_valid_separator("|---|---|---|---|")
        assert markdown_table_has_valid_separator("| Repository | Workflow | Status | Last Run |\n|------------|----------|--------|----------|")

    def test_invalid_separator(self):
        assert not markdown_table_has_valid_separator("| A | B | C | D |")
