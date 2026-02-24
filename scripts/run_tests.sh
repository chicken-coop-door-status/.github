#!/usr/bin/env bash
# Single entry point for tests and checks in this repo.
set -e
cd "$(dirname "$0")/.."
if command -v pytest >/dev/null 2>&1; then
  pytest tests/ -v
elif command -v python3 >/dev/null 2>&1; then
  python3 -m pytest tests/ -v
else
  python -m pytest tests/ -v
fi
