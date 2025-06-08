#!/usr/bin/env python
from scipy.stats import chi2, binom


probabilities = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]
print("Valores de las áreas:")
for i, prob in enumerate(probabilities):
    print(f"\t{i + 1}: {100 * prob}%")


frequencies = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
n = sum(frequencies)

print("\nFrecuencias observadas:")
for i, freq in enumerate(frequencies):
    print(f"\t{i + 1}: {100 * (freq / n)}%")


""" 
La hipótesis nula será que la muestra observada proviene
de una variable aleatoria X con P(X = i) = probabilities[i - 1]
"""


def calculate_T(n_list, sample_size):
    t = 0

    for p_j, n_j in zip(probabilities, n_list):
        if n_j == 0:
            continue

        t += (n_j - sample_size * p_j) ** 2 / (sample_size * p_j)

    return t


def pvalue_pearson(n_list, sample_size):
    t = calculate_T(n_list, sample_size)

    chi2_gr = len([n for n in n_list if n > 0]) - 1

    return chi2.sf(x=t, df=chi2_gr)


def generate_n_list(sample_size):
    n_list = []
    n_sum = 0
    cdf = 0

    for j in range(10):
        p_j = probabilities[j]
        n_j = binom.rvs(n=sample_size - n_sum, p=p_j / (1 - cdf))

        n_list.append(n_j)
        n_sum += n_j
        cdf += p_j

    return n_list


def pvalue_simulate(n_list, sample_size, n_sims):
    t = calculate_T(n_list, sample_size)

    bigger_than_t = 0

    for _ in range(n_sims):
        sim_sample = generate_n_list(sample_size)

        if calculate_T(sim_sample, sample_size) >= t:
            bigger_than_t += 1

    return bigger_than_t / n_sims


print(f"\np-valor usando prueba de chi²: {pvalue_pearson(frequencies, n)}")
print(f"\np-valor usando una simulación: {pvalue_simulate(frequencies, n, 10_000)}")
