#!/usr/bin/python3
# File: 1-calculation.py
# Author: Donald Mwanga <donaldmwanga33@gmail.com>

if __name__ == "__main__":

    """print the sum,difference,multiplication and quotientof 10 and 5"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
