#!/usr/bin/env python
import numpy as np
from scipy.stats import uniform, expon


n_sims = 10_000
sample = np.sort(
    [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
)
sample_size = len(sample)
estimated_scale = np.mean(sample)  # scale = 1 / lambda

d = -np.inf

for i, x in enumerate(sample):
    j = i + 1
    f = np.float64(expon.cdf(x=x, scale=estimated_scale))

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


print(f"p-valor: {bigger_than_d / n_sims}")
