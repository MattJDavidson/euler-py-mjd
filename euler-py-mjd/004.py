#! /usr/bin/env python
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

def main():
    """ This is bad practice.

    Creates a list of palindromes which are the product of two 3 digit numbers.
    Double iterators give us the numbers in the list generator.
    The palindrome is checked taking advantage of list splicing syntax.
    """

    print max([i*j for i in xrange(999, 100, -1) for j in xrange(i, 100, -1) if str(i*j) == str(i*j)[::-1]])


if __name__ == "__main__":
    sys.exit(main())
