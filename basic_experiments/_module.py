import time
from random import Random
from functools import cache, lru_cache

@lru_cache(maxsize=10)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        # print(n)
        return fibo(n - 1) + fibo(n - 2)


start = time.perf_counter()

fibo(40)

end = time.perf_counter()

print(end-start)