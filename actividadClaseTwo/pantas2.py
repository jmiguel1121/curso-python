import pandas as pd
import numpy as np
# Importar la funcion de NumPy para crear arreglos de numeros enteros
from numpy.random import randn
a = np.random.seed(10)
print(a)
# Inicializar el generador aleatorio
# Forma rapida de crear una lista de python desde strings
print('A B C D E F G H'.split())
df = pd.DataFrame(randn(5, 4),
                  index='Lunes Martes Miercoles Jueves Viernes'.split(),
                  columns='Uvas Manzanas Peras Mangos '.split())
print(df)
print('El número de filas y columnas del df es:', df.shape)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
# mostrar columna
print(df['Peras'])
df['banano'] = df['Uvas'] + df['Peras']
print(df)
print(df.shape)
# eliminar dato
df = df.drop('Peras', axis=1)
print(df)
print(df.shape)
