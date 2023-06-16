#Guardando graficas
import matplotlib.pyplot as plt
import numpy as np

#Matplotlib puede generar resultados de alta calidad en varios formatos, 
# incluidos PNG, JPG, EPS, SVG, PGF y PDF. 
# Para guardar una figura en un archivo, podemos usar el método savefig de la clase Figure:
# generacion de datos aleatorios
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

#Lo primero es antes de crear una grafica definir la clase Figure al principio de todo la grafica, Ejemplo:
fig = plt.figure(figsize=(10,4)) 
plt.scatter(x, y) 
plt.title("Scatter plot Simple");
fig.savefig("figura.png")
#Aquí también podemos especificar opcionalmente el DPI y elegir entre diferentes formatos de salida (PNG, JPG, EPS, SVG, PGF y PDF):
fig.savefig("figura.pdf", dpi=200)