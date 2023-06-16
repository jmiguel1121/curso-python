import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5, 11)
#mas colores
#color y alpha. Alpha indica opacidad.
plt.plot(x, x, color="red") # Medio transparente
plt.plot(x, x+1, color="red", alpha=0.5) # Medio transparente
plt.plot(x, x+2, color="#8B008B")        # RGB hex code
plt.plot(x, x+3, color="#F08C08");       # RGB hex code 
plt.grid(True) # poner grid en la grafica
plt.show()