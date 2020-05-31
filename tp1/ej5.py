
import numpy as np

#Importacion de ejercicio 1
modulo = 2**32
multiplicador = 1013904223
incremento = 1664525

def GCL(valor):
  return (valor * multiplicador + incremento) % modulo

def testEstadistico(cantidadGapsDeseada):
    gaps = []
    cantidadDeseada = cantidadGapsDeseada
    valorActual = 0.7
    gapActual = 0

    while(len(gaps) < cantidadDeseada):
        valorActual = GCL(valorActual)
        if(valorActual/modulo >= 0.2 and valorActual/modulo <= 0.5):
              gaps.append(gapActual)
              gapActual = 0
        else:
              gapActual = gapActual + 1

    maxGap = np.amax(gaps)
    frecuencias = np.full(maxGap+1, 0)

    for gap in gaps:
        frecuencias[gap] = frecuencias[gap] + 1

    p = 0.3
    probabilidades = []
    for i in range(maxGap+1):
        probabilidades.append(pow(0.7, i) * p)

    #Aplicacion de test estadistico
    from scipy.stats import chi2

    D2 = 0
    for i in range(len(frecuencias)):
        frecuenciaObservada = frecuencias[i]
        frecuenciaEsperada = probabilidades[i]*len(gaps)
        acumulador = (frecuenciaObservada-frecuenciaEsperada)**2
        acumulador = acumulador / frecuenciaEsperada
        D2 = D2 + acumulador    

    limiteSuperior = chi2.ppf(0.99, df=len(gaps)-1)
    print("Cantidad de gaps: " + str(cantidadGapsDeseada))
    print("Limite superior: {:.2f} ".format(limiteSuperior))
    print("Estadistico: {:.2f} ".format(D2))
    if D2 <= limiteSuperior:
     print("El test acepta la hipotesis nula.")
    else:
     print("El test rechaza la hipótesis nula")
    print("-------------")
    
testEstadistico(10)
testEstadistico(100)
testEstadistico(1000)
testEstadistico(10000)
testEstadistico(100000)