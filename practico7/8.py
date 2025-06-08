#!/usr/bin/env python
from math import sqrt, erf
from random import gauss, gammavariate
import numpy as np
from scipy.stats import uniform


def rt(df):  # df grados de libertad
    x = gauss(0.0, 1.0)
    y = 2.0 * gammavariate(0.5 * df, 2.0)
    return x / sqrt(y / df)


def normal_cdf(x):
    return erf(x / sqrt(2.0)) / 2 + 0.5


sample_sizes = [10, 20, 100, 1000]
n_sims = 10_000

print("| número de elementos | estadístico D | p-valor |")

for sample_size in sample_sizes:
    sample = np.sort([rt(11) for _ in range(sample_size)])
    d = -np.inf

    for i, x in enumerate(sample):
        j = i + 1
        f = normal_cdf(x)

        d = max(d, j / sample_size - f, f - (j - 1) / sample_size)

    bigger_than_d = 0

    for _ in range(n_sims):
        uniforms = np.sort(uniform.rvs(size=sample_size))

        d_j = -np.inf

        for i, u_j in enumerate(uniforms):
            j = i + 1

            d_j = max(d_j, j / sample_size - u_j, u_j - (j - 1) / sample_size)

        if d_j >= d:
            bigger_than_d += 1

    print(f"| {sample_size:<19} | {d:.11f} | {(bigger_than_d / n_sims):.5f} |")
