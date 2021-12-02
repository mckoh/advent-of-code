# Advent of Code

In this repo, I am collecting all my AOC code files. There is a sub folder for each year holding that year's code sources. Make sure to install the requirements that are necessary to execute the code. Although I try to keep these dependencys low profile, there are some references to external packages.

![Advent of Code Banner Image](static/aoc_banner.png)

## How to use the data loading package

```python
from aocd.models import Puzzle
puzzle = Puzzle(year=2017, day=20)
data = puzzle.input_data
puzzle.answer_a = 299

# easy way to get your data
from aocd import get_data
get_data(day=24, year=2015)

# built-in splitting/casting options
from aocd import lines
from aocd import numbers

# submit an answer
from aocd import submit
submit(my_answer, part="a", day=25, year=2017)

```