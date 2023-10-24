#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input("Age? (>100): "))
    if n < 100:
        print("Illegal value of n")
        exit(1)

    if n % 10 == 1 and n % 100 != 11:
        print(f"Мне {n} год")
    elif n % 10 in (2, 3, 4) and (n % 100 < 10 or n % 100 > 20):
        print(f"Мне {n} года")
    else:
        print(f"Мне {n} лет")

