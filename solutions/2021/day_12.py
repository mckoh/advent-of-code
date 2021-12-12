"""
Day 12 Solution for Advent of Code
Date: 2021-12-12
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from _utilities import to_complex


input_data = to_complex(
    get_data(),
    sep="-",
    type_map=[("origin", str), ("destination", str)]
)


def constuct_graph(data):
    graph = {}
    for edge in data:
        orig = edge["origin"]
        dest = edge["destination"]

        if orig in graph.keys():
            graph[orig].append(dest)
        else:
            graph[orig] = [dest]

        if dest in graph.keys():
            graph[dest].append(orig)
        else:
            graph[dest] = [orig]

    return graph


def count_a(data, node, visited = set()):
    graph = constuct_graph(data)
    if node == "end":
        return 1
    total = 0
    for next in graph[node]:
        if next in visited:
            continue
        total += count_a(data, next, visited | {node} if node == node.lower() else visited)
    return total


def count_b(data, node, visited = set(), twice = False):
    graph = constuct_graph(data)
    if node == "end":
        return 1
    total = 0
    for next in graph[node]:

        if next == "start":
            continue
        if next in visited and twice:
            continue

        if next in visited:
            total += count_b(data, next, visited | {node} if node == node.lower() else visited, True)
        else:
            total += count_b(data, next, visited | {node} if node == node.lower() else visited, twice)
    return total


def solution_1(data):
    return count_a(data, "start")


def solution_2(data):
    return count_b(data, "start")


# %%
submit(
    solution_1(data=input_data),
)

# %%
submit(
    solution_2(data=input_data),
)
