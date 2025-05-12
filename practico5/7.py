#!/usr/bin/env python
from math import exp, e, log
from numpy.random import uniform


def transinv():
    return exp(uniform())


def reject():
    while True:
        Y = (e - 1) * uniform() + 1
        U = uniform()
        if U < 1/Y:
            return Y


n_sims = 10_000
print(f'Se estimará realizando {n_sims} simulaciones')

exact_mean = e - 1
print(f'Valor exacto de la esperanza: {exact_mean}')

acc = 0
for _ in range(n_sims):
    acc += transinv()

print(f'Valor estimado de la esperanza con método de la transformada inversa: {acc / n_sims}')


acc = 0
for _ in range(n_sims):
    acc += reject()

print(f'Valor estimado de la esperanza con método de rechazo: {acc / n_sims}')




prob_less_2 = log(2)
print(f'Valor exacto de P(X <= 2): {prob_less_2}')

less_2 = 0
for _ in range(n_sims):
    if transinv() <= 2:
        less_2 += 1

print(f'Valor estimado de P(X <= 2) con método de la transformada inversa: {less_2 / n_sims}')


less_2 = 0
for _ in range(n_sims):
    if reject() <= 2:
        less_2 += 1

print(f'Valor estimado de P(X <= 2) con método de rechazo: {less_2 / n_sims}')
