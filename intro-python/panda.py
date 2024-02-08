import pandas as pd

datos = {
    'nombre': ['Juan', 'Ana', 'Jose', 'Arturo'],
    'edad': [25, 18, 23, 27],
}

# creando un DataFrame de pandas
df = pd.DataFrame(datos)

condicion = df['edad'] > 20

# print( df[ condicion ]['edad'].min() )

print( df.shape )
