#!/usr/bin/env python3

for i in range(256):
    print("\033[48;5;"+str(i)+"m\033[38;5;15m"+ " %03d " % i, end='')
    print("\033[33;5;0m\033[38;5;"+str(i)+"m"+ " %03d " % i, end='')
    if ((i + 1)  % 16) == 0:
        print("\033[0m")

