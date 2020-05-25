import numpy 
import pylab 
import random 
  
x = 0
y = 0
xPositions = []
yPositions = []

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
      
  
# plotting stuff: 
pylab.title("Movimiento aleatorio de particula 2D") 
pylab.plot(xPositions, yPositions) 
pylab.show() 
