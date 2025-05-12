#!/usr/bin/env python
from numpy.random import uniform
from math import log, sqrt, sin, pi, exp
from time import time


def reject() -> float:
    while True:
        Y1 = -log(uniform())
        Y2 = -log(uniform())

        if Y2 >= (Y1 - 1) ** 2 / 2:
            if uniform() < 0.5:
                return Y1
            return -Y1


def polar() -> float:
    R_square = -2 * log(1 - uniform())
    theta = 2 * pi * uniform()
    return sqrt(R_square) * sin(theta)


def uniforms_ratio() -> float:
    const_coeff = 4 * exp(-0.5) / sqrt(2.0)
    while True:
        U1 = uniform()
        U2 = 1.0 - uniform()
        Z = const_coeff * (U1 -  0.5) / U2
        ZZ = Z * Z / 4.0

        if ZZ <= -log(U2):
            return Z


n_sims = 10_000
print(f'Se estimará una normal haciendo {n_sims} simulaciones')
print(f'Esperanza: 0,   Varianza: 1')
for generator in [reject, polar, uniforms_ratio]:
    values = []
    acc_mean = 0

    start = time()
    for _ in range(n_sims):
        X = generator()
        acc_mean += X
        values.append(X)
    elapsed = time() - start

    mean = acc_mean / n_sims

    acc_variance = 0
    for v in values:
        acc_variance += (v - mean) ** 2

    print(f'\n----- {generator.__name__} (tardó {elapsed} segundos) -----')
    print(f'Estimación de la esperanza: {mean}')
    print(f'Estimación de la varianza: {acc_variance / n_sims}')
