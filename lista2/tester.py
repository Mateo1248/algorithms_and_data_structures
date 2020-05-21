import argparse
from sort import *
import random

algorithm = dict([
        ('quick', Sort.quick),
        ('merge', Sort.merge)
    ])

comp = lambda x, y: x <= y
path = "./ex2_test/"


for k in [1, 10]:
    for n in range(500, 10001, 500):
        for i in range(k):
            keys = [random.random() for _ in range(n)]
            for key in algorithm:
                keys_cpy = list(keys)
                stat = algorithm[key](comp, keys_cpy, True)
                stat.write_stat_to_file(path+str(key)+str(k)+".txt")
    if k > 1:
        for key in algorithm:
            out = ""
            with open(path+str(key)+str(k)+".txt", "r") as f:
                lines = f.readlines()

                nn = 500
                comparisions = 0
                transpositions = 0
                time = 0
                for l in lines:
                    lsplited = l.split()
                        
                    if nn == int(lsplited[0]):
                        comparisions += int(lsplited[1])
                        transpositions += int(lsplited[2])
                        time += float(lsplited[3])
                    else:
                        out +=  str(nn) + "\t" + \
                                str(comparisions//k) + "\t" + \
                                str(transpositions//k) + "\t" + \
                                str(time/k) + "\n"
                        nn = int(lsplited[0])
                        comparisions = int(lsplited[1])
                        transpositions = int(lsplited[2])
                        time = float(lsplited[3])

                out +=  str(nn) + "\t" + \
                        str(comparisions//k) + "\t" + \
                        str(transpositions//k) + "\t" + \
                        str(time/k) + "\n"
                        
            with open(path+str(key)+str(k)+".txt", "w") as f:
                f.write(out)
                
