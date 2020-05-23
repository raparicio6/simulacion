import matplotlib.pyplot as plot
import math 
import numpy as np
pi = math.pi


#Generador del 1)
modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
semilla = int((98967 + 94241 + 101004 + 78189) / 4)
secuencia = [semilla]


def GCL(valor):
  return (valor * multiplicador + incremento) % modulo


def generarSecuencia(secuencia, inicio, fin):
  for i in range(inicio, fin):
    secuencia.append(GCL(secuencia[i-1]))
secuencia2 = [0.7]
generarSecuencia(secuencia2, 1, 100000)

# Para que de numeros entre 0 y 1, divido por su modulo
secuencia2 = list(map(lambda n: n / modulo, secuencia2))



#ejercicio 3)
# Problema: no puedo despejar completamente x para obtener la funcion inversa, solucion: la aproximo
def aproximador_de_raices(u,values,acumulative):
    min_dif = 10
    x = 3
    for z in range(len(values)):
        calc = abs(acumulative[z] - u)
        if( calc<min_dif):
            x = values[z]
            min_dif = calc
    return(x)

u = np.random.rand()
f = []
lenght_steps = pi/32	#debe ser un numero tal que -pi/2 + N*lenght_stepts = pi/2 para que los valores limites sean -pi/2 y pi/2
values = np.arange(-pi/2, (pi/2)+lenght_steps, lenght_steps)
cant_bins = int(len(values))
acumulative = []
for z in values:
    acumulative.append((13*z/(12*pi)) - ((z**3)/(3*(pi**3))) + 0.5)

for i in secuencia2:
    f.append(aproximador_de_raices(i,values,acumulative))

print(values)


plot.hist(f, color='green', bins=cant_bins, alpha=0.5, ec='black')
plot.grid(True)
plot.title('Funcion de probabilidad acumulada')
plot.xlim((-pi/2), (pi/2))
plot.title('Histograma')
plot.xlabel('Frecuencia')
plot.ylabel('Valor')
plot.show()
plot.clf()