#!/usr/bin/python3
# 8-class_to_json.py
# Donald Mwanga <donaldmwanga33@gmail.com>
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
