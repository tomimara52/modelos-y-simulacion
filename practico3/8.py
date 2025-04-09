#!/usr/bin/env python
from numpy.random import uniform
from math import exp

def estimate_maxprod(n: int) -> float:
    values_sum = 0
    limit_value = exp(-3)

    for _ in range(n):
        uniform_product = 1
        i = 0

        while uniform_product >= limit_value:
            uniform_product *= uniform()
            i += 1

        values_sum += i - 1

    return values_sum / n


def estimate_maxprod_probability(p: int, n: int) -> float:
    successes = 0
    limit_value = exp(-3)

    for _ in range(n):
        uniform_product = 1
        i = 0

        while uniform_product >= limit_value:
            uniform_product *= uniform()
            i += 1

        if i - 1 == p:
            successes += 1

    return successes / n


print(f"estimation of E[N] with n=100:      {estimate_maxprod(100)}")
print(f"estimation of E[N] with n=1000:     {estimate_maxprod(1000)}")
print(f"estimation of E[N] with n=10000:    {estimate_maxprod(10000)}")
print(f"estimation of E[N] with n=100000:   {estimate_maxprod(100000)}")
print(f"estimation of E[N] with n=1000000:  {estimate_maxprod(1000000)}")

print(f"estimation of P(N = 0) with n = 1000000: {estimate_maxprod_probability(0, 1000000)}")
print(f"estimation of P(N = 1) with n = 1000000: {estimate_maxprod_probability(1, 1000000)}")
print(f"estimation of P(N = 2) with n = 1000000: {estimate_maxprod_probability(2, 1000000)}")
print(f"estimation of P(N = 3) with n = 1000000: {estimate_maxprod_probability(3, 1000000)}")
print(f"estimation of P(N = 4) with n = 1000000: {estimate_maxprod_probability(4, 1000000)}")
print(f"estimation of P(N = 5) with n = 1000000: {estimate_maxprod_probability(5, 1000000)}")
print(f"estimation of P(N = 6) with n = 1000000: {estimate_maxprod_probability(6, 1000000)}")
