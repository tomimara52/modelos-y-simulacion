#!/usr/bin/env python
from math import log
from numpy.random import uniform


def exponential(l: float) -> float:
    return -log(1 - uniform()) / l


def comp_exponential(l_arr: list[float], p_arr: list[float]) -> float:
    U = uniform()
    probs_sum = p_arr[0]
    i = 0

    while U >= probs_sum:
        i += 1
        probs_sum += p_arr[i]

    return exponential(l_arr[i])


n_sims = 100_000
l_arr = [1/3, 1/5, 1/7]
p_arr = [0.5, 0.3, 0.2]

exact_mean = sum([p * 1 / l for (l, p) in zip(l_arr, p_arr)])
print(f'Esperanza exacta: {exact_mean}')

acc = 0
for _ in range(n_sims):
    acc += comp_exponential(l_arr, p_arr)

print(f'Esperanza estimada con {n_sims} simulaciones: {acc / n_sims}')
