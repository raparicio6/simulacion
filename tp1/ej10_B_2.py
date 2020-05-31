import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import random

samples = 100
upper_limit = 100
lower_limit = 0
left_limit = 0
right_limit = 100
healthy=0
sick=1

fig, ax = plt.subplots()

x = [0 for x in range(samples)]
y = [0 for y in range(samples)]
state = [healthy for state in range(samples)]
movements_left = [0 for movements_left in range(samples)]
sick_people = []
movements_till_cured = [0 for movements_till_cured in range(samples)]


for i in range(samples):
	x[i]=np.random.rand()*100
	y[i]=np.random.rand()*100
	if (np.random.rand() < 0.05):
		state[i]=sick
		movements_left[i] = int((np.random.rand()*10))+10
		movements_till_cured[i] = 20
	else:
		state[i]=healthy
		
		


sc = ax.scatter(x,y,c=state)
plt.xlim(0,upper_limit)
plt.ylim(0,upper_limit)


def move_piece(i,direction):
	return(i+direction)


def got_sick(i,current_state):
	for z in range(samples):
		if((state[z]==sick) and abs(x[z]-x[i])<2 and abs(y[z]-y[i])<2 and current_state==healthy):
			if(np.random.rand() < 0.6):
				current_state = sick
				movements_left[i] = int((np.random.rand()*10))+10
	return(current_state)
			


def reduce_movements_left(i):
	if(state[i]==sick and movements_left[i]>0):
		movements_left[i] = movements_left[i]-1
	if(state[i]==sick and movements_till_cured[i]>0):
		movements_till_cured[i] = movements_till_cured[i]-1

def cure(i):
	if(state[i]==sick and movements_till_cured[i]==0 and np.random.rand() < 0.8):
		state[i]=healthy

def update_sick_ones():
	for i in range(samples):
		state[i] = got_sick(i,state[i])


def posible_movements(i):
	choises = []
	if(x[i]<upper_limit):
		choises.append("up")
	if(x[i]>lower_limit):
		choises.append("down")
	if(y[i]<right_limit):
		choises.append("right")
	if(y[i]>left_limit):
		choises.append("left")
	return(choises)


def move(i):
	if(state[i]==healthy or movements_left[i]>0): #se mueven los sanos o infectados que les queden movimientos
		choises = posible_movements(i)
		movement = random.choice(choises)
		if(movement=="up"):
			x[i]=move_piece(x[i],1)
		if(movement=="down"):
			x[i]=move_piece(x[i],-1)
		if(movement=="right"):
			y[i]=move_piece(y[i],1)
		if(movement=="left"):
			y[i]=move_piece(y[i],-1)


def count_sick():
	sick_counter = 0
	for i in range(samples):
		if(state[i]==sick):
			sick_counter = sick_counter + 1
	return(sick_counter)

def save_charts(length):
	ani.event_source.stop()
	plt.show(block=False)
	plt.savefig('scatter_10_B_2.png')
	plt.cla()
	plt.clf()
	plt.plot(np.arange(1, length, 1), sick_people)
	plt.xlim(0,length)
	plt.ylim(0,100)
	plt.ylabel('cantidad infectados')
	plt.xlabel('tiempo')
	plt.title('avance infectados')
	plt.savefig('avance_infectados_10_B_2.png')
	plt.cla()
	plt.clf()
	plt.plot(np.arange(1, length, 1), samples-np.array(sick_people))
	plt.xlim(0,length)
	plt.ylim(0,100)
	plt.ylabel('cantidad sanos')
	plt.xlabel('tiempo')
	plt.title('avance sanos')
	plt.savefig('avance_sanos_10_B_2.png')


def animate(i):
	for i in range(int(samples)):
		move(i)
		reduce_movements_left(i)
		cure(i)

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
                frames=2, interval=10, repeat=True) 

plt.show()
