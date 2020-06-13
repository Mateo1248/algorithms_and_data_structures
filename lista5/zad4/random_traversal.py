import random
from utils import *
import sys


def random_traversal_graph_adapter(graph):
    graph_trans = {}

    for v in graph:
        graph_trans[v] = set(graph[v])

    return graph_trans


@stat
def random_traversal(graph, v, start):
    steps = 0
    weight = 0

    current_v = start
    visited = set([current_v])

    print(f"Random tree traversal.", file=sys.stderr)

    while len(visited) < v:
        next_v = random.sample(
            graph[current_v],
            1
        )[0]

        weight += next_v[1]
        steps += 1
        visited.add(next_v[0])
        print(f"({current_v}, {next_v[0]})={next_v[1]}", file=sys.stderr)
        current_v = next_v[0]

    return steps, weight