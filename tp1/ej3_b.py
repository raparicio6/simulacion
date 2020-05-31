import matplotlib.pyplot as plot
import math 
import numpy as np
pi = math.pi
x = np.arange(-pi/2, 0.1+ pi/2, pi/16)

#b) probabilidad acumulada:
def probabilidad_acumulada(x):
    return ((13*x/(12*pi))-(x*x*x/(3*pi*pi*pi))+(0.5))
# Valores del eje X que toma el gráfico.
# Graficar.
plot.plot(x, [probabilidad_acumulada(i) for i in x])
plot.title('Funcion de probabilidad acumulada')
plot.xlabel('x')
plot.ylabel('y')
plot.grid(True)
plot.ylim(0, 1)
plot.xlim((-pi/2), (pi/2))
plot.show()
plot.clf()