#!/usr/bin/env python
from numpy import sqrt
from scipy.stats import norm
from numpy.random import uniform


def uniform_in_square() -> float:
    return uniform() * 2 - 1


def estimate_a() -> float:
    n = 1
    x = uniform_in_square()
    y = uniform_in_square()
    p = int(x**2 + y**2 <= 1)

    while n < 100 or sqrt(p * (1 - p) / n) > 0.01:
        n += 1

        x = uniform_in_square()
        y = uniform_in_square()

        bernoulli = int(x**2 + y**2 <= 1)

        p = p + (bernoulli - p) / n

    return p


def estimate_b(
    confidence: float,
    interval_length: float,
) -> tuple[float, int]:
    alpha_2 = (1 - confidence) / 2
    z_alpha_2 = norm.ppf(1 - alpha_2)
    d = interval_length / (2 * z_alpha_2)

    n = 1
    x = uniform_in_square()
    y = uniform_in_square()
    p = int(x**2 + y**2 <= 1)

    while n < 100 or sqrt(p * (1 - p) / n) > d:
        n += 1

        x = uniform_in_square()
        y = uniform_in_square()

        bernoulli = int(x**2 + y**2 <= 1)

        p = p + (bernoulli - p) / n

    return p, n


print(4 * estimate_a())

p, n = estimate_b(0.95, 0.1)
print(f"Estimación con intervalo de confianza 95% con ancho menor a 0.1: {4 * p}")
print(f"Se hicieron {n} iteraciones")
