#!/usr/bin/env python
from numpy.random import uniform


def mean_proportion(a: float, b: float, x_values: list[int], n: int) -> float:
    successes = 0

    for _ in range(n):
        bootstrap_sample = [
            x_values[int(uniform() * len(x_values))] for _ in range(len(x_values))
        ]
        avg = sum(bootstrap_sample) / len(bootstrap_sample)

        if a < avg < b:
            successes += 1

    return successes / n


values = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
avg = sum(values) / len(values)

print(f"Valores de X_i: {values}")
print(
    f"Estimación de P(-5 <= X̄(10) - μ <= 5): {mean_proportion(-5 + avg, 5 + avg, values, 10000)}"
)
