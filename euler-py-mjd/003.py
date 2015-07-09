#! /usr/bin/env python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import sys

def prime_factors(n):
    """ Returns a list of the prime factors for a number """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def main():
    print max(prime_factors(600851475143))

if __name__ == "__main__":
    sys.exit(main())
