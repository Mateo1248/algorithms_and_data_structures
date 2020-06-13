import random
from utils import *
import sys

def min_traversal_graph_adapter(graph):
    graph_trans = {}

    for ver in graph:
        graph_trans[ver] = {k: v for v, k in sorted(graph[ver], key=lambda item: item[1], reverse=True)}

    return graph_trans

@stat
def min_traversal(graph, v, start):
    steps = 0
    weight = 0

    current_v = start
    visited = set([current_v])
    print(f"Minimum tree traversal.", file=sys.stderr)

    while len(visited) < v:

        try:
            next_v = graph[current_v].popitem()
            if next_v[1] not in visited:
                steps += 1
                weight += next_v[0]
                visited.add(next_v[1])
                print(f"({current_v}, {next_v[1]})={next_v[0]}", file=sys.stderr)
                current_v = next_v[1]
        except KeyError:
            print("Cos nie działa :(")

    return steps, weight