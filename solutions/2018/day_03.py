# %%
from aocd.models import Puzzle
from numpy.core.numeric import zeros_like
puzzle = Puzzle(year=2018, day=3)
data = puzzle.input_data.split("\n")

# %%
def deconstruct_claim(claim):
    parts = claim.replace(":", "").split(" ")
    ident = parts[0]
    start_x, start_y = parts[2].split(",")
    width, height = parts[3].split("x")
    return ident, int(start_x), int(start_y), int(width), int(height)


def  count_multi_patch(canvas):
    count = 0
    for row in canvas:
        for cell in row:
            if cell > 1:
                count += 1
    return count


def solution_1(data, base_w=1000, base_h=1000):
    from numpy import zeros

    canvas = zeros((base_w, base_h))

    for claim in data:
        ident, x, y, w, h = deconstruct_claim(claim)
        canvas[y:y+h, x:x+w] += 1

    return count_multi_patch(canvas)


def solution_2(data, base_w=1000, base_h=1000):
    from numpy import zeros

    canvas = zeros((base_w, base_h))

    first = True
    for claim in data:
        ident, x, y, w, h = deconstruct_claim(claim)
        canvas[y:y+h, x:x+w] += 1
        if not first:
            if count_multi_patch(canvas[y:y+h, x:x+w])/w/h == 0:
                return ident
        first = False

# %%
d = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2"
]


# %%
def claim_overlap_check(claim_a, claim_b, base_w, base_h):
    ident_a, x_a, y_a, w_a, h_a = deconstruct_claim(claim_a)
    ident_b, x_b, y_b, w_b, h_b = deconstruct_claim(claim_b)

    from numpy import zeros
    canvas = zeros((base_w, base_h))

    canvas[y_a:y_a+h_a, x_a:x_a+w_a] += 1
    canvas[y_b:y_b+h_b, x_b:x_b+w_b] += 1

    print(canvas)

    max=0
    for cell in canvas.reshape(-1):
        if max < cell:
            max = cell

    if max > 1:
        return True
    else:
        return False

# %%
solution_2(data=data, base_w=1000, base_h=1000)

