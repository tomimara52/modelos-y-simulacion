#!/usr/bin/env python
from scipy.stats import uniform, binom
import numpy as np
from math import sqrt


# ejericio 2d
def simulate_pvalue(n_simulations, d0, sample_size):
    bigger_than_d0 = 0

    for _ in range(n_simulations):
        uniforms = np.sort(uniform.rvs(size=sample_size))

        d_i = -np.inf

        for i, u in enumerate(uniforms):
            j = i + 1

            d_i = max(d_i, j / sample_size - u, u - (j - 1) / sample_size)

        if d_i >= d0:
            bigger_than_d0 += 1

    return bigger_than_d0 / n_simulations


d0 = 0.15347
sample_size = 9
n_simulations = 10_000

print(
    f"p-valor obtenido simulando uniformes: {simulate_pvalue(n_simulations, d0, sample_size)}"
)


# ejercicio 2e
uniforms = np.sort([0.23, 0.12, 0.45, 0.67, 0.01, 0.51, 0.38, 0.92, 0.84])
d_i = -np.inf

for i, u in enumerate(uniforms):
    j = i + 1

    d_i = max(d_i, j / 9 - u, u - (j - 1) / 9)

print(
    f"Valor del estadístico de la muestra de uniformes vs estadístico de la muestra real: {d_i}, {d0}"
)


# ejercicio 3d

t0 = 3.0181185228436624 
p0 = 0.217
n_simulations = 10_000
bigger_than_t0 = 0

for i in range(n_simulations):
    sample = np.array(binom.rvs(n=3, p=p0, size=1000))
    p_sim = np.mean(sample) / 3

    probs_sim = [binom.pmf(k=i, n=3, p=p_sim) for i in range(4)]
    n_sim = np.zeros(4, dtype=int)
    for v in sample:
        n_sim[v] += 1

    t_sim = sum(
        [(n_i - 1000 * p_i) ** 2 / (1000 * p_i) for n_i, p_i in zip(n_sim, probs_sim)]
    )

    if t_sim >= t0:
        bigger_than_t0 += 1

print(f"pvalor simulando binomiales: {bigger_than_t0 / n_simulations}")


# ejercicio 4

f = lambda x: (1 / x**2) * ((1 / x - 1) / (1 + (1 / x - 1) ** 4))


def monte_carlo(z_alpha_2, semi_length, fixed_iterations=None):
    d = semi_length / z_alpha_2

    n = 1
    mean = f(uniform.rvs())
    s2 = 0

    while n < 100 or sqrt(s2 / n) >= d or not fixed_iterations is None:
        next_mean = mean + (f(uniform.rvs()) - mean) / (n + 1)
        s2 = (1 - 1 / n) * s2 + (n + 1) * (next_mean - mean) ** 2
        mean = next_mean
        n += 1

        if fixed_iterations == n:
            break

    return mean, sqrt(s2), 2 * z_alpha_2 * sqrt(s2 / n), n


print("| iteraciones | estimación | desviación estándar | longitud de intervalo |")

mean, s, ic, n = monte_carlo(1.96, 0.001)
print(f"| {n:<11} | {mean:.8f} | {s:.17f} | {ic:.19f} |")

for n in [1000, 5000, 7000]:
    mean, s, ic, n = monte_carlo(1.96, 0.001, n)
    print(f"| {n:<11} | {mean:.8f} | {s:.17f} | {ic:.19f} |")
