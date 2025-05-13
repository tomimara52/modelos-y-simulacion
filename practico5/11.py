#!/usr/bin/env python
from numpy.random import uniform, normal
from math import pi, tan
from time import time


def cauchy_ratio_uniforms(l: float) -> float:
    while True:
        U = uniform()
        V = 2 * uniform() - 1

        if U*U + V*V < 1:
            return l * V / U


def cauchy_transinv(l: float) -> float:
    return l * tan(pi * (uniform() - 0.5))


l_arr = [1.0, 2.5, 0.3]
n_sims = 10_000
exact_value = 0.5

print(f'P(-λ < X < λ) = {exact_value}')

print(f'\nEstimaciones usando radio de uniformes')
for l in l_arr:
    
    in_interval = 0
    start = time()
    for _ in range(n_sims):
        if -l < cauchy_ratio_uniforms(l) < l:
            in_interval += 1
    elapsed = time() - start

    print(f'\n\t----- Cauchy(λ = {l}) (tardó {elapsed} segundos)-----')
    print(f'\tValor estimado de P(-λ < X < λ): {in_interval / n_sims}')


print(f'\nEstimaciones usando transformada inversa')
for l in l_arr:
    
    in_interval = 0
    start = time()
    for _ in range(n_sims):
        if -l < cauchy_transinv(l) < l:
            in_interval += 1
    elapsed = time() - start

    print(f'\n\t----- Cauchy(λ = {l}) (tardó {elapsed} segundos)-----')
    print(f'\tValor estimado de P(-λ < X < λ): {in_interval / n_sims}')
