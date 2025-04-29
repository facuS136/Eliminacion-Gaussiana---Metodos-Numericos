import numpy as np
import matplotlib.pyplot as plt
import time
from conPivoteo import eg_con_pivoteo
from sinPivoteo import eg_sin_pivoteo

def crear_placa(n, alpha):
    placa = np.zeros((n*n, n*n), dtype=np.float64)

    for i in range (n):
        for j in range (n):
            d = i*n + j
            placa[d][d] = 1 + 4*alpha

            if (j != 0):
                placa[d][d-1] = -alpha
            if (j != n-1):
                placa[d][d+1] = -alpha
        
            if (i != 0):
                placa[d][d-n] = -alpha
            if (i != n-1):
                placa[d][d+n] = -alpha                
    
    return placa

def difusion_2D(n, t, alpha, con_pivoteo):
    u = np.zeros((t, n*n), dtype=np.float64)

    tiempos = []

    u[0][(n*n)//2] = 100.0
    placa = crear_placa(n, alpha)
    
    plt.pcolor(u[0].reshape(n,n), vmin=0, vmax=100, cmap="hot")
    plt.colorbar()
    plt.title("Instante: 1")
    if(con_pivoteo):
        plt.savefig(f"difusion_2D_{1}_con_pivoteo.png")
    else:
        plt.savefig(f"difusion_2D_{1}_sin_pivoteo.png")
    plt.clf()

    for k in range(1, t):
        t1 = time.time()
        if(con_pivoteo):
            u_obtenido = eg_con_pivoteo(placa.copy(), u[k-1].copy(), 0.001)
        else:
            u_obtenido = eg_sin_pivoteo(placa.copy(), u[k-1].copy())
        t2 = time.time()
        tiempos.append((t2 - t1)*1000)

        u[k] = u_obtenido

        u[k][(n*n)//2] = 100.0
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == (n-1) or j == (n-1):
                    u[k][i*n + j] = 0

        print("iteracion ", k, " calculada")

        if k in [9, 49, 99]:
            plt.pcolor(u[k].reshape(n,n), vmin=0, vmax=100, cmap="hot")
            plt.colorbar()
            plt.title("Instante: " + str(k + 1))
            if(con_pivoteo):
                plt.savefig(f"difusion_2D_{k+1}_con_pivoteo.png")
            else:
                plt.savefig(f"difusion_2D_{k+1}_sin_pivoteo.png")
            plt.clf()
    
    return tiempos

tiempos_con_pivoteo = difusion_2D(15, 100, 0.1, con_pivoteo=True)

tiempos_sin_pivoteo = difusion_2D(15, 100, 0.1, con_pivoteo=False)

plt.boxplot([tiempos_con_pivoteo, tiempos_sin_pivoteo], positions=[1, 2], vert=True, labels=["Con pivoteo", "Sin pivoteo"])
plt.ylabel("milisegundos")
plt.title("Tiempos de computo")
plt.savefig("comparacion_tiempo_difusion_pivoteo_vs_sinPivoteo.png")