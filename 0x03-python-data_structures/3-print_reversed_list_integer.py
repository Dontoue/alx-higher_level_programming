#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Donald Mwanga  <donaldmwanga33@gmail.com>


def print_reversed_list_integer(my_list=[]):
    """print all interger of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
