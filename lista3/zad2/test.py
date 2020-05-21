from main import *
import random

k = 100
f = lambda x, n, avg: (sum(list(map(lambda w: (w-avg)**2, x)))/n)**(1/2)

for n in [10,100,1000]:
    rs_comp = []
    s_comp = []
    for _ in range(k):
        A1 = [random.randint(1, 1000) for _ in range(n)]
        A2 = A1[:]

        stat1 = Stat()
        randomized_select(A1, 0, n-1, n/2, stat1)
        rs_comp.append(stat1.comp)

        stat2 = Stat()
        select(A2, 0, n-1, n/2, stat2)
        s_comp.append(stat2.comp)
    print(f"n: {n}")
    print(f"średnia:")
    rs_avg = sum(rs_comp)/k
    print(f"\trandomized_select: {rs_avg}")
    s_avg = sum(s_comp)/k
    print(f"\tselect: {s_avg}")

    print(f"odchylenie standardowe:")
    rs_avg = sum(rs_comp)/k
    print(f"\trandomized_select: {f(rs_comp, n, rs_avg)}")
    s_avg = sum(s_comp)/k
    print(f"\tselect: {f(s_comp, n, s_avg)}\n\n")