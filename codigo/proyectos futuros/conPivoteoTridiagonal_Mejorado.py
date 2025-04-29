import sys
import numpy as np
import numpy.linalg as lng

def swap(array_a, array_b, pos_a, pos_b):
    val_pos_a = array_a[pos_a]
    val_pos_b = array_b[pos_b]
    array_a[pos_a] = val_pos_b
    array_b[pos_b] = val_pos_a

def eg_tridiagonal(a, b, c, d, tolerancia):  
    n = b.size

    A = np.zeros(n-2)                                                   # diagonal auxiliar por encima de c

    for i in range(n-1):                                                # recorremos la diagonal
        if(b[i] < a[i]):                                                # si el pivot de abajo es mejor, intercambiamos las filas (no hace falta ver los de mas abajo porque ya se que valen 0)
            swap(b,a,i,i)                                               #
            swap(c,b,i,i+1)                                             #
            if(i + 1 < n - 1):                                          #
                swap(A,c,i,i+1)                                         #
            swap(d,d,i,i+1)                                

        factor = a[i]/b[i]                                              # calculamos el factor

        if abs(b[i]) < tolerancia:                                      # vemos si el pivot es demasiado pequeño
            print(f"Advertencia de posible error numérico: hay una división por un valor cercano a cero ({abs(b[i])})")

        # solo aplicamos la transformacion lineal a la fila directamente abajo
        a[i] = a[i] - (b[i]*factor)         
        b[i+1] = b[i+1] - (c[i]*factor)
        if(i + 1 < n - 1):
            c[i+1] = c[i+1] - (A[i]*factor)
        d[i+1] = d[i+1] - (d[i]*factor)
    
    # Sustituir para atras (Backward substitution)
    x = np.zeros(n) 

    for i in range(n - 1, -1, -1):
        sumatoria = 0

        # la sumatoria a lo sumo va a tener dos sumas
        if(i < n - 1):
            sumatoria += c[i]*x[i+1]
        if(i < n - 2):
            sumatoria += A[i]*x[i+2]

        x[i] = (d[i] - sumatoria)/b[i]
    
    return x
