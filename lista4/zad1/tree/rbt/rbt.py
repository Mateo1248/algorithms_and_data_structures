from tree.tree import *
from utils.utils import *


class RBT(Tree):
    '''
        Red black tree.
    '''

    def __init__(self):
        super().__init__()
        self.TNULL = Node(None)
        self.TNULL.color = Color.BLACK
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL


    def delete(self, key:str):
        self.stat.delete()
        self.__delete_node_helper(self.root, key)

    def __delete_node_helper(self, node, key):
        # find the node containing key
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            return
        
        self.stat.dec()

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self.__fix_delete(x)


    def __fix_delete(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == Color.RED:
                    # case 3.1
                    s.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == Color.BLACK and s.right.color == Color.BLACK:
                    # case 3.2
                    s.color = Color.RED
                    x = x.parent
                else:
                    if s.right.color == Color.BLACK:
                        # case 3.3
                        s.left.color = Color.BLACK
                        s.color = Color.RED
                        self.right_rotate(s)
                        s = x.parent.right

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = Color.BLACK
                    s.right.color = Color.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == Color.RED:
                    # case 3.1
                    s.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == Color.BLACK and s.right.color == Color.BLACK:
                    # case 3.2
                    s.color = Color.RED
                    x = x.parent
                else:
                    if s.left.color == Color.BLACK:
                        # case 3.3
                        s.right.color = Color.BLACK
                        s.color = Color.RED
                        self.left_rotate(s)
                        s = x.parent.left 

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = Color.BLACK
                    s.left.color = Color.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def insert(self, keyy: str):
        self.stat.insert() #stat inc

        def restore(k: Node):
            while k.parent.color == Color.RED:
                if k.parent == k.parent.parent.right:
                    u = k.parent.parent.left # uncle
                    if u.color == Color.RED:
                        u.color = Color.BLACK
                        k.parent.color = Color.BLACK
                        k.parent.parent.color = Color.RED
                        k = k.parent.parent
                    else:
                        if k == k.parent.left:
                            k = k.parent
                            self.right_rotate(k)
                        k.parent.color = Color.BLACK
                        k.parent.parent.color = Color.RED
                        self.left_rotate(k.parent.parent)
                else:
                    u = k.parent.parent.right # uncle

                    if u.color == Color.RED:
                        u.color = Color.BLACK
                        k.parent.color = Color.BLACK
                        k.parent.parent.color = Color.RED
                        k = k.parent.parent 
                    else:
                        if k == k.parent.right:
                            k = k.parent
                            self.left_rotate(k)
                        k.parent.color = Color.BLACK
                        k.parent.parent.color = Color.RED
                        self.right_rotate(k.parent.parent)
                if k == self.root:
                    break
            self.root.color = Color.BLACK


        key = Utils.match(keyy)
        if key:
            self.stat.inc() #stat inc
            node = Node(key)
            node.parent = None
            node.data = key
            node.left = self.TNULL
            node.right = self.TNULL
            node.color = Color.RED 
            y = None
            x = self.root

            while x != self.TNULL:
                y = x
                if node.data < x.data:
                    x = x.left
                else:
                    x = x.right

            node.parent = y
            if y == None:
                self.root = node
            elif node.data < y.data:
                y.left = node
            else:
                y.right = node

            if node.parent == None:
                node.color = 0
                return

            if node.parent.parent == None:
                return

            restore(node)


    def left_rotate(self, x: Node):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    
    def right_rotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y