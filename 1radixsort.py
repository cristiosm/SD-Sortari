import random
import time

def radixsort(nums):
    # determinarea valorii maxime din nums
    max_value = max(nums)

    # determinarea numarului maxim de cifre
    num_digits = len(str(max_value))

    # loop prin cifre, de la cifra unitatilor la cea mai semnificativa cifra
    for i in range(num_digits):
        # lista pentru fiecare cifra
        buckets = [[] for _ in range(10)]

        # loop prin fiecare numar si distribuirea lor în bucket-uri
        for num in nums:
            digit = (num // 10 ** i) % 10
            buckets[digit].append(num)

        # reconstruirea listei cu numerele sortate la fiecare cifra
        nums = [num for bucket in buckets for num in bucket]

    return nums

for x in range(1,6):
    fileout = open(f"2.radixsort{x}.out", "w")
    for y in range(1,21):
        s=0
        file = open(f"z.lista{x}.{y}.in", "r")
        for i in range(1000):
            lista=file.readline()
            start_time = time.time()
            radixsort(eval(lista))
            end_time = time.time()
            s=s+(end_time - start_time)*1000
        fileout.write((str(s/1000)+'\n'))