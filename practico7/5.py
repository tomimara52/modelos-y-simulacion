#!/usr/bin/env python
from scipy.stats import binom, chi2
import numpy as np


"""
Código calcular el p-valor con hipótesis nula que la 
muestra proviene de Binomial(n=8, p) con p desconocido

n_list será un array de 9 elementos donde
n_list[i] representa N_i
"""


def calculate_T(n_list, sample_len, estimated_p):
    t = 0

    for j, n_j in enumerate(n_list):
        if n_j == 0:
            continue

        p_j = binom.pmf(k=j, n=8, p=estimated_p)

        t += (n_j - sample_len * p_j) ** 2 / (sample_len * p_j)

    return t


def generate_sample(p, sample_size):
    return binom.rvs(n=8, p=p, size=sample_size)


def get_frequency_list(sample):
    n_list = np.zeros(9)
    for v in sample:
        n_list[v] += 1

    return n_list


def estimate_p(sample: list[int], n_sims: int):
    sample_len = len(sample)
    estimated_p = np.mean(sample) / 8

    n_list = get_frequency_list(sample)

    t = calculate_T(n_list, sample_len, estimated_p)

    chi2_gr = len(n_list[[n > 0 for n in n_list]]) - 2
    pvalue_pearson = chi2.sf(x=t, df=chi2_gr)

    bigger_than_t = 0

    for _ in range(n_sims):
        sim_sample = generate_sample(estimated_p, sample_len)
        sim_p = np.mean(sim_sample) / 8
        sim_n_list = get_frequency_list(sim_sample)

        if calculate_T(sim_n_list, sample_len, sim_p) >= t:
            bigger_than_t += 1

    return pvalue_pearson, bigger_than_t / n_sims


sample = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
n_sims = 10_000

pvalue_person, pvalue_sim = estimate_p(sample, n_sims)
print(f"p-valor con H0 = '{sample} viene de una binomial con n=8':")
print(f"valor estimado usando prueba de Pearson con chi²: {pvalue_person}")
print(f"valor estimado simulando muestras: {pvalue_sim}")
