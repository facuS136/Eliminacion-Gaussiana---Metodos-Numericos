import sys
import numpy as np
import numpy.linalg as lng

def matriz_extendida(A, b):
    return np.append(A, np.reshape(b, (b.size, 1)), axis=1)

def eg_sin_pivoteo(A, b):   

    M = matriz_extendida(A, b)
    n = M.shape[0] 

    # Triangular
    for j in range(n):                                                      # iterando la diagonal
        for i in range(j + 1, n):                                           # iterando las columnas debajo de la parte de la diagonal que nos encontramos

            if M[j][j] == 0:                                                # si el pivot es 0, abortamos el algoritmo
                raise Exception("No se puede encontrar la solución")

            factor = M[i][j] / M[j][j]                                      # calculamos el factor 

            for k in range(j, n + 1):                                       # cambiamos el valor de las filas debajo del pivot
                M[i][k] = M[i][k] - factor*M[j][k]
                
    # Sustituir para atras (Backward substitution)
    res = np.zeros(n)                                                       # vector donde guardaremos la solucion

    for i in range(n - 1, -1, -1):

        sumatoria = 0

        for j in range(i + 1, n):
            sumatoria += M[i][j] * res[j]
        
        res[i] = (M[i][n] - sumatoria)/M[i][i]

    return res

"""
# Ejemplo q no funciona con este algoritmo
#A = np.array([[2, 1, -1, 3], [-2, 8, 4, 0], [4, 1, -2, 4], [-6, -1, 2, -3]], dtype=np.float64)
#b = np.array([2, 3, 4 ,5], dtype=np.float64)
#A = np.array([[0, 1], [1, 0]], dtype=np.float64)
#b = np.array([1, 1], dtype=np.float64)

# casos que funcionan
#A = np.array([[2, 3, -1], [4, 1, 2], [-2, 2, 3]], dtype=np.float64)
#b = np.array([1, 2, 3], dtype=np.float64)
#A = np.array([[1, 0], [0, 1]], dtype=np.float64)
#b = np.array([1, 1], dtype=np.float64)

#x_solve = lng.solve(A,b)
#print("El que esta bien: ",x_solve)

#res = eg_sin_pivoteo(A, b)
#print("El que nuestro: ", res)
"""

if __name__ == "__main__":
    # python conPivoteo.py MATRIZ TERMINO_INDEPENDIENTE "TIPO DE DATO"
    type = eval(sys.argv[3])
    matriz = np.array(eval(sys.argv[1]), dtype=type)
    termino_ind = np.array(eval(sys.argv[2]), dtype=type)

    print("Obtenido: ", eg_sin_pivoteo(matriz, termino_ind))
    print("Esperado: ", lng.solve(matriz, termino_ind))