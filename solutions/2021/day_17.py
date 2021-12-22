"""
Day 17 Solution for Advent of Code
Date: 2021-12-21
Author: Michael Kohlegger
"""

# %%
from aocd import submit
from aocd import get_data


input_data = get_data(day=17, year=2021)


def split_data(data):
    return tuple(
        (int(item.split("..")[0]), int(item.split("..")[1]))
        for item in data.split(": ")[-1].replace(
            "x=", ""
        ).replace(
            "y=", ""
        ).split(", ")
    )


class Shot:

    def __init__(
        self,
        data,
        start_x=0,
        start_y=0):

        self.target = {
            "x_min": split_data(data)[0][0],
            "x_max": split_data(data)[0][1],
            "y_min": split_data(data)[1][0],
            "y_max": split_data(data)[1][1]
        }

        self.x_position = start_x
        self.y_position = start_y

        self.x_velocity = None
        self.y_velocity = None

    def _update_position(self):
        self.x_position += self.x_velocity
        self.y_position += self.y_velocity

    def _update_velocity(self, x_rate=1, y_rate=1):
        if self.x_velocity > 0:
            self.x_velocity -= x_rate
        elif self.x_velocity < 0:
            self.x_velocity += x_rate
        self.y_velocity -= y_rate

    def _check_hit(self, step, debug=False):
        if debug:
            print(f"Step: {step}")
            print("x: ", self.target["x_max"], self.x_position, self.target["x_min"], self.target["x_max"] >= self.x_position >= self.target["x_min"])
            print("y: ", self.target["y_max"], self.y_position, self.target["y_min"], self.target["y_max"] >= self.y_position >= self.target["y_min"])
            print("---")
        if self.target["x_max"] >= self.x_position >= self.target["x_min"]:
            if self.target["y_max"] >= self.y_position >= self.target["y_min"]:
                return True
        return False

    def fire(self, x_velocity, y_velocity, debug=False):
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        y_max = 0
        step=0

        while True:

            step += 1

            if self.x_position > self.target["x_max"] or self.y_position < self.target["y_min"]:
                return False, y_max

            self._update_position()
            self._update_velocity()

            if self._check_hit(step, debug=debug):
                return True, y_max


            if self.y_position > y_max:
                y_max = self.y_position


class ShotSolver:

    def __init__(self, data):
        self.data = data
        self.max_x_velocity = max(
            split_data(data)[0][0],
            split_data(data)[0][1]
        )
        self.max_y_velocity = min(
            split_data(data)[1][0],
            split_data(data)[1][1]
        )

    def find_highest(self, velocity_limit=100):

        y_total_max = 0
        best_pair = []

        for x in range(1, self.max_x_velocity+5):
            for y in range(self.max_y_velocity-5, velocity_limit):

                shot = Shot(self.data)
                hit, y_max = shot.fire(x_velocity=x, y_velocity=y, debug=False)

                if hit:
                    if y_max > y_total_max:
                        y_total_max = y_max

                    best_pair.append((x, y))

        return best_pair, y_total_max


def solution_1(data):
    ts = ShotSolver(data)
    return ts.find_highest()[1]


def solution_2(data, limit=300):
    ts = ShotSolver(data)
    a, _ = ts.find_highest(velocity_limit=limit)
    return len(a)


# %%
submit(
    solution_1(data=input_data),
    day=17,
    year=2021
)

# %%
submit(
    solution_2(data=input_data),
    day=17,
    year=2021
)
