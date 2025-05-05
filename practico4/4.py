#!/usr/bin/env python
import time
from numpy.random import uniform

probs = [0.11, 0.14, 0.09, 0.08, 0.12, 0.1, 0.09, 0.07, 0.11, 0.09]
min_c = 1.4
A = []
for (i, p) in enumerate(probs):
    n_elems = round(p * 100)
    A += [i+1] * n_elems


def prob(x: int) -> float:
    return probs[x - 1]


def acceptance(c: float) -> int:
    while True:
        Y = int(10 * uniform()) + 1
        U = uniform()

        if U < prob(Y) / (c / 10):
            return Y


def acceptance_c_min() -> int:
    return acceptance(min_c)


def acceptance_c_3() -> int:
    return acceptance(3)


def inverse_transform() -> int:
    U = uniform()
    if U < 0.14:
        return 2
    elif U < 0.26:
        return 5
    elif U < 0.37:
        return 1
    elif U < 0.48:
        return 9
    elif U < 0.58:
        return 6
    elif U < 0.67:
        return 3
    elif U < 0.76:
        return 7
    elif U < 0.85:
        return 10
    elif U < 0.93:
        return 4
    else:
        return 8


def urn() -> int:
    return A[int(uniform() * 100)]


N = 10_000
for estimator_function in [acceptance_c_min, acceptance_c_3, inverse_transform, urn]:
    freqs = [0] * 10

    start = time.time()
    for _ in range(N):
        X = estimator_function()
        freqs[X - 1] += 1
    elapsed = time.time() - start

    estimated_probs = [f/N for f in freqs]

    avg_error = 0
    for (i, p) in enumerate(estimated_probs):
        avg_error += abs((p - prob(i+1)) / prob(i+1))
    avg_error = avg_error / 10

    print(f'---------------- {estimator_function.__name__} ----------------')
    for (i, p) in enumerate(estimated_probs):
        print(f'estimated P(X = {i+1}): {p}')
    print(f'Average error: {avg_error}')
    print(f'Took {elapsed} seconds\n')

