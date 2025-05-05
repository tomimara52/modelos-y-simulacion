#!/usr/bin/env python
from numpy.random import uniform
from math import comb
from time import time

def binomial_transinv(n: int, p: float) -> int:
    U = uniform()
    prob = lambda x: comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
    i, F = 0, prob(0)

    while U >= F:
        i += 1
        F += prob(i)

    return i


def binomial_simulate(n: int, p: float) -> int:
    successes = 0

    for _ in range(n):
        if uniform() < p:
            successes += 1

    return successes


n_simulations = 10_000
n = 10
p = 0.3

for generator in [binomial_transinv, binomial_simulate]:
    print(f'------------------ {generator.__name__} ------------------')
    freqs = [0] * n

    start = time()

    for _ in range(n_simulations):
        freqs[generator(n, p)] += 1 

    elapsed = time() - start
    print(f'Tardó {elapsed} segundos')

    print(f'Valores estimados de P(X = i):')
    for (i, f) in enumerate(freqs):
        estimated_prob = f / n_simulations
        print(f'{i}: {estimated_prob}', end=', ')

    print('\n')
    

print(f'Valores exactos de P(X = i):')
for i in range(n + 1):
    prob = comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    print(f'{i}: {prob}', end=', ')

print()
