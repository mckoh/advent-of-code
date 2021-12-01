# %%

from functions.functions import get_split_data
data = get_split_data(year=2020, day=9, typ="int")

data_s = [
    "35",
    "20",
    "15",
    "25",
    "47",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576"
]
data_s = list(map(lambda x: int(x), data_s))

# %%
def part_one(data=data):
    from itertools import combinations
    for pointer in range(25, len(data)):
        preambel = data[pointer-25:pointer]
        datapoint = data[pointer]

        match = False
        for t in combinations(preambel, r=2):
            if t[0]+t[1] == datapoint:
                match = True

        if not match:
            return datapoint

# %%
part_one(data)