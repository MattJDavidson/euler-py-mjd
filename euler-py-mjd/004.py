#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import sys

def is_palindrome(text):
    """Returns True if number is a palindrome.

    It is recognised this could be more efficient.
    """
    text = str(text) if not isinstance(text, str) else text
    return all([c == text[-i-1] for i,c in enumerate(text)])


def largest_palindrome(digit_length):
    """Returns largest palindrome for product of numbers for length of digits.

    This creates a list of all palindromes. Very inefficient.
    """
    return max(i*j
               for i in reversed(xrange(1, 10**digit_length))
               for j in reversed(xrange(1, 10**digit_length))
               if is_palindrome(i*j))


def main():
    print largest_palindrome(3)

if __name__ == "__main__":
    sys.exit(main())
