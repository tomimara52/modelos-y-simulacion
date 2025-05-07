#!/usr/bin/env python
from numpy.random import uniform
from math import exp, factorial

def prob_X(k: int, l: float, i: int) -> float:
    if i < 0 or i > k:
        return 0

    summation = 0
    for j in range(k + 1):
        summation += (l ** j / factorial(j)) * exp(-l)

    return ((l ** i / factorial(i)) * exp(-l)) / summation


def estimate_transinv(k: int, l: float) -> int:
    U = uniform()
    i = 0
    F = prob_X(k, l, i)

    while U >= F:
        i += 1
        F += prob_X(k, l, i)

    return i


"""
Devuelve el valor de c para usar en el método de rechazo, asumiendo que se
usará una uniforme {0, ..., k}.
"""
def get_c(k: int, l: float) -> float:
    c = 0

    for i in range(0, k + 1):
        ratio = prob_X(k, l, i) * (k + 1)

        if ratio > c:
            c = ratio

    return c


def estimate_reject(k: int, l: float) -> int:
    c = get_c(k, l)

    while True:
        # Genero uniforme {0, ..., k}
        Y = int(uniform() * (k + 1))
        U = uniform()

        if U < prob_X(k, l, Y) / (c / (k + 1)):
            return Y


k = 10
l = 0.7

X_gt_2_exact = sum([prob_X(k, l, i) for i in range(3, k+1)])
print(f'Valor exacto de P(X > 2): {X_gt_2_exact}')


n_sims = 1_000
X_gt_2 = 0

for _ in range(n_sims):
    if estimate_transinv(k, l) > 2:
        X_gt_2 += 1

print(f'Estimación de P(X > 2) con método de transformada inversa: {X_gt_2 / n_sims}')


X_gt_2 = 0

for _ in range(n_sims):
    if estimate_reject(k, l) > 2:
        X_gt_2 += 1

print(f'Estimación de P(X > 2) con método de rechazo: {X_gt_2 / n_sims}')
