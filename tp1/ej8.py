import numpy 
import pylab 
import random 

#Declara posicion inicial y arrays con futuras posiciones
x = 0
y = 0
xPositions = []
yPositions = []

#Random Walk de la particula
for i in range(1000):
    direction = random.choice(["up", "down", "left", "right"])
    
    if(direction == "up"):
        y = y+1

    if(direction == "down"):
        y = y-1

    if(direction == "right"):
        x = x+1

    if(direction == "left"):
        x = x-1
    xPositions.append(x)
    yPositions.append(y)
      
  
# Visualizacion 
pylab.title("Movimiento aleatorio de particula 2D") 
pylab.plot(xPositions, yPositions) 
pylab.show() 
