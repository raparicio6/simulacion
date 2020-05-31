import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random


def generate_by_acceptance_rejection(n, mu, sigma):
  numbers = np.array([])
  rejected = 0

  while len(numbers) < n:
    x = np.random.exponential()
    probability = stats.norm.pdf(x) / (((2 * stats.norm.pdf(1)) / stats.expon.pdf(1))
                                       * stats.expon.pdf(x))
    y = random.random()
  
    if y <= probability:
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
          1.0 / numbers.size, color='green', ec='black', alpha=0.5, bins=20)
  ax.set_xlabel("Rango numérico")
  ax.set_ylabel("Frecuencia relativa")


def draw_normal_pdf(mu, sigma):
  x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
  plt.plot(x, stats.norm.pdf(x, mu, sigma), "-r")


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
  draw_normal_pdf(mu, sigma)
  plt.show()

  # Calculo y comparo la media y la varianza de la distribución obtenida con los valores teóricos
  average = np.average(numbers)
  variance = np.var(numbers)
  print("Valores teóricos: media = {}, varianza = {}".format(mu, sigma ** 2))
  print("Valores prácticos: media = {}, varianza = {}".format(average, variance))
  print("Diferencia entre ambas: media = {}, varianza = {}".format(
    mu - average if mu >= average else average - mu, 
    sigma ** 2 - variance if sigma ** 2 >= variance else variance - sigma ** 2))
