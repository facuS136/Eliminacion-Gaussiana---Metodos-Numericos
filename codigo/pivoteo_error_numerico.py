import sys
import numpy as np
import numpy.linalg as lng
import matplotlib.pyplot as plt
from conPivoteo import eg_con_pivoteo


def matriz_epsilon(e):
    return np.array([[0, e, -e],
                     [-e, 0, e],
                     [e, -e, 0]], dtype=type(e))

A_base = [[1, 2, 3],
          [1, 2, 3],
          [1, 2, 3]]

d_base = [6, 6, 6]

x_base = [1, 1, 1]

def obtener_error(x, x_esperado):
    return np.max(np.abs(x - x_esperado))

def graficar(x, y, nombre):
    plt.figure()
    plt.plot(x,y, '-r')
    plt.xlabel("epsilon")
    plt.ylabel("errores")
    plt.xscale("log")
    plt.legend(["|x* - x|"])
    plt.title("Medicion de error con " + nombre)
    plt.savefig("grafico_" + nombre + ".png")

def pivoteo_error_numerico(saltos, tipos_de_float):
    for type in tipos_de_float:
        epsilons = np.logspace(-6, 0, num=saltos, dtype=type)
        errores = np.zeros(epsilons.size, dtype=type)

        for i in range(epsilons.size):
            x_obtenido = eg_con_pivoteo(np.array(A_base, dtype=type) + matriz_epsilon(epsilons[i]), np.array(d_base, dtype=type), 0)
            errores[i]  = obtener_error(x_obtenido, np.array(x_base, dtype=type))
        graficar(epsilons, errores, type.__name__)

# parametros: 
#   cantidad de muestreos de epsilon
#   tipos de datos para comparar error
pivoteo_error_numerico(1000, [np.float32, np.float64])