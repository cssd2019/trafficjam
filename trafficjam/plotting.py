#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import numpy as np

def plot(data):
    '''Given the position-history array, plot the time evolution of the car positions.
    
    Args:
        distance_array: The value of x positions of the cars, each row
             represents a different car, each column is a time point in the simulation.

    Returns:
        position_plot: A plot of the car positions (y-axis) with time (x-axis)
            with each car on a new line
    '''

    # Number of cars and time points
    nCars, nTime = data.shape

    # Max and min distances in table
    max_x = max(data.max())
    min_x = min(data.min())

    # Convert data to np.array
    data = data.values

    # Colours for cars
    colours = cm.rainbow(np.linspace(0, 1, nCars))
        
    # Set up the figure
    fig = plt.figure()
    
    # Subplot axes1: distance/time lines
    axes1 = fig.add_subplot(311, ylim=(0, nTime), xlim=(min_x, max_x))
    axes1.set_xlabel("Distance")
    axes1.set_ylabel("Time")
    # Lines list
    lines = []
    for index in range(nCars):
        lobj = axes1.plot([], [], lw=2, color=colours[index])[0]
        lines.append(lobj)

    # Subplot axes2: car symbols
    axes2 = fig.add_subplot(313, ylim=(-0.5, 2.5), xlim=(min_x, max_x))
    axes2.set_axis_off()
    # Road lines
    axes2.plot([min_x, max_x], [0, 0], lw=2, color="grey")
    axes2.plot([min_x, max_x], [1, 1], lw=2, color="grey")
    # Cars list
    cars = []
    for index in range(nCars):
        cobj = axes2.add_patch(plt.Rectangle((0, 0), width=0.1, height = 1, color=colours[index]))
        cars.append(cobj)

    # Subplot axes3: velocity/time lines
    axes3 = fig.add_subplot(312, ylim=(0, 100), xlim=(0, nTime))
    axes3.set_xlabel("Time")
    axes3.set_ylabel("Velocity")
    # VLines list
    vlines = []
    for index in range(nCars):
        vobj = axes3.plot([], [], lw=2, color=colours[index])[0]
        vlines.append(vobj)
    

    # Initialization function: plot the background of each frame
    def init():
        for line in lines:
            line.set_data([],[])    

        for car in cars:
            car.set_x(0)

        for vline in vlines:
            vline.set_data([],[])
        
        return lines, cars, vlines,

    # Animation function: This is called sequentially
    def animate(i):
        for lnum,line in enumerate(lines):
            x = data[lnum, :i]
            y = range(i)
            line.set_data(x, y)
            
        for lnum,car in enumerate(cars):
            x = data[lnum, i]
            car.set_x(x)

        for lnum,vline in enumerate(vlines):
            x = range(i)
            y = np.diff(np.append([0], data[lnum, :i]))

            vline.set_data(x, y)
            
        return lines, cars, vlines,

    # Call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=range(nTime), interval=100, blit=False, repeat=True)

    plt.show()


## Main code
if __name__ == "__main__":
    if len(sys.argv) <= 1 :
        exit("No input file given to arguments")

    # Data file name from args
    data_file = sys.argv[1]

    # Read in data from given cvs file
    data = pd.read_csv(data_file, header=0, index_col=0)

    # Run plot code with data table
    plot(data)
    
    
    
    
    