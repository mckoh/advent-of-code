"""
Day 01 Solution for Advent of Code
Date: 01.12.2021
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from util_ import to_int

input_data = to_int(get_data())


# %%
def solution_1(data):
    """Returns the number of times that the value in data increases.

    :param data: List of integer values
    :return: Count of increases
    """
    count=0
    last_value = data[0]
    for value in data[1:]:
        if value > last_value:
            count += 1
        last_value = value
    return count


def return_window_sum(data, position, steps):
    """Returns the sum of values of an n-step
    sliding window.

    :param data: A list of integer values
    :param steps: The number of steps for the sliding window
    :param position: The starting position of the window
    :return: Sum of values in the window
    """
    return sum(data[position:position+steps])


def solution_2(data, steps):
    """Returns the number of times that the value of an n-step
    sliding window increases

    :param data: A list of integer values
    :param steps: The number of steps for the sliding window
    :return: Count of increases
    """

    count=0
    last_value = return_window_sum(data, 0, steps)
    for i in range(1, len(data[1:])):

        value = return_window_sum(data, i, steps)

        if value > last_value:
            count += 1

        last_value = value
    return count


# %%
submit(
    solution_1(data=input_data),
    part="a",
    day=1,
    year=2021
)

# %%
submit(
    solution_2(data=input_data, steps=3),
    part="b",
    day=1,
    year=2021
)
