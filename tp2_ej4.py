import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

POBLACION_TOTAL = 1.
INFECTADOS_INICIAL, RECUPERADOS_INICIAL = 0.03, 0
SUSCEPTIBLES_INICIAL = POBLACION_TOTAL - INFECTADOS_INICIAL - RECUPERADOS_INICIAL
ALFA, BETA = 0.27, 0.043
TIEMPO_DIAS = np.linspace(0, 150, 150)

def modelo_sir(y, t, N, alfa, beta):
    S, I, R = y
    dSdt = -alfa * S * I / N
    dIdt =  alfa * S * I / N - beta * I
    dRdt = beta * I    

    return dSdt, dIdt, dRdt


ESTADO_INICIAL = SUSCEPTIBLES_INICIAL, INFECTADOS_INICIAL, RECUPERADOS_INICIAL

ret = odeint(modelo_sir, ESTADO_INICIAL, TIEMPO_DIAS, args=(POBLACION_TOTAL, ALFA, BETA))
S, I, R = ret.T

fig = plt.figure()
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(TIEMPO_DIAS, S, 'b')
ax.plot(TIEMPO_DIAS, I, 'r')
ax.plot(TIEMPO_DIAS, R, 'g')
ax.set_xlabel('Dias')
ax.set_ylabel('% Poblacion')
ax.set_title('Evolucion Epidemia')
ax.set_ylim(0, 1.25)
ax.set_xlim(0, 180)

plt.savefig('evolucion_pandemia.png')
plt.show()