"""
Day 14 Solution for Advent of Code
Date: 2021-12-14
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from _utilities import to_complex


input_data = get_data(day=14, year=2021)
test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


# %%
def break_data(data, part):
    return data.split("\n\n")[part]


def return_base(data):
    return break_data(data, part=0)


def return_dictionary(data):
    return {
        value.split(" -> ")[0]: value.split(" -> ")[1]
        for value
        in break_data(data, part=1).split("\n")
    }


def step(dictionary, string, size=2):
    output=string[0]
    for i in range(0, len(string)-1):
        output += dictionary[string[i:i+size]] + string[i+1]
    return output


def walk(data, steps):
    dictionary = return_dictionary(data)
    base_string = return_base(data)
    for _ in range(steps):
        base_string = step(dictionary, base_string)
    return base_string


def count_characters(string):
    dictionary = {}
    for character in string:
        if character in dictionary.keys():
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary


def solution_1(data, steps=10):
    counts = count_characters(
        walk(data=data, steps=steps)
    )
    occurence_list = list(counts.values())
    occurence_list.sort()
    return occurence_list[-1] - occurence_list[0]


def solution_2(data, steps=40):
    dictionary = return_dictionary(data)
    base_string = return_base(data)

    for _ in range(steps):


# %%
submit(
    solution_1(input_data),
    day=14,
    year=2021
)

# %%
submit(
    solution_2(data=input_data),
)
