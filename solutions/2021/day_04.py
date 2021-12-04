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


# %%
print(input_data)

# %%

def get_numbers(data):
    """Extracts number series from aoc input

    :param data: Your aoc input data
    :return: List of bingo numbers
    """
    numbers = data.split("\n")[0]
    return [int(number) for number in numbers.split(",")]

def get_boards(data):
    """Extracts bingo boards as numpy matrices from aoc input

    :param data: Your aoc input data
    :return: Dictionary with bingo boards and hit_boards (all 0)
    """
    from numpy import array, zeros
    bingo_boards = {}

    boards = data.split("\n\n")[1:]
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
    """Checks if a board contains the bingo number and where

    :param board: The bingo board to check
    :param number: The number to find on the board
    :return: True if hit with v and h coordinates of hit
    """
    from numpy import where
    try:
        h, v = where(board == number)
        return True, h[0], v[0]
    except IndexError:
        return False, 0, 0


def check_hits(hit_board):
    """Checks if a bingo board is finishes

    :param hit_board: The hit matrix with 1 (hit) and 0 (unhit)
    :return: True if board wins
    """
    for row in hit_board:
        if sum(row) == 5:
            return True
    for row in hit_board.T:
        if sum(row) == 5:
            return True
    return False


def sum_unhit(board, hit_board):
    """Returns the sum of unhit numbers from a bingo board

    :param board: The bingo board to check
    :param hit_board: The hit matrix with 1 (hit) and 0 (unhit)
    :return: Sum of unhit cells
    """
    from numpy import where
    v, h = where(hit_board!=1)
    return sum(board[v,h])


class BingoEngine:

    def __init__(self, data):
        """BingoEngine class lets you play Bingo games

        :param data: Your input Data
        :return: None
        """
        self.boards = get_boards(data)
        self.numbers = get_numbers(data)

    def play_round(self, number):
        """Plays a traditional bingo stage

        :param number: Number to be applied to bingo boards
        :return: False or board sum and key
        """
        for key in self.boards.keys():
            hit, v, h = find_hit(self.boards[key]["values"], number)

            if hit:
                self.boards[key]["hits"][v,h] = 1

            if check_hits(self.boards[key]["hits"]):
                points = sum_unhit(
                    self.boards[key]["values"],
                    self.boards[key]["hits"]
                )
                return points * number, key

        return False

    def play_squid_round(self, number, boards):
        """Plays a squid bingo game stage

        :param number: Number that should be applied to bingo boards
        :param boards: Remaining boards that have not yet won
        :return: False or winning boards of round {key: sum}
        """
        winners = {}
        for key in boards:
            hit, v, h = find_hit(self.boards[key]["values"], number)

            if hit:
                self.boards[key]["hits"][v,h] = 1

            if check_hits(self.boards[key]["hits"]):
                points = sum_unhit(
                    self.boards[key]["values"],
                    self.boards[key]["hits"]
                )
                winners[key] = points * number

        return winners

    def play_game(self):
        """Plays a sequence of Numbers in a traditional bingo game

        :return: Winning-response
        """
        for number in self.numbers:
            response = self.play_round(number)[0]
            if response:
                return response

    def play_squid_game(self):
        """Plays a sequence of Numbers in a squid bingo game

        :return: Winning-response
        """
        for number in self.numbers:
            response = self.play_squid_round(number, self.boards)

            if len(response)>0:

                for key in response.keys():
                    if len(self.boards) > 1:
                        self.boards.pop(key)
                    else:
                        return response[key]

def solution_1(data):
    """Resembles solution 1 of aoc day 4"""
    be = BingoEngine(data)
    return be.play_game()

def solution_2(data):
    """Resembles solution 2 of aoc day 4"""
    be = BingoEngine(data)
    return be.play_squid_game()


# %%
submit(
    solution_1(input_data)
)

#%%
submit(
    solution_2(input_data)
)
