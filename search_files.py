#!/usr/bin/env python3

import sys

for line in sys.stdin:
    f = open(line[:-1])
    lines = f.readlines()

    has_text = False
    for l in lines:
        if l.find(sys.argv[1]) >= 0:
            has_text = True
            break

    if has_text == True:
        print(line)

    f.close()
