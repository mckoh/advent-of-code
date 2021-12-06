"""
Day 6 Solution for Advent of Code
Date: 2021-12-06
Author: Michael Kohlegger
"""

# %%
from os import popen
from aocd import submit
from aocd import get_data
from _utilities import to_int, to_complex, to_str


input_data = [int(number) for number in get_data().split(",")]


class Game:
    def __init__(self, data, days=80):
        """Simulates the growth of a fish population

        :param data: Your AOC input data
        :param days: The number of days to simulate growth
        """
        self.days = days
        self.data = data

        self.population = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }

        self.generate_fish()

    def generate_fish(self):
        """Initializes the population using the input data"""
        for number in self.data:
            self.population[number] += 1

    def step(self):
        """Run the simulation for one day and update population"""
        next_gen_population = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }

        for days_left, count in self.population.items():

            # count down
            if days_left > 0:
                next_gen_population[days_left-1] += count

            # generate new kids
            if days_left == 0:
                next_gen_population[8] += count
                next_gen_population[6] += count

        self.population = next_gen_population

    def walk(self):
        """Runs the game over n days"""
        for _ in range(self.days):
            self.step()

        output_count = 0

        for _, count in self.population.items():
            output_count += count

        return output_count

def solution_1(data):
    """Resembles first part of this day's solution"""
    game = Game(input_data, days=80)
    game.walk()


def solution_2(data):
    """Resembles second part of this day's solution"""
    game = Game(input_data, days=256)
    game.walk()


# %%
submit(
    solution_1(data=input_data)
)

# %%
submit(
    solution_2(data=input_data)
)
