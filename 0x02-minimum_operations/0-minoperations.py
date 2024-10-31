#!/usr/bin/python3
"""minimun operations"""


def minOperations(n):
    """minimum operations"""
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0
