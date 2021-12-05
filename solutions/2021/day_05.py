"""
Day 05 Solution for Advent of Code
Date: 2021-12-05
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from util_ import to_str

input_data = to_str(get_data())


# %%
def deconstruct_data(data):
    """Deconstructs input data into x/y parts

    :param data: Your input data
    """
    output = []
    for row in data:
        origin = row.split(" ")[0]
        destinaton = row.split(" ")[2]

        x1, y1 = origin.split(",")
        x2, y2 = destinaton.split(",")
        output.append(
            {
                "x1": int(x1), "y1": int(y1),
                "x2": int(x2), "y2": int(y2)
            }
        )
    return output

def filter_orthogonales(data):
    """Filters only horizontal and vertical lines

    :param data: Your deconstructed data
    """
    return [line for line in data if line["x1"]==line["x2"] or line["y1"]==line["y2"]]

def construct_canvas(hor_dimension, vert_dimension):
    """creates your game canvas

    :param hor_dimension: Number of columns in canvas
    :param vert_dimensions: Number of rows in canvas
    :return: Matrix with 0 in every position
    """
    from numpy import zeros
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
        if max(line["x1"], line["x2"]) > horizontal_max:
            horizontal_max = max(line["x1"], line["x2"])
        if max(line["y1"], line["y2"]) > vertical_max:
            vertical_max = max(line["y1"], line["y2"])
    return vertical_max+1, horizontal_max+1

def get_steps(x1, x2, y1, y2):
    """Returns the number of steps to go between x and y

    :param x1: First x coordinate
    :param x2: Second x coordinate
    :param y1: First y coordinate
    :param y2: Second y coordinate
    :return: Number of steps to go
    """
    if x1 == x2:
        steps = get_abs(y2-y1)
    else:
        steps = get_abs(x2-x1)
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
        x1, x2 = line["x1"], line["x2"]
        y1, y2 = line["y1"], line["y2"]

        x, y = x1, y1

        steps = get_steps(x1, x2, y1, y2)

        for _ in range(steps+1):
            canvas[y, x] += 1

            if y2 > y1:
                y += 1
            elif y2 < y1:
                y -= 1

            if x2 < x1:
                x -= 1
            elif x2 > x1:
                x += 1

    return count_concentration_points(canvas, 2)

# %%
submit(
    solution(data=input_data, part=1),
)

# %%
submit(
    solution(data=input_data, part=2)
)
