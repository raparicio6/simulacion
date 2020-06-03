import numpy as np 
import pylab 
import random 
import matplotlib.pyplot as plt
import matplotlib.animation


xPositions = []
yPositions = []
xPositions.append(0)
yPositions.append(0)

fig, ax = plt.subplots()
sc = ax.scatter(xPositions[0],yPositions[0])
plt.xlim(-10,10)
plt.ylim(-10,10)



def move():
#Random Walk de la particula

    x=xPositions[-1]
    y=yPositions[-1]

    direction = random.choice(['right','left','down','up'])

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
      


def animate(i):
	move()
	sc.set_offsets(np.c_[xPositions[-1],yPositions[-1]])
	pylab.title("Movimiento aleatorio de particula 2D") 
	pylab.plot([xPositions[-2],xPositions[-1]], [yPositions[-2],yPositions[-1]],color='black') 
	plt.xlim(round(min(xPositions)-5,-1),round(max(xPositions)+5,-1))
	plt.ylim(round(min(yPositions)-5,-1),round(max(yPositions)+5,-1))
	if((len(yPositions)%100) == 0):
		print(len(yPositions)) #referencia para saber cuantos instantes van
	if(len(yPositions)>1000):	#al pasar la longitud,completé los 1000 instantes de tiempo y paro el grafico
		pylab.plot(xPositions,yPositions,color='black')
		plt.xlim(min(xPositions)-5,max(xPositions)+5)
		plt.ylim(min(yPositions)-5,max(yPositions)+5)
		plt.savefig('camino_8.png')
		plt.close()

ani = matplotlib.animation.FuncAnimation(fig, animate,
                frames=1, interval=100, repeat=True) 

plt.show()