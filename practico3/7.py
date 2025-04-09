#!/usr/bin/env python
from numpy.random import uniform

def estimate_minsum(n: int) -> float:
    values_sum = 0

    for _ in range(n):
        uniform_sum = 0
        i = 0

        while uniform_sum <= 1:
            uniform_sum += uniform()
            i += 1

        values_sum += i

    return values_sum / n

print(f"estimation with n=100:      {estimate_minsum(100)}")
print(f"estimation with n=1000:     {estimate_minsum(1000)}")
print(f"estimation with n=10000:    {estimate_minsum(10000)}")
print(f"estimation with n=100000:   {estimate_minsum(100000)}")
print(f"estimation with n=1000000:  {estimate_minsum(1000000)}")
