#!/usr/bin/python3
# 2-replace_in_list.py
# Donald Mwanga <donaldmwanga33@gmail.com>


def replace_in_list(my_list, idx, element):
    """replaces and element of a list in specific position"""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return (my_list)
