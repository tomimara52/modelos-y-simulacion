#!/usr/bin/env python
from numpy.random import uniform


def cauchy(l: float) -> float:
    while True:
        U = uniform()
        V = 2 * uniform() - 1

        if U*U + V*V < 1:
            return l * V / U


l_arr = [1.0, 2.5, 0.3]
n_sims = 10_000
exact_value = 0.5

print(f'P(-λ < X < λ) = {exact_value}')

for l in l_arr:
    print(f'\n----- Cauchy(λ = {l}) -----')
    
    in_interval = 0
    for _ in range(n_sims):
        if -l < cauchy(l) < l:
            in_interval += 1

    print(f'Valor estimado de P(-λ < X < λ): {in_interval / n_sims}')
