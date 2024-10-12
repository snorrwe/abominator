#!/usr/bin/env bash

set -euo pipefail
set -x

file=$(mktemp --suffix .c)
echo Hello, World | python3 abominator.py > $file
gcc $file -o out
./out
