import random

for x in range(1,5):
    for y in range(1,21):
        file=open(f"z.lista{x}.{y}.in", "w")

        for i in range(1000):
            def generate(n, min_value, max_value):
                return [random.randint(min_value, max_value) for _ in range(n)]

            result = generate(10**x, 1, 10**y)
            file.write(str(result) + "\n")

with open('1radixsort.py') as f:
    code = compile(f.read(), '1radixsort.py', 'exec')
    exec(code)

with open('1mergesort.py') as f:
    code = compile(f.read(), '1mergesort.py', 'exec')
    exec(code)

with open('1shellsort.py') as f:
    code = compile(f.read(), '1shellsort.py', 'exec')
    exec(code)

with open('1introsort.py') as f:
    code = compile(f.read(), '1introsort.py', 'exec')
    exec(code)