#ejemplo muy simple usando dos arreglos numpy. También se pueden usar listas, pero lo más probable es usar arreglos Numpy o columnas de pandas (que esencialmente también se comportan como arreglos). Los datos que queremos graficar:
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5, 11)
y = x ** 2

#Podemos configurar los rangos de los ejes usando los métodos ylim y xlim 
# en el objeto del eje, o axis('tight') para obtener automáticamente 
# rangos de ejes “tightly fitted”:
plt.figure(figsize=(12, 4))

plt.subplot(1,3,1)
plt.plot(x, x**2, x, x**3)
plt.title("Rango por defecto de los ejes")

plt.subplot(1,3,2)
plt.plot(x, x**2, x, x**3)
plt.axis('tight')
plt.title("Ejes apretados")

plt.subplot(1,3,3)
plt.plot(x, x**2, x, x**3)
plt.ylim([0, 60])
plt.xlim([2, 5])
plt.title("ejes de rango personalizados");

plt.tight_layout() # para que no se superpongan las graficas

#plt.show()


#Escala Logaritmica
plt.figure(figsize=(10,4))
      
plt.subplot(1,2,1)
plt.plot(x, x**2, x, np.exp(x))
plt.title("escala Normal")

plt.subplot(1,2,2)
plt.plot(x, x**2, x, np.exp(x))
plt.yscale("log")
plt.title("Escala Logaritmica(y)");

plt.tight_layout() # para que no se superpongan las graficas
plt.show()