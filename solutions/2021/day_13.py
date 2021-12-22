"""
Day 13 Solution for Advent of Code
Date: 2021-12-15
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from numpy import array
from _utilities import to_complex


input_data = get_data(
    day=13,
    year=2021
)


def break_data(data, part):
    """Separates part 1 and 2 of the input data

    :param data: Input data
    :param part: Part of the split data to return
    """
    return data.split("\n\n")[part]


def return_coordinates(data):
    """Extracts the coordinates of points from the input data

    :param data: Your input data
    :return: List of coordinates
    """
    return {
        (
            int(value.split(",")[0]),
            int(value.split(",")[1])
        ): True
        for value
        in break_data(data, 0).split("\n")
    }


def return_folding(data):
    """Extracts the folding commands from the input data

    :param data: Your input data
    :return: List of commands
    """
    return [
        to_complex(
            line.split(" ")[-1],
            sep="=",
            type_map=[("axis", str), ("value", int)]
        )[0]
        for line in break_data(data, 1).split("\n")
    ]


def fold_point(coordinates, axis, position):
    """Projects a given point along the given axis

    :param coordinates: x, y coordinate of point as tuple
    :param axis: The axis along which to project ("x"/"y")
    :param position: The position of the axis to copy along
    :return: x and y coordinate of point after folding
    """
    assert axis in ["x", "y"], "Axis must be x and y"

    horizontal, vertical = coordinates

    if axis == "x":
        if horizontal > position:
            return position - (horizontal - position), vertical
    elif axis == "y":
        if vertical > position:
            return horizontal, position - (vertical-position)
    return horizontal, vertical


def render(points):
    """Renders the output of part b

    :param points: Coordinates of all data points
    """
    x_max, y_max = 0, 0
    for key in points.keys():
        if key[1] > y_max:
            y_max = key[1]
        if key[0] > x_max:
            x_max = key[0]
    x_max, y_max = x_max + 1, y_max + 1

    image = array([" "]*x_max*y_max).reshape((y_max, x_max))
    for coordinates in points:
        horizontal, vertical = coordinates[0], coordinates[1]
        image[vertical][horizontal] = "█"

    for line in image:
        print("".join(line))


def solution(data, part="a"):
    """Resembles first part of day 13 solution"""
    folding_commands = return_folding(data)
    points = return_coordinates(data)

    for command in folding_commands:

        output = {}

        for coordinates in points.keys():
            new_coordinates = tuple(fold_point(
                coordinates=coordinates,
                axis=command["axis"],
                position=command["value"]
            ))
            output[new_coordinates] = True

        points = output
        if part == "a":
            return len(points)

    render(points)

    return True


# %%
submit(
    solution(data=input_data, part="a"),
    day=13,
    year=2021,
    part=1
)

# %%
solution(data=input_data, part="b")
