#!/usr/bin/env python
from math import sqrt
from numpy.random import uniform
from time import time

def add_two_uniforms() -> float:
    return uniform() + uniform()


def transinv() -> float:
    U = uniform()

    if U < 0.5:
        return sqrt(2 * U)
    else:
        return 2 - sqrt(2 * (1 - U))


def reject() -> float:
    while True:
        Y = uniform() * 2
        U = uniform()

        f = lambda x: x if x < 1 else 2 - x

        if U < f(Y):
            return Y


n_sims = 10_000

x0 = 1.5
exact_mean = 1
print(f'Valor esperado: {exact_mean}')
print('P(X > 1.5): 0.125')
print(f'Se estimará haciendo {n_sims} simulaciones')

acc = 0
gt_x0 = 0
start = time()
for _ in range(n_sims):
    X = add_two_uniforms()
    acc += X
    if X > x0:
        gt_x0 +=1
print(f'\n----- Método de sumar dos uniformes (tardó {time() - start} segundos) -----')
print(f'Estimación de la esperanza: {acc / n_sims}')
print(f'Estimación de P(X > x0): {gt_x0 / n_sims}')


acc = 0
gt_x0 = 0
start = time()
for _ in range(n_sims):
    X = transinv()
    acc += X
    if X > x0:
        gt_x0 +=1
print(f'\n----- Método de la transformada inversa (tardó {time() - start} segundos) -----')
print(f'Estimación de la esperanza: {acc / n_sims}')
print(f'Estimación de P(X > x0): {gt_x0 / n_sims}')


acc = 0
gt_x0 = 0
start = time()
for _ in range(n_sims):
    X = reject()
    acc += X
    if X > x0:
        gt_x0 +=1
print(f'\n----- Método de aceptación y rechazo (tardó {time() - start} segundos) -----')
print(f'Estimación de la esperanza: {acc / n_sims}')
print(f'Estimación de P(X > x0): {gt_x0 / n_sims}')
