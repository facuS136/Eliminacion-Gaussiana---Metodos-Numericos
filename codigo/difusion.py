import numpy as np
import matplotlib.pyplot as plt
import math
from conPivoteoTridiagonal import eg_thomas_algoritm

def difusion(n, r, m, alpha):
    u = np.zeros((m, n), dtype=np.float64)
    for i in range(0, n):
        if(math.floor(n/2) - r < i and i < math.floor(n/2) + r):
            u[0][i] = 1

    a = np.full(n, -alpha, dtype=np.float64)
    c = np.full(n, -alpha, dtype=np.float64)
    b = np.full(n, 1 + 2*alpha, dtype=np.float64)

    for k in range(1, m):
        u_obtenido = eg_thomas_algoritm(a.copy(), b.copy(), c.copy(), u[k-1].copy(), 0.001)
        for i in range(0, n):
            u[k][i] = u_obtenido[i]

    plt.pcolor(u.transpose())
    plt.xlabel("k")
    plt.ylabel("x")
    plt.colorbar().set_label("n")
    plt.title("alpha = " + str(alpha))
    plt.savefig("difusion_"+ str(alpha) + ".png")
    plt.clf()

difusion(101, 10, 1000, 0.1)
difusion(101, 10, 1000, 0.5)
difusion(101, 10, 1000, 1)
difusion(101, 10, 1000, 3)
difusion(101, 10, 1000, 5)