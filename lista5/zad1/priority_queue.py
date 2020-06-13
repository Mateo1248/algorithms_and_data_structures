import numpy  as np
import copy
from dataclasses import dataclass




@dataclass
class Element:
    '''
        Priority queue heap element
    '''

    k: int
    p: int


    def __str__(self):
        return f"({self.k}, {self.p})"




class PriorityQueue:
    '''
        Priority queue implementation using heap
    '''

    array: dict
    last_idx: int


    def __init__(self):
        super().__init__()
        self.array = {}
        self.last_idx = 1


    def __str__(self):
        return "".join([str(self.array[i+1]) for i in range(self.last_idx-1)])


    def print(self):
        print(self)


    def top(self):
        return self.array[1]


    def empty(self):
        return self.last_idx == 1


    def insert(self, key:int, priority:int):

        self.array[self.last_idx] = Element(key, priority)
        i = self.last_idx
        j = i//2

        while j > 0 and self.array[i].p < self.array[j].p:
            self.array[j], self.array[i] = self.array[i], self.array[j]
            i = j
            j = i//2

        self.last_idx += 1


    def pop(self):    

        def min_child(i, last):
            if i * 2 + 1 > last:
                return i * 2
            if self.array[i * 2].p < self.array[i * 2 + 1].p:
                return i * 2
            return i * 2 + 1

        if self.last_idx > 1:
            self.last_idx -= 1
            first = self.array.pop(1)

            if self.last_idx > 1:
                self.array[1] = self.array.pop(self.last_idx)
                i=1
                while i * 2 <= self.last_idx-1:
                    mc = min_child(i, self.last_idx-1)
                    if self.array[i].p > self.array[mc].p:
                        self.array[i], self.array[mc] = self.array[mc], self.array[i]
                    i = mc
            return first

        return None


    def priority(self, key:int, priority:int):
        if priority >= 0:
            for idx in range(self.last_idx-1):
                idx += 1
                if self.array[idx].k == key:
                    if self.array[idx].p <= priority:
                        continue
                    
                    self.array[idx].p = priority
                    i = idx
                    j = i//2

                    while j > 0 and self.array[i].p < self.array[j].p:
                        self.array[j], self.array[i] = self.array[i], self.array[j]
                        i = j
                        j = i//2
