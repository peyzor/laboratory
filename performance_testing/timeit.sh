#!/bin/bash
SETUP="
import random
def my_sort(x):
    return sorted(x)

def my_reversed_sort(x):
    return sorted(x, reverse=True)

x = [i for i in range(100, 10_000, 3)]
"

#SETUP2="
#from itertools import chain
#x = range(10_000)
#y = range(10_000)
#"

echo append impl:
python -m timeit -s "$SETUP" "random.shuffle(x)" "my_sort(x)"

#echo chain iterator impl:
#python -m timeit -s "$SETUP2" "sum(chain(x, y))"
