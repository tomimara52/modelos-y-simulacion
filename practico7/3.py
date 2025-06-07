#!/usr/bin/env python
from numpy import float64
from numpy.random import uniform
from numpy.typing import NDArray


"""
este código usa el test de Kolmogorov-Smirnov para 
ver si una muestra proviene de una U(0, 1)
"""


def calculate_D(sample: list[float] | NDArray[float64]) -> float:
    sample.sort()
    n = len(sample)

    D = 1 / n - sample[0]

    for i, u in enumerate(sample):
        j = i + 1
        D = max(D, j / n - u, u - (j - 1) / n)

    return D


def estimate_pvalue(sample: list[float], n_sims: int) -> float:
    D = calculate_D(sample)

    n = len(sample)

    bigger_than_D = 0

    for _ in range(n_sims):
        uniforms = uniform(size=n)
        D_j = calculate_D(uniforms)

        if D_j >= D:
            bigger_than_D += 1

    return bigger_than_D / n_sims


sample = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
n_sims = 10_000
print(f"p-valor con {n_sims} simulaciones: {estimate_pvalue(sample, n_sims)}")
