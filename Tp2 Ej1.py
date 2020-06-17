import numpy as np
import matplotlib.pyplot as plt

#Si la distribucion es exponencial con media u=4hs entonces para una hora es de 0.25

cantidadDeSolicitudes=100

def getTiemposDeEspera(tiemposDeEspera, duracionesDeProcesamientos, tiemposEntreArribos)
    tiemposDeEspera=[0]
    for i in range(1, len(duracionesDeProcesamientos)):
        espera = tiemposDeEspera[i-1] + duracionesDeProcesamientos[i-1] - tiemposEntreArribos[i]
        if(espera < 0):
            tiemposDeEspera.append(0)
        else:
            tiemposDeEspera.append(espera)

#genero llegadas de muestras
tiemposEntreArribos = np.random.exponential(4,cantidadDeSolicitudes)
tiemposDeArriboDeMuestras=np.concatenate(([0],np.cumsum(tiemposEntreArribos)),axis=None) 

#Separo tiempos de arribo de muestras en maquinas A1 y A2
# probabilidades = np.random.rand(cantidadDeSolicitudes)
# tiemposDeArriboDeMuestrasA1 =[0]
# tiemposDeArriboDeMuestrasA2 =[0]
# for i in range (cantidadDeSolicitudes):
#     if(probabilidades[i] < 0.6):
#         tiemposDeArriboDeMuestrasA1.append(tiemposDeArriboDeMuestras[i])
#     else:
#         tiemposDeArriboDeMuestrasA2.append(tiemposDeArriboDeMuestras[i])

# tiemposEntreArribosA1=np.asarray(tiemposDeArriboDeMuestrasA1[1:])-np.asarray(tiemposDeArriboDeMuestrasA1[0:-1])
# tiemposEntreArribosA2=np.asarray(tiemposDeArriboDeMuestrasA2[1:])-np.asarray(tiemposDeArriboDeMuestrasA2[0:-1]

# duracionesDeProcesamientosMaquinaA1 = np.random.exponential(10/7,len(tiemposEntreArribosA1)) 
# duracionesDeProcesamientosMaquinaA2 = np.random.exponential(1,len(tiemposEntreArribosA2))

# tiemposDeEsperaA1=[]
# tiemposDeEsperaA2=[]
                                                                             
# getTiemposDeEspera(tiemposDeEsperaA1, duracionesDeProcesamientosMaquinaA1,tiemposEntreArribosA1)
    
#genero tiempos de procesamientos de maquinaB 1/0.8 = 1.25
duracionesDeProcesamientosMaquinaB = np.random.exponential(1.25,cantidadDeSolicitudes)
    
#La primera muestra no espera
getTiemposDeEspera(tiemposDeEspera, duracionesDeProcesamientosMaquinaB, tiemposEntreArribos);

print('Tiempo de espera promedio en maquinaB: ' + str(np.mean(tiemposDeEspera) * 60) + ' minutos')

# plt.step(muestras,range(len(muestras)),where= 'post' ,label='λ=4')
# plt.legend()
# plt.show()
