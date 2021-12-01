
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=2, typ="str")

# %%
data_s = data[:5]

# %%

def split_item_into_parts(item):
    preamble = item.split(": ")[0]
    range_part = preamble.split( )[0]
    char_part = preamble.split( )[1]
    from_char = int(range_part.split("-")[0])
    to_char = int(range_part.split("-")[1])
    password = item.split(": ")[1]

    return (from_char, to_char, char_part, password)


def count_chars(passwort, character):
    occurences = 0
    for char in passwort:
        if char == character:
            occurences += 1
    return occurences


def iterate_items(data):
    correct_passwords = 0
    for item in data:
        f, t, c, p = split_item_into_parts(item)
        n = count_chars(passwort=p, character=c)
        if n >= f and n <= t:
            correct_passwords += 1
    
    return correct_passwords


def iterate_items_part2(data):
    correct_passwords = 0
    for item in data:
        f, t, c, p = split_item_into_parts(item)

        first_char = p[f-1]
        second_char = p[t-1]

        if first_char == c and second_char != c:
            correct_passwords += 1
        elif first_char != c and second_char == c:
            correct_passwords += 1

    return correct_passwords

# %%

# Part 1
iterate_items(data)

# %%

# Part 2
iterate_items_part2(data)
