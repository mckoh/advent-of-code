#
# %%
from logging import _FormatStyle
from aocd.models import Puzzle
puzzle = Puzzle(year=2018, day=2)
data = puzzle.input_data.split("\n")


# %%
def count(char, text):
    return len([c for c in text if c==char])


def unique(code):
    out = []
    for char in code:
        if char not in out:
            out.append(char)
    return out


def delta(str_a, str_b):
    count = 0
    for i in range(len(str_a)):
        if str_a[i]!=str_b[i]:
            count += 1

    return count


def match(str_a, str_b):
    out = ""
    for i in range(len(str_a)):
        if str_a[i]==str_b[i]:
            out += str_a[i]
    return out


def compare_all(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if delta(data[i], data[j])==1:
                return match(data[i], data[j])


def solution_1(data):
    two, three = False, False
    two_codes, three_codes = 0, 0

    for code in data:
        for char in unique(code):
            if count(char, code) == 2:
                two = True
            if count(char, code) == 3:
                three = True

        if two:
            two_codes += 1
        if three:
            three_codes += 1

        two, three = False, False

    return two_codes * three_codes


def solution_2(data):
    return(compare_all(data))


# %%
solution_1(data=data)

# %%
solution_2(data=data)