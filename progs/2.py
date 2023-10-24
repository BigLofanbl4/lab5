#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    numbers = [
        int(input("Enter first number: ")),
        int(input("Enter second number: ")),
        int(input("Enter third number: ")),
    ]
    maximum = numbers[0]
    minimum = numbers[0]

    for i in range(0, len(numbers)):
        if maximum < numbers[i]:
            maximum = numbers[i]
        if minimum > numbers[i]:
            minimum = numbers[i]

    print(f"Maximal enetered number is {maximum}")
    print(f"Minimal entered number is {minimum}")
