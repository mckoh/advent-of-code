"""
Some AOC Utilities
Date: 02.12.2021
Author: Michael Kohlegger
"""


def to_int(data, sep="\n"):
    """Breaks input data into a list of int elements

    :param data: An AOC input data string
    :return: List of str elements
    """
    return [int(value) for value in data.split(sep)]


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
    an integer value in second, you can specify:

    type_map=[("label1", str), ("label2", int)]

    Here you can use all valid python data types (int, str, float, bool etc.).
    The label is an expression that can be used to describe the value and
    must be unique, e.g.:

    a = "a b 1\\nb c 2\\nc d 3\\ne f 4"
    to_complex(
        a,
        sep=" ",
        type_map=[("h_command", str), ("v_command", str), ("val", int)]
    )

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
            element = {}
            for i, item in enumerate(value):
                element[type_map[i][0]] = type_map[i][1](item)
            output.append(
                element
            )
        return output


def absolute(value):
    """Returns an absolute interger value

    :param vaue: Your input value
    :return: Absolute Value
    """
    return int((value**2)**0.5)