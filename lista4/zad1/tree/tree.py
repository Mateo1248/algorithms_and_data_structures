import sys
import enum

from utils.stat import *

sys.setrecursionlimit(10**8) 

class Color(enum.Enum):
    '''
        Rbt node color.
    '''

    RED = 1
    BLACK = 2




class Node:
    '''
        Tree node representation.
    '''

    key:str


    def __init__(self, key: str, parent = None, color:Color = None):
        self.key = key
        self.parent = parent
        self.color = color
        self.right = None
        self.left = None


    def __str__(self):
        out = ""
        if self.left and self.left.key:
            out += self.left.__str__()
        out += f" {self.key} "
        if self.right and self.right.key:
            out += self.right.__str__()
        return out




class Tree:
    '''
        Tree class representation.
    '''

    stat: Stat
    root: Node


    def __init__(self):
        self.stat = Stat()


    def load(self, file_path):
        try:
            with open(file_path, "r", errors="ignore") as file:
                keys = file.read().split()
                self.stat.load() #stat inc
                
                for key in keys:
                    self.insert(key)
        except:
            print(sys.exc_info()[0])
            print(f"Can't open file {file_path}.")
            sys.exit(1)
    

    def find(self, key):
        self.stat.find() #stat inc

        node = self.root
        while node and node.key:
            if node.key == key:
                self.stat.comp()
                return 1
            elif node.key < key:
                self.stat.comp()
                node = node.right
            else:
                node = node.left
        return 0


    def inorder(self):
        self.stat.inorder() #stat inc

        if self.root and self.root.key:
            return self.root.__str__()
        return ""

    
    def min(self):
        self.stat.min() #stat inc

        node = self.root
        min_key = ""
        while node and node.key:
            min_key = node.key
            node = node.left
        return min_key


    def max(self):
        self.stat.max() #stat inc   

        node = self.root
        max_key = ""
        while node and node.key:
            max_key = node.key
            node = node.right
        return max_key


    def successor(self, key):
        self.stat.successor() #stat inc

        node = self.root
        found = False
        while node and node.key:
            if  node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
            else:
                found = True
                break        
        
        if found:
            if node.right and node.right.key:
                node = node.right
                while node.left and node.left.key:
                    node = node.left
                return node.key

            y = node.parent
            while y and y.key and node != y.left:
                node = y
                y = y.parent
            if y:
                return y.key
        return ""


    def getStat(self):
        return self.stat


    def __str__(self):
        return self.stat.__str__()