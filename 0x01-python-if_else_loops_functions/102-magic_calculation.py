#!/usr/bin/python3
# 102-magic_calculation.py
# Donald Mwanga  <donaldmwanga33@gmail.com>


def magic_calculation(a, b, c):
    """Match bytecode provided."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
