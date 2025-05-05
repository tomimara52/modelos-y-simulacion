#!/usr/bin/env python
from numpy.random import uniform, binomial
from math import comb
from time import time

probs = [0.15, 0.2, 0.1, 0.35, 0.2]


def sim_trans_inv(c, n, p) -> int:
    U = uniform()

    if U < 0.35:
        return 3
    elif U < 0.55:
        return 1
    elif U < 0.75:
        return 4
    elif U < 0.9:
        return 0
    else:
        return 2


def sim_reject(c: float, n: int, p: float) -> int:
    while True:
        Y = binomial(n, p)
        U = uniform()

        if U < probs[Y] / (c * bin_prob(n, p, Y)):
            return Y


def bin_prob(n: int, p: float, x: int) -> float:
    if x < 0 or x > n:
        return 0

    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))


n = 4
p = 0.45

print(f'Valores posibles de Bin({n}, {p}):')
for x in range(n + 1):
    print(f'\tP(Y = {x}) = {bin_prob(n, p, x)}')
print()

c = 0
print(f'Valores de P(X = x_i) / P(Y = y_i):')
for x in range(n + 1):
    ratio = probs[x] / bin_prob(n, p, x)
    print(f'\tP(X = {x}) / P(Y = {x}) = {ratio}')
    if ratio > c:
        c = ratio
print(f'Menor c posible: {c}\n')


for (i, probability) in enumerate(probs):
    print(f'P(X = {i}): {probability}')
print()

n_sims = 10_000

for generator in [sim_trans_inv, sim_reject]:
    print(f'---------------------------------- {generator.__name__} ----------------------------------')

    freqs = [0] * (n+1)

    start = time()

    for _ in range(n_sims):
        freqs[generator(c, n, p)] += 1

    elapsed = time() - start
    print(f'Tardó {elapsed} segundos')

    for (i, f) in enumerate(freqs):
        print(f'Estimación de P(X = {i}): {f / n_sims}')
    print()
