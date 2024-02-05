
class Mascota:
    # Atributos/Propiedades
    # tipo = 'Perro'
    # comidas_favoritas = [] # la lista se comparte entre todas las instancias

    #Constructor
    def __init__(self, nombre:str, raza:str, tipo:str='Perro'):
        self.nombre = nombre
        self.raza = raza
        self.tipo = tipo
        self.comidas_favoritas = []
        print('Se ha creado una mascota')

    # Métodos / Comportamientos
    def correr(self):
        print("Corriendo")
    
    def datos_generales(self):
        print(f'Nombre: {self.nombre}, es un {self.tipo} raza: {self.raza}')


# Instanciar la clase
mascota1 = Mascota(nombre='Apolo', raza='Terrier' )

mascota1.comidas_favoritas.append('Pollito')

mascota2 = Mascota('Mishi', 'Persa', 'Gato' )

mascota2.comidas_favoritas.append('Pescado')

# Acceder a los atributos
# mascota2.tipo = 'Gato'

# Acceder a los métodos

# podemos guardar la referencia del método en una variable
datos = mascota1.datos_generales
print(mascota1.comidas_favoritas)

# Luego podemos ejecutarlo
datos()

mascota2.datos_generales()
print(mascota2.comidas_favoritas)
# mascota1.correr()