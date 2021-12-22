"""
Day 14 Solution for Advent of Code
Date: 2021-12-14
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from requests.api import head


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
    occurrence_list = list(counts.values())
    occurrence_list.sort()
    return occurrence_list[-1] - occurrence_list[0]


def solution_2(data, steps=40):
    dictionary = return_dictionary(data)
    base_string = return_base(data)

    pair_count = {}
    for i in range(0, len(base_string)-1):
        if base_string[i:i+2] not in pair_count.keys():
            pair_count[base_string[i:i+2]] = 1
        else:
            base_string[i:i+2] += 1

    for _ in range(steps):
        new_pair_count = {}
        for pair in pair_count:

            inserter = dictionary[pair]
            first_new_pair = pair[0]+inserter
            second_new_pair = inserter+pair[1]

            if first_new_pair not in new_pair_count:
                new_pair_count[first_new_pair] = 0

            if second_new_pair not in new_pair_count:
                new_pair_count[second_new_pair] = 0

            new_pair_count[first_new_pair] += pair_count[pair]
            new_pair_count[second_new_pair] += pair_count[pair]

        pair_count = new_pair_count

    head_count = {}
    tail_count = {}

    for pair in pair_count:
        if pair[0] not in head_count.keys():
            head_count[pair[0]] = 0
        if pair[1] not in tail_count.keys():
            tail_count[pair[1]] = 0

        head_count[pair[0]] += pair_count[pair]
        tail_count[pair[1]] += pair_count[pair]

    characters = set(list(head_count.keys()) + list(tail_count.keys()))
    character_counts = {}

    for character in characters:
        if character not in character_counts.keys():
            character_counts[character] = 0

        if head_count.get(character):
            character_counts[character] += head_count.get(character)
        if tail_count.get(character):
            character_counts[character] += tail_count.get(character)

    counts = list(character_counts.values())
    counts.sort()
    return counts[-1] - counts[0], counts


# %%
submit(
    solution_1(input_data),
    day=14,
    year=2021
)

# %%
submit(
    solution_2(data=input_data),
    day=14,
    year=2021
)
