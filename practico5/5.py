#!/usr/bin/env python
from math import log, inf
from numpy.random import uniform


def exponential(l: float) -> float:
    return -log(1 - uniform()) / l


def min_exponential(l_arr: list[float], n: int) -> float:
    r = inf
    for i in range(n):
        r = min(r, exponential(l_arr[i]))

    return r


def max_exponential(l_arr: list[float], n: int) -> float:
    r = 0
    for i in range(n):
        r = max(r, exponential(l_arr[i]))

    return r


n_sims = 10
l_arr = [1.0, 2.0, 3.0]

print(f'Generación de 10 valores de m (mínimo de {len(l_arr)} exponenciales):')
for _ in range(n_sims):
    print(min_exponential(l_arr, len(l_arr)))


print(f'\nGeneración de 10 valores de M (máximo de {len(l_arr)} exponenciales):')
for _ in range(n_sims):
    print(max_exponential(l_arr, len(l_arr)))
