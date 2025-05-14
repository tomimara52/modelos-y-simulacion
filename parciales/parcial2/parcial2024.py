#!/usr/bin/env python
from numpy.random import uniform
from math import pow, sqrt, log 
from scipy.integrate import quad

# Ejercicio 1

"""
probs tiene que ser un array de 4 elementos
probs[i] representa P(X = i)
"""
def algo_p(probs: list[float]) -> int:
    c = max([4 * prob for prob in probs])
    while True:
        Y = int(uniform() * 4)
        U = uniform()
        if c * U < 4 * probs[Y]:
            return Y

probs = [0.13, 0.22, 0.35, 0.3]
esperanza = sum([i * p for (i, p) in enumerate(probs)])
print('---------- Ejercicio 1 ----------')
print(f'Esperanza: {esperanza}')
acc = 0
for _ in range(10_000):
    acc += algo_p(probs)
print(f'Estimación de la esperanza: {acc / 10_000}')



# Ejercicio 2

def ejercicio2() -> float:
    U = uniform()
    if U < 2 / 3:
        return pow(1.5 * U, 2 / 3)
    else:
        return 3 * U - 1


print('\n---------- Ejercicio 2 ----------')
print(f'E[X] = {quad(lambda x: x * sqrt(x), 0, 1)[0] + quad(lambda x: x / 3, 1, 2)[0]}')

n_sims = 10_000
gt_4 = 0
acc = 0
for _ in range(n_sims):
    X = ejercicio2()
    acc += X
    if X > 4:
        gt_4 += 1
print(f'Estimación de E[X]: {acc / n_sims}')
print(f'Estimación de P(X > 4): {gt_4 / n_sims}')



# Ejercicio 3

def hot_dog(T: float) -> tuple[int, list[float]]:
    interv = [1, 2, 6, 8, 9] # 0 <= T <= 9
    lamda  = [10, 15, 20, 18, 14]
    lambda_t = lambda t: 5 + 5*t if t < 3 else 20 if t <= 5 else 30 - 2*t
    j = 0 
    t = -log ( 1 - uniform() ) / lamda[j]
    n_eventos = 0
    eventos = []

    while t <= T:
        if t <= interv[j]:
            V = uniform()
            if V < lambda_t(t) / lamda[j]:
                n_eventos += 1
                eventos.append(t)
            t += -log(1 - uniform()) / lamda[j]
        else: #t > interv[j]
            t = interv[j] + (t - interv[j]) * lamda[j] / lamda[j + 1]
            j += 1

    return n_eventos, eventos


print('\n---------- Ejercicio 3 ----------')
esperanza = quad(lambda t: 5 + 5*t, 0, 3)[0] + quad(lambda _: 20, 3, 5)[0] + quad(lambda t: 30 - 2*t, 5, 9)[0]
print(f'E[ N(9) ] = {esperanza}')

n_sims = 10_000
acc = 0
for _ in range(n_sims):
    acc += hot_dog(9)[0]
print(f'Estimación de E[ N(9) ]: {acc / n_sims}')



# Ejercicio 4

def area(N: int) -> float:
    puntos_adentro = 0

    for _ in range(N):
        U = uniform() * 3 - 1.5
        V = uniform() * 3 - 1.5
        if U ** 2 + (V - pow(abs(U), 1.5)) ** 2 <= 1:
            puntos_adentro += 1

    return 9 * puntos_adentro / N


print('\n---------- Ejercicio 4 ----------')
N = 100_000
print(f'Estimación del área con {N} simulaciones: {area(N)}')
