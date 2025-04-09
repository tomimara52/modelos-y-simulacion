#!/usr/bin/env python
from numpy.random import randint

def play() -> int:
    dice = randint(1, 7)

    if dice == 1 or dice == 6:
        return 2 * randint(1, 7)
    else:
        return randint(1, 7) + randint(1, 7)


def estimate_win_prob(n: int) -> float:
    times_won = 0

    for _ in range(n):
        if play() > 6:
            times_won += 1

    return times_won / n

print(f"estimación con n = 1000:    {estimate_win_prob(1000)}")
print(f"estimación con n = 10000:   {estimate_win_prob(10000)}")
print(f"estimación con n = 100000:  {estimate_win_prob(100000)}")
print(f"estimación con n = 1000000: {estimate_win_prob(1000000)}")
