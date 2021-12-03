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


def find_max_min(data, col=0):
    """Find the most/least often occuring value in a column

    :param data: Die original list of binary numbers
    :param col: The column to consider
    :return: Max value, Min value
    """
    occ0 = count_value(to_columns(data, col=col), search="0")
    occ1 = count_value(to_columns(data, col=col), search="1")

    if occ0 > occ1:
        return ("0", "1")
    else:
        return ("1", "0")


def solution_1(data=test_data):
    """Resembles solution a of aoc day 3

    :param data: The data to play with
    :return: Day 3 solution
    """
    gamma_rate = ""
    epsilon_rate = ""
    for col in range(12):
        max_occ, min_occ = find_max_min(data=data, col=col)
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


def solution_2(data=test_data):
    """Resembles solution a of aoc day 3"""
    oxygen_gen_rate = ""
    CO2_scrubber_rate = ""


# %%
submit(
    solution_1(data=input_data),
)

# %%
submit(
    solution_2(data=input_data, steps=3),
)
