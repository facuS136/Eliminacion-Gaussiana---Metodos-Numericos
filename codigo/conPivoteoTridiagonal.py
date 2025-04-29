import sys
import numpy as np
import numpy.linalg as lng


def eg_thomas_algoritm(a, b, c, d, tolerancia):
    # PRE: a[0] = c[n-1] = 0
    n = b.size
    
    for i in range(1, n):
        factor = a[i] / b[i-1]
        
        if abs(b[i-1]) < tolerancia:
            print(f"Advertencia de posible error numérico: hay una división por un valor cercano a cero ({abs(b[i-1])})")

        b[i] = b[i] - factor * c[i-1]
        d[i] = d[i] - factor * d[i-1]
    
    x = np.zeros(n)

    x[n-1] = d[n-1] / b[n-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

    return x

def precomputar(a, b, c, tolerancia):
    # PRE: a[0] = c[n-1] = 0
    n = b.size
    factores = np.zeros(n)
    
    for i in range(1, n):
        factor = a[i] / b[i-1]
        factores[i] = factor

        if abs(b[i-1]) < tolerancia:
            print(f"Advertencia de posible error numérico: hay una división por un valor cercano a cero ({abs(b[i-1])})")

        b[i] = b[i] - factor * c[i-1]

    return b, c, factores

def eg_thomas_algoritm_precomputado(b_prec, c_prec, factores, d):
    n = b_prec.size

    for i in range(1, n):
        d[i] = d[i] - factores[i] * d[i-1]
        
    x = np.zeros(n)

    x[n-1] = d[n-1] / b_prec[n-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c_prec[i] * x[i + 1]) / b_prec[i]

    return x

