#!/usr/bin/env python
import time
from math import exp
from numpy.random import uniform

def exact(N: int) -> float:
    value = 0

    for k in range(1, N+1):
        value += exp(k / N)

    return value


def estimate(N: int, M: int) -> float:
    value = 0

    for _ in range(M):
        random = int(N * uniform()) + 1
        value += exp(random / N)

    return N * (1 / M) * value


def estimate_M_first(N: int, M: int) -> float:
    value = 0

    for k in range(1, M+1):
        value += exp(k / N)

    return N * (1 / M) * value


start = time.time()
exact = exact(10000)
elapsed = time.time() - start
print(f'Exact value of sum with N=10000: {exact} (took {elapsed} seconds)')

start = time.time()
estimation = estimate(10000, 100)
elapsed = time.time() - start
print(f'Estimation value of sum with N=10000 using 100 random values: {estimation} (took {elapsed} seconds)')

start = time.time()
estimation = estimate_M_first(10000, 100)
elapsed = time.time() - start
print(f'Estimation value of sum with N=10000 using 100 first values: {estimation} (took {elapsed} seconds)')
