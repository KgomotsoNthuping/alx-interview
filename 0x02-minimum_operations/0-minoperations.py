#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Calculate fewest number of operations needed to result in n H characters in file"""
    a = 0
    b = 2
    while n > 1:
        while not n % b:
            a += b
            n /= b
        b += 1
    return a
