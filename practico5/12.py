#!/usr/bin/env python
from numpy.random import uniform
from math import log, factorial, exp


def exponential(l: float) -> float:
    return -log(1 - uniform()) / l


def homo_poisson_process(T: int, l: float) -> tuple[int, list[float]]:
    t = 0
    n_events = 0
    events = []

    while t < T:
        t += exponential(l)

        if t <= T:
            n_events += 1
            events.append(t)

    return n_events, events


l = 2.4
T = 5
i = 10

expected_value = T * l
print(f'E[ N({T}) ] = {expected_value}')

n_sims = 10_000
acc = 0

for _ in range(n_sims):
    acc += homo_poisson_process(T, l)[0]

print(f'Valor estimado de P(N({T}) <= {i}): {acc / n_sims}')
