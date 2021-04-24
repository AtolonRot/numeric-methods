import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5)  # aqui se escribe el intervalo
y = np.cos(x) - x  # aqui se pone la funcion
yy = x * 0

plt.title("gráfica de la función f(x)=cos(x)-x")
plt.plot(x, y, x, yy)  # aqui se grafica
plt.show()