import pandas as pd
# Crear dataframe desde un diccionario
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
print(data)
# conversion del diccionario a dataframe
df = pd.DataFrame(data)
print(df)
# Se puede usar el método .groupby() para agrupar filas en función de un nombre de columna. Por ejemplo, vamos a agruparnos a partir de la Compañía. Esto creará un objeto DataFrameGroupBy:
# agrupar por Company
print(df.groupby('Company'))
# Se puede grabar este objeto en una nueva variable:
by_comp = df.groupby("Company")
"""Ejercicio: muestre la variable"""
# Promedio de ventas por company
print(by_comp.mean())
