from random_traversal import *
from min_traversal import *
from spanning_tree import *
import random

n = int(input())
m = ((n-1)*n)//2

graph = {
    i+1: [] for i in range(n)
}

for _ in range(m):
    edge = input().split()
    graph[int(edge[0])].append((int(edge[1]), float(edge[2])))
    graph[int(edge[1])].append((int(edge[0]), float(edge[2])))

start = random.randint(1, n)
print(f"source: {start}")
print(
    random_traversal(
        random_traversal_graph_adapter(graph),
        n,
        start
    )
)

print(
    min_traversal(
        min_traversal_graph_adapter(graph),
        n,
        start
    )
)

print(
    spanning_tree_traversal(
        spanning_tree_traversal_graph_adapter(graph),
        n,
        start
    )
)