#!/usr/bin/env python
from numpy.random import uniform


def bootstrap_variance(x_values: list[int], n: int) -> float:
    S2_values = []
    avg_S2 = 0

    for _ in range(n):
        bootstrap_sample = [
            x_values[int(uniform() * len(x_values))] for _ in range(len(x_values))
        ]

        sample_avg = sum(bootstrap_sample) / len(bootstrap_sample)
        sample_S2 = sum([(v - sample_avg) ** 2 for v in bootstrap_sample]) / (
            len(bootstrap_sample) - 1
        )

        avg_S2 += sample_S2
        S2_values.append(sample_S2)

    avg_S2 /= n

    return sum([(S2 - avg_S2) ** 2 for S2 in S2_values]) / (n - 1)


values = [5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8]
print(f"Valores de X_i: {values}")
print(f"Estimación de Var(S²): {bootstrap_variance(values, 10_000)}")
