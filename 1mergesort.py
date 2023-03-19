import random
import time


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


for x in range(1,6):
    fileout = open(f"2.mergesort{x}.out", "w")
    for y in range(1,21):
        s=0
        file = open(f"z.lista{x}.{y}.in", "r")
        for i in range(1000):
            lista=file.readline()
            start_time = time.time()
            mergesort(eval(lista))
            end_time = time.time()
            s=s+(end_time - start_time)*1000
        fileout.write((str(s/1000)+'\n'))