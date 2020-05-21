import sys
import random
import time


#share utils to collect statistics
class Stat:
    def __init__(self, length):
        super().__init__()
        self.comparisions = 0
        self.transpositions = 0
        self.correctness = "-"
        self.keys = "-"
        self.length = length
        self.start = 0
        self.stop = 0
        self.msg = ""


    '''
        start measuring time.
    '''
    def startTime(self):
        self.start = time.time()


    '''
        Stop measuring time.
    '''
    def stopTime(self):
        self.stop = time.time()


    '''
        Print msg stderr.
    '''
    def stat_msg(self, msg):
        self.msg += msg


    '''
        Inc comparisions
    '''
    def inc_comp(self):
        self.comparisions += 1


    '''
        Inc comparisions
    '''
    def inc_trans(self):
        self.transpositions += 1


    '''
        Add stat about result correctnes and final algorithm result.
    '''
    def final_stat(self, correctness, keys):
        self.correctness = correctness
        self.keys = keys


    '''
        Print stat.
    '''
    def print(self):
        sys.stderr.write(self.msg)
        sys.stderr.write("Total comparisions: " + str(self.comparisions) + "\n")
        sys.stderr.write("Total transpositions: " + str(self.transpositions) + "\n")
        sys.stderr.write("Correct result: " + str(self.correctness) + "\n")
        sys.stderr.write("Opaerating time: " + str(self.stop-self.start) + "\n")
        print("Table length: ", self.length)
        print(self.keys)


    '''
        Write stat to file
    '''
    def write_stat_to_file(self, file):
        try:
            with open(file, "a") as f:
                f.write(str(self.length) + "\t" +
                        str(self.comparisions) + "\t" +
                        str(self.transpositions) + "\t" +
                        str(self.stop-self.start) + "\n"
                    )
        except:
            sys.stderr.write("Can't write to file.")
            sys.exit(1)





