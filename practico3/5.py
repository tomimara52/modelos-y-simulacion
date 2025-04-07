#!/usr/bin/env python
from numpy.random import uniform
from collections.abc import Callable
from math import e

def monte_carlo(n: int, f: Callable[..., float], n_args: int = 1) -> float:
    summation = 0

    for _ in range(n):
        summation += f(*(uniform() for _ in range(n_args)))

    return summation / n


f = lambda x : (1-x*x)**1.5
print("Estimación de integral (0, 1) de (1-x²)^(3/2):")
print("\tn = 1000:", monte_carlo(1000, f))
print("\tn = 5000:", monte_carlo(5000, f))
print("\tn = 10000:", monte_carlo(10000, f))
print("\tn = 1000000:", monte_carlo(1000000, f))
print("\tValor real: 0.589048622")

f = lambda x : (x + 2) / ((x + 2)**2 - 1)
print("Estimación de integral (2, 3) de x / (x²-1):")
print("\tn = 1000:", monte_carlo(1000, f))
print("\tn = 5000:", monte_carlo(5000, f))
print("\tn = 10000:", monte_carlo(10000, f))
print("\tn = 1000000:", monte_carlo(1000000, f))
print("\tValor real: 0.4904146265")

f = lambda x : (1/x - 1) / ((1 + (1/x - 1)**2)*x)**2
print("Estimación de integral (0, infinito) de x * (x²+1)⁻²:")
print("\tn = 1000:", monte_carlo(1000, f))
print("\tn = 5000:", monte_carlo(5000, f))
print("\tn = 10000:", monte_carlo(10000, f))
print("\tn = 1000000:", monte_carlo(1000000, f))
print("\tValor real: 0.5")

f = lambda x : 2 * e**(-(1/x - 1)**2) / x**2
print("Estimación de integral (-infinito, infinito) de e^(-x²):")
print("\tn = 1000:", monte_carlo(1000, f))
print("\tn = 5000:", monte_carlo(5000, f))
print("\tn = 10000:", monte_carlo(10000, f))
print("\tn = 1000000:", monte_carlo(1000000, f))
print("\tValor real: 1.772453851")


f = lambda x, y : e**((x + y)**2)
print("Estimación de integral (0, 1) (0, 1) de e^(-(x+y)²):")
print("\tn = 1000:", monte_carlo(1000, f, 2))
print("\tn = 5000:", monte_carlo(5000, f, 2))
print("\tn = 10000:", monte_carlo(10000, f, 2))
print("\tn = 1000000:", monte_carlo(1000000, f, 2))
print("\tValor real: 4.89916")


f = lambda x, y : e**(-(1/x + 1/y - 2)) / (x*y)**2 if 1/x - 1 > 1/y - 1 else 0
print("Estimación de integral (0, infinito) (0, x) de e^-(x+y):")
print("\tn = 1000:", monte_carlo(1000, f, 2))
print("\tn = 5000:", monte_carlo(5000, f, 2))
print("\tn = 10000:", monte_carlo(10000, f, 2))
print("\tn = 1000000:", monte_carlo(1000000, f, 2))
print("\tValor real: 0.5")
