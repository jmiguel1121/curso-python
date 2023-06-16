#pasteles
import matplotlib.pyplot as plt

labels = 'Caballos', 'Cerdos', 'Perros', 'Vacas'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # solo "Saque" el 2do pedazo (ejem. 'cerdos')

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

plt.axis('equal')  #La relación de aspecto igual garantiza que el círculo sea homogeneo
plt.show()