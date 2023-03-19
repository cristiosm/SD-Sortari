import random
import time

def shellsort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

for x in range(1,5):
    fileout = open(f"2.shellsort{x}.out", "w")
    for y in range(1,21):
        s=0
        file = open(f"z.lista{x}.{y}.in", "r")
        for i in range(1000):
            lista=file.readline()
            start_time = time.time()
            shellsort(eval(lista))
            end_time = time.time()
            s=s+(end_time - start_time)*1000
        fileout.write((str(s/1000)+'\n'))