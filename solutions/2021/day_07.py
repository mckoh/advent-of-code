"""
Day 07 Solution for Advent of Code
Date: 2021-12-07
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from _utilities import to_int, absolute
from numpy import median


input_data = to_int(get_data(), sep=",")


def solution_1(data, sensitivity=20):
    """Resembles the solution of part 1 of this puzzle

    :param data: Your input data
    :param sensitivity: The range around the median to consider
    """

    # I use the median to get a better start position
    start = int(median(data))

    distances = []
    for position in range(start-sensitivity, start+sensitivity):
        distances.append(
            sum([absolute(value-position) for value in data])
        )

    return min(distances)


def calculate_distance(delta):
    """Calculates fuel consumtion for puzzle part 2

    :param delta: The distance between start and destination
    """
    return sum(list(range(1, delta + 1)))


def solution_2(data):
    """Resembles the solution of part 2 of this puzzle

    :param data: Your input data
    """

    distances = []
    for position in range(min(input_data), max(input_data)):
        distances.append(sum(
            [calculate_distance(absolute(value-position)) for value in data]
        ))

    return min(distances)


# %%
submit(
    solution_1(data=input_data),
)

# %%
submit(
    solution_2(data=input_data),
)
