import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import random

samples = 10000 #ya aguanta 10mil pero mejor dejarlo en menos para hacer mas pruebas
upper_limit = 20
lower_limit = 0
left_limit = 0
right_limit = 10
blue=0
yellow=1

fig, ax = plt.subplots()

x = [0 for x in range(samples)]
y = [0 for y in range(samples)]
gas_colour = [blue for gas_colour in range(samples)]  #antes state
frames = []


for i in range(samples):
	x[i]=np.random.rand()*right_limit
	y[i]=np.random.rand()*upper_limit
	if (x[i] <5):
		gas_colour[i]=blue
	else:
		gas_colour[i]=yellow
		


sc = ax.scatter(x,y,c=gas_colour)
plt.xlim(0,right_limit)
plt.ylim(0,upper_limit)



def move_piece(i):
	return(i+random.choice([0.1,-0.1]))


def inside_box_height(i):
	if(i>upper_limit):
		i=upper_limit
	elif(i<lower_limit):
		i=lower_limit
	return(i)

def inside_box_width(i):
	if(i>right_limit):
		i=right_limit
	elif(i<left_limit):
		i=left_limit
	return(i)
			

def move(i):
	movement = random.choice(["up-down","left-right"])
	if(movement=="up-down"):
		x[i]=move_piece(x[i])
	else:
		y[i]=move_piece(y[i])
	x[i]=inside_box_width(x[i])
	y[i]=inside_box_height(y[i])


def save_charts(length):
	plt.savefig('scatter_9_A.png')
	ani.event_source.stop()
	plt.show(block=False)

def animate(i):
	for i in range(int(samples)):
		move(i)
		
	sc.set_offsets(np.c_[x,y])
	sc.set_array(np.array(gas_colour))
	sc.set_sizes([10] * 3)
	frames.append(1)


	if((len(frames)%100) == 0): #referencia para saber cuantos instantes van
		print(len(frames))
	if(len(frames)>4000):	#al pasar la longitud,completé los 4000 instantes de tiempo y paro el grafico
		save_charts(4002)
		print('termino')		

ani = matplotlib.animation.FuncAnimation(fig, animate,
                frames=2, interval=100, repeat=True) 

plt.show()