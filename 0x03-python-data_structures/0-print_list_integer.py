#!/usr/bin/python3
# 0-print_list_integer.py
# Donald Mwanga <donaldmwanga33@gmail.com>

def print_list_integer(my_list=[]):

    """prints all elements of a list"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
