import sys
import numpy as np
import numpy.linalg as lng
import matplotlib.pyplot as plt
from conPivoteoTridiagonal import eg_thomas_algoritm

def laplace(d, tolerancia):
    a = np.full(d.size, 1, dtype=d.dtype)
    b = np.full(d.size, -2, dtype=d.dtype)
    c = np.full(d.size, 1, dtype=d.dtype)
    a[0] = 0
    c[-1] = 0
    return eg_thomas_algoritm(a, b, c, d, tolerancia)



tipo = np.float64
tolerancia = 0.001
n = 101

d1 = np.zeros(n, dtype=tipo)
d2 = np.zeros(n, dtype=tipo)
d3 = np.zeros(n, dtype=tipo)

for i in range(0, n):
    if(i == int(tipo(n)/2) + 1):
        d1[i] = 4.0/tipo(n)
    d2[i] = 4.0/(tipo(n)*tipo(n))
    d3[i] = ((-1.0 + ((2.0*i)/(tipo(n) - 1.0)))*12.0)/(tipo(n)*tipo(n))

plt.plot(laplace(d1, tolerancia), color="blue")
plt.plot(laplace(d2, tolerancia), color="orange")
plt.plot(laplace(d3, tolerancia), color="green")
plt.legend(["(a)", "(b)", "(c)"])
plt.xlabel("x")
plt.ylabel("n")
plt.savefig("laplace.png")