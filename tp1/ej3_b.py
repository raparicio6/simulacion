import matplotlib.pyplot as plot
import math 
import numpy as np
pi = math.pi
x_prob_acum = np.arange(-pi/2, 0.1+ pi/2, pi/16)

#probabilidad acumulada:
def probabilidad_acumulada(x):
    return ((13*x/(12*pi))-(x*x*x/(3*pi*pi*pi))+(0.5))
# Valores del eje X que toma el gráfico.


#inversa:
def aproximador_de_raices(u,values,acumulative):
    min_dif = 10
    x = 3
    for z in range(len(values)):
        calc = abs(acumulative[z] - u)
        if( calc<min_dif):
            x = values[z]
            min_dif = calc
    return(x)
lenght_steps = pi/256	#debe ser un numero tal que -pi/2 + N*lenght_stepts = pi/2 para que los valores limites sean -pi/2 y pi/2
values = np.arange(-pi/2, (pi/2)+lenght_steps, lenght_steps)
acumulative = []
for z in values:
    acumulative.append((13*z/(12*pi)) - ((z**3)/(3*(pi**3))) + 0.5)
x_inversa = np.arange(0, 1.01, pi/256)


# Graficar.


fig, (ax1,ax2) = plot.subplots(1,2, figsize=(10,4))  # 1 row, 2 columns

ax1.plot(x_prob_acum, [probabilidad_acumulada(i) for i in x_prob_acum])
ax1.axes.set_title('Funcion de probabilidad acumulada')
ax1.axes.set_xlabel('x')
ax1.axes.set_ylabel('y')
ax1.grid(True)
ax1.axes.set_ylim(0, 1)
ax1.axes.set_xlim((-pi/2), (pi/2))

ax2.plot(x_inversa, [aproximador_de_raices(i,values,acumulative) for i in x_inversa])
ax2.axes.set_title('Funcion inversa')
ax2.axes.set_xlabel('x')
ax2.axes.set_ylabel('y')
ax2.grid(True)
ax2.axes.set_ylim((-pi/2), (pi/2))
ax2.axes.set_xlim(0, 1)

plot.show()
plot.clf()