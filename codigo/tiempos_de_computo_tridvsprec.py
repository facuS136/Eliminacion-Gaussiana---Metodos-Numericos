import time
import numpy as np
import matplotlib.pyplot as plt

from conPivoteoTridiagonal import precomputar, eg_thomas_algoritm_precomputado
from conPivoteoTridiagonal import eg_thomas_algoritm

def tiempo_thomas_vs_precomputado(a, b, c, d, tolerancia):
    cantidad_de_repeticiones = 100
    sin_precomputo_times = []
    con_precomputo_times = []
    repeticiones = [i for i in range(10, cantidad_de_repeticiones)]

    b_prec = c_prec = factores = None

    # medimos el tiempo de thomas algoritm
    
    for r in repeticiones:
        tiempo_sin_precomputo = []
        for _ in range(20):
            sin_precomputo_start = time.time()
            for _ in range(r):
                eg_thomas_algoritm(a.copy(), b.copy(), c.copy(), d.copy(), tolerancia)
            sin_precomputo_end = time.time()
            tiempo_sin_precomputo.append(sin_precomputo_end - sin_precomputo_start)
        sin_precomputo_times.append(min(tiempo_sin_precomputo))
    
    # medimos el tiempo del precomputo
    
    for r in repeticiones:
        tiempo_con_precomputo = []
        for _ in range(20):
            con_precomputo_start = time.time()
            b_prec, c_prec, factores = precomputar(a.copy(), b.copy(), c.copy(), tolerancia)
            for _ in range(r):
                eg_thomas_algoritm_precomputado(b_prec.copy(), c_prec.copy(), factores.copy(), d.copy())
            con_precomputo_end = time.time()
            tiempo_con_precomputo.append(con_precomputo_end - con_precomputo_start)
        con_precomputo_times.append(min(tiempo_con_precomputo))

    plt.plot(repeticiones, sin_precomputo_times, color="red")
    plt.plot(repeticiones, con_precomputo_times, color="blue")
    plt.legend(["Sin precomputo", "Con precomputo"])
    plt.xlabel("Repeticiones (n)")
    plt.xscale("log")
    plt.yscale("log")
    plt.ylabel("Tiempo (Segundos)")
    plt.savefig("tiempos_sin_precomputo_vs_precomputo.png")


a = np.full(100, 1, dtype=np.float64)
b = np.full(100, -2, dtype=np.float64)
c = np.full(100, 1, dtype=np.float64)
d = np.full(100, 25, dtype=np.float64)
a[0] = 0
c[-1] = 0

tiempo_thomas_vs_precomputado(a, b, c, d, 0.002)