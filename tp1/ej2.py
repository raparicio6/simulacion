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
generarSecuencia(secuencia2, 1, 10000)

# Para que de numeros entre 0 y 1, divido por su modulo
secuencia2 = list(map(lambda n: n / modulo, secuencia2))


# Ejercicio 2)
# 2-a)Llamando al experimento A, el espacio muestral es S={2,3,4,5,6,7,8,9,10,11,12}
# P(A=2)=1/12       P(A=3)=2/12       P(A=4)=3/12       P(A=5)=4/12       P(A=6)=5/12       P(A=7)=6/12
# P(A=8)=5/12       P(A=9)=4/12       P(A=10)=3/12       P(A=11)=2/12       P(A=12)=1/12

# 2-b)
# Probabilidades de cada resultado respectivamente
probabilidades = [1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]

# Cotas superiores de cada resultado posible,resultado de la suma de todas las probabilidades anteriores
cota_superior = [0 for x in range(11)]
for z in range(11):
    for i in range(z+1):
        cota_superior[z]+= probabilidades[i]

# Asigna un resultado del evento según el valor de la variable "uniforme"
def asignar_resultados(x):
    resultado = 0
    resultado_obtenido = False
    i=0
    while(resultado_obtenido==False):
        if(x<=cota_superior[i]):
            resultado_obtenido = True
            resultado = i+2
        i = i+1
    return (resultado)

f = []

for i in secuencia2:
    f.append(asignar_resultados((i)))


# Histograma
plot.hist(f, color='green', bins=11, alpha=0.5, ec='black')
plot.title('Histograma')
plot.xlabel('Valor')
plot.ylabel('Frecuencia')
plot.grid(True)
plot.show()
plot.clf()
