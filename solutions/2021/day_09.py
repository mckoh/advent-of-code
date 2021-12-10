"""
Day 9 Solution for Advent of Code
Date: 2021-12-10
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from _utilities import to_str


input_data = to_str(get_data(day=9, year=2021))
test_data = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]


def get_working_data(data):
    from numpy import array
    return array([[int(character) for character in line] for line in data])


def get_play_map(data, fill_value=9):
    return [[fill_value]*(len(data[0])+2)] + [[fill_value]+list(line)+[9] for line in data] + [[fill_value]*(len(data[0])+2)]


def check_value(row, column, value, data):

    play_map = get_play_map(data)
    row, column = row + 1, column + 1

    below = play_map[row+1][column]
    above = play_map[row-1][column]
    left = play_map[row][column-1]
    right = play_map[row][column+1]

    min_neighbor = min([below, above, left, right])

    if value < min_neighbor:
        return get_risk_level(value)
    else:
        return 0


def get_risk_level(value):
    return value + 1


def solution_1(data):
    data = get_working_data(data)
    total_risk = 0
    for row, line in enumerate(data):
        for column, value in enumerate(line):
            total_risk += check_value(
                row=row,
                column=column,
                value=value,
                data=data
            )
    return total_risk


def solution_2(data):
    pass

# %%
submit(
    solution_1(data=input_data),
    part="a",
    day=9,
    year=2021
)

# %%
submit(
    solution_2(data=input_data),
)
