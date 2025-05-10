#!/usr/bin/env python
from numpy.random import uniform
from math import log, pow, gamma

def pareto(a: float) -> float:
    return pow(1 / uniform(), 1 / a)


def erlang(k: int, mu: float) -> float:
    U = 1
    for _ in range(k):
        U *= 1 - uniform()

    return -log(U) * mu


def weibull(l: float, b: float) -> float:
    return l * pow(log(1 / (1 - uniform())), 1 / b)


n_sims = 10_000
a = 2
mu = 2
k = 2
l = 1
b = 2

acc = 0

for _ in range(n_sims):
    acc += pareto(a)

print(f'Esperanza de variable aleatoria Pareto: {"infinito" if a <= 1 else a/(a - 1)}')
print(f'Esperanza estimada con {n_sims} simulaciones: {acc / n_sims}\n')



acc = 0

for _ in range(n_sims):
    acc += erlang(k, mu)

print(f'Esperanza de variable aleatoria Erlang: {k * mu}')
print(f'Esperanza estimada con {n_sims} simulaciones: {acc / n_sims}\n')



acc = 0

for _ in range(n_sims):
    acc += weibull(l, b)

print(f'Esperanza de variable aleatoria Weibull: {l * gamma(1 + 1/b)}')
print(f'Esperanza estimada con {n_sims} simulaciones: {acc / n_sims}\n')
