#!/usr/bin/python3
# 9-multiple_by_2.py
# Donald Mwanga <donaldmwanga33@gmail.com>


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
