# print("Hola mundo")
# print("Mi nombre es Juan Alvarenga")

#comentario de una linea

#Declaración de variables
nombre = "Juan Alvarenga" # String
edad = 29 # int
sueldo = 1.02 # float
casado = True # boolean

# print(nombre + " tengo " + str(edad))
# print(type(edad)) # para saber el tipo de variable
# print(f"{nombre} tengo {edad} años") # otra forma de concatenar

# listas ✅, tuplas ✅ , diccionarios, set

mi_lista = ["Juan", 29, 29, True, "otra cosa", [1,2,3,True] ] # lista
# copia_lista = mi_lista # hacer referencia a la lista original
copia_lista = mi_lista.copy() # copiar la lista original

print("Copia!!!!",copia_lista)

# mi_lista[30] = 'Holii' # no se puede agregar un valor a una posicion que no existe
mi_lista[0] = "Juanito" # cambiar el valor de la lista

# agregar valores a la lista
mi_lista.append('nuevo valor') # agregar un nuevo valor a la lista
mi_lista.insert(3, 'este es el nuevo valor') # agregar un nuevo valor a la lista en la posicion 3
mi_lista.extend(['Apolo', 'Polar', True]) # agregar varios valores a la lista

#eliminar valores de la lista
# mi_lista.pop() # elimina el ultimo valor de la lista
# mi_lista.remove('Juanito') # elimina el valor de la lista que coincida con el valor que se le pasa por parametro
# mi_lista.pop(0) # elimina el valor de la posicion 2 de la lista

copia_lista.clear() # elimina todos los valores de la lista

print(mi_lista) # imprime la lista
print(len(mi_lista)) # imprime la cantidad de elementos de la lista 
print(mi_lista.count(29)) # imprime la cantidad de veces que se repite el valor en la lista
print(mi_lista[2:5]) # imprime los valores de la posicion 2 a la 5, sin incluir el ultimo valor
print(mi_lista[4:]) # imprime los valores de la posicion 4 hasta el final
print(mi_lista.index(True)) # imprime la posicion del valor que se le pasa por parametro

# tuplas
mi_tupla = ('Juan', 29, 29, True, 'otra cosa', [1,2,3,True]) # tupla

# mi_tupla[0] = 'Juanito' # no se puede cambiar el valor de una tupla porque es inmutable

print(mi_tupla[0]) # imprime la cantidad de veces que se repite el valor en la tupla