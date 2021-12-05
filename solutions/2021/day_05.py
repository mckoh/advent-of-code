"""
Day 05 Solution for Advent of Code
Date: 2021-12-05
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from numpy import zeros
from util_ import to_str


input_data = to_str(get_data())


def deconstruct_data(data):
    """Deconstructs input data into hor_position/vert_position parts

    :param data: Your input data
    """
    output = []
    for row in data:
        origin = row.split(" ")[0]
        destinaton = row.split(" ")[2]

        horizonatal_start, vertial_start = origin.split(",")
        horizonatal_end, vertial_end = destinaton.split(",")
        output.append(
            {
                "horizonatal_start": int(horizonatal_start),
                "vertial_start": int(vertial_start),
                "horizonatal_end": int(horizonatal_end),
                "vertial_end": int(vertial_end)
            }
        )
    return output

def filter_orthogonales(data):
    """Filters only horizontal and vertical lines

    :param data: Your deconstructed data
    """
    return [
        line for line in data
        if line["horizonatal_start"]==line["horizonatal_end"]
        or line["vertial_start"]==line["vertial_end"]
    ]

def construct_canvas(hor_dimension, vert_dimension):
    """creates your game canvas

    :param hor_dimension: Number of columns in canvas
    :param vert_dimensions: Number of rows in canvas
    :return: Matrix with 0 in every position
    """
    return zeros((vert_dimension, hor_dimension))

def count_concentration_points(canvas, min_concentration):
    """Counts all datapoints with a value larger than min concentration

    :param canvas: Your game canvas to count on
    :param min_concentration: The min value to start counting at
    """
    count = 0
    for row in canvas:
        for col in row:
            if col >= min_concentration:
                count += 1
    return count

def find_max_dims(data):
    """Finds the number of dimensions, that the canvas needs to have

    :param data: Your deconstructed data
    :return: Vertical and Horizontal dimension
    """
    horizontal_max = 0
    vertical_max = 0
    for line in data:

        if max(
            line["horizonatal_start"],
            line["horizonatal_end"]
        ) > horizontal_max:

            horizontal_max = max(
                line["horizonatal_start"],
                line["horizonatal_end"]
            )

        if max(
            line["vertial_start"],
            line["vertial_end"]
        ) > vertical_max:

            vertical_max = max(
                line["vertial_start"],
                line["vertial_end"]
            )

    return vertical_max+1, horizontal_max+1

def get_steps(horizonatal_start,
              horizonatal_end,
              vertial_start,
              vertial_end):
    """Returns the number of steps to go between x and y

    :param horizonatal_start: First x coordinate
    :param horizonatal_end: Second x coordinate
    :param vertial_start: First y coordinate
    :param vertial_end: Second y coordinate
    :return: Number of steps to go
    """
    if horizonatal_start == horizonatal_end:
        steps = get_abs(vertial_end-vertial_start)
    else:
        steps = get_abs(horizonatal_end-horizonatal_start)
    return steps

def get_abs(value):
    """Returns an absolute interger value

    :param vaue: Your input value
    :return: Absolute Value
    """
    return int((value**2)**0.5)

def solution(data, part=1):
    """Resembles the solution of this AOC day

    :param data: Your input data from AOC
    :param part: The puzzle part you want to work on
    :return: Your puzzle solution
    """
    if part == 2:
        working_data = deconstruct_data(data)
    elif part == 1:
        working_data = filter_orthogonales(deconstruct_data(data))

    vert_dimension, hor_dimension = find_max_dims(working_data)
    canvas = construct_canvas(
        hor_dimension=hor_dimension,
        vert_dimension=vert_dimension
    )
    for line in working_data:
        horizonatal_start = line["horizonatal_start"]
        horizonatal_end = line["horizonatal_end"]
        vertial_start = line["vertial_start"]
        vertial_end = line["vertial_end"]

        hor_position, vert_position = horizonatal_start, vertial_start

        steps = get_steps(
            horizonatal_start,
            horizonatal_end,
            vertial_start,
            vertial_end
        )

        for _ in range(steps+1):
            canvas[vert_position, hor_position] += 1

            if vertial_end > vertial_start:
                vert_position += 1
            elif vertial_end < vertial_start:
                vert_position -= 1

            if horizonatal_end < horizonatal_start:
                hor_position -= 1
            elif horizonatal_end > horizonatal_start:
                hor_position += 1

    return count_concentration_points(canvas, 2)

# %%
submit(
    solution(data=input_data, part=1),
)

# %%
submit(
    solution(data=input_data, part=2)
)
