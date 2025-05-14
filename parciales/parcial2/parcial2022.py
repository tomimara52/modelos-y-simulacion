#!/usr/bin/env python
from math import log, exp, inf, pow
from numpy.random import uniform
from scipy.integrate import quad


# EJ 1
A = [0] * 32 + [1] * 21 + [2] * 33 + [3] * 14

def urna() -> int:
    random_index = int(uniform() * 100)
    return A[random_index]

freqs = [0] * 4
for _ in range(10_000):
    freqs[urna()] += 1

print('---------- Ejercicio 1 ----------')
for (i, f) in enumerate(freqs):
    print(f'Estimación de P(X = {i}): {f / 10_000}')



# EJ 2

def transformada_inversa() -> float:
    U = uniform()
    if U < 1 / 3:
        return log(3 * U)
    else:
        return 0.5 * log(1 / (1.5 * (1 -U)))


print('---------- Ejercicio 2 ----------')
f = lambda x: (1 / 3) * exp(x) if x <= 0 else (4 / 3) * exp(-2 * x)
print(f'P(X <= 1) = {quad(f, -inf, 1)[0]}')

less_than_1 = 0
for _ in range(10_000):
    if transformada_inversa() <= 1:
        less_than_1 += 1
print(f'Estimación de P(X <= 1) = {less_than_1 / 10_000}')



print('---------- Ejercicio 3 ----------')

def aceptaction_rechazo() -> float:
    while True:
        Y = 2 * uniform() - 1
        U = uniform()
        if U < 1 - Y * Y:
            return Y


print('P(X > 0) = 0.5')

gt_0 = 0
for _ in range(10_000):
    if aceptaction_rechazo() > 0:
        gt_0 += 1
print(f'Estimación de P(X > 0): {gt_0 / 10_000}')



print('---------- Ejercicio 4 ----------')

def tirar_moneda(p: float) -> float:
    n = 1
    prev_cara = uniform() < p

    while True:
        n += 1
        cara = uniform() < p
        if cara != prev_cara:
            return n
        prev_cara = cara


def geométrica(p: float) -> float:
    n = 1
    success = uniform() < p
    while not success:
        n += 1
        success = uniform() < p
    
    return n


def moneda_rechazo() -> float:
    while True:
        Y = geométrica(1/3)
        U = uniform()
        if Y != 1 and U < 0.5 + pow(2, 1 - Y):
            return Y


print(f'P(X = 4) = {10 / 3 ** 4}')

eq_4 = 0
for _ in range(100_000):
    if tirar_moneda(1/3) == 4:
        eq_4 += 1
print(f'Estimación de P(X = 4) simulando tiradas de moneda: {eq_4 / 100_000}')

eq_4 = 0
for _ in range(100_000):
    if moneda_rechazo() == 4:
        eq_4 += 1
print(f'Estimación de P(X = 4) con aceptación rechazo: {eq_4 / 100_000}')
