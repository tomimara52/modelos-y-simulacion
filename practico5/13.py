#!/usr/bin/env python
from math import log
from numpy.random import uniform


def exponential(l: float) -> float:
    return -log(1 - uniform()) / l


def homo_poisson_bondis(T: int, l: float) -> int:
    t = 0
    n_fans = 0

    while t < T:
        t += exponential(l)

        if t <= T:
            n_fans += int(21 * uniform()) + 20

    return n_fans


# promedio de llegadas de bondis por hora multiplicado por el promedio de hinchas por bondi
expected = 5 * 30
print(f'En promedio, deberían llegar {expected} aficionados en una hora')

n_sims = 10_000

acc = 0
for _ in range(n_sims):
    acc += homo_poisson_bondis(1, 5)

print(f'En promedio, llegaron {acc / n_sims} aficionados en una hora')
