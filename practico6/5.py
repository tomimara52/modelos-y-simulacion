#!/usr/bin/env python
from math import sqrt
from numpy.random import uniform
import scipy.stats as st


def simulate() -> int:
    n = 2
    u = uniform()

    while True:
        v = uniform()

        if v < u:
            return n

        u = v
        n += 1


def estimate_c() -> tuple[float, float]:
    n = 1
    mean = simulate()
    s2 = 0

    while n < 100 or s2 / n >= 0.01:
        next_mean = mean + (simulate() - mean) / (n + 1)
        s2 = (1 - 1 / n) * s2 + (n + 1) * (next_mean - mean) ** 2
        mean = next_mean
        n += 1

    return mean, s2


def estimate_d(
    confidence: float,
    interval_length: float,
) -> float:
    alpha_2 = (1 - confidence) / 2
    z_alpha_2 = st.norm.ppf(1 - alpha_2)
    d = interval_length / (2 * z_alpha_2)

    n = 1
    mean = simulate()
    s2 = 0

    while n < 100 or sqrt(s2 / n) >= d:
        next_mean = mean + (simulate() - mean) / (n + 1)
        s2 = (1 - 1 / n) * s2 + (n + 1) * (next_mean - mean) ** 2
        mean = next_mean
        n += 1

    return mean


print(f"Estimación de e con varianza menor a 0.01: {estimate_c()}")
print(
    f"Estimación de e con longitud de intervalo de confianza del 95% menor a 0.1: {estimate_d(0.95, 0.1)}"
)
