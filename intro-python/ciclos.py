#clave PC: UNAH1234567@
rango = range(1, 10, 2)

# for valor in numeros:
#     print(valor)

mascota = {
    "nombre": "Tom",
    "tipo": "gato",
    "edad": 2
}

for llave, valor in mascota.items():
    print(f"{llave}: {valor}")

nombre = 'Juan Alvarenga'

# for letra in nombre:
#     print(letra)

contador = 0
while contador < 10:
    # print("Hola")
    contador += 1


numeros = [1, 2, 3, 4, 5, 6, 3, 5,1,7, 8, 1, 9]

control = []
for numero in numeros:
    if numero in control:
        print(f"el primer numero repetido es: {numero}");
        break #rompe el ciclo
        # continue
    else:
        control.append(numero)


duplicados = []

# print(numeros.count(1) > 1)
#forma 1
for numero in numeros:
    if numero not in duplicados and numeros.count(numero) > 1:
        duplicados.append(numero)


#forma 2
        
# set, es una estructura de datos que no permite duplicados
duplicados = list(set([numero for numero in numeros if numeros.count(numero) > 1]))

print(duplicados)

cadena = 'hola mundo hola hola mundo mundo mundo hola hola mundo mundo mundo mundo'

palabras = {}

for palabra in cadena.split(' '):
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

for palabra, cantidad in palabras.items():
    print(f"{palabra}: {cantidad}")
