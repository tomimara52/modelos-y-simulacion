#!/usr/bin/env python
import numpy as np
from numpy.random import uniform
from math import exp, log, comb, sqrt


def ejercicio2c(tam_muestra, d_KS, n_sim):
    mayores_d_KS = 0

    for _ in range(n_sim):
        uniformes = np.sort(uniform(size=tam_muestra))

        d_i = -np.inf

        for i, u in enumerate(uniformes):
            j = i + 1

            d_i = max(d_i, j / tam_muestra - u, u - (j - 1) / tam_muestra)

        if d_i >= d_KS:
            mayores_d_KS += 1

    p_valor = mayores_d_KS / n_sim
    print(f"Ejercicio 2c:")
    print(f"El pvalor obtenido simulando uniformes es: {p_valor}")

    if p_valor < 0.04:
        print("La hipótesis nula se rechaza con nivel de rechazo 4%")
    else:
        print("No hay evidencia suficiente para rechazar la H0 con nivel de rechazo 4%")


d_KS = 0.0744289456538767
data = [
    15.22860536,
    40.60145536,
    33.67482894,
    44.03841737,
    15.69560109,
    16.2321714,
    25.02174735,
    30.34655637,
    3.3181228,
    5.69447539,
    10.1119561,
    49.10266584,
    3.6536329,
    35.82047148,
    3.37816632,
    36.72299321,
    50.67085322,
    3.25476304,
    20.12426236,
    20.2668814,
    17.49593589,
    2.70768636,
    14.77332745,
    1.72267967,
    23.34685662,
    8.46376635,
    9.18330789,
    9.97428217,
    2.33951729,
    137.51657441,
    9.79485269,
    10.40308179,
    1.57849658,
    6.26959703,
    4.74251574,
    1.53479053,
    34.74136011,
    27.47600572,
    9.1075566,
    1.88056595,
    27.59551348,
    6.82283137,
    12.45162807,
    28.01983651,
    0.36890593,
    7.82520791,
    3.17626161,
    46.91791271,
    38.08371186,
    41.10961135,
]
n = len(data)
ejercicio2c(n, d_KS, 10_000)


def ejercicio2d(tam_muestra, d_KS, n_sim):
    mayores_d_KS = 0

    for _ in range(n_sim):
        exponenciales = []
        for _ in range(tam_muestra):
            exponenciales.append(-log(1 - uniform()) / 0.05)
        exponenciales.sort()

        d_i = -np.inf

        for i, v in enumerate(exponenciales):
            j = i + 1
            F_j = 1 - exp(-0.05 * v)

            d_i = max(d_i, j / tam_muestra - F_j, F_j - (j - 1) / tam_muestra)

        if d_i >= d_KS:
            mayores_d_KS += 1

    p_valor = mayores_d_KS / n_sim
    print(f"Ejercicio 2d:")
    print(f"El pvalor obtenido simulando exponenciales es: {p_valor}")

    if p_valor < 0.04:
        print("La hipótesis nula se rechaza con nivel de rechazo 4%")
    else:
        print("No hay evidencia suficiente para rechazar la H0 con nivel de rechazo 4%")


ejercicio2d(n, d_KS, 10_000)


def binomial(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = uniform()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i


def ejercicio3(t, p, tam_muestra, n_sim):
    mayores_t = 0

    for _ in range(n_sim):
        muestra = []
        for _ in range(tam_muestra):
            muestra.append(binomial(5, p))

        p_sim = np.mean(muestra) / 5

        frecuencias = [0] * 6
        for v in muestra:
            frecuencias[v] += 1

        t_sim = 0

        for j, frecuencia in enumerate(frecuencias):
            p_i = comb(5, j) * (p_sim**j) * ((1 - p_sim) ** (5 - j))

            t_sim += (frecuencia - tam_muestra * p_i) ** 2 / (tam_muestra * p_i)

        if t_sim >= t:
            mayores_t += 1

    print("Ejercicio 3:")
    print(f"Estimación del pvalor simulando: {mayores_t / n_sim}")


t = 8.161627432060547
p = 0.494
tam_muestra = 1000
n_sim = 1000
ejercicio3(t, p, tam_muestra, n_sim)


def ejercicio4(z_alpha_2, semi_ancho):
    f = lambda x: exp(-2 - x) * (1 - (2 + x) ** 4)
    d = semi_ancho / z_alpha_2

    n = 1
    media = f(uniform())
    s2 = 0

    print("Ejercicio 4:")
    print("| iteraciones | estimación | desviación estándar | longitud de intervalo |")

    while n < 100 or sqrt(s2 / n) >= d:
        next_media = media + (f(uniform()) - media) / (n + 1)
        s2 = (1 - 1 / n) * s2 + (n + 1) * (next_media - media) ** 2
        media = next_media
        n += 1

        if n in [1000, 5000, 7000]:
            print(
                f"| {n:<11} | {media:.7f} | {sqrt(s2):.17f} | {(2 * z_alpha_2 * sqrt(s2 / n)):.19f} |"
            )

    print(
        f"| {n:<11} | {media:.7f} | {sqrt(s2):.17f} | {(2 * z_alpha_2 * sqrt(s2 / n)):.19f} |"
    )


ejercicio4(1.96, 0.001)
