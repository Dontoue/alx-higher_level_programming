#!/usr/bin/python3
# 8-simple_delete.py
# Donald Mwanga <donaldmwanga33@gmail.com>


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
