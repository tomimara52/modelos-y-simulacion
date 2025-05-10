#!/usr/bin/env python
from numpy.random import uniform
from math import sqrt, cbrt, log

def a() -> float:
    U = uniform()
    
    if U <= 0.25:
        return 2 * (sqrt(U) + 1)
    else:
        return 6 - sqrt(12 * (1 - U))


def b() -> float:
    U = uniform()

    if U <= 3/5:
        return sqrt(9 + (35/3) * U) - 3
    else:
        return cbrt((35/2) * (U - 3/5) + 1)


def c() -> float:
    U = uniform()

    if U <= 1/16:
        return log(16*U) / 4
    else:
        return 4 * U - 1 / 4
