#!/bin/bash
set -e

echo "Running lint..."
./scripts-dev/lint.sh

echo "Running unit tests..."
python3 -m pytest tests/unit

echo "Running integration tests..."
python3 -m pytest tests/integration

echo "All tests passed."
