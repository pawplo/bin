#!/usr/bin/env python3

import sys

for line in sys.stdin:
    sys.stdout.write(line)

if line[-1] != '\n':
   sys.stdout.write('\n')

