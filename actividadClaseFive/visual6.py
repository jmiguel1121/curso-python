import matplotlib.pyplot as plt
#Multiples Subplots
# la funcion es plt.subplot(nrows, ncols, plot_number)
plt.subplot2grid((3,3), (0,0), colspan=3)
plt.subplot2grid((3,3), (1,0), colspan=2)
plt.subplot2grid((3,3), (1,2), rowspan=2)
plt.subplot2grid((3,3), (2,0))
plt.subplot2grid((3,3), (2,1))
plt.tight_layout() # para que no se superpongan las graficas
plt.show()