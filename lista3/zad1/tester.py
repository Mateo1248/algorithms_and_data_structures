import argparse
from sort import *
import random

algorithm = dict([
        ('quick', Sort.quick),
        ('merge', Sort.merge),
        ('radix', Sort.radix)
    ])

comp = lambda x, y: x <= y

n = 10000
for z in [n, n*n, n*n*n, n*n*n*n] :
    keys = [random.randint(0,z) for _ in range(n)]
    print(f"################################################\nZakres liczb [0:{z}]")
    for key in algorithm:
        keys_cpy = list(keys)
        stat = algorithm[key](comp, keys_cpy, True)
        print(f"\n{key} {z}")
        stat.print()

                
