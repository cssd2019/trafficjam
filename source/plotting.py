#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import numpy as np

def plot(distance_array):
    '''Given the position-history array, plot the time evolution of the car positions.
    
    Args:
        distance_array: The value of x positions of the cars, each row
             represents a different car, each column is a time point in the simulation.

    Returns:
        position_plot: A plot of the car positions (y-axis) with time (x-axis)
            with each car on a new line
    '''
    pass

def animated_plot(updated_positions):
    ''' Given the positions of the cars at the current time point, produce a
    live plot.

    Args:
       updated_positions: The positions of the cars at the current time steps.
        
    Returns:
        time_evolution_plot: An animated plot of the positions, a 1-D plot of
            the car positions that changes with time.
    '''
    pass

data_file = "../data/simpleDistanceHistory.csv"
data = pd.read_csv(data_file, header=0, index_col=0)

max_x = max(data.max())
min_x = min(data.min())

nCars, nTime = data.shape
    
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
#axes = plt.axes(ylim=(0, nTime), xlim=(min_x, max_x))

# Subplot 1
axes1 = fig.add_subplot(211, ylim=(0, nTime), xlim=(min_x, max_x))
axes1.set_xlabel("Distance")
axes1.set_ylabel("Time")

# Subplot 2
axes2 = fig.add_subplot(212, ylim=(0, 10), xlim=(min_x, max_x))
axes2.set_xlabel("Distance")
axes2.set_ylabel("Lane")

# line colours
colours = cm.rainbow(np.linspace(0, 1, nCars))

# Lines list
lines = []
for index in range(nCars):
    lobj = axes1.plot([], [], lw=2, color=colours[index])[0]
    lines.append(lobj)

# Balls list
balls = []
for index in range(nCars):
    bobj = axes2.add_patch(plt.Circle((0,0), radius=1, color=colours[index]))
    balls.append(bobj)

# Initialization function: plot the background of each frame
def init():
    for line in lines:
        line.set_data([],[])    

    for ball in balls:
        ball.center = (0,0)
    
    return lines, balls,

# Animation function: This is called sequentially
def animate(i):
    for lnum,line in enumerate(lines):
        x = data.iloc[lnum, :i]
        y = range(i)
        line.set_data(x, y)
        
    for lnum,ball in enumerate(balls):
        x = data.iloc[lnum, i]
        y = 5
        ball.center = (x, y)
    #ball.center = (5,i)
        
    return lines, ball,

# Call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=range(nTime), interval=100, blit=False, repeat=True)

plt.show()

    
    
    
    
    
    