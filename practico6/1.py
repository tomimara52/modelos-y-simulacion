#!/usr/bin/env python
from math import log
from numpy.random import uniform


def std_normal():
    while True:
        Y1 = -log(1 - uniform())
        Y2 = -log(1 - uniform())

        if Y2 >= (Y1 - 1) ** 2 / 2:
            if uniform() < 0.5:
                return Y1
            return -Y1


n = 1
mean = std_normal()
s2 = 0

#             S/sqrt(n) >= 0.1
while n < 100 or s2 / n >= 0.01:
    x = std_normal()
    next_mean = mean + (x - mean) / (n + 1)
    s2 = (1 - 1 / n) * s2 + (n + 1) * (next_mean - mean) ** 2
    mean = next_mean
    n += 1

print(f"Se generaron {n} datos")
print(f"La media muestral es {mean}")
print(f"La varianza muestral es {s2}")
