"""
Day 10 Solution for Advent of Code
Date: 2021-12-10
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from requests.api import get
from _utilities import to_int, to_complex, to_str


input_data = to_str(get_data())

opposites = {
    ")": "(", "]": "[", ">": "<", "}": "{",
    "(": ")", "[": "]", "<": ">", "{": "}"
}
opening = list(opposites.values())[:4]
closing = list(opposites.values())[4:]


def check_consistency_a(string):
    """Checks for inconsistent strings

    :param string: Input string to check
    :return: Score
    """
    last_open = []
    incomplete = []

    for character in string:

        if character in opening:
            last_open.append(character)
        if character in closing:
            if len(last_open) > 0:
                if last_open[-1] == opposites[character]:
                    last_open = last_open[:-1]
                else:
                    return get_points_a(character)
            else:
                incomplete.append(character)
    return incomplete


def check_consistency_b(string):
    """Checks for incomplete strings

    :param string: Input string to check
    :return: Score
    """

    last_open = []

    for character in string:

        if character in opening:
            last_open.append(character)
        if character in closing:
            if last_open[-1] == opposites[character]:
                last_open = last_open[:-1]
            else:
                return 0

    s = 0
    for item in last_open[::-1]:
        s *= 5
        s += get_points_b(opposites[item])
    return s


def get_points_a(character):
    """Calculates points for inconsistent strings

    :param character: The character to score
    """
    return {")": 3, "]": 57, "}": 1197, ">": 25137}[character]


def get_points_b(character):
    """Calculates points for incomplete strings

    :param character: The character to score
    """
    return {")": 1, "]": 2, "}": 3, ">": 4}[character]


def solution_1(data):
    """Resembles part a solution of day 10

    :param data: Your input data
    """
    s = 0
    for line in data:
        s += check_consistency_a(line)
    return s


def solution_2(data):
    """Resembles part b solution of day 10

    :param data: Your input data
    """
    scores = []
    for line in data:
        result = check_consistency_b(line)
        if result > 0:
            scores.append(result)
    scores.sort()
    return scores[int(len(scores)/2)]


# %%
submit(
    solution_1(data=input_data),
)

# %%
submit(
    solution_2(data=input_data),
)
