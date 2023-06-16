import pandas as pd # libreria manipulacion de datos
import seaborn as sns # Libreria graficas
#import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline
archivo = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/anscombe.csv')
'''print('archivo ********************')
print(archivo)
print('****************************')

#Calcular los valores de la media y la varianza de cada dataset
agg = archivo.groupby('dataset').agg([np.mean, np.var])
print('agg ************************')
print(agg)
print('****************************')
'''

res=[g for _, g in archivo.groupby('dataset')]

print(res)

'''
#Calcular la correlacion
corr = [g.corr()['x'][1] for _, g in archivo.groupby('dataset')]
print(corr)

#Graficar los datasets, haciendo un scatterplot y una regression lineal
# Grafica Usando seaborn
sns.set(style="ticks")
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=archivo,
               col_wrap=2, ci=None, palette="muted", height=4,
               scatter_kws={"s": 50, "alpha": 1});

#Calculo de los valores de la regresion lineal
fits = [np.polyfit(g['x'], g['y'], 1) for _, g in archivo.groupby('dataset')]
# Almacenar los valores calculados de las regresiones lineales en un dataframe
val_reg = pd.DataFrame(fits,columns=['pendiente','intercepto'],index='I II II IV'.split())
val_reg.index.names = ['dataset']
print(val_reg)'''