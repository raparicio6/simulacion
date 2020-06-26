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


# ITEM C

POBLACION_TOTAL = 1000
INFECTADOS_INICIAL, RECUPERADOS_INICIAL = POBLACION_TOTAL * 0.03, 0
SUSCEPTIBLES_INICIAL = POBLACION_TOTAL - INFECTADOS_INICIAL - RECUPERADOS_INICIAL
CAPACIDAD_SISTEMA_SANITARIO = POBLACION_TOTAL * 0.3
PASO_ALFA = 0.01
TIEMPO_DIAS = np.linspace(0, 250, 250)
ESTADO_INICIAL = SUSCEPTIBLES_INICIAL, INFECTADOS_INICIAL, RECUPERADOS_INICIAL

while True:
    se_saturo = False
    ret = odeint(modelo_sir, ESTADO_INICIAL, TIEMPO_DIAS, args=(POBLACION_TOTAL, ALFA, BETA))
    S, I, R = ret.T

    for i in range(len(I)):
        if (I[i] > CAPACIDAD_SISTEMA_SANITARIO):
            print("Saturado con Alfa: {}".format(ALFA))
            ALFA = ALFA - PASO_ALFA;
            se_saturo=True
            break;

    if not se_saturo:
        print("NO SATURADO CON ALFA: {}".format(ALFA))
        for i in range(len(I)):
            if (I[i] < 1):
                print("Dia con menos de 1 infectado: {}".format(i))
                break
        break

fig = plt.figure()
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(TIEMPO_DIAS, S, 'b')
ax.plot(TIEMPO_DIAS, I, 'r')
ax.plot(TIEMPO_DIAS, R, 'g')
ax.plot([0,250], [CAPACIDAD_SISTEMA_SANITARIO,CAPACIDAD_SISTEMA_SANITARIO],'k')
ax.set_xlabel('Dias')
ax.set_ylabel('Cantidad Personas')
ax.set_title('Evolucion Epidemia sin Saturar')
ax.set_ylim(0,POBLACION_TOTAL * 1.10)
ax.set_xlim(0, 250)
ax.plot()

plt.savefig('evolucion_pandemia_sin_saturar.png')
plt.show()
