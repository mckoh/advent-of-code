"""
Day 03 Solution for Advent of Code
Date: 03.12.2021
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data

from util_ import to_str

input_data = to_str(get_data())

test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


# %%
def to_columns(data, col=0):
    """Transform rows into columns

    :param data: Die original list of binary numbers
    :param col: The colum that should be returned
    :return: The list of n-th (col) items
    """
    return [value[col] for value in data]


def count_value(data, search="0"):
    """Count the number of occurences of the search value

    :param data: Die original list of binary numbers
    :param search: The value that should be counted
    :return: The number of occurences of search
    """
    return len([value for value in data if value==search])


def find_extreme(data, col=0, method="max"):
    """Find the most/least often occuring value in a column

    :param data: Die original list of binary numbers
    :param col: The column to consider
    :return: Max value, Min value
    """
    occ0 = count_value(to_columns(data, col=col), search="0")
    occ1 = count_value(to_columns(data, col=col), search="1")

    if occ0 > occ1:
        if method == "max":
            return "0"
        if method == "min":
            return "1"
    else:
        if method == "max":
            return "1"
        if method =="min":
            return "0"

    return "1"


def solution_1(data):
    """Resembles solution a of aoc day 3

    :param data: The data to play with
    :return: Day 3 solution
    """
    gamma_rate = ""
    epsilon_rate = ""
    for col in range(12):
        max_occ = find_extreme(data=data, col=col, method="max")
        min_occ = find_extreme(data=data, col=col, method="min")
        gamma_rate += max_occ
        epsilon_rate += min_occ
    return to_dec(gamma_rate) * to_dec(epsilon_rate)


def to_dec(bin_number):
    """Converts a binary number into decimal

    :param bin_number: The binary number to convert
    :return: The decimal number
    """
    output = 0
    for i, pos in enumerate(bin_number[::-1]):
        output += int(pos) * 2 ** i
    return output


def filter_numbers(data, col=0, method="max"):
    """Filter only the numbers with the fitting digit in the n-th place

    :param data: Your input List of binary numbers
    :param col: The column which to consider for filtering
    :param method: The method to applie for filtering (min/max)
    :return: The filtered list
    """

    most_common = find_extreme(data=data, col=col, method=method)
    return [value for value  in data if value[col]==most_common]


def walk_list(data, objective="oxygen"):
    """Sequentially filters the list until only one number remains

    :param data: The original list to start with
    :param objective: A switch wheather to do this for oxygen or co2
    :return: The remaining binary number
    """
    if objective == "oxygen":
        method = "max"
    elif objective == "co2":
        method = "min"

    remaining_data = data
    col = 0

    while True:

        remaining_data = filter_numbers(remaining_data, col=col, method=method)

        if len(remaining_data)==1:
            return remaining_data[0]
        col += 1


def solution_2(data):
    """Resembles solution a of aoc day 3"""
    oxygen_rate = walk_list(data=data, objective="oxygen")
    co2_rate = walk_list(data=data, objective="co2")

    return to_dec(oxygen_rate) * to_dec(co2_rate)


# %%
submit(
    solution_1(data=input_data),
)

# %%
submit(
    solution_2(data=input_data),
)
