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


generarSecuencia(secuencia, 1, 10)
print("Primeros 10 numeros generados: {}".format(secuencia))

# ---------

# Creo una nueva secuencia con una semilla de 0.7
secuencia2 = [0.7]
generarSecuencia(secuencia2, 1, 100000)

# Para que de numeros entre 0 y 1, divido por su modulo
secuencia2 = list(map(lambda n: n / modulo, secuencia2))

# Histograma
plot.title('Histograma')
plot.xlabel('Valor')
plot.ylabel('Frecuencia')
plot.hist(secuencia2, color='green', bins=60, alpha=0.5, ec='black')
plot.grid(True)
plot.show()
plot.clf()
