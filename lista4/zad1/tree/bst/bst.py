from utils.utils import *
from tree.tree import *


class BST(Tree):
    '''
        Binary search tree.
    '''


    def __init__(self):
        super().__init__()
        self.root = None


    def insert(self, key: str):
        self.stat.insert() #stat inc

        def insert_(new_key, root):
            if root.key > new_key:
                if root.left:
                    insert_(new_key, root.left)
                else:
                    root.left = Node(new_key, parent=root)
            else:
                if root.right:
                    insert_(new_key, root.right)
                else:
                    root.right = Node(new_key, parent=root)


        new_key = Utils.match(key)
        if new_key:
            self.stat.inc() #stat inc
            if self.root:
                insert_(new_key, self.root)
            else:
                self.root = Node(new_key)


    def delete(self, key: str):
        self.stat.delete() #stat inc

        def  min_val(node):
            current = node  
            while(current.left is not None): 
                current = current.left           
            return current

        def del_(root, key):
            if root is None: 
                return root  

            if key < root.key: 
                root.left = del_(root.left, key) 

            elif(key > root.key): 
                root.right = del_(root.right, key) 

            else: 
                self.stat.dec() #stat inc
                if root.left is None : 
                    temp = root.right  
                    root = None 
                    return temp  
                    
                elif root.right is None : 
                    temp = root.left  
                    root = None
                    return temp 
        
                temp = min_val(root.right) 
                root.key = temp.key 
                root.right = del_(root.right , temp.key) 
        
            return root  
        
        self.root = del_(self.root, key)
                

            