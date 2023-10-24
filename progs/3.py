#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input("Enter value of n (1 <= n <= 4): "))
    if n < 1 or n > 4:
        print("Illegal value of n")
        exit(1)

    start = 1 * 10 ** (n - 1)
    end = 10 ** n
    result = sum(range(start, end))

    print(f"Sum of {n}-digit numbers is {result}")
