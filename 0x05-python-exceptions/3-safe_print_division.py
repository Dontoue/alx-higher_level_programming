#!/usr/bin/python3
# 3-safe_print_division.py
# Donald Mwanga <donaldmwanga33@gmail.com>


def safe_print_division(a, b):
    """divides two intergers and prints the result"""
    try:
        div = a / b
    except(TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return (div)
