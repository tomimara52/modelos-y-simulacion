#!/usr/bin/env python
from math import exp, factorial
from numpy.random import uniform
from time import time

# P(Y > 2) = 1 - P(Y <= 2) = 0.002_769_395_716
P = 1 - 0.002_769_395_716


def prob_poisson(l: int, i: int) -> float:
    if i < 0:
        return 0

    return exp(-l) * ((l ** i) / factorial(i))


def transinv_bad(l: int) -> int:
    U = uniform()

    i = 0
    F = prob_poisson(l, i)

    while U >= F:
        i += 1
        F += prob_poisson(l, i)

    return i


def transinv_good(l: int) -> int:
    """
    esta iteración rara hace que se vayan iterando en el orden de los valores más probables
    por ejemplo, si l = 10, se hará la iteración en el siguiente orden:
        10, 9, 11, 8, 12, 7, 13, 6, 14, 5, ...
    """

    U = uniform()

    high = l + 1
    low = l - 1
    x = l
    F = prob_poisson(l, x)
    i = 1

    while U >= F:
        if (i % 2) == 0 or low < 0:
            x = high
            high += 1
        else:
            x = low
            low -= 1

        F += prob_poisson(l, x)

    return x


n_sims = 100_000
l = 10

print(f'Valor exacto de P(Y > 2): {P}')

for generator in [transinv_bad, transinv_good]:
    freqs = {}

    start = time()

    for _ in range(n_sims):
        x = generator(l)
        freqs[x] = freqs.get(x, 0) + 1

    elapsed = time() - start

    estimation = 1 - sum([freqs.get(i, 0) / n_sims for i in range(3)])
    print(f'({generator.__name__}) Estimación de P(Y > 2): {estimation} (tardó {elapsed} segundos)')
