#! /usr/bin/env python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys

def get_numbers(max):
    return sum([x for x in xrange(max) if (x%3==0 or x%5==0)])

def main(max):
    print get_numbers(max)

if __name__ == "__main__":
    sys.exit(main(1000))
