#!/bin/bash

success=1
for f in test-data/*.fa; do
    if ! cmp -s <(./fastarecs $f) $f-fasta-recs-expected; then
        echo "./fastarecs $f did not produce the expected output"
        diff <(./fastarecs $f) $f-fasta-recs-expected
        echo
        success=0
    fi
done

if (( success == 1 )); then
    echo "Success."
else
    exit 2
fi
