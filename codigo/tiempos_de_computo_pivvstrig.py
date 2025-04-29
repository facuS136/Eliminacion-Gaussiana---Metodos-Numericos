import time
import numpy as np
import matplotlib.pyplot as plt
from conPivoteo import eg_con_pivoteo
from conPivoteoTridiagonal import eg_thomas_algoritm


def construir_matriz(a, b, c):
    n = b.size
    matriz = np.zeros((n, n), dtype=b.dtype)
    for i in range(0, n):
        matriz[i][i] = b[i]
        if i+1 < n:
            matriz[i][i+1] = c[i]
            matriz[i+1][i] = a[i+1]
    return matriz
    

def tiempo_pivoteo_vs_thomas(a, b, c, d):
    
    A = construir_matriz(a, b, c)
    cantidad_de_casos = 100
    tolerancia = 0.002
    
    con_pivoteo_times = []
    tridiagonal_times = []
    sizes = []
    
    while cantidad_de_casos > 0:
        sizes.append(b.size)

        tiempos_pivoteo = []
        for _ in range(10):
            con_pivoteo_start = time.time()
            eg_con_pivoteo(A.copy(), d.copy(), tolerancia)
            con_pivoteo_end = time.time()
            tiempos_pivoteo.append(con_pivoteo_end - con_pivoteo_start)

        con_pivoteo_times.append(min(tiempos_pivoteo))

        tiempos_tridiagonal = []
        for _ in range(10):
            tridiagonal_start = time.time()
            eg_thomas_algoritm(a.copy(), b.copy(), c.copy(), d.copy(), tolerancia)
            tridiagonal_end = time.time()
            tiempos_tridiagonal.append(tridiagonal_end - tridiagonal_start)

        tridiagonal_times.append(min(tiempos_tridiagonal))

        # Agrandar matriz
        a = np.append(a, a[1])
        b = np.append(b, b[0])
        c[-1] = c[0]
        c = np.append(c, 0)
        d = np.append(d, d[0])
        A = construir_matriz(a, b, c)

        cantidad_de_casos -= 1
    
    # Graficar times vs sizes

    plt.plot(sizes, con_pivoteo_times, color="red")
    plt.plot(sizes, tridiagonal_times, color="blue")
    plt.legend(["Con pivoteo", "Thomas (Tridiagonal)"])
    plt.xlabel("Tamaño de matriz (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig("tiempo_pivoteo_vs_thomas.png")


a = np.full(10, 1, dtype=np.float64)
b = np.full(10, -2, dtype=np.float64)
c = np.full(10, 1, dtype=np.float64)
d = np.full(10, 25, dtype=np.float64)
a[0] = 0
c[-1] = 0

tiempo_pivoteo_vs_thomas(a, b, c, d)