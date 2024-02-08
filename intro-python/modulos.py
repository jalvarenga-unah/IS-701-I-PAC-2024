
# Importar un módulo (con todas sus funciones)
# import mis_modulos.operaciones as op

from mis_modulos.operaciones import suma, division
import random as rd
import math as mt

import numpy as np  # trabajar con arreglos

mt.sqrt(16)

# suma = op.suma
# resta = op.resta(3,6)
# multiplicacion = op.multiplicacion
# division = op.division

# print(suma(3,6))
# print(division(3,6))

# print(rd.randint(1, 100))

# trabajar con arreglos/listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

np_numeros = np.array(numeros)

cuadrados = np_numeros ** 2

arreblo_bidimensional = np.array([np_numeros,cuadrados])

producto_punto = np.dot(np_numeros, cuadrados)

# mean = np.mean(np_numeros)
print(producto_punto)

print(np.shape(arreblo_bidimensional))

# print((numeros))
# print((mean))
