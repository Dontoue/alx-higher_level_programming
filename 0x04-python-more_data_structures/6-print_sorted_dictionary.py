#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Donald Mwanga <donaldmwanga33@gmail.com>


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
