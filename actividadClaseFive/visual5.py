import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5, 11)
y = x ** 2
#Subplots
# la funcion es plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,2,1) # subplot fila=1 Col=2, grafica=1
plt.plot(x, y, 'r--') # r-- color rojo y linea discontinua
plt.subplot(1,2,2) # subplot fila=1 Col=2, grafica=2
plt.plot(y, x, 'g*-'); # para no mostrar info de la funcion
plt.tight_layout() # para que no se superpongan las gra
plt.show()