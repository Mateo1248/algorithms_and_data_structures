import argparse
from sort import *
import random
import tracemalloc

#dlugosc tablicy
length = 10

comp = lambda x, y: x <= y

for n in [10, 1000, 100000, 10000000, 1000000000]:
    print(f"\nNumber range: [0:{n}]")
    keys = [random.randint(0,n) for _ in range(length)]
    tracemalloc.start()
    stat = Sort.radix(comp, keys, True)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB; Difference {(peak-current)/10**6}MB")
    tracemalloc.stop()
    stat.print()