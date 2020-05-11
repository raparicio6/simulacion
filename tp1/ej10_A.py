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


for i in range(muestras):
	x[i]=np.random.rand()*100
	y[i]=np.random.rand()*100
	if (np.random.rand() < 0.05):
		state[i]=1
	else:
		state[i]=0


sc = ax.scatter(x,y,c=state)
plt.xlim(0,upper_limit)
plt.ylim(0,upper_limit)


def move(i):
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
			



def animate(i):
	for i in range(100):
		movement = random.choice(["up-down","left-right"])
		if(movement=="up-down"):
			x[i]=move(x[i])
		else:
			y[i]=move(y[i])
		x[i]=inside_box(x[i])
		y[i]=inside_box(y[i])

	for i in range(100):
		state[i] = got_sick(i,state[i])
		
	sc.set_offsets(np.c_[x,y])
	sc.set_array(np.array(state))

ani = matplotlib.animation.FuncAnimation(fig, animate, 
                frames=5, interval=300, repeat=True) 
plt.show()
