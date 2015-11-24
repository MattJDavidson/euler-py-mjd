#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""
import sys


def sum_of_squares(end):
    return sum([x**2 for x in xrange(1, end+1)])


def square_of_sums(end):
    return sum(xrange(1, end+1))**2


def main():
    end = 100
    print square_of_sums(end) - sum_of_squares(end)
    return

if __name__ == "__main__":
    sys.exit(main())
