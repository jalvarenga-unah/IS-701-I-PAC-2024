
mascota = { 
    'nombre': 'Apolo', 
    'edad': 2, 
    'raza': 'Terrier',
    'comidas_favoritas': ['pollo', 'carne', 'pescado']
}

# otra forma de crear un diccionario
test = dict(nombre='Apolo', edad=2, raza='Terrier')
# print(nombre in test)

#hacer una copia
mascota2 = mascota.copy()

mascota2['apodo'] = 'Apolito'

#eliminar un valor
del mascota2['comidas_favoritas']

print(mascota)
print(mascota2)

llaves = mascota.keys() # obtener las llaves del diccionario
valores = mascota.values() # obtener los valores del diccionario

print(llaves)
print(valores)

print(mascota.get('apodo', 'No tiene apodo'))
print(mascota2.get('apodo', 'No tiene apodo'))
print('tamanio',len(mascota)) # obtener el tamanio del diccionario
print(mascota.items()) # obtener los items del diccionario     
#TODO: por investigar
# print(mascota.has_key('apodo')) # verificar si existe una llave en el diccionario

nuevos_datos = {
    'edad': 3,
    'apodo': 'Apolito',
    'comidas_favoritas': ['pollo', 'huesos']
}

# actualizar un diccionario
# actualiza los valores de las llaves que existen y agrega las que no existen
# mutando el diccionario original
mascota.update(nuevos_datos) 
print(mascota)
mascota.pop('apodo') # eliminar un valor del diccionario
mascota.clear() # eliminar todos los valores del diccionario
print(mascota)