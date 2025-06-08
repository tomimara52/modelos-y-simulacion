#!/usr/bin/env python
import numpy as np
from scipy.stats import expon, uniform

sample_size = 30
sample = np.sort(expon.rvs(scale=1, size=sample_size))
print(f"Muestra: {sample}")
print(f"Media muestral: {np.mean(sample)}")

d = -np.inf

for i, x in enumerate(sample):
    j = i + 1
    f = np.float64(expon.cdf(x=x, scale=1))
    d = max(d, j / sample_size - f, f - (j - 1) / sample_size)


n_sims = 10_000
bigger_than_d = 0

for _ in range(n_sims):
    uniforms = np.sort(uniform.rvs(size=sample_size))

    d_j = -np.inf

    for i in range(sample_size):
        u_j = uniforms[i]
        j = i + 1

        d_j = max(d_j, j / sample_size - u_j, u_j - (j - 1) / sample_size)

    if d_j >= d:
        bigger_than_d += 1

print(f"p-valor: {bigger_than_d / n_sims}")
