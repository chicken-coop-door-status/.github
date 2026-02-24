"""Unit tests for aggregate_workflow_statuses pure helpers."""

from datetime import datetime, timezone

import pytest

# Import from script in repo root
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.aggregate_workflow_statuses import (
    conclusion_to_status,
    row_from_run,
    table_from_rows,
)


def test_conclusion_to_status_success():
    assert conclusion_to_status("success") == "✅ Passed"


def test_conclusion_to_status_failure():
    assert conclusion_to_status("failure") == "❌ Failed"


def test_conclusion_to_status_cancelled():
    assert conclusion_to_status("cancelled") == "❌ Failed"


def test_conclusion_to_status_none():
    assert conclusion_to_status(None) == "⏳ Running"


def test_conclusion_to_status_other():
    assert conclusion_to_status("skipped") == "❓ skipped"


def test_row_from_run():
    row = row_from_run(
        "my-repo",
        "CI",
        "success",
        datetime(2025, 2, 24, 12, 0, 0, tzinfo=timezone.utc),
    )
    assert "| my-repo | CI | ✅ Passed | 2025-02-24 12:00 |" == row


def test_row_from_run_no_date():
    row = row_from_run("r", "W", None, None)
    assert "| r | W | ⏳ Running | — |" == row


def test_table_from_rows_empty():
    out = table_from_rows([], "2025-02-24 12:00:00 UTC")
    assert "# Workflow Statuses Across Organization" in out
    assert "| Repository | Workflow | Status | Last Run |" in out
    assert "Updated: 2025-02-24 12:00:00 UTC" in out


def test_table_from_rows_with_data():
    rows = ["| repo1 | CI | ✅ Passed | 2025-02-24 |"]
    out = table_from_rows(rows, "2025-02-24 12:00:00 UTC")
    assert "| repo1 | CI | ✅ Passed | 2025-02-24 |" in out
