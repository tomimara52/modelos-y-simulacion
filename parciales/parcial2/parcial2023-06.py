#!/usr/bin/env python
from numpy.random import uniform, geometric
from math import log, exp, inf
from scipy.integrate import quad


# Ejercicio 1

def juan() -> int:
    cartas = [i + 1 for i in range(10)]
    x = 0
    
    while True:
        predicción = cartas[int(uniform() * len(cartas))]
        carta_sacada = cartas[int(uniform() * len(cartas))]
        x += 1

        if predicción == carta_sacada:
            return x

        cartas.remove(carta_sacada)


print('---------- Ejercicio 1 ----------')
print('Valor esperado: 5.5')
acc = 0
for _ in range(10_000):
    acc += juan()
print(f'Valor estimado: {acc / 10_000}')



# Ejercicio 2

def composición() -> float:
    if uniform() < 0.3:
        return -log(1 - uniform()) / 4.0
    else:
        return -log(1 - uniform()) / 3.0

print('\n---------- Ejercicio 2 ----------')
print(f'E[X] = {quad(lambda x: x * (1.2 * exp(-4*x) + 2.1 * exp(-3*x)), 0, inf)[0]}')
acc = 0
for _ in range(10_000):
    acc += composición()
print(f'Estimación de E[X]: {acc / 10_000}')



# Ejercicio 3

def ej3() -> int:
    while True:
        Y = geometric(0.4) + geometric(0.4)
        if Y >= 4:
            return Y
