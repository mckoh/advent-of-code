
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=3, typ="str")

# %%
data_s = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]

data_s

# %%
class TobogganSlide:

    def __init__(self, base_map, part=1):
        self.base_map = base_map
        self.base_map_w = len(base_map[0])
        self.base_map_h = len(base_map)

        print(f"Map is of size {self.base_map_w} x {self.base_map_h}.")

        print(self._get_map(n_w=6))

    def _get_map(self, n_w=1):
        return list(map(lambda x: x*n_w, self.base_map))

# %%

# Part 1
ts = TobogganSlide(base_map=data_s, part=1)

# %%

# Part 2

# %%
a = ["#####","....."]

# %%
