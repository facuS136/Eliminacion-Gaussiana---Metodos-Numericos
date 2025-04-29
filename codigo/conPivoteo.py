import sys
import numpy as np
import numpy.linalg as lng

def matriz_extendida(A, b):
    return np.append(A, np.reshape(b, (b.size, 1)), axis=1)

def eg_con_pivoteo(A, b, tolerancia):   

    M = matriz_extendida(A, b)
    n = M.shape[0]

    # Triangular
    for j in range(n):                                              # iterando la diagonal
        
        fila_a_pivotear = j                                         # inicio con el pivot M[j][j]
        for k in range(j + 1, n):                                   # recorro las filas debajo 
            if abs(M[k][j]) > abs(M[fila_a_pivotear][j]):                # y busco si hay un mejor pivot
                fila_a_pivotear = k

        # Swapeear filas
        M[[j, fila_a_pivotear]] = M[[fila_a_pivotear, j]]

        if M[j][j] == 0:                                            # si el pivot es 0, abortamos el algoritmo
            raise Exception("No se puede encontrar la solución")
            
        for i in range(j + 1, n):                                   # iterando las columnas debajo de la parte de la diagonal que nos encontramos

            factor = M[i][j] / M[j][j]                              # calculamos el factor 
            if abs(M[j][j]) < tolerancia:                           # vemos si el pivot es demasiado pequeño
                print(f"Advertencia de posible error numérico: hay una división por un valor cercano a cero ({abs(M[j][j])})")
            for k in range(j, n + 1):                               # cambiamos el valor de las filas debajo del pivot
                M[i][k] = M[i][k] - factor*M[j][k]
                
    # Sustituir para atras (Backward substitution)
    res = np.zeros(n)
    for i in range(n - 1, -1, -1):
        
        sumatoria = 0

        for j in range(i + 1, n):
            sumatoria += M[i][j] * res[j]
        
        res[i] = (M[i][n] - sumatoria)/M[i][i]

    return res


if __name__ == "__main__":
    # python conPivoteo.py MATRIZ TERMINO_INDEPENDIENTE TOLERANCIA "TIPO DE DATO"
    type = eval(sys.argv[4])
    tolerancia = type(sys.argv[3])
    matriz = np.array(eval(sys.argv[1]), dtype=type)
    termino_ind = np.array(eval(sys.argv[2]), dtype=type)

    print("Obtenido: ", eg_con_pivoteo(matriz, termino_ind, tolerancia))
    print("Esperado: ", lng.solve(matriz, termino_ind))