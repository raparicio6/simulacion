import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random

c = np.sqrt(2 * np.e / np.pi)

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
            

def draw_histogram(numbers):
  ax = plt.figure().add_subplot(1, 1, 1)
  ax.hist(numbers, weights=np.zeros_like(numbers) +
          1.0 / numbers.size, color="green", ec="black", alpha=0.5, bins=20)
  ax.set_xlabel("Rango numérico")
  ax.set_ylabel("Frecuencia relativa")


def draw_acumulada_empirica(numbers):
  x = np.linspace(mu - 4 * sigma, mu + 4 * sigma)
  plt.plot(x, [prob_acumulada_empirica(numbers, i) for i in x],'k')  

def draw_norm_cdf(mu, sigma):
  x = np.linspace(mu - 4 * sigma, mu + 4 * sigma)
  plt.plot(x, stats.norm.cdf(x, mu, sigma), "b-")


alpha=0.01
n = 100
mu = 25
sigma = 2
plus_deviations = []
minus_deviations = []


# Genero números aleatorios siguiendo una distribucion normal
numbers = generate_by_acceptance_rejection(n, mu, sigma)

#Ordeno las muestras de forma ascendente y busco los estadisticos
sorted_numbers = np.sort(numbers)

###############
#TODO: REVISAR POR QUE ESTA RECHAZANDO, QUEDAN MUY GRANDES LOS DESVIOS 
##############
for i in range(1,n):
  plus_deviations.append(i/n - stats.norm.cdf(sorted_numbers[i]))

for i in range(1,n):
  minus_deviations.append(stats.norm.cdf(sorted_numbers[i]) - (i - 1)/n)

kn_plus = np.sqrt(n) * np.max(plus_deviations)
kn_minus = np.sqrt(n) * np.max(minus_deviations)

estadistico = np.maximum(kn_plus, kn_minus)

#busco el limite en la tabla de kolmogorov-smirnof
valor_limite = stats.ksone.ppf(1-alpha, n)

print("Limite superior: {:.2f} ".format(valor_limite))
print("Estadistico: {:.2f} ".format(estadistico))
if estadistico <= valor_limite:
  print("El test acepta la hipotesis nula.")
else:
  print("El test rechaza la hipótesis nula")


# Dibujo superpuestas la acumulada empirica y la acumulada esperada (normal)
draw_acumulada_empirica(numbers)
draw_norm_cdf(mu, sigma)
plt.show()