#!/usr/bin/env python
import numpy as np
from scipy.stats import uniform, norm


n_sims = 10_000
sample = np.sort(
    [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
)
sample_size = len(sample)
estimated_mean = np.mean(sample)

# ddof=1 hace que el denominador sea N-1
estimated_std = np.std(sample, ddof=1)

d = -np.inf

for i, x in enumerate(sample):
    j = i + 1
    f = np.float64(norm.cdf(x=x, loc=estimated_mean, scale=estimated_std))

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
