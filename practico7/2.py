#!/usr/bin/env python
from scipy.stats import binom, chi2


"""
Código para calcular o simular el p-valor de una muestra
cuya hipótesis nula es que viene de tirar n veces un dado honesto
"""


def calculate_T(N_list: list[int], n: int) -> float:
    return (6 / n) * sum([(N - n / 6) ** 2 for N in N_list])


def pearson_pvalue(N_sample: list[int], n: int) -> float:
    T = calculate_T(N_sample, n)

    return float(chi2.sf(T, 5))


def simulate_T(n: int) -> float:
    N_list = []
    N_sum = 0
    F = 0

    for _ in range(6):
        N = binom.rvs(n - N_sum, 1 / (6 * (1 - F)))

        N_list.append(N)
        N_sum += N
        F += 1 / 6

    return calculate_T(N_list, n)


def estimate_pvalue(N_sample: list[int], n: int, n_sims: int) -> float:
    T = calculate_T(N_sample, n)

    bigger_than_T = 0

    for _ in range(n_sims):
        if simulate_T(n) > T:
            bigger_than_T += 1

    return bigger_than_T / n_sims


sample = [158, 172, 164, 181, 160, 165]
n = 1000

print(f"p-valor usando prueba de Pearson: {pearson_pvalue(sample, n)}")
print(f"p-valor realizando una simulación: {estimate_pvalue(sample, n, 10_000)}")
