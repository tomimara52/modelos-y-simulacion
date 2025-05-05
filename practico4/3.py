#!/usr/bin/env python
from numpy.random import uniform
from math import sqrt

def simulate() -> int:
    values_seen = set()
    i = 0

    while len(values_seen) < 11:
        dice1 = int(6 * uniform()) + 1
        dice2 = int(6 * uniform()) + 1

        values_seen.add(dice1 + dice2)
        i += 1

    return i


def estimate_stats(N: int, lower_bound: int = 1, higher_bound: int = 1) -> (int, int):
    values_sum = 0
    values = []
    values_lower = 0
    values_higher = 0

    for _ in range(N):
        v = simulate()
        values_sum += v
        values.append(v)

        if v >= lower_bound:
            values_lower += 1

        if v <= higher_bound:
            values_higher += 1

    mean = values_sum / N
    sqr_diff_sum = 0

    for v in values:
        sqr_diff_sum += (mean - v) ** 2

    stddev = sqrt(sqr_diff_sum / N)

    return (mean, stddev, values_lower / N, values_higher / N)


for N in [100, 1000, 10_000, 100_000]:
    (mean, stddev, lower_percentage, higher_percentage) = estimate_stats(N, 15, 9)
    print(f'Estimated mean: {mean}, estimated standard deviation: {stddev}.', end=' ')
    print(f'Estimated prob that N is at least 15: {lower_percentage}, estimated prob that N is at most 9: {higher_percentage}')
