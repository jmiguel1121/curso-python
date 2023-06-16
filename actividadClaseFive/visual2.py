#ejemplo muy simple usando dos arreglos numpy. También se pueden usar listas, pero lo más probable es usar arreglos Numpy o columnas de pandas (que esencialmente también se comportan como arreglos). Los datos que queremos graficar:
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5, 11)
y = x ** 2
print(x) 
print(y)

#Podemos crear un diagrama de líneas muy simple usando lo siguiente:
# Metodo basico para graficar X vs Y
plt.plot(x, y) # se grafica una linea de color azul
#plt.show() # Mostrar la grafica luego de que ya se definio todos los elementos
plt.title('Grafica X vs Y'); # definir el titulo de la grafica
#plt.show() # Mostrar la grafica luego de que ya se definio todos los elementos
#nombres de los ejes
plt.xlabel('eje X') # definir el nombre del eje X
plt.ylabel('eje Y') # definir el nombre del eje Y
#plt.show() # Mostrar la grafica luego de que ya se definio todos los elementos
#legend
plt.plot(x, y, label="x vs y") # se grafica una linea de color azul
plt.legend(); # agregar el legend al plot
#plt.show() # Mostrar la grafica luego de que ya se definio todos los elementos
"""
Ejercicio1
¿Por que la gráfica paso de color azul a rojo?
"""
#grilla
#plt.grid(True) # poner grid en la grafica
#plt.show() # Mostrar la grafica luego de que ya se definio todos los elementos
#tamaños
# figsize es una tupla del ancho y alto de la figura en pulgadas
# dpi es el punto por pulgada (pixel por pulgada).
# se cambia el tamaño de la figura y el numero de puntos por pulgada
#plt.figure(figsize=(8,4), dpi=100)
#plt.show() # Mostrar la grafica luego de que ya se definio todos los elementos
"""
Ejercicio2
¿Por qué aparece una doble ventana grafica?
"""
#colores de línea
# Estilo MATLAB de estilo y color de linea
plt.plot(x, x**2, 'b.-') # linea azul con puntos
plt.plot(x, x**3, 'g--'); # Linea verde discontinua
plt.plot(x, x**4, 'r--'); # Linea roja discontinua
plt.show()