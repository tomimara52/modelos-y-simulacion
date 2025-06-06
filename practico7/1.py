#!/usr/bin/env python
from scipy.stats import binom, chi2


def simulate_T(values: list[int], probabilities: list[float], n: int) -> float:
    N_list = []
    N_sum = 0
    F = 0

    for j in range(len(values)):
        N_j = binom.rvs(n - N_sum, probabilities[j] / (1 - F))

        N_list.append(N_j)
        N_sum += N_j
        F += probabilities[j]

    T = 0
    for i in range(len(values)):
        T += (N_list[i] - n * probabilities[i]) ** 2 / (n * probabilities[i])

    return T


def pearson_p(
    N_list: list[int],
    probabilities: list[float],
    n: int,
):
    T = 0
    for i in range(len(probabilities)):
        T += (N_list[i] - n * probabilities[i]) ** 2 / (n * probabilities[i])

    return (1 - chi2.cdf(T, len(probabilities) - 1)).tolist()


def estimate_p(
    N_list: list[int],
    values: list[int],
    probabilities: list[float],
    n: int,
    n_sims: int,
) -> float:
    T = 0
    for i in range(len(values)):
        T += (N_list[i] - n * probabilities[i]) ** 2 / (n * probabilities[i])

    bigger_than_T = 0

    for _ in range(n_sims):
        if simulate_T(values, probabilities, n) > T:
            bigger_than_T += 1

    return bigger_than_T / n_sims


values = [1, 2, 3]
probabilities = [0.25, 0.5, 0.25]
N_list = [141, 291, 132]
n = 564

print(f"p-valor Pearson: {pearson_p(N_list, probabilities, n)}")
print(
    f"Valor estimado del p-valor: {estimate_p(N_list, values, probabilities, 564, 10_000)}"
)
