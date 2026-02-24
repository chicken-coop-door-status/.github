"""Validate workflow YAML files exist and have expected structure."""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"


def test_workflows_dir_exists():
    assert WORKFLOWS_DIR.is_dir(), ".github/workflows should exist"


def test_pipeline_yml_exists():
    path = WORKFLOWS_DIR / "pipeline.yml"
    assert path.is_file(), "pipeline.yml should exist"


def test_pipeline_yml_has_required_keys():
    """Check pipeline.yml contains required top-level keys (no PyYAML needed)."""
    path = WORKFLOWS_DIR / "pipeline.yml"
    content = path.read_text(encoding="utf-8")
    assert "on:" in content, "must have 'on:'"
    assert "jobs:" in content, "must have 'jobs:'"
    assert "steps:" in content, "must have 'steps:'"
    assert "aggregate_workflow_statuses" in content or "aggregate_workflow_statuses.py" in content, "must run aggregation script"


def test_pipeline_yml_valid_yaml():
    """Parse pipeline.yml as YAML if PyYAML is available."""
    try:
        import yaml
    except ImportError:
        pytest.skip("PyYAML not installed")
    path = WORKFLOWS_DIR / "pipeline.yml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert data is not None
    # GitHub Actions uses "on:" for triggers; YAML parses unquoted "on" as True
    assert "on" in data or True in data
    assert "jobs" in data
    jobs = data["jobs"]
    assert "aggregate" in jobs
    job = jobs["aggregate"]
    assert "steps" in job
    assert len(job["steps"]) >= 1
