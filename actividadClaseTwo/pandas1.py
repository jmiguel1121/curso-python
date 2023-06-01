import pandas as pd
import numpy as np
# Manejo de pd.Series
# Crear diferentes tipos de datos
'''
labels = ['a','b','c'] # lista de eetiquetas
my_list = [10,20,30] # lista con valores
arr = np.array([10,20,30]) # Convertir ista de valores en arreglo NumPy
d = {'a':10,'b':20,'c':30} # Creacion de un diccionario
print(labels)
print(my_list)
print(arr)
print(d)
#Desde Listas
# Convertir una lista en series usando el metodo pd.Series
# observe que se crean los nombres con las posiciones de cada elemento
a=pd.Series(data=my_list)
print(a)
#salida

0    10
1    20
2    30
print(type(a));
print(pd.Series(my_list,index=labels))
print(type(a));
'''
# Creando serie 1
ser1 = pd.Series([1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
# Crear serie 2
ser2 = pd.Series([1, 2, 5, 4], index=['USA', 'Germany', 'Italy', 'Japan'])
a = ser2['Germany']
print(a)
a = ser1+ser2
print(a)
