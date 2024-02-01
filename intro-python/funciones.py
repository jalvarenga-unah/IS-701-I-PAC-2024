
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
    '''
    Calcula el área de un triángulo
    base: base del triángulo
    altura: altura del triángulo
    '''
    return (base * altura) / 2

area = area_triangulo(5, 10)

print(area)

def suma_numeros(*valores): #tupla
   # valores es una tupla y no se puede modificar
    print(valores) 
    suma = 0
    for valor in valores:
        suma += valor
    return suma

print( suma_numeros(1,4,6,8) )

# **kwargs
def persona( ** atributos ): #diccionario
    return atributos

persona1 = persona(nombre = 'Juan', edad = 25)

print(persona1) 