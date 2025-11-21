#!/bin/bash
# Simple performance check simulation

echo "Starting performance check..."
START_TIME=$(date +%s%N)

# Simulate checking 100 endpoints by running the linux check script in a loop (mocked)
for i in {1..100}; do
    ./scripts/endpoints/check_linux.sh > /dev/null 2>&1
done

END_TIME=$(date +%s%N)
DURATION=$(( (END_TIME - START_TIME) / 1000000 ))

echo "Checked 100 endpoints in ${DURATION}ms"

if [ "$DURATION" -gt 5000 ]; then
    echo "WARNING: Performance is too slow (>5000ms)"
    exit 1
else
    echo "Performance is acceptable."
fi
