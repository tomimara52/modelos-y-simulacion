#!/usr/bin/env python
from math import sqrt
from numpy.random import uniform
import scipy.stats as st


def simulate() -> int:
    sum = 0
    n = 0

    while sum <= 1:
        sum += uniform()
        n += 1

    return n


def estimate(
    confidence: float,
    interval_length: float,
    fixed_iterations: None | int = None,
) -> tuple[float, float, int]:
    alpha_2 = (1 - confidence) / 2
    z_alpha_2 = st.norm.ppf(1 - alpha_2)
    d = interval_length / (2 * z_alpha_2)

    n = 1
    mean = simulate()
    s2 = 0

    while True:
        next_mean = mean + (simulate() - mean) / (n + 1)
        s2 = (1 - 1 / n) * s2 + (n + 1) * (next_mean - mean) ** 2
        mean = next_mean
        n += 1

        if (
            fixed_iterations is None and n >= 100 and sqrt(s2 / n) < d
        ) or n == fixed_iterations:
            break

    return (mean, sqrt(s2 / n), n)


m, s, n = estimate(1, 1, 1000)
print("Estimación con 1000 iteraciones:")
print(f"\tIteraciones: {n}")
print(f"\tMedia muestral: {m}")
print(f"\tDesviación estándar muestral: {s}")


m, s, n = estimate(0.95, 0.025)
print("\nEstimación con longitud de intervalo de confianza del 95% a lo sumo 0.025:")
print(f"\tIteraciones: {n}")
print(f"\tMedia muestral: {m}")
print(f"\tDesviación estándar muestral: {s}")
