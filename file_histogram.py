#!/usr/bin/env python3
import sys

data = sys.stdin.buffer.read()

a = []
for i in range(256):
    a.insert(i, 0)

for i in range(len(data)):
    a[data[i]] = a[data[i]] + 1

#print(a)

for i in range(len(a)):
    if a[i] != 0:
        print(str(a[i])+" ["+str(i)+"]")
