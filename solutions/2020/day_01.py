
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=1, typ="int")

# %%

# Part 1

for item_a in data:
    for item_b in data:

        if item_a + item_b == 2020:
            output = item_a*item_b

print(output)


# %%

# Part 2

for item_a in data:
    for item_b in data:
        for item_c in data:

            if item_a + item_b + item_c == 2020:
                output = item_a*item_b*item_c

print(output)
