#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

EPS = 1e-10

if __name__ == "__main__":
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x")
        exit(1)

    a = 1
    S, n = a, 1

    while math.fabs(a) > EPS:
        a *= (-1 * x ** 2 * (4 * n + 1)) / (8 * n ** 2 + 18 * n + 10);
        S += a
        n += 1

    print(f"C(x) = {S}")
