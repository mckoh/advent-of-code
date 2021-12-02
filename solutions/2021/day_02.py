"""
Day 02 Solution for Advent of Code
Date: 02.12.2021
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data

input_data = list(get_data().split('\n'))


# %%
def solution_1(data):
    """Resembles the solution b of aoc day 2.

    :param data: Input list of str commands
    :return: Horizontal position times Depth
    """

    h_position, depth = 0, 0

    for command in data:
        direction, distance = command.split(" ")
        distance = int(distance)

        if direction == "forward":
            h_position += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance

    return h_position * depth


def solution_2(data):
    """Resembles the solution b of aoc day 2.

    :param data: Input list of str commands
    :return: Horizontal position times Depth
    """

    h_position, depth, aim = 0, 0, 0

    for command in data:
        direction, distance = command.split(" ")
        distance = int(distance)

        if direction == "forward":
            h_position += distance
            depth +=  aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    return h_position * depth

# %%
submit(
    solution_1(data=input_data),
    part="a",
    day=2,
    year=2021
)

# %%
submit(
    solution_2(data=input_data),
    part="b",
    day=2,
    year=2021
)
