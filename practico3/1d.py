#!/usr/bin/env python
from math import pi

def generate_points(n: int, a: int, c: int, M: int, seed: int) -> float:
    total_points = 0
    in_sphere_points = 0

    r = seed
    generator = lambda x : (a*x + c) % M

    sphere_center = M / 2
    sphere_radius_squared = (M / 10)**2

    for _ in range(n):
        distance_squared = 0

        for _ in range(3):
            distance_squared += (r - sphere_center)**2 
            r = generator(r)

        total_points += 1

        if distance_squared <= sphere_radius_squared:
            in_sphere_points += 1

    return in_sphere_points / total_points

M = 2**31
expected = ( (4/3) * pi * (M**3 / 1000) ) / (M - 1)**3
print("Expected value with M = 2^31:", expected)
randu = generate_points(10000000, 2**16 + 3, 0, 2**31, 42)
print("RANDU:", randu)
print("Percentual error:", abs((expected - randu)/expected))

M = 2**31 - 1
expected = ( (4/3) * pi * (M**3 / 1000) ) / (M - 1)**3
print("Expected value with M = 2^31 - 1:", expected)
second = generate_points(10000000, 7**5, 0, 2**31 - 1, 42)
print("el otro:", second)
print("Percentual error:", abs((expected - second)/expected))
