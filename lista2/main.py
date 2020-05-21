import argparse
from sort import *
import random

def main():
    parser = argparse.ArgumentParser(description='Program help you to sort arrays of objects with define compare() operation, with given algorithm and order.')
    parser.add_argument('--type', choices=["insert", "merge", "quick", "dpqs", "hybrid"], type=str, help='Algorithm type.', required=True)
    parser.add_argument('--comp', default="<=", type=str, help='Order, default \'<=\'. You can use this command to type python lambda function and \
        compare other objects than numbers for ex.: to compare chars type \'ord(x) <= ord(y).')
    parser.add_argument('--stat', type=str, nargs=2, metavar=('file', 'k'), help='First - file_name, second - k as repeat.')

    args = parser.parse_args()

    algorithm = dict([
        ('insert', Sort.insert),
        ('merge', Sort.merge),
        ('dpqs', Sort.dpqs),
        ('hybrid', Sort.hybrid),
        ('quick', Sort.quick)
    ])

    if str(args.comp).find('x') >= 0 and str(args.comp).find('y') >= 0:
        comp = lambda x, y: eval(args.comp)
    else:
        comp = lambda x, y: eval("float(x)" + args.comp + "float(y)")
    
    if(args.stat):
        file, k = args.stat

        for n in range(200, 5001, 200):
            for i in range(int(k)):
                keys = [random.random() for _ in range(n)]
                stat = algorithm[args.type](comp, keys, True)
                stat.write_stat_to_file(file)
        
        if int(k)>1:
            out = ""
            with open(file, "r") as f:
                lines = f.readlines()

                nn = 200
                comparisions = 0
                transpositions = 0
                time = 0
                print(len(lines))
                for l in lines:
                    lsplited = l.split()
                        
                    if nn == int(lsplited[0]):
                        comparisions += int(lsplited[1])
                        transpositions += int(lsplited[2])
                        time += float(lsplited[3])
                    else:
                        out +=  str(nn) + "\t" + \
                                str(comparisions//int(k)) + "\t" + \
                                str(transpositions//int(k)) + "\t" + \
                                str(time/float(k)) + "\n"
                        nn = int(lsplited[0])
                        comparisions = int(lsplited[1])
                        transpositions = int(lsplited[2])
                        time = float(lsplited[3])
                        
                out +=  str(nn) + "\t" + \
                        str(comparisions//int(k)) + "\t" + \
                        str(transpositions//int(k)) + "\t" + \
                        str(time/float(k)) + "\n"
                        
            with open(file, "w") as f:
                f.write(out)

    else:
        print("Insert elements separated by a space.")
        keys = input(":").split()
        stat = algorithm[args.type](comp, keys, False)
        stat.print()

if __name__ == '__main__':
    main()