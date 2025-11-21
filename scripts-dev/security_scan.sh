#!/bin/bash
set -e

echo "Running bandit..."
python3 -m bandit -r ai/src cli -c pyproject.toml

echo "Running pip-audit..."
pip-audit

echo "Security scan complete."
