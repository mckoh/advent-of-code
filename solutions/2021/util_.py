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


def to_complex(data, sep=" ", type_map=None):
    """Breaks input data into a list of tuples

    The function can be used with a type_map parameter, allowing you
    to specify the datatype for teach part that a line element is broken
    into. If left blank, the method will simply return a tuple of strings.

    If it e.g. should return a tuple with a string in its first place and
    an integer value in second, you can specify type_map=[str, int]. Here
    you can use all valid python data types (int, str, float, bool etc.).

    :param data: An AOC input data string
    :param sep: The seperator character used to split each line
    :param type_map: A list of datatypes to be applied to the line's elements
    :return: List of str elements
    """
    if not type_map:
        return [tuple(value.split(sep)) for value in data.split("\n")]
    if type_map:
        output = []
        values = [tuple(value.split(sep)) for value in data.split("\n")]
        for value in values:
            element = []
            for i, item in enumerate(value):
                element.append(
                    type_map[i](item)
                )
            output.append(
                tuple(element)
            )
        return output