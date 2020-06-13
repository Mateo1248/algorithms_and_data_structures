import sys
sys.path.append('../')
from zad1.priority_queue import *



class UnionFind:

    def __init__(self):
        self.sets = {}
        self.idx = 0

    def make(self, x):
        x_set = {x}
        if x_set not in self.sets.values():
            self.sets[self.idx] = x_set
            self.idx += 1

    def find(self, x):
        for k in self.sets:
            if x in self.sets[k]:
                return k
        return None

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != None and y != None and x != y:
            self.sets[x].update(self.sets[y])
            self.sets.pop(y, None)



def kruskal(graph, n):
    min_tree = {}
    sets = UnionFind()
    sum_w = 0
    queue = PriorityQueue()

    for k in graph:
        queue.insert(k, graph[k])

    for i in range(n):
        sets.make(i+1)

    while not queue.empty():
        
        node = queue.pop()
        edge = node.k
        weight = node.p

        if sets.find(edge[0]) != sets.find(edge[1]):
            min_tree[edge] = weight
            sum_w += weight
            sets.union(*edge)

    return min_tree, sum_w
