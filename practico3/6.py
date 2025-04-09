#!/usr/bin/env python
from numpy.random import uniform
from numpy import pi as numpy_pi
from math import pi as math_pi

def estimate_pi(n: int) -> float:
    total_points = 0
    points_in_circle = 0

    for _ in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)

        if x*x + y*y <= 1:
            points_in_circle += 1

        total_points += 1

    return 4 * points_in_circle / total_points

print(f"numpy.pi:                   {numpy_pi}")
print(f"math.pi:                    {math_pi}")
print(f"estimation with n=1000:     {estimate_pi(1000)}")
print(f"estimation with n=10000:    {estimate_pi(10000)}")
print(f"estimation with n=100000:   {estimate_pi(100000)}")
print(f"estimation with n=1000000:  {estimate_pi(1000000)}")
