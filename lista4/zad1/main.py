from tree.bst.bst import *
from tree.rbt.rbt import *
from hmap.hmap import *
from tree.tree import *
import argparse

def main():
    d_str = {
        "bst" : BST,
        "rbt" : RBT,
        "hmap" : HMAP
    }

    parser = argparse.ArgumentParser(description='Program help you test various data struct type.')
    parser.add_argument('--type', choices=["bst", "rbt", "hmap"], help='Data struct type.')

    args = parser.parse_args()
    print(f"Tree type: {args.type}. \nexit - end program and show statistics.")
    if args.type:
        s = d_str[args.type]()
        stat = s.getStat()

        while True:
            com = input(":").split()
            if com[0] == "exit":
                break
            stat.start()
            
            if len(com) == 2:
                x = eval("s." + com[0])(com[1])
                if x != None:
                    print(x)
            elif len(com) == 1:
                x = eval("s." + com[0])
                if x != None:
                    print(x())
            
            stat.end()
        
        print(f"\n###############################################################\n{s}\n###############################################################")

if __name__ == '__main__':
    main()