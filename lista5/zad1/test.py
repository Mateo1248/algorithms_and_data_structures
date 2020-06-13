from priority_queue  import *
import random
import sys

func = {
    'insert': PriorityQueue.insert,
    'empty': PriorityQueue.empty,
    'top': PriorityQueue.top,
    'pop': PriorityQueue.pop,
    'priority': PriorityQueue.priority,
    'print': PriorityQueue.print
}

pq = PriorityQueue()

try:
    m = int(input('M:'))
except:
    print('Podaj dodatnią liczbe całkowitą będącą liczbą operacji na kolejce.')
    sys.exit(1)

if m == -1:
    file_path = input("Podaj plik:")
    with open(file_path, "r") as file:
        refs = file.readlines()

        for r in refs:
                ref = r.split()
                print(ref, end=" ")
                f = func[ref[0]]
                result = f(pq, *map(int, ref[1:]))

                if ref[0] == 'empty':
                    print(result)
                elif ref[0] == 'top' or ref[0] == 'pop':
                    if result != None:
                        print(result.k)
                else:
                    print()
                
else:
    for _ in range(m):
        ref = input(':').split()
        try:
            f = func[ref[0]]
            result = f(pq, *map(int, ref[1:]))

            if ref[0] == 'empty':
                print(result)
            elif ref[0] == 'top' or ref[0] == 'pop':
                if result != None:
                    print(result.k)
                else:
                    print()

        except:
            print('Błędna funckja!!!')

    

