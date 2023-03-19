import math
import random
import time


def introsort(arr):
    # determinam adancimea maxima a stivei de recursivitate
    depth_limit = math.floor(2*math.log2(len(arr)))
    # sortam șirul folosind Quicksort
    quickSort(arr, 0, len(arr)-1, depth_limit)

# Quicksort cu limita de adancime a stivei de recursivitate
def quickSort(arr, lo, hi, depth_limit):
    # daca dimensiunea sirului este micq, folosim Insertion Sort
    if hi-lo < 20:
        insertionSort(arr, lo, hi)
        return
    # dacă adqncimea stivei de recursivitate depqșește limita, folosim Heapsort
    if depth_limit == 0:
        heapSort(arr, lo, hi)
        return
    # alegem pivotul și imparțim sirul în doua sub-siruri
    pivot = medianOfThree(arr, lo, hi)
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    # sortam cele doua sub-siruri cu Quicksort
    quickSort(arr, lo, j, depth_limit-1)
    quickSort(arr, j+1, hi, depth_limit-1)

# Heapsort
def heapSort(arr, lo, hi):
    # construim max-heap-ul
    heapify(arr, lo, hi)
    # extragem elementele in ordine descrescatoare și le asezam la sfarsitul sirului
    for i in range(hi, lo, -1):
        arr[lo], arr[i] = arr[i], arr[lo]
        siftDown(arr, lo, lo, i-1)

def medianOfThree(arr, lo, hi):
    mid = (lo + hi) // 2
    if arr[lo] > arr[mid]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    if arr[lo] > arr[mid]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    return arr[mid]

# construim un max-heap
def heapify(arr, lo, hi):
    n = hi - lo + 1
    for i in range(lo + n//2, lo-1, -1):
        siftDown(arr, lo, i, hi)

# coboram elementul i in max-heap pana cand se asează în locul potrivit
def siftDown(arr, lo, i, hi):
    while True:
        left = lo + 2*(i - lo) + 1
        right = lo + 2*(i - lo) + 2
        maxChild = i
        if left <= hi and arr[left] > arr[maxChild]:
            maxChild = left
        if right <= hi and arr[right] > arr[maxChild]:
            maxChild = right
        if maxChild == i:
            break
        arr[i], arr[maxChild] = arr[maxChild], arr[i]
        i = maxChild

# sortam elementele sirului cu Insertion Sort
def insertionSort(arr, lo, hi):
    for i in range(lo+1, hi+1):
        j = i
        while j > lo and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

for x in range(1,5):
    fileout = open(f"2.introsort{x}.out", "w")
    for y in range(1,21):
        s=0
        file = open(f"z.lista{x}.{y}.in", "r")
        for i in range(1000):
            lista=file.readline()
            start_time = time.time()
            introsort(eval(lista))
            end_time = time.time()
            s=s+(end_time - start_time)*1000
        fileout.write((str(s/1000)+'\n'))