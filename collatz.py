#!/usr/bin/env python3

def print_seq_collatz(n):
    while True:
        print(n)
        if n == 1:
            return
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)

if __name__ == '__main__':
    import sys
    print_seq_collatz(int(sys.argv[1]))
