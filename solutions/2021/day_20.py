"""
Day 20 Solution for Advent of Code
Date: 2021-12-22
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from numpy import array


input_data = get_data(day=20, year=2021)
test_data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


# %%
def get_algorith(data):
    """Returns your transformation algorithm
    :param data: Your input data
    :return: Your algorithm
    """
    return data.replace("#", "1").replace(".", "0").split("\n\n")[0].replace("\n", "")


def get_input_image(data):
    """Returns the input image from your data
    :param data: Your input data
    :return: Your input image
    """
    return [[int(character) for character in value] for value in data.replace("#", "1").replace(".", "0").split("\n\n")[1].split("\n")]


def get_command(data, index):
    """Returns the command value for a vertain index
    :param data: Your input data
    :param index: The commands index value
    :return: The command value (1 or 0)
    """
    return int(get_algorith(data)[index])


def get_index(binary):
    """Returns decimal value of a binary number
    :param binary: Binary number
    :return: Decimal number
    """
    output=0
    for i, character in enumerate(binary[::-1]):
        output += int(character)*2**i
    return output


def read_kernel(input_image, position=(0,0)):
    """Returns kernel values from input image

    The kernel values are returned as a flat
    sequence k1, k2, k3, ..., k9 and can be
    arranged according to the following image:

    [
        [k1, k2, k3],
        [k4, k5, k6],
        [k7, k8, k9]
    ]

    :param input_image: Your input image
    :param position: Your k5 position (Middle)
    :return: Kernel values (k1 to k9)
    """

    x, y = position[0], position[1]

    x_max = len(input_image[0]) - 1
    y_max = len(input_image) - 1

    k1, k2, k3 = 0, 0, 0
    k4, k5, k6 = 0, input_image[y][x], 0
    k7, k8, k9 = 0, 0, 0

    if x > 0 and y > 0:
        k1 = input_image[y-1][x-1]

    if y > 0:
        k2 = input_image[y-1][x]

    if y > 0 and x < x_max:
        k3 = input_image[y-1][x+1]

    if x > 0:
        k4 = input_image[y][x-1]

    if x < x_max:
        k6 = input_image[y][x+1]

    if x > 0 and y < y_max:
        k7 = input_image[y+1][x-1]

    if y < y_max:
        k8 = input_image[y+1][x]

    if y < y_max and x < x_max:
        k9 = input_image[y+1][x+1]

    return k1, k2, k3, k4, k5, k6, k7, k8, k9


def enlarge_input_image(input_image, n_dim):
    """Adds additional zero space around an input image
    :param input_image: The input image to transform
    :param n_dim: The number of rows/cols to add t/b/l/r
    :return: The enlarged image
    """
    return list(
        [[0] * (len(input_image[0]) + 2 * n_dim)] * n_dim
    ) + [
        [0] * n_dim + row + [0] * n_dim
        for row in input_image
    ] + list(
        [[0] * (len(input_image[0]) + 2 * n_dim)] * n_dim
    )


def get_binary_from_kernel(input_image, position):
    """Converts a kernal output to a binary number
    :param input_image: Your input image
    :param position: The kernel position
    :return: Binary representation as string
    """
    kernel = list(read_kernel(
        input_image=input_image,
        position=position
    ))
    return "".join([str(value) for value in kernel])

def return_output_image(data, iterations=2, n_dim=2):
    """Transforms an input image over n iterations
    :param data: Your input data
    :param iterations: Number of transformations
    """
    input_image = get_input_image(data)
    algorith = get_algorith(data)

    for step in range(iterations):
        output_image = []
        input_image = enlarge_input_image(
            input_image=input_image,
            n_dim=n_dim
        )
        for y, row in enumerate(input_image):
            output_row = []
            for x, field in enumerate(row):
                binary = get_binary_from_kernel(
                    input_image=input_image,
                    position=(x, y)
                )
                index = get_index(binary=binary)
                output_value = get_command(data, index=index)
                output_row.append(output_value)
            output_image.append(output_row)

        output_image = [row[1:-1] for row in output_image[1:-1]]
        input_image = output_image

    return output_image


def render_image(image):
    """Renders the output image to your console
    :param image: The image to render (0 and 1)
    :return: None
    """
    print(
        "\n".join([
            "".join([
                "#" if value == 1 else " "
                for value
                in row
            ])
            for row
            in image
        ])
    )


def solution_1(data):
    """Solves part a of this day's puzzle
    :param data: Your input data
    :return: Number of filled cells
    """
    output_image = return_output_image(data, iterations=2)
    return array(output_image).sum()


def solution_2(data):
    pass


# %%
submit(
    solution_1(data=input_data),
    day=20,
    year=2021
)

# %%
submit(
    solution_2(data=input_data),
)
