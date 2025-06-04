#!/usr/bin/env python
from typing import Callable
from numpy.random import uniform
from math import log
import matplotlib.pyplot as plt


def poisson_process(T: float, l: float, l_t: Callable[[float], float]) -> list[float]:
    events = []
    t = -log(1 - uniform()) / l

    while t <= T:
        V = uniform()
        if V < l_t(t) / l:
            events.append(t)
        t += -log(1 - uniform()) / l

    return events


def lambda_t(t: float) -> float:
    x = t % 10

    if x <= 5:
        return 3 * x + 4
    else:
        return 19 - 3 * (x - 5)


def simulate_server(T: float, debug: bool = False) -> float:
    job_events = poisson_process(T, 19, lambda_t)

    if debug:
        print(job_events)

    time = 0
    total_sleep_time = 0
    next_job = 0

    while next_job < len(job_events):
        if job_events[next_job] > time:
            # sleep
            sleep_time = uniform() * 0.3

            if debug:
                print(f"Sleep from {time} to {time + sleep_time}")

            time += sleep_time
            total_sleep_time += sleep_time
        else:
            # service time
            work_time = -log(uniform()) / 25

            if debug:
                print(f"Work from {time} to {time + work_time}")

            time += work_time
            next_job += 1

    # add sleep time if finished all jobs before T
    if time < T:
        total_sleep_time += T - time

        if debug:
            print(f"Sleep from {time} to {T}")

    return total_sleep_time


def estimate_sleep_time(T: float, n_sims: int) -> tuple[float, list[float]]:
    acc = 0
    sleep_times = []

    for _ in range(n_sims):
        sleep_time = simulate_server(T)
        acc += sleep_time
        sleep_times.append(sleep_time)

    return acc / n_sims, sleep_times


estimated_sleep_time, sleep_times = estimate_sleep_time(100, 5000)
print(
    f"Tiempo que el servidor está detenido estimado en las primeras 100 horas: {estimated_sleep_time}"
)


# lógica para hacer que los bins vayan en incrementos de medio segundo
min_sleep_time = min(sleep_times)
max_sleep_time = max(sleep_times)
lower_edge = (
    int(min_sleep_time)
    if min_sleep_time - int(min_sleep_time) < 0.5
    else int(min_sleep_time) + 0.5
)
upper_edge = (
    int(max_sleep_time) + 0.5
    if max_sleep_time - int(max_sleep_time) < 0.5
    else int(max_sleep_time) + 1
)

bin_edges = []
i = lower_edge
while i <= upper_edge:
    bin_edges.append(i)
    i += 0.5


_, bins, _ = plt.hist(sleep_times, bins=bin_edges, color="skyblue", edgecolor="black")
plt.xticks(bins, [f"{edge:.1f}" for edge in bins], rotation=50, fontsize=8)
plt.title("Histograma de tiempos detenido en las primeras 100 horas")
plt.xlabel("Tiempo en horas")
plt.ylabel("Frecuencia")

plt.savefig("histograma.png", dpi=300, bbox_inches="tight")
plt.show()
