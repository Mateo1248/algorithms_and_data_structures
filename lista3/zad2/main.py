import argparse
import random
import sys

class Stat:
    def __init__(self):
        super().__init__()
        self.comp = 0
        self.tab = []

'''
    Randomized select.
'''
def randomized_select(A, p, r, i, stat):
    
    def randomized_partition(A, p, r, stat):
        i = random.randint(p, r)
        A[p], A[i] = A[i], A[p]
        return partition(A, p, r, stat)

    def partition(A, p, r, stat):
        x = A[p]
        i = p
        j = r
        while i < j:
            while j > p and A[j] >= x:
                j -= 1
                stat.comp += 1
            while i < r and A[i] <= x:
                i += 1
                stat.comp += 1
            if i < j:
                A[j], A[i] = A[i], A[j]
        return j

    if p == r:
        A[p] = [A[p]]
        return stat
    q = randomized_partition(A, p, r, stat)
    k = q - p + 1
    if i <= k:
        randomized_select(A, p, q, i, stat)
    else:
        randomized_select(A, q+1, r, i-k, stat)



'''
    Randomized select.
'''
def select(A, p, r, i, stat):
    
    def partition(A, p, r, x, stat):
        for i in range(p, r): 
            if A[i] == x: 
                stat.comp += 1
                A[r], A[i] = A[i], A[r]
                break
        x = A[r]  
        i = p  
        for j in range(p, r):  
            if (A[j] <= x):  
                stat.comp += 1
                A[j], A[i] = A[i], A[j]  
                i += 1
        A[r], A[i] = A[i], A[r]
        return i 
    
    def med_med(A, p, r, k, stat):
        n = r - p + 1
        median = []
        i=0
        while(i<n//5):
            median.append(findMedian(A, p+i*5, 5, stat))
            i += 1
        if(i*5<n):
            median.append(findMedian(A, p+i*5, n%5, stat))
            i += 1
        if i ==  i:
            return median[i-1]
        else:
            return select(median, 0, i-1, i//2)

    def findMedian(A, l, n, stat): 
        stat.comp += 3
        lis = [] 
        for i in range(l, l + n): 
            lis.append(A[i]) 
        lis.sort() 
        return lis[n // 2]


    pos = partition(A, p, r, med_med(A, p, r, i, stat), stat)
    if (pos - p == i - 1): 
        stat.tab = A
        stat.tab[pos] = [A[pos]] 
        return A[pos]  
    if (pos - p > i - 1):  
        return select(A, p, pos - 1, i, stat)  
    return select(A, pos + 1, r, i - pos + p - 1, stat)  



def main():
        parser = argparse.ArgumentParser(description='Program znajduje k-tą  statystykę.')
        parser.add_argument('-r', action='store_true', help='Losowe dane długości n.')
        parser.add_argument('-p', action='store_true', help='Losowa permutacja zbioru {1,2,...,n}.')

        args = parser.parse_args()

        if (args.r or args.p) and not (args.r and args.p):
            
                n = int(input("n: "))
                k = int(input("k: "))

                if 1 <= k and k <= n:
                    if args.r:
                        A = [random.randint(1, 1000) for _ in range(n)]
                    else:
                        A = [i+1 for i in range(n)]
                        random.shuffle(A)

                    print(f"Wygenerowana tablica: {A}")
                    print()
                    A1 = A[:]
                    A2 = A[:]

                    print("randomized select: ")
                    stat1 = Stat()
                    randomized_select(A1, 0, n-1, k, stat1)
                    print(f"Comparisions: {stat1.comp}")
                    print(A1)
                    print()

                    print("select: ")
                    stat2 = Stat()
                    select(A2, 0, n-1, k, stat2)
                    print(f"Comparisions: {stat2.comp}")
                    print(stat2.tab)
                    print()
                else:
                    print("Błędne dane!")
                    sys.exit(1)
            
        else:
            parser.print_help()



if __name__ == '__main__':
    main()
