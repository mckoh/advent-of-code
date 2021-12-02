
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=7, typ="str")

data_s = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags."
]

data_e = [
"shiny gold bags contain 2 dark red bags.",
"dark red bags contain 2 dark orange bags.",
"dark orange bags contain 2 dark yellow bags.",
"dark yellow bags contain 2 dark green bags.",
"dark green bags contain 2 dark blue bags.",
"dark blue bags contain 2 dark violet bags.",
"dark violet bags contain no other bags."
]

def split_string(string):
    return int(string[:string.find(" ")]), string[string.find(" ")+1:]


class PlayBook:

    def __init__(self, data=data):

        from networkx import DiGraph

        self.data = data
        self.nodes = list()
        self.edges = list()
        self.graph = DiGraph()

        self.get_rule_graph()

    def return_clean_data(self):
        return list(map(lambda x: "1 " + x.replace(" contain ", ", ").replace("bags", "bag").replace(".", "").replace(" no ", " 0 no "), self.data))
    
    def return_split_data(self):
        return list(map(lambda x: (x.split(", ")[0], x.split(", ")[1:]), self.return_clean_data()))

    def check_nodes(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
        
    def get_rule_graph(self):
                                                  
        from networkx import DiGraph

        # empty graph
        self.nodes = list()
        self.edges = list()
        self.graph = DiGraph()
        
        for root, rules in self.return_split_data():
            oa, ob = split_string(string=root)
            self.check_nodes(node=ob)
            for rule in rules:
                ra, rb = split_string(string=rule)
                self.check_nodes(rb)
                self.edges.append((ob, rb, {'weight': ra}))
        
        # construct graph
        self.graph.add_nodes_from(self.nodes)
        self.graph.add_edges_from(self.edges)


    def draw(self):
        
        from matplotlib.pyplot import show
        from networkx import draw_circular

        draw_circular(self.graph, with_labels = True)
        show()

    def find_adjacent_in(self, searched="shiny gold bag"):
        in_shelf = [searched]
        out_shelf = list()
        while True:
            if len(in_shelf) > 0:
                item = in_shelf.pop(0)
                edges = self.graph.in_edges(item)
                for edge in edges:
                    if edge[0] not in out_shelf:
                        out_shelf.append(edge[0])
                    in_shelf.append(edge[0])
            else:
                return out_shelf

    def find_adjacent_out(self, start="shiny gold bag"):
        in_shelf = [(start, 1)]
        out_shelf = list()
        count = 0
        while True:
            if len(in_shelf) > 0:
                item_tuple = in_shelf.pop(0)
                
                item = item_tuple[0]
                parent_weight = int(item_tuple[1])
                
                edges = self.graph.out_edges(item)

                print(edges)
                for edge in edges:
                    weight = self.graph.get_edge_data(
                        u=item, 
                        v=edge[1]
                    )["weight"]

                    if edge[1] not in out_shelf:
                        out_shelf.append((edge[1], weight))
                    
                    in_shelf.append((edge[1], weight))

                    count += parent_weight * weight

            else:
                return count
    
    def walk_graph(self, edges):

        if len(edges) == 1:
            edge = edges[0]
            weight = self.graph.get_edge_data(
                u=edge[0], # from element
                v=edge[1]  # to element
            )["weight"]

# %%
# Part 1
p = PlayBook(data=data)
len(p.find_adjacent_in())

# %%
# Part 2
p = PlayBook(data=data_s)
p.find_adjacent_out()


# %%
from networkx import all_simple_paths

# %%
list(all_simple_paths(p.graph, "shiny gold bag", 'no other bag'))

# %%
weights = list()
for path in list(all_simple_paths(p.graph, "shiny gold bag", 'no other bag')):
    path_weights = [1]
    for i in range(len(path)-2):
        path_weights.append(p.graph.get_edge_data(u=path[i], v=path[i+1])["weight"])
    weights.append(path_weights)
weights

# %%
count = 0
for path in weights:
    for i in range(len(path)-1):
        count += path[::-1][i]*path[::-1][i+1]


# %%%
count