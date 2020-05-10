import matplotlib.pyplot as plot
import math 
import numpy as np
pi = math.pi
x = np.arange(-1.6, 1.7, 0.1)

#a) funcion de densidad
def density_function(x):
    return ((13/(12*pi))-(x*x/(pi*pi*pi)))
# Valores del eje x

# Funcion de densidad:
plot.plot(x, [density_function(i) for i in x])
plot.title('Funcion de densidad')
plot.xlabel('x')
plot.ylabel('y')
plot.grid(True)
plot.show()
plot.clf()
