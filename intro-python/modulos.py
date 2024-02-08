
# Importar un módulo (con todas sus funciones)
# import mis_modulos.operaciones as op

from mis_modulos.operaciones import suma, division
import random as rd
import math as mt

import numpy as np #trabajar con arreglos

mt.sqrt(16)

# suma = op.suma
# resta = op.resta(3,6)
# multiplicacion = op.multiplicacion
# division = op.division

print(suma(3,6))
print(division(3,6))

print(rd.randint(1, 100))