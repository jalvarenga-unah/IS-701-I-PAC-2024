#clave PC: UNAH1234567@
rango = range(1, 10, 2)

numeros = [1, 2, 3, 4, 5, 6, 3, 5,1,7, 8, 9]

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

control = []
for numero in numeros:
    if numero in control:
        print(f"el primer numero repetido es: {numero}");
        break #rompe el ciclo
    else:
        control.append(numero)
        
