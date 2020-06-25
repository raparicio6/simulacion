import numpy as np
import matplotlib.pyplot as plt

cantidadDeSolicitudes=100000

def getTiemposDeEspera(duracionesDeProcesamientos, tiemposEntreArribos):
    #La primera muestra no espera
    tiemposDeEspera=[0]
    for i in range(1, len(duracionesDeProcesamientos)):
        espera = tiemposDeEspera[i-1] + duracionesDeProcesamientos[i-1] - tiemposEntreArribos[i]
        if(espera < 0):
            tiemposDeEspera.append(0)
        else:
            tiemposDeEspera.append(espera)
    return tiemposDeEspera

def getZeros(collection):
    count = 0
    for i in range(0, len(collection)):
        if(collection[i]==0):
            count = count +1
    return count

def getTiemposTotales(duracionesProcesamiento, tiemposDeEspera):
    tiemposTotales = []
    for i in range(len(duracionesProcesamiento)):
        duracionTotal = duracionesProcesamiento[i] + tiemposDeEspera[i]
        tiemposTotales.append(duracionTotal)
    return tiemposTotales

#genero llegadas de muestras
#Si la distribucion es exponencial con media u=4hs entonces para una hora es de 1/4
#exponencial es 1/lambda entonces 1/1/4 --> 4
tiemposEntreArribos = np.random.exponential(4,cantidadDeSolicitudes)
tiemposDeArriboDeMuestras=np.concatenate(([0],np.cumsum(tiemposEntreArribos)),axis=None) 

#Separo tiempos de arribo de muestras en maquinas A1 y A2
probabilidades = np.random.rand(cantidadDeSolicitudes)
tiemposDeArriboDeMuestrasA1 =[0]
tiemposDeArriboDeMuestrasA2 =[0]
for i in range (cantidadDeSolicitudes):
    if(probabilidades[i] < 0.6):
        tiemposDeArriboDeMuestrasA1.append(tiemposDeArriboDeMuestras[i])
    else:
        tiemposDeArriboDeMuestrasA2.append(tiemposDeArriboDeMuestras[i])

tiemposEntreArribosA1=np.asarray(tiemposDeArriboDeMuestrasA1[1:])-np.asarray(tiemposDeArriboDeMuestrasA1[0:-1])
tiemposEntreArribosA2=np.asarray(tiemposDeArriboDeMuestrasA2[1:])-np.asarray(tiemposDeArriboDeMuestrasA2[0:-1])

duracionesDeProcesamientosMaquinaA1 = np.random.exponential(10/7,len(tiemposEntreArribosA1)) 
duracionesDeProcesamientosMaquinaA2 = np.random.exponential(1,len(tiemposEntreArribosA2))

tiemposDeEsperaA1=[]
tiemposDeEsperaA2=[]
                                                                             
tiemposDeEsperaA1 = getTiemposDeEspera(duracionesDeProcesamientosMaquinaA1,tiemposEntreArribosA1)
tiemposDeEsperaA2 = getTiemposDeEspera(duracionesDeProcesamientosMaquinaA2,tiemposEntreArribosA2)                                                                             

tiemposDeEsperaA =  tiemposDeEsperaA1 + tiemposDeEsperaA2

print('Tiempo de espera promedio en maquinas A: ' + str(np.mean(tiemposDeEsperaA) * 60) + ' minutos')
print("Fraccion de solicitudes que no esperaron:" + str(getZeros(tiemposDeEsperaA)/cantidadDeSolicitudes))

duracionesTotalesA1 = getTiemposTotales(duracionesDeProcesamientosMaquinaA1, tiemposDeEsperaA1)
duracionesTotalesA2 = getTiemposTotales(duracionesDeProcesamientosMaquinaA2, tiemposDeEsperaA2)
duracionesTotalesA = duracionesTotalesA1 + duracionesTotalesA2

promedioTiempoResolucionA = np.mean(duracionesTotalesA)
                                                                             
#genero tiempos de procesamientos de maquinaB 1/0.8 = 1.25
duracionesDeProcesamientosMaquinaB = np.random.exponential(1.25,cantidadDeSolicitudes)

tiemposDeEsperaB = getTiemposDeEspera(duracionesDeProcesamientosMaquinaB, tiemposEntreArribos)

print('Tiempo de espera promedio en maquina B: ' + str(np.mean(tiemposDeEsperaB) * 60) + ' minutos')
print("Fraccion de solicitudes que no esperaron:" + str(getZeros(tiemposDeEsperaB)/cantidadDeSolicitudes))

duracionesTotalesB = getTiemposTotales(duracionesDeProcesamientosMaquinaB, tiemposDeEsperaB)
promedioTiempoResolucionB = np.mean(duracionesTotalesB)

print("Promedio tiempo A: " + str(promedioTiempoResolucionA))
print("Promedio tiempo B: " + str(promedioTiempoResolucionB))
if(promedioTiempoResolucionA  < promedioTiempoResolucionB * 0.5):
    print("Conviene comprar Opcion A")
else:
    print("Conviene comprar Opcion B")   
