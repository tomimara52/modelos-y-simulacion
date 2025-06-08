#!/usr/bin/env python
from typing import Callable
from numpy import float64
from numpy.random import uniform
from numpy.typing import NDArray
from math import exp


"""
este código usa el test de Kolmogorov-Smirnov para 
ver si una muestra proviene de una exponencial con media 50
"""


def calculate_D(
    sample: list[float] | NDArray[float64], F: Callable[[float], float]
) -> float:
    sample.sort()
    n = len(sample)

    D = 1 / n - sample[0]

    for i, u in enumerate(sample):
        j = i + 1
        D = max(D, j / n - F(u), F(u) - (j - 1) / n)

    return D


def estimate_pvalue(sample: list[float], n_sims: int) -> float:
    D = calculate_D(sample, lambda x: 1 - exp(-x / 50))

    n = len(sample)

    bigger_than_D = 0

    for _ in range(n_sims):
        uniforms = uniform(size=n)
        D_j = calculate_D(uniforms, lambda x: x)

        if D_j >= D:
            bigger_than_D += 1

    return bigger_than_D / n_sims


sample = [
    86.0,
    133.0,
    75.0,
    22.0,
    11.0,
    144.0,
    78.0,
    122.0,
    8.0,
    146.0,
    33.0,
    41.0,
    99.0,
]
n_sims = 10_000
print(f"p-valor con {n_sims} simulaciones: {estimate_pvalue(sample, n_sims)}")
