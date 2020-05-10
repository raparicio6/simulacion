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
generarSecuencia(secuencia2, 1, 500000)

# Para que de numeros entre 0 y 1, divido por su modulo
secuencia2 = list(map(lambda n: n / modulo, secuencia2))



#ejercicio 3)
# Problema: no puedo despejar completamente x para obtener la funcion inversa, solucion: la aproximo
def aproximador_de_raices(u):
    values = np.arange(-pi/2, pi/2, 0.01)
    min_dif = 10
    x = 3
    for z in values:
	#La distribucion inversa resulta 13*x/(12*pi) -x³/(3*pi³) + 0.5 = u
	#Igualo a 0 y obtengo x por método de aproximacion de raices(que termina siendo mucho mas ineficiente)
        calc = abs((13*z/(12*pi)) - ((z**3)/(3*(pi**3))) + 0.5- u)
        if( calc<min_dif):
            x = z
            min_dif = calc
    return(x)

# otro intento, esta vez reduciendo en 0.1 el rando de los costados
u = np.random.rand()
f = []
for i in secuencia2:
    f.append(aproximador_de_raices((i)))
    #f.append(aproximador_de_raices((0.8*i+0.1)))


plot.hist(f, color='green', bins=75, alpha=0.5, ec='black')
plot.grid(True)
plot.title('Funcion de probabilidad acumulada')
plot.xlim((-pi/2), (pi/2))
plot.title('Histograma')
plot.xlabel('Frecuencia')
plot.ylabel('Valor')
plot.show()
plot.clf()