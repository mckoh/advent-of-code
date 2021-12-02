"""
Day 02 Solution for Advent of Code
Date: 01.12.2021
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data

input_data = list(get_data().split('\n'))

d = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

# %%
def solution_1(data):
    """Resembles the solution b of aoc day 2.

    :param data: Input list of str commands
    """

    h_pos, depth = 0, 0

    for command in data:
        direction, distance = command.split(" ")
        distance = int(distance)

        if direction == "forward":
            h_pos += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
    return h_pos * depth


def solution_2(data):
    """Resembles the solution b of aoc day 2.

    :param data: Input list of str commands
    """

    h_pos, depth, aim = 0, 0, 0

    for command in data:
        direction, distance = command.split(" ")
        distance = int(distance)

        if direction == "forward":
            h_pos += distance
            depth +=  aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return h_pos * depth

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
