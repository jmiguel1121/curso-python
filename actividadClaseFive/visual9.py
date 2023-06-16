import matplotlib.pyplot as plt
import numpy as np
#ESTADISTICA
#Grafica X vs Y
# crear datos aleatorios
N = 50
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y)
plt.title("Scatter plot Simple");
#plt.show() # En jupyter notebook no es necesario este comando

#Con las graficas de scatter o dispersion se pueden representar mas de 2 variables en una misma grafica, en el siguiente ejemplo se realizara la comparacion de x vs y el color de los puntos se representara con otra variable y el tamaño de los puntos sera otra variable
# se creara otra variable que se representara con colores
colors = np.random.rand(N) # usar colores aleatorios

# se creara otra variable que se representara con el area de los puntos
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radio

plt.scatter(x, y, s=area, c=colors, alpha=0.5) # el atributo alpha es para la transparencia
plt.title("Scatter plot de representacion de 4 variables");
plt.show()