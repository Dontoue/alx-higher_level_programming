#!/usr/bin/python3
# 3-common_elements.py
# Donald Mwanga  <donaldmwanga33@gmail.com>


def only_diff_elements(set_1, set_2):
    """Return all elements present in only one set."""
    return (set_1 ^ set_2)
