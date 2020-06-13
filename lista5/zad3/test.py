from kruskal import *
from prim import *
import sys
sys.path.append('../')
from zad1.priority_queue import *
import time

func = {
    "-k" : kruskal,
    "-p" : prim
}

if len(sys.argv) == 2:
    if sys.argv[1] in func:
        f = func[sys.argv[1]]
    else:
        print("Wrong argument!")
        sys.exit(1)
else:
    print("\"-k\" for kruskal algorithm and \"-p\" for prim algorithm.")
    sys.exit(1)

# pobranie danych

n = int(input("n:")) #vertices
m = int(input("m:")) #edges

vertices = [i+1 for i in range(n)]
graph = {}

print(f"{m} edges in format (source, target, cost)")
for _ in range(m):
    edge = list(map(float, input().split()))

    if int(edge[0]) in vertices and int(edge[1]) in vertices:
        graph[(int(edge[0]), int(edge[1]))] = edge[2]
        graph[(int(edge[1]), int(edge[0]))] = edge[2]
    else:
        print(f"Edge coordinates should be from range[1, {n}]")
        sys.exit(1)



#uruchomienie algorytmu

min_tree, w = f(graph, n)


print("u \t v \t w")
for k  in min_tree:
    if k[0] < k[1]:
        print(f"{k[0]} \t {k[1]} \t {min_tree[k]}")
    else:
        print(f"{k[1]} \t {k[0]} \t {min_tree[k]}")
print(f"\nCost: {w}")