from djikstra import *
import sys
import time


# pobranie danych

n = int(input("n:")) #vertices
m = int(input("m:")) #edges

vertices = [i+1 for i in range(n)]
graph = {}
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i+1,j+1] = -1
        else:
            graph[i+1,j+1] = float("inf")

print(f"{m} edges in format (source, target, cost)")
for _ in range(m):
    edge = list(map(float, input().split()))

    if int(edge[0]) in vertices and int(edge[1]) in vertices:
        graph[int(edge[0]), int(edge[1])] = edge[2]
    else:
        print(f"Edge coordinates should be from range[1, {n}]")
        sys.exit(1)

source = int(input("source:"))


#uruchomienie algorytmu

start = time.time()
distance, predecessor = djikstra(graph, source, n)
end = time.time()

print("\ntarget \t distance")
for i in range(n):
    print(f"{i+1} \t {distance[i+1]}")

print(f"\nTime: {(end-start)/1000}ms", file=sys.stderr)

print("\nPaths:", file=sys.stderr)
for i in range(n):
    target = i+1
    print(f"target: {target}", file=sys.stderr)
    while predecessor[target] > 0:
        print(f"\t({predecessor[target]}, {target}) = {graph[predecessor[target], target]}", file=sys.stderr)
        target = predecessor[target]