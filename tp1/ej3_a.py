import matplotlib.pyplot as plot
import math 
import numpy as np
pi = math.pi
x = np.arange(-pi/2, 0.1+ pi/2, pi/16)

#a) funcion de densidad
def density_function(x):
    return ((13/(12*pi))-(x*x/(pi*pi*pi)))
# Valores del eje y

# Funcion de densidad:
plot.plot(x, [density_function(i) for i in x],'k')
plot.plot([-pi/2,-pi/2],[density_function(-pi/2),0],'k')
plot.plot([pi/2,pi/2],[density_function(pi/2),0],'k')
plot.title('Funcion de densidad')
plot.xlabel('x')
plot.ylabel('y')
plot.grid(True)
plot.xlim(-0.1-pi/2,0.1+pi/2)
plot.ylim(0,0.4)
plot.show()
plot.clf()
