from tree.rbt.rbt  import *
from utils.utils import *
import math
import sys
import collections as cl

class HMAP:


    class HNode:
        def __init__(self, NT : int):
            super().__init__()
            self.NT = NT
            self.struct = []

        def insert(self, key):
            if isinstance(self.struct, list):
                self.struct.append(key)
                if len(self.struct) == self.NT:
                    tree = RBT()
                    for el in self.struct:
                        tree.insert(el)
                    self.struct = tree
            else:
                self.struct.insert(key)

        def delete(self, key):
            if isinstance(self.struct, list):
                try:
                    self.struct.remove(key)
                except:
                    return False
            else:
                self.struct.delete(key)
                if self.struct.getStat().end_all < self.NT:
                    struct = list(struct.inorder().split())
                    return False
            return True

        def find(self, key):
            if isinstance(self.struct, list):
                i=0
                for x in self.struct:
                    i+=1
                    if x == key:
                        return 1, i
                return 0, len(self.struct)
            else:
                return self.struct.find(key), self.struct.getStat().c

        def inorder(self):
            if isinstance(self.struct, list):
                return " ".join(self.struct)
            return self.struct.inorder()

    M : int =  128
    NT : int = 300
    table : dict
    stat : Stat

    def __init__(self):
        super().__init__()
        self.stat = Stat()
        self.table = dict()


    def __str__(self):
        return self.stat.__str__()


    def load(self, file_path):
        try:
            with open(file_path, "r", errors="ignore") as file:
                keys = file.read().split()

                self.stat.load() #stat inc

                for key in keys:
                    self.insert(key)
        except:
            print(f"Can't open file {file_path}.")
            sys.exit(1)


    def inorder(self):
        self.stat.inorder() #stat inc
        return ""


    def print(self):
        r = ""
        for x in self.table.values():
            r += " " + x.inorder()
        return r


    def min(self):
        self.stat.min() #stat inc
        return ""


    def max(self):
        self.stat.min() #stat inc
        return ""


    def successor(self, key):
        self.stat.successor() #stat inc
        return ""


    def insert(self, key):
        key = Utils.match(key)
        self.stat.insert()
        if key:
            self.stat.inc()
            h = self.getHash(key)

            if h not in self.table:
                self.table[h] = self.HNode(self.NT)

            self.table[h].insert(key)


    def delete(self, key):
        h = self.getHash(key)
        self.stat.delete()
        if h in self.table:
            if self.table[h].delete(key):
                self.stat.dec()


    def find(self, key):
        self.stat.find() #stat inc

        h = self.getHash(key)
        if h in self.table:
            res, c = self.table[h].find(key)
            self.stat.comp(times=c)
            return res
        return 0


    def getHash(self, key : str):
        return abs(hash(key) % self.M)


    def getStat(self):
        return self.stat