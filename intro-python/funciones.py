
def saludar(): # retorna "None"
    print('Hola mundo')
    print('Esto se ejecuta desde una función')

def saludo(nombre): # retorna String
    return f'Hola {nombre}' #return es la ultima instrucción que se ejecuta en una función
    print('Texto despues del retorno') # <- esta instrucción no se ejecuta

# la definición de la varibale "nombre", está fuera de la función
nombre = 'Juan'

# ejecutar mi función
# saludar() # <- ejcuta la funcion "saludar"
# print(saludar())
print(saludo('Enrique'))

def area_triangulo(base: float, altura: float):
    return (base * altura) / 2

area = area_triangulo(altura = 5, base = 10)

print(area)

def suma_numeros(*valores):
   # valores es una tupla y no se puede modificar
    print(valores)
    suma = 0
    for valor in valores:
        suma += valor
    return suma
