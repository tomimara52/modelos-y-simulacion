#!/usr/bin/env python
from numpy.random import uniform

def play(n: int) -> float:
    won = 0

    for _ in range(n):
        if uniform() < 0.5:
            x = uniform() + uniform()
        else:
            x = uniform() + uniform() + uniform()

        if x >= 1:
            won += 1

    return won / n

print("n = 100:", play(100))
print("n = 1000:", play(1000))
print("n = 10000:", play(10000))
print("n = 100000:", play(100000))
print("n = 1000000:", play(1000000))
