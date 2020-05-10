import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(-10, 20)
    ax.set_ylim(-10, 20)
    return ln,

def update(frame):
    ln.set_data(posiciones[frame][0], posiciones[frame][1])
    return ln,

x = 0
y = 0
positions = []
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
    positions.append([x, y])


ani = FuncAnimation(fig, update, frames=len(positions),init_func=init, interval=500, blit=True)
plt.show()
