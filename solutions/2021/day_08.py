"""
Day 8 Solution for Advent of Code
Date: 2021-12-08
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from itertools import permutations
from _utilities import to_str


input_data = to_str(get_data())


digit_segments = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
}


def count_digit_segments(numbers=digit_segments, keys=[1, 4, 7, 8]):
    """Gets counts of each number's segments

    :param keys: The numbers of interest
    :return: A list of counts
    """
    return [len(value) for key, value in numbers.items() if key in keys]


def solution_1(data):
    """Resembles part a solution of day 8

    :param data: Your input data
    """
    count = 0

    for item in data:
        _, part_b = item.split(" | ")
        for number in part_b.split(" "):
            if len(number) in count_digit_segments(keys=[1, 4, 7, 8]):
                count += 1
    return count


def solution_2(data):
    """Resembles part b solution of day 8

    :param data: Your input data
    """
    output = 0

    requrired = set(digit_segments.values())

    for item in data:
        part_a, part_b = item.split(" | ")

        for permutation in permutations("abcdefg"):

            # create a map of all possible wirings for abcdefg
            # this is very brute force
            wire_map = {
                key: value
                for key, value
                in zip(permutation, "abcdefg")
            }

            wiring = {
                "".join(sorted(map(wire_map.get, value)))
                for value in part_a.split()
            }

            if wiring == requrired:
                output_value = [
                    "".join(sorted(map(wire_map.get, number)))
                    for number in part_b.split()
                ]

                output_value = "".join(
                    str(requrired.index(number))
                    for number in output_value
                )
                output += int(output_value)

    return output


# %%
submit(
    solution_1(data=input_data),
)

# %%
submit(
    solution_2(data=input_data),
)
