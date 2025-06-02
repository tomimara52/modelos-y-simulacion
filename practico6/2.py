#!/usr/bin/env python
from collections.abc import Callable
from numpy.random import uniform
from math import exp, sqrt, inf
from scipy.integrate import quad


def monte_carlo(f: Callable[..., float]) -> tuple[float, float, int]:
    n = 1
    mean = f(uniform())
    s2 = 0

    while n < 100 or sqrt(s2 / n) >= 0.01:
        next_mean = mean + (f(uniform()) - mean) / (n + 1)
        s2 = (1 - 1 / n) * s2 + (n + 1) * (next_mean - mean) ** 2
        mean = next_mean
        n += 1

    return (mean, s2, n)


# i)
print("f(x) = e^x / sqrt(2x)")
f = lambda x: exp(x) / sqrt(2 * x)

print(f"Valor esperado de la integral de f entre 0 y 1: {quad(f, 0, 1)[0]}")

mean, s2, n = monte_carlo(f)

print(f"Valor estimado: {mean}, con {n} iteraciones y desviación estándar {sqrt(s2)}")


# ii)
print("\nf(x) = x² * e^(-x²)")
f = lambda x: x**2 * exp(-(x**2))
h = lambda y: 2 * 1 / y**2 * f(1 / y - 1)

print(f"Valor esperado de la integral de f entre -∞ y ∞: {quad(f, -inf, inf)[0]}")

mean, s2, n = monte_carlo(h)

print(f"Valor estimado: {mean}, con {n} iteraciones y desviación estándar {sqrt(s2)}")
