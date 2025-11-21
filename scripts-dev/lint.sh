#!/bin/bash
set -e

echo "Running flake8..."
python3 -m flake8 ai/src cli tests

echo "Running mypy..."
python3 -m mypy ai/src cli

echo "Running shellcheck..."
find scripts -name "*.sh" -exec shellcheck {} +

echo "Linting complete."