class Sort:
    '''
        Insertion Sort
    '''
    @staticmethod
    def insert(compare, keys, file):
        #stat obj
        stat = Stat(len(keys))
        stat.startTime()

        for i in range(len(keys)): 
    
            key = keys[i] 
            j = i-1
            while j >= 0 and compare(key, keys[j]):
                #stat.stat_msg("Comparision: " + str(key) + " " + str(keys[j]))
                stat.inc_comp()
                #stat.stat_msg(msg="Transposition: " + str(keys[j+1]) + " " + str(keys[j]))
                stat.inc_trans()
                keys[j + 1] = keys[j] 
                j -= 1
            #stat.stat_msg(msg="Transposition: " + str(keys[j + 1]) + " " + str(key))
            stat.inc_trans()
            keys[j + 1] = key 
        
        stat.stopTime()
        stat.final_stat(Sort.check(compare, keys), keys)
        return stat
    

    '''
        Merge Sort
    '''
    @staticmethod
    def merge(compare, keys, file):
        stat = Stat(len(keys))


        def merge(compare, keys, stat):
            if len(keys) > 1:
                middle = len(keys)//2
                L = keys[:middle]
                R = keys[middle:]

                merge(compare, L, stat)
                merge(compare, R, stat)

                #merge two arrays
                i = j = k = 0
                while i < len(L) and j < len(R): 
                    #stat.stat_msg(msg="Comparision: " + str(L[i]) + " " + str(R[j]))
                    stat.inc_comp()
                    if compare(L[i], R[j]): 
                        #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(L[i]))
                        stat.inc_trans()
                        keys[k] = L[i] 
                        i+=1
                    else: 
                        #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(R[j]))
                        stat.inc_trans()
                        keys[k] = R[j] 
                        j+=1
                    k+=1
                
                while i < len(L): 
                    #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(L[i]))
                    stat.inc_trans()
                    keys[k] = L[i] 
                    i+=1
                    k+=1
                
                while j < len(R): 
                    #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(R[j]))
                    stat.inc_trans()
                    keys[k] = R[j] 
                    j+=1
                    k+=1


        stat.startTime()
        merge(compare, keys, stat)
        stat.stopTime()
        stat.final_stat(Sort.check(compare, keys), keys)
        return stat
    
    
    '''
        Quick Sort
    '''
    @staticmethod
    def quick(compare, keys, file):
        stat = Stat(len(keys))


        def partition(compare, keys, start, end, stat):
            pivot = keys[start]
            low = start+1
            high = end
            
            while True:
                while low <= high:
                    #stat.stat_msg(msg="Comparision: " + str(keys[high]) + " " + str(pivot))
                    stat.inc_comp()
                    if not compare(keys[high], pivot):
                        high -= 1
                    else:
                        break

                while low <= high:
                    #stat.stat_msg(msg="Comparision: " + str(keys[low]) + " " + str(pivot))
                    stat.inc_comp()
                    if compare(keys[low], pivot):
                        low += 1
                    else:
                        break

                if low <= high:
                    #stat.stat_msg(msg="Transposition: " + str(keys[low]) + " " + str(keys[high]))
                    stat.inc_trans()
                    keys[low], keys[high] = keys[high], keys[low]
                else:
                    break

            keys[start], keys[high] = keys[high], keys[start]
            return high


        def quick(compare, keys, start, end, stat):
            if start < end:
                pivot = partition(compare, keys, start, end, stat)
                quick(compare, keys, start, pivot-1, stat)
                quick(compare, keys, pivot+1, end, stat)


        stat.startTime()
        quick(compare, keys, 0, len(keys)-1, stat)
        stat.stopTime()
        stat.final_stat(Sort.check(compare, keys), keys)
        return stat
    

    '''
        Dual Pivot Quick Sort. 
    '''
    @staticmethod
    def dpqs(compare, keys, file):
        stat = Stat(len(keys))


        def c_partition(compare, keys, p, q, start, end, stat):
            i = start+1
            k = end-1
            j = i
            d = 0
            while j<=k:
                if d>0:
                    #stat.stat_msg(msg="Comparision: " + str(p) + " " + str(keys[j]))
                    stat.inc_comp()
                    if not compare(p, keys[j]):
                        #stat.stat_msg(msg="Transposition: " + str(keys[i]) + " " + str(keys[j]))
                        stat.inc_trans()
                        keys[i], keys[j] = keys[j], keys[i]
                        i += 1
                        j += 1
                        d += 1
                    else:
                        #stat.stat_msg(msg="Comparision: " + str(q) + " " + str(keys[j]))
                        stat.inc_comp()
                        if not compare(q, keys[j]):
                            j += 1
                        else:
                            #stat.stat_msg(msg="Transposition: " + str(keys[j]) + " " + str(keys[k]))
                            stat.inc_trans()
                            keys[k], keys[j] = keys[j], keys[k]
                            k -= 1
                            d -= 1
                else:
                    while not compare(keys[k], q):
                        #stat.stat_msg(msg="Comparision: " + str(keys[k]) + " " + str(q))
                        stat.inc_comp()
                        k -= 1
                        d -= 1
                    if j <= k:
                        #stat.stat_msg(msg="Comparision: " + str(p) + " " + str(keys[k]))
                        stat.inc_comp()
                        if not compare(p, keys[k]):
                            #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(keys[j]))
                            #stat.stat_msg(msg="Transposition: " + str(keys[j]) + " " + str(keys[i]))
                            #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(keys[i]))
                            stat.inc_trans() 
                            stat.inc_trans()
                            stat.inc_trans()
                            keys[k], keys[j], keys[i] = keys[j], keys[i], keys[k]
                            d += 1
                            i += 1
                        else:
                            #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(keys[j]))
                            stat.inc_trans()
                            keys[k], keys[j] = keys[j], keys[k]
                        j += 1

            #stat.stat_msg(msg="Transposition: " + str(keys[i-1]) + " " + str(keys[start]))
            #stat.stat_msg(msg="Transposition: " + str(keys[end]) + " " + str(keys[k+1]))
            stat.inc_trans()
            stat.inc_trans()
            keys[start], keys[i-1] = keys[i-1], keys[start]
            keys[k+1], keys[end] = keys[end], keys[k+1]    
            return i-1, k+1


        def dpqs(compare, keys, start, end, stat):
            if start < end:
                #stat.stat_msg(msg="Comparision: " + str(keys[end]) + " " + str(keys[start]))
                stat.inc_comp()
                if compare(keys[end], keys[start]):
                    #stat.stat_msg(msg="Transposition: " + str(keys[end]) + " " + str(keys[start]))
                    stat.inc_trans()
                    keys[end], keys[start] = keys[start], keys[end]
                p = keys[start]
                q = keys[end]
                posp, posq = c_partition(compare, keys, p, q, start, end, stat)

                dpqs(compare, keys, start, posp-1, stat)
                dpqs(compare, keys, posp+1, posq-1, stat)
                dpqs(compare, keys, posq+1, end, stat)


        stat.startTime()
        dpqs(compare, keys, 0, len(keys)-1, stat)
        stat.stopTime()
        stat.final_stat(Sort.check(compare, keys), keys)
        return stat


    '''
        Dual pivot quick sort with insertion sort for parts smaller than limit, deafult limit value is 10. 
    '''
    @staticmethod
    def hybrid(compare, keys, file, LIMIT=5):
        stat = Stat(len(keys))


        def c_partition(compare, keys, p, q, start, end, stat):
            i = start+1
            k = end-1
            j = i
            d = 0
            while j<=k:
                if d>0:
                    #stat.stat_msg(msg="Comparision: " + str(p) + " " + str(keys[j]))
                    stat.inc_comp()
                    if not compare(p, keys[j]):
                        #stat.stat_msg(msg="Transposition: " + str(keys[i]) + " " + str(keys[j]))
                        stat.inc_trans()
                        keys[i], keys[j] = keys[j], keys[i]
                        i += 1
                        j += 1
                        d += 1
                    else:
                        #stat.stat_msg(msg="Comparision: " + str(q) + " " + str(keys[j]))
                        stat.inc_comp()
                        if not compare(q, keys[j]):
                            j += 1
                        else:
                            #stat.stat_msg(msg="Transposition: " + str(keys[j]) + " " + str(keys[k]))
                            stat.inc_trans()
                            keys[k], keys[j] = keys[j], keys[k]
                            k -= 1
                            d -= 1
                else:
                    while not compare(keys[k], q):
                        #stat.stat_msg(msg="Comparision: " + str(keys[k]) + " " + str(q))
                        stat.inc_comp()
                        k -= 1
                        d -= 1
                    if j <= k:
                        #stat.stat_msg(msg="Comparision: " + str(p) + " " + str(keys[k]))
                        stat.inc_comp()
                        if not compare(p, keys[k]):
                            #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(keys[j]))
                            #stat.stat_msg(msg="Transposition: " + str(keys[j]) + " " + str(keys[i]))
                            #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(keys[i]))
                            stat.inc_trans() 
                            stat.inc_trans()
                            stat.inc_trans()
                            keys[k], keys[j], keys[i] = keys[j], keys[i], keys[k]
                            d += 1
                            i += 1
                        else:
                            #stat.stat_msg(msg="Transposition: " + str(keys[k]) + " " + str(keys[j]))
                            stat.inc_trans()
                            keys[k], keys[j] = keys[j], keys[k]
                        j += 1

            #stat.stat_msg(msg="Transposition: " + str(keys[i-1]) + " " + str(keys[start]))
            #stat.stat_msg(msg="Transposition: " + str(keys[end]) + " " + str(keys[k+1]))
            stat.inc_trans()
            stat.inc_trans()
            keys[start], keys[i-1] = keys[i-1], keys[start]
            keys[k+1], keys[end] = keys[end], keys[k+1]    
            return i-1, k+1


        def dpqs(compare, keys, start, end, stat, LIMIT):
            if end-start <= LIMIT: #insertion sort
                for ii in range(end-start+1):
                    i = start + ii
                    key = keys[i] 
                    j = i-1
                    while j >= 0 and compare(key, keys[j]):
                            #stat.stat_msg(msg="Comparision: " + str(key) + " " + str(keys[j]))
                            stat.inc_comp()
                            #stat.stat_msg(msg="Transposition: " + str(keys[j+1]) + " " + str(keys[j]))
                            stat.inc_trans()
                            keys[j + 1] = keys[j] 
                            j -= 1
                    #stat.stat_msg(msg="Transposition: " + str(keys[j + 1]) + " " + str(key))
                    stat.inc_trans()
                    keys[j + 1] = key 

            else: #quick sort
                #stat.stat_msg(msg="Comparision: " + str(keys[end]) + " " + str(keys[start]))
                stat.inc_comp()
                if compare(keys[end], keys[start]):
                    #stat.stat_msg(msg="Transposition: " + str(keys[end]) + " " + str(keys[start]))
                    stat.inc_trans()
                    keys[end], keys[start] = keys[start], keys[end]
                p = keys[start]
                q = keys[end]
                posp, posq = c_partition(compare, keys, p, q, start, end, stat)

                dpqs(compare, keys, start, posp-1, stat, LIMIT)
                dpqs(compare, keys, posp+1, posq-1, stat, LIMIT)
                dpqs(compare, keys, posq+1, end, stat, LIMIT)


        stat.startTime()
        dpqs(compare, keys, 0, len(keys)-1, stat, LIMIT)
        stat.stopTime()
        stat.final_stat(Sort.check(compare, keys), keys)
        return stat



    '''
        Radix sort.
    '''
    @staticmethod
    def radix(compare, keys, file):
        
        def counting(keys, file, exp, stat, n):
            output = [0] * (n) 
            count = [0] * (10) 
        
            for key in keys: 
                index = int(key/exp) 
                count[index%10] += 1

            for i in range(1,10): 
                    count[i] += count[i-1] 
    
            for key in reversed(keys):
                index = int(key/exp)
                output[count[index%10]-1] = key 
                count[index%10] -= 1

            i = 0
            for i in range(n):
                keys[i] = output[i]


        stat = Stat(len(keys))

        stat.startTime()
        keys = [int(key) for key in keys]
        max_val = max(keys)
        exp = 1
        n = len(keys)

        while max_val >= exp:
            counting(keys, file, exp, stat, n)
            exp *= 10

        try:
            if compare(2,1):
                keys = list(reversed(keys))
        except:
            print("Wrong comparision function for radix sort.")
            sys.exit(1)

        stat.stopTime()
        stat.final_stat(Sort.check(lambda x, y : x <= y, keys), keys)
        stat.comparisions = "-"
        stat.transpositions = "-"
        return stat
    
    
    '''
        Check order
    '''
    @staticmethod
    def check(compare, keys):
        for i in range(len(keys)-1):
            if not compare(keys[i], keys[i+1]):
                return False
        return True