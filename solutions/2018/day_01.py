# %%
from aocd.models import Puzzle
puzzle = Puzzle(year=2018, day=1)
data = puzzle.input_data.split("\n")
data = map(lambda x: int(x), data)


def solution_1(data, start=0):
    state = start
    for step in data:
        state += step
    return state


def solution_2(data, start=0):

    from itertools import cycle

    frequency = start
    frequency_list = {frequency: 1}

    for delta in cycle(data):

        frequency += delta

        if frequency_list.get(frequency):
            frequency_list[frequency] += 1
        else:
            frequency_list[frequency] = 1

        if frequency_list.get(frequency)>1:
            return frequency

# %%
solution_1(data=data, start=0)

# %%
solution_2(data=data, start=0)

# %%
d = [+1, -1]
solution_2(data=d, start=0)

# %%
d = [+3, +3, +4, -2, -4]
solution_2(data=d, start=0)

# %%
d = [-6, +3, +8, +5, -6]
solution_2(data=d, start=0)

# %%
d = [+7, +7, -2, -7, -4]
solution_2(data=d, start=0)