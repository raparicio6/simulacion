import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random


c = (2 * stats.norm.pdf(1)) / stats.expon.pdf(1)


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


def draw_histogram(numbers):
  ax = plt.figure().add_subplot(1, 1, 1)
  ax.hist(numbers, weights=np.zeros_like(numbers) +
          1.0 / numbers.size, color="green", ec="black", alpha=0.5, bins=20)
  ax.set_xlabel("Rango numérico")
  ax.set_ylabel("Frecuencia relativa")


def draw_pdf(mu, sigma):
  x = np.linspace(mu - 4 * sigma, mu + 4 * sigma)
  plt.plot(x, stats.norm.pdf(x, mu, sigma), "b-")


n = 100000
mu = 25
sigma = 2

if __name__ == "__main__":
  # Genero números aleatorios
  numbers = generate_by_acceptance_rejection(n, mu, sigma)

  # Realizo histograma de frecuencias relativas con dichos números
  draw_histogram(numbers)
  plt.show()

  # Comparo el histograma realizado en el punto anterior con la función de densidad de probabilidad
  draw_histogram(numbers)
  draw_pdf(mu, sigma)
  plt.show()

  # Calculo y comparo la media y la varianza de la distribución obtenida con los valores teóricos
  mean = np.mean(numbers)
  variance = np.var(numbers)
  print("Valores teóricos: media = {}, varianza = {}".format(mu, sigma ** 2))
  print("Valores prácticos: media = {}, varianza = {}".format(mean, variance))
  print("Diferencia entre ambas: media = {}, varianza = {}".format(
    mu - mean if mu >= mean else mean - mu, 
    sigma ** 2 - variance if sigma ** 2 >= variance else variance - sigma ** 2))
