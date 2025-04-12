#!/bin/bash
SETUP="
x = range(10_000)
y = range(10_000)
"

SETUP2="
from itertools import chain
x = range(10_000)
y = range(10_000)
"

echo append impl:
python -m timeit -s "$SETUP" "sum(list(x) + list(y))"

echo chain iterator impl:
python -m timeit -s "$SETUP2" "sum(chain(x, y))"
