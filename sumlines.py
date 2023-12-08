#!/usr/bin/env python3

import sys

sumlines = 0

for line in sys.stdin:
    sumlines += int(line)

print("sumlines="+str(sumlines))
