import sys
sys.path.append('../')
from zad1.priority_queue import *


def djikstra(G, source, vertices_len):
        
    predecessor = {}
    distance = {}

    for i in range(vertices_len):
        predecessor[i+1] = 0
        distance[i+1] = float("inf")
    distance[source] = 0 

    queue = PriorityQueue()

    for i in range(vertices_len):
        queue.insert(i+1, G[source,  i+1])


    while not queue.empty():

        node = queue.pop().k
        
        for i in range(vertices_len):
            if G[node, i+1] != float("inf") and G[node, i+1] != -1:
                weight = G[node, i+1]
                if distance[i+1] > distance[node] + weight:
                    distance[i+1] = distance[node] + weight
                    predecessor[i+1] = node
                queue.priority(i+1, distance[i+1])
    
    return distance, predecessor
