import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random
from math import e, pi, sqrt

c = sqrt(2 * e / pi)

def generate_by_acceptance_rejection(n, mu, sigma):
  numbers = np.array([])
  rejected = 0

  while len(numbers) < n:
    x = np.random.exponential()
    probability = stats.norm.pdf(x) / (c * stats.expon.pdf(x))

    if random.random() <= probability:
      if random.random() < 0.5:
        numbers = np.append(numbers, x)
      else:
        numbers = np.append(numbers, -x)
    else:
      rejected += 1
  
  print("Cantidad rechazos: {}".format(rejected))
  return numbers * sigma + mu

def prob_acumulada_empirica(numbers, x):
  elementos = list(filter(lambda element: element <= x, numbers))
  return len(elementos) / len(numbers)

def draw_acumulada_empirica(numbers):
  x = np.linspace(mu - 4 * sigma, mu + 4 * sigma)
  plt.plot(x, [prob_acumulada_empirica(numbers, i) for i in x],'k')  

def draw_norm_cdf(mu, sigma):
  x = np.linspace(mu - 4 * sigma, mu + 4 * sigma)
  plt.plot(x, stats.norm.cdf(x, mu, sigma), "b-")


alpha=0.01
n = 10000
mu = 25
sigma = 2
plus_deviations = []
minus_deviations = []


# Genero n números aleatorios siguiendo una distribucion N(mu, sigma)
numbers = generate_by_acceptance_rejection(n, mu, sigma)

# Efectua el test Komogorov-Smirnov y obtiene el p-value
statistic, pvalue = stats.kstest(numbers, stats.norm(loc=mu, scale=sigma).cdf)

print("Nivel de Significacion: {:.2f} ".format(alpha))
print("p-valor: {:.2f} ".format(pvalue))

# Comparo el p-value con el nivel de significancia deseado, y si es mayor, entonces
# no hay evidencia para rechazar la hipotesis nula, y se acepta
if alpha <= pvalue:
  print("El test acepta la hipotesis nula.")
else:
  print("El test rechaza la hipótesis nula")


# Alternativa: Ordena las muestras de manera ascendente y obtiene el estadistico
# y lo compara con el valor limite obtenido de la tabla de Kolgomorov-Smirnov, 
# Si el estadistico es <= valor limite, aceptamos la hipotesis
'''
#Ordeno las muestras de forma ascendente
sorted_numbers = np.sort(numbers)

#Obtengo las distancias entre la acumulada que evaluamos en la H0 y la empirica
#de la muestra para asi hallar el estadistico
for i in range(1,n):
  plus_deviations.append(i/n - stats.norm.cdf(sorted_numbers[i], mu, sigma))

for i in range(1,n):
  minus_deviations.append(stats.norm.cdf(sorted_numbers[i], mu, sigma) - (i - 1)/n)

kn_plus = sqrt(n) * max(plus_deviations)
kn_minus = sqrt(n) * max(minus_deviations)

estadistico = max(kn_plus, kn_minus)

#busco el limite en la tabla de kolmogorov-smirnof
valor_limite = sqrt(n) * stats.ksone.ppf(1-alpha, n)

print("Limite superior: {:.2f} ".format(valor_limite))
print("Estadistico: {:.2f} ".format(estadistico))
if estadistico <= valor_limite:
  print("El test acepta la hipotesis nula.")
else:
  print("El test rechaza la hipótesis nula")
'''  


# Dibujo superpuestas la acumulada empirica y la acumulada esperada (N(25,2)),
# donde no se aprecian distancias visibles en esta escala
draw_acumulada_empirica(numbers)
draw_norm_cdf(mu, sigma)
plt.show()