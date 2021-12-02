"""
Some AOC Utilities
Date: 02.12.2021
Author: Michael Kohlegger
"""


def to_int(data):
    """Breaks input data into a list of int elements

    :param data: An AOC input data string
    :return: List of str elements
    """
    return [int(value) for value in data.split("\n")]


def to_str(data):
    """Breaks input data into a list of string elements.

    :param data: An AOC input data string
    :return: List of int elements
    """
    return list(data.split('\n'))