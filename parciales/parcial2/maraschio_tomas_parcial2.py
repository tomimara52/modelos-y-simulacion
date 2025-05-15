#!/usr/bin/env python
from numpy.random import uniform

# EJERCICIO 1

def ejercicio1():
    while True:
        Y = uniform()
        U = uniform()
        if 1.875 * U < 30 * (Y ** 2 - 2 * Y ** 3 + Y ** 4):
            return Y


acc = 0
for _ in range(10_000):
    acc += ejercicio1()

print(f'Valor esperado estimado de X: {acc / 10_000}')



# EJERCICIO 2

def codigoX(p):
    U = uniform()
    i = 10  # empiezo en i=10 porque es el menor valor que puede tomar X
    F = p   # F guardará el valor de F(i) en cada iteración
    P = p   # P guardará el valor de P(X = i) en cada iteración

    while U >= F:
        i += 1
        P *= 1 - p  # Acá uso la fórmula del inciso a: P(X = i+1) = (1-p)*P(X = i)
        F += P

    return i    # retorno el i que cumple F(i-1) <= U < F(i))


acc = 0
for _ in range(10_000):
    acc += codigoX(0.5)

print(f'Estimación de E[X] con p=0.5: {acc / 10_000}')
