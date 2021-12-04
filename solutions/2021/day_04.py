"""
Day 04 Solution for Advent of Code
Date: 2021-12-04
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data
from aocd.transforms import numbers
from numpy import zeros


input_data = get_data()

test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


# %%

def get_numbers(data):
    numbers = data.split("\n")[0]
    return [int(number) for number in numbers.split(",")]

def get_boards(data):

    from numpy import array, zeros
    bingo_boards = {}

    boards = data.split("\n\n")[1:]
    boards = test_data.split("\n\n")[1:]
    for i, board in enumerate(boards):
        values = []
        for row in board.split("\n"):
            row = row.strip().replace("  ", " ").split(" ")
            row = [int(value) for value in row]
            values.append(row)
        values = array(values)
        values.reshape((5,5))
        bingo_boards[i] = {
            "values": values,
            "hits": zeros((5,5))
        }
    return bingo_boards


def find_hit(board, number):
    from numpy import where
    try:
        h, v = where(board == number)
        return True, h[0], v[0]
    except IndexError:
        return False, 0, 0


def check_hits(hit_board):
    for row in hit_board:
        if sum(row) == 5:
            return True
    for row in hit_board.T:
        if sum(row) == 5:
            return True
    return False


def sum_unhit(board, hit_board):
    from numpy import where
    v, h = where(hit_board!=1)
    return sum(board[v,h])


class BingoEngine:

    def __init__(self, data):
        self.boards = get_boards(data)
        self.numbers = get_numbers(data)

    def play_round(self, number):

        for key in self.boards.keys():
            hit, v, h = find_hit(self.boards[key]["values"], number)

            if hit:
                self.boards[key]["hits"][v,h] = 1

            if check_hits(self.boards[key]["hits"]):
                points = sum_unhit(
                    self.boards[key]["values"],
                    self.boards[key]["hits"]
                )
                return points * number

        return False

    def play_game(self):
        for number in self.numbers:
            response = self.play_round(number)
            if response:
                return response


def solution_1(data):
    be = BingoEngine(data)
    return be.play_game()

def solution_2(data):
    pass


solution_1(test_data)

# %%
be = BingoEngine(test_data)
be.play_round(14)
be.play_round(10)
be.play_round(18)
be.play_round(22)
be.play_round(2)

# %%
sum_unhit(
    be.boards[2]["values"],
    be.boards[2]["hits"]
)