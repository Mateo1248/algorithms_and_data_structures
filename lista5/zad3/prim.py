import sys
sys.path.append('../')
from zad1.priority_queue import *
import random

def prim(graph, n):
    source = n
    min_tree = {}
    sum_w = 0

    queue = PriorityQueue()
    to_find = set([i+1 for i in range(n-1)])
    for i in range(n):
        w = graph.pop((source, i+1), None)
        if w != None:
            queue.insert(
                (source, i+1),
                w
            )

    while not queue.empty() and len(to_find) > 0:
        node = queue.pop()
        edge = node.k
        weight = node.p
        if edge[1] in to_find:
            to_find.discard(edge[1])
            min_tree[edge] = weight
            sum_w += weight

            for i in range(n):
                w = graph.pop((edge[1], i+1), None)
                if w != None:
                    queue.insert(
                        (edge[1], i+1),
                        w
                    )

    return min_tree, sum_w