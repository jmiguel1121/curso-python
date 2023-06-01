import numpy as np
'''
#vector
a=np.array([1, 3, 5, 7, 9, 2, 4, 6, 8])
print(a)
#matriz
b=np.array([[1, 3, 5], [7, 9, 2], [4, 6, 8]])
print(b)
#rango
c=np.array(range(1, 10))
print(c)
#dtype
d=np.array([x**2 for x in range(20)], dtype=float)
print(d)
#inicializar en ceros
a=np.zeros(10)
print(a)
#inicalizar en uonos
a=np.ones(10)
print(a)
#inicializar en cualquier valor, en este caso 3
a=np.full(10, 3)
print(a)
#rango lim inf, lim sup y salto de 2.5
a=np.arange(0., 100., 2.5)
print(a)
a=np.linspace(0, 5, 7)
print (a)
#matriz cuadrada
a=np.diag([3, 5, 7, 9])
print(a)
#matriz aleatoria random

a=np.random.random((2, 3))
print(a)
#lim sup negativo
a=4*np.random.random((2, 3)) - 5
print(a)
#Distribuccion normal
a=np.random.normal(0, 1, 10)
print(a)
#matriz aleatoria
a=np.random.randint(-9, 10, (5, 5))
print(a)
'''
#Cargar datos desde archivo plano
a=np.loadtxt("datos.txt")
print(a)