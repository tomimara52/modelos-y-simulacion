#!/usr/bin/env python
from numpy.random import uniform
from collections.abc import Callable

def monte_carlo(n: int, f: Callable[..., float], n_args: int = 1) -> float:
    summation = 0

    for _ in range(n):
        summation += f(uniform())

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
