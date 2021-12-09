from math import prod
import networkx as nx


def get_payload():
    with open('day9.txt') as file:
        return file.read().splitlines()


data = get_payload()
grid = nx.grid_2d_graph(len(data), len(data[0]))
depth = {(i, j): int(data[i][j]) for i, j in grid.nodes}


def q1():
    output = sum(depth[v] + 1 for v in grid.nodes if all(depth[v] < depth[u] for u in grid.neighbors(v)))
    print(output)


def q2():
    grid.remove_nodes_from(k for k, v in depth.items() if v == 9)
    output = prod(sorted(map(len, nx.connected_components(grid)))[-3:])
    print(output)


q1()
q2()
