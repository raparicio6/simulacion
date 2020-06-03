import matplotlib.pyplot as plot

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


# Creo una nueva secuencia con una semilla de 0.7
secuencia2 = [0.7]
generarSecuencia(secuencia2, 1, 20000)

# Para que de numeros entre 0 y 1, divido por su modulo
secuencia2 = list(map(lambda n: n / modulo, secuencia2))


# Asigna un resultado del evento según el valor de la variable "uniforme"
def generar_valor_dado(x):
    valor = 0
    for i in range(1,7):
        if(x<(i/6) and valor==0):
            valor=i
    return (valor)

f = []

for i in range(1,len(secuencia2),2):
    dado_1 = generar_valor_dado(secuencia2[i])
    dado_2 = generar_valor_dado(secuencia2[i-1])
    f.append(dado_1+dado_2)

# Histograma
plot.hist(f, color='green', bins=11, alpha=0.5, ec='black')
plot.title('Histograma')
plot.xlabel('Valor')
plot.ylabel('Frecuencia')
plot.grid(True)
plot.show()
plot.clf()
