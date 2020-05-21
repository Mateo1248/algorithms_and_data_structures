import random
import time

def binary_search(A, element, counter=0):
    if len(A) > 0:
        middle = len(A)//2
        if A[middle] < element:
            return binary_search(A[middle+1:], element, counter+1)
        elif A[middle] > element:
            return binary_search(A[:middle], element, counter+2)
        else:
            return 1, counter
    else:
        return 0, counter

def main():
    n = int(input("Długość tablicy: "))
    A = [random.randint(0,n*10) for _ in range(n)]
    A.sort()
    print("Tblica:", A)
    el = int(input("Wyszukiwany element: "))
    res, comp = binary_search(A, el)
    print(f"Znaleziono: {res}, porównania: {comp}.")

if __name__ == '__main__':
    main()