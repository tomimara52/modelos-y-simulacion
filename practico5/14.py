#!/usr/bin/env python
from math import log, inf
from scipy.integrate import quad
from numpy.random import uniform
from collections.abc import Callable
from time import time


def exponential(l: float) -> float:
    return -log(1 - uniform()) / l


def no_homo_poisson(T: float, l_t: Callable[[float], float], l: float) -> tuple[int, list[float]]:
    n_events = 0
    events = []
    t = exponential(l)

    while t <= T:
        V = uniform()
        if V < l_t(t) / l:
            n_events += 1
            events.append(t)

        t += exponential(l)

    return n_events, events


def no_homo_poisson_intervals(
        T: float, 
        l_t: Callable[[float], float], 
        interval: list[float],
        max_l_arr: list[float]
        ) -> tuple[int, list[float]]:
    n_events = 0
    events = []
    j = 0
    t = exponential(max_l_arr[j])

    while t <= T:
        if t <= interval[j]:
            V = uniform()
            if V < l_t(t) / max_l_arr[j]:
                n_events += 1
                events.append(t)

            t += exponential(max_l_arr[j])
        else:
            t = interval[j] + (t - interval[j]) * max_l_arr[j] / max_l_arr[j + 1]
            j += 1

    return n_events, events


n_sims = 10_000


l_t = lambda t: 3 + 4 / (t + 1)
max_l = 7
T = 2.67
expected = quad(l_t, 0, T)
print(f'Simulación de proceso de Poisson con λ(t) = 3 + 4 / (t+1), hasta T = {T}')
print(f'\tPromedio exacto: {expected[0]}')


acc = 0

start = time()
for _ in range(n_sims):
    acc += no_homo_poisson(T, l_t, max_l)[0]
elapsed = time() - start

print(f'\tPromedio estimado sin adelgazamiento: {acc / n_sims} (tardó {elapsed} segundos)')


acc = 0
interval = [1.0, 2.0, 3.0]
max_l_arr = [l_t(i-1) for i in interval]

start = time()
for _ in range(n_sims):
    acc += no_homo_poisson_intervals(T, l_t, interval, max_l_arr)[0]
elapsed = time() - start

print(f'\tPromedio estimado con adelgazamiento: {acc / n_sims} (tardó {elapsed} segundos)')






l_t = lambda t: (t - 2)**2 - 5 * t + 17
max_l = 21
T = 4.2143 
expected = quad(l_t, 0, T)
print(f'Simulación de proceso de Poisson con λ(t) = (t - 2)**2 - 5 * t + 17, hasta T = {T}')
print(f'\tPromedio exacto: {expected[0]}')

acc = 0

start = time()
for _ in range(n_sims):
    acc += no_homo_poisson(T, l_t, max_l)[0]
elapsed = time() - start

print(f'\tPromedio estimado sin adelgazamiento: {acc / n_sims} (tardó {elapsed} segundos)')


acc = 0
interval = [5/3, 10/3, 5.0]
max_l_arr = [l_t(i-5/3) for i in interval]

start = time()
for _ in range(n_sims):
    acc += no_homo_poisson_intervals(T, l_t, interval, max_l_arr)[0]
elapsed = time() - start

print(f'\tPromedio estimado con adelgazamiento: {acc / n_sims} (tardó {elapsed} segundos)')






l_t = lambda t: t / 2 - 1 if 2 <= t <= 3 else 1 - t / 6 if 3 < t <= 6 else 0
max_l = 1
T = 16
expected = quad(l_t, 0, T)
print(f'Simulación de proceso de Poisson con λ(t) = t / 2 - 1 if 2 <= t <= 3 else 1 - t / 6 if 3 < t <= 6 else 0, hasta T = {T}')
print(f'\tPromedio exacto: {expected[0]}')

acc = 0

start = time()
for _ in range(n_sims):
    acc += no_homo_poisson(T, l_t, max_l)[0]
elapsed = time() - start

print(f'\tPromedio estimado sin adelgazamiento: {acc / n_sims} (tardó {elapsed} segundos)')


acc = 0
interval = [3.5, 4.5, inf]
max_l_arr = [1, 5/12, 1/4]

start = time()
for _ in range(n_sims):
    acc += no_homo_poisson_intervals(T, l_t, interval, max_l_arr)[0]
elapsed = time() - start

print(f'\tPromedio estimado con adelgazamiento: {acc / n_sims} (tardó {elapsed} segundos)')
