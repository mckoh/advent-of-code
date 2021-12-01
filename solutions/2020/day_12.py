
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=12, typ="str")


class Navigator:
    
    def __init__(self, data):
        self.data = data
        self.direction = 0
        self.x = 0
        self.y = 0
        
    def navigate(self, code):
        
        from math import sin, cos
        
        direction = code[:1]
        degree = int(code[1:])
        
        if direction == "R":
            self.direction -= degree
        elif direction == "L":
            self.direction += degree
        elif direction == "E":
            self.x += degree
        elif direction == "W":
            self.x -= degree
        elif direction == "N":
            self.y += degree
        elif direction == "S":
            self.y -= degree
        elif direction == "F":
            
            self.x += degree*cos(self.direction)
            self.y += degree*sin(self.direction)
            
    def move(self):
        for code in self.data:
            self.navigate(code=code)
        
        return abs(self.x) + abs(self.y)

# %%
# Part 1
n = Navigator(data=data)
n.move()


# %%
# Part 2


# %%
data_s = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11"
]