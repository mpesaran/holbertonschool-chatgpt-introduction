#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer `n` recursively.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)