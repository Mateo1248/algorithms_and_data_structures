import collections as cl
import time

class Stat:
    '''
        Stat counter.
    '''
    

    counter: cl.Counter
    max_el:int
    end_all:int
    s:int
    t:int

    def __init__(self):
        super().__init__()
        self.counter = cl.Counter()
        self.end_all = 0
        self.max_el = 0
        self.t = 0
        self.c = 0

    def comp(self, times=1):
        self.c += times

    def inc(self, times = 1):
        self.end_all += times
        if self.end_all > self.max_el:
            self.max_el = self.end_all


    def dec(self, times = 1):
        self.end_all -= 1


    def insert(self):
        self.counter["insert"] += 1


    def load(self):
        self.counter["load"] += 1


    def delete(self):
        self.counter["delete"] += 1


    def find(self):
        self.counter["find"] += 1


    def min(self):
        self.counter["min"] += 1


    def max(self):
        self.counter["max"] += 1


    def successor(self):
        self.counter["successor"] += 1


    def inorder(self):
        self.counter["inorder"] += 1

    def start(self):
        self.s = time.time()

    def end(self):
        self.t += time.time()-self.s
        self.s = 0

    def __str__(self):
        out = "Operations counter:\n"
        for x in self.counter.most_common():
            out += (f"  {x[0]}: {x[1]}\n")
        out += (f"\nMax filling: {self.max_el}\n")
        out += (f"End filling: {self.end_all}\n")
        out += (f"Total time: {self.t}s")
        #out += (f"\nfind comparision: {self.c//10}")
        return out