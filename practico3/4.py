#!/usr/bin/env python
from numpy.random import exponential, uniform

def wait(
        c1_p: float, c1_scale: int, 
        c2_p: float, c2_scale: int, 
        c3_p: float, c3_scale: int, 
        wait_time: float,
        n: int
        ) -> float:

    success = 0

    for _ in range(n):
        c = uniform()

        if c < c1_p:
            scale = c1_scale
        elif c < c1_p + c2_p:
            scale = c2_scale
        else:
            scale = c3_scale

        waited = exponential(scale)

        if waited < wait_time:
            success += 1

    return success / n


def choose_cashier(
        c1_p: float, c1_scale: int, 
        c2_p: float, c2_scale: int, 
        c3_p: float, c3_scale: int, 
        wait_time: float,
        n: int
        ) -> float:

    successes = [0, 0, 0]

    for _ in range(n):
        c = uniform()

        if c < c1_p:
            scale = c1_scale
            chosen_c = 0
        elif c < c1_p + c2_p:
            scale = c2_scale
            chosen_c = 1
        else:
            scale = c3_scale
            chosen_c = 2

        waited = exponential(scale)

        if waited > wait_time:
            successes[chosen_c] += 1

    waited_more_times = sum(successes)

    return successes[0] / waited_more_times, successes[1] / waited_more_times, successes[2] / waited_more_times


print("Caja 1: porcentaje 40%, escala 3")
print("Caja 2: porcentaje 32%, escala 4")
print("Caja 3: porcentaje 28%, escala 5")
print("Prob de esperar menos de 4 min estimada:", wait(0.4, 3, 0.32, 4, 0.28, 5, 4, 1000000))
print("Prob de elegir cada caja dado que esperó más de 4 min:", choose_cashier(0.4, 3, 0.32, 4, 0.28, 5, 4, 1000000))
