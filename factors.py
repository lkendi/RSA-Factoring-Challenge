#!/usr/bin/python3
import sys


def factorize(num):
    for i in range(2, num):
        if (num % i == 0):
            return i, num//i
    return None, None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for line in file:
            n = int(line.strip())
            p, q = factorize(n)
            print(f"{n}={p}*{q}")
