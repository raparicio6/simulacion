import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import random

samples = 10000 #ya aguanta 10mil
upper_limit = 20
lower_limit = 0
left_limit = 0
right_limit = 10
blue=0
yellow=1

fig, ax = plt.subplots()

x = [0 for x in range(samples)]
y = [0 for y in range(samples)]
gas_colour = [blue for gas_colour in range(samples)]
left_side_graph = []
right_side_graph = []


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
	plt.cla()
	plt.clf()
	plt.plot(np.arange(0, len(left_side_graph), 1), left_side_graph)
	plt.xlim(0,len(left_side_graph))
	plt.ylim(0.65,1)
	plt.ylabel('proporcion')
	plt.xlabel('tiempo')
	plt.title('Proporcion azules lado izquierdo')
	plt.savefig('Proporcion_azules_lado_izquierdo_9_A.png')
	plt.cla()
	plt.clf()
	plt.plot(np.arange(0, len(right_side_graph), 1), right_side_graph)
	plt.xlim(0,len(left_side_graph))
	plt.ylim(0.65,1)
	plt.ylabel('proporcion')
	plt.xlabel('tiempo')
	plt.title('Proporcion amarillos lado derecho')
	plt.savefig('Proporcion_amarillos_lado_derecho_9_A.png')


def count_proportions_side():

	samples_on_left_side = 0
	blue_samples_on_left_side = 0
	samples_on_right_side = 0
	yellow_samples_on_right_side = 0
	for i in range(int(samples)):
		if(x[i]<right_limit/2):
			samples_on_left_side=samples_on_left_side+1
			if(gas_colour[i]==blue):
				blue_samples_on_left_side=blue_samples_on_left_side+1
		else:
			samples_on_right_side=samples_on_right_side+1
			if(gas_colour[i]==yellow):
				yellow_samples_on_right_side=yellow_samples_on_right_side+1

	proportions_left_side = blue_samples_on_left_side/samples_on_left_side
	proportions_right_side = yellow_samples_on_right_side/samples_on_right_side
	left_side_graph.append(proportions_left_side)
	right_side_graph.append(proportions_right_side)
	return([proportions_left_side,proportions_right_side])



def animate(i):
	for i in range(int(samples)):
		move(i)
		
	sc.set_offsets(np.c_[x,y])
	sc.set_array(np.array(gas_colour))
	sc.set_sizes([10] * 3)

	proportions = count_proportions_side()

	if((len(left_side_graph)%100) == 0):
		print(len(left_side_graph)) #referencia para saber cuantos instantes van
		print(proportions)
	if(len(left_side_graph)>3000):	#al pasar la longitud,completé los 2000 instantes de tiempo y paro el grafico
		save_charts(3002)
		print('termino')

ani = matplotlib.animation.FuncAnimation(fig, animate,
                frames=2, interval=100, repeat=True) 

plt.show()