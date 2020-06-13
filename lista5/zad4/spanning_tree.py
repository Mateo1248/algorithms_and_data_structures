import sys
sys.path.append('../')
from zad3.kruskal import *
from utils import *


def spanning_tree_traversal_graph_adapter(graph):
    graph_trans = {}

    for in_v in graph:
        for out_v in graph[in_v]:
            graph_trans[(in_v, out_v[0])] = out_v[1]

    min_tree, sum_w = kruskal(graph_trans, len(graph))

    return min_tree


@stat
def spanning_tree_traversal(graph, v, start):
    visited = set([])
    
    print(f"Spaning tree traversal.", file=sys.stderr)

    def rec(start):
        steps = 0
        weight = 0
        visited.add(start)
        for i in range(v):
            if i+1 not in visited:
                try : 
                    weight += graph[(start, i+1)]
                    print(f"({start}, {i+1})={graph[(start, i+1)]}", file=sys.stderr)
                except:
                    try:
                        weight += graph[(i+1, start)]
                        print(f"({i+1}, {start})={graph[(i+1, start)]}", file=sys.stderr)
                    except:
                        continue
                
                steps += 1
                steps_, weight_ = rec(i+1)
                steps += steps_
                weight += weight_

        return steps, weight

    return rec(start)