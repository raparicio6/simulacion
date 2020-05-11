import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import random

muestras = 100
upper_limit = 100
lower_limit = 0

fig, ax = plt.subplots()

x = [0 for x in range(muestras)]
y = [0 for y in range(muestras)]
state = [0 for state in range(muestras)]
sick_people = []


for i in range(muestras):
	x[i]=np.random.rand()*100
	y[i]=np.random.rand()*100
	if (np.random.rand() < 0.05):
		state[i]=1
		


sc = ax.scatter(x,y,c=state)
plt.xlim(0,upper_limit)
plt.ylim(0,upper_limit)


def move_piece(i):
	movement = random.choice([1,-1])
	i=i+movement
	return(i)


def inside_box(i):
	if(i>upper_limit):
		i=upper_limit
	elif(i<lower_limit):
		i=lower_limit
	return(i)

def got_sick(i,current_state):
	for z in range(muestras):
		if((state[z]==1) and abs(x[z]-x[i])<2 and abs(y[z]-y[i])<2 and current_state==0):
			if(np.random.rand() < 0.6):
				current_state = 1
	return(current_state)
			


def update_sick_ones():
	for i in range(muestras):
		state[i] = got_sick(i,state[i])

def move(i):
	movement = random.choice(["up-down","left-right"])
	if(movement=="up-down"):
		x[i]=move_piece(x[i])
	else:
		y[i]=move_piece(y[i])
	x[i]=inside_box(x[i])
	y[i]=inside_box(y[i])

def count_sick():
	sick_counter = 0
	for i in range(muestras):
		if(state[i]==1):
			sick_counter = sick_counter + 1
	return(sick_counter)


def save_charts(length):
	ani.event_source.stop()
	plt.show(block=False)
	plt.savefig('scatter_A_1.png')
	plt.cla()
	plt.clf()
	plt.plot(np.arange(1, length, 1), sick_people)
	plt.title('avance infectados')
	plt.savefig('avance_infectados_A_1.png')
	plt.cla()
	plt.clf()
	plt.plot(np.arange(1, length, 1), muestras-np.array(sick_people))
	plt.title('avance sanos')
	plt.savefig('avance_sanos_A_1.png')

def animate(i):
	for i in range(int(muestras)):
		move(i)

	update_sick_ones()
		
	sc.set_offsets(np.c_[x,y])
	sc.set_array(np.array(state))

	sick_ones = count_sick()
	sick_people.append(sick_ones)


	if((len(sick_people)%100) == 0): #referencia para saber cuantos instantes van
		print(len(sick_people))
	if(len(sick_people)>4000):	#al pasar la longitud,completé los 4000 instantes de tiempo y paro el grafico
		save_charts(4002)
		print('termino')
	elif(sick_ones==100):
		save_charts(len(sick_people)+1) #si ya están todos contagiados, paro el grafico
		print('termino')		

ani = matplotlib.animation.FuncAnimation(fig, animate,
                frames=2, interval=50, repeat=True) 

plt.show()
