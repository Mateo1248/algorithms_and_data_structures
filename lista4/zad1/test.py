from tree.bst.bst import *
from tree.rbt.rbt import *
from hmap.hmap import *
import random

d_str = {
    "rbt" : RBT,
    "hmap" : HMAP
}

file = "lotr.txt"
    
for structure in d_str:
    s = d_str[structure]()
    stat = s.getStat()
    s.load(file)
    for _ in range(10):
        stat.start()
        #97,122 105,114 97,105 114,122
        s.find("".join([chr(random.randint(105,114)) for _ in range(5)]))
        stat.end()
    print(f"{structure}\n{s}\n")

    stat.c = 0
    stat.t = 0
    for _ in range(10):
        stat.start()
        #97,122 105,114 97,105 114,122
        s.find("".join([chr(random.randint(97,105)) for _ in range(5)]))
        stat.end()
    print(f"{structure}\n{s}\n")

    stat.c = 0
    stat.t = 0
    for _ in range(10):
        stat.start()
        #97,122 105,114 97,105 114,122
        s.find("".join([chr(random.randint(114,122)) for _ in range(5)]))
        stat.end()
    print(f"{structure}\n{s}\n")