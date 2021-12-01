session_string = {
    2020: "53616c7465645f5fd24cb9a99b4e58a7873788ef51fb9e5bd9c6de1c3c8489a99b79256691d7e5377f080a1f66a89236"
}

def get_split_data(day, year=2020, typ="int"):
    """Splits the data and lets you create a list of strings or ints
    
    :param data: Returned data object from aocd
    :param typ: Type of data to return (String/Integer)
    :returns: List of items
    """

    from aocd import get_data

    data = get_data(year=year, day=day, session=session_string[year])
    data = data.split("\n")
    if typ == "int":
        int_data = list()
        for item in data:
            int_data.append(int(item))
        return int_data
    else:
        return data

def combinations(l, r=2):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                print((l[i], l[j]))