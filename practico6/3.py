#!/usr/bin/env python
from collections.abc import Callable
from numpy.random import uniform
from math import sqrt, inf, sin, pi
from scipy.integrate import quad
import scipy.stats as st


def monte_carlo(
    f: Callable[[float], float],
    confidence: float,
    semi_length: float,
    fixed_iterations: None | int = None,
) -> float:
    alpha_2 = (1 - confidence) / 2
    z_alpha_2 = st.norm.ppf(1 - alpha_2)
    d = semi_length / z_alpha_2

    n = 1
    mean = f(uniform())
    s2 = 0

    while n < 100 or sqrt(s2 / n) >= d:
        next_mean = mean + (f(uniform()) - mean) / (n + 1)
        s2 = (1 - 1 / n) * s2 + (n + 1) * (next_mean - mean) ** 2
        mean = next_mean
        n += 1

        if fixed_iterations and n >= fixed_iterations:
            break

    std_dev = sqrt(s2 / n)
    print(f"\tSe hicieron {n} iteraciones")
    print(f"\tDesviación estándar muestral: {std_dev}")
    print(
        f"\tIC({confidence}): ({mean - z_alpha_2 * std_dev}, {mean + z_alpha_2 * std_dev})"
    )
    print(f"\tLongitud del intervalo: {2 * z_alpha_2 * std_dev}")

    return mean


# i)
print("f(x) = sen(x) / x")
f = lambda x: sin(x) / x
h = lambda y: pi * f(pi * (y + 1))

print(f"Valor esperado de la integral de f entre π y 2π: {quad(f, pi, 2 * pi)[0]}\n")

mean = monte_carlo(h, 0.95, 0.001)

print(
    f"Valor estimado con semi-ancho del intervalo de confianza del 95% inferior a 0.001: {mean}\n"
)

for n in [1000, 5000, 7000]:
    print(f"Valor estimado con {n} interaciones: {monte_carlo(h, 0.95, 0.001, n)}\n")


# ii)
print("\nf(x) = 3 / (3 + x⁴)")
f = lambda x: 3 / (3 + x**4)
h = lambda y: (1 / y**2) * f(1 / y - 1)

print(f"Valor esperado de la integral de f entre 0 y ∞: {quad(f, 0, inf)[0]}\n")

mean = monte_carlo(h, 0.95, 0.001)

print(
    f"Valor estimado con semi-ancho del intervalo de confianza del 95% inferior a 0.001: {mean}\n"
)

for n in [1000, 5000, 7000]:
    print(f"Valor estimado con {n} interaciones: {monte_carlo(h, 0.95, 0.001, n)}\n")
