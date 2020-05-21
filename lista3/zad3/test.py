from main import *
import random
import time
import math

print(f"n\tcomp\ttime\tlog(n)/comp\tlog(n)/time")
for n in range(10000, 100001, 10000):
    comp = 0
    t=0
    for i in range(50):
        A = [random.randint(0,n) for _ in range(n)]
        A.sort()
        element = random.randint(0,n)
        start = time.time()
        _, comp_temp = binary_search(A, element)
        end = time.time()
        t += end-start
        comp +=  comp_temp
    print(f"{n}\t{comp/50}\t{t/50}[s]\t{(math.log(n)/math.log(2))/(comp/50)}\t{(math.log(n)/math.log(2))/(t/50)}[1/s]")