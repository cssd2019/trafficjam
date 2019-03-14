#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

def plot(data):
    '''Given the position-history table, plot the time evolution of the car positions.
    
    Args:
        data: A pandas data table of the distance (x) positions of the cars. Each row
             represents a different car, and each column is a time point in the simulation.

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
    axes2 = fig.add_subplot(313, ylim=(-0.2, 2.2), xlim=(min_x, max_x))
    axes2.set_axis_off()
    # Road lines
    axes2.plot([min_x, max_x], [0, 0], lw=2, color="grey")
    axes2.plot([min_x, max_x], [1, 1], lw=2, color="grey")
    # Cars list
    cars = []
    for index in range(nCars):
        cobj = axes2.add_patch(plt.Rectangle((0, 0.2), width=max_x/200, height = 0.6, color=colours[index]))
        cars.append(cobj)

    # Subplot axes3: velocity change lines
    axes3 = fig.add_subplot(312, ylim=(-10, 60), xlim=(0, nCars))
    axes3.set_xlabel("Car")
    axes3.set_ylabel("Velocity")
    axes3.plot([0, nCars], [0, 0], lw=1, color="black")
    # VLines list
    vlines = []
    for index in range(nCars):
        vobj = axes3.add_patch(plt.Rectangle((0, -10), width=1, height = 10, color=colours[index]))
        vlines.append(vobj)
    # vlines = []
    # for index in range(nCars):
    #     vobj = axes3.plot([], [], lw=2, color=colours[index])[0]
    #     vlines.append(vobj)

    # Initialization function: plot the background of each frame
    def init():
        for line in lines:
            line.set_data([],[])    

        for car in cars:
            car.set_x(0)

        for vline in vlines:
            vline.set_height(10)

        # for vline in vlines:
        #     vline.set_data([],[])
        
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
            a = np.append([0], data[lnum, ])
            h = a[i+1] - a[i]
            if (h < 10):
                h = 10
            x = lnum
            vline.set_x(x)
            vline.set_height(h)

        # for lnum,vline in enumerate(vlines):
        #     x = lnum
        #     y = np.diff(np.append([0], data[lnum, :i]))

        #     vline.set_data(x, y)
            
        return lines, cars, vlines,

    # Call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=range(nTime), interval=10, blit=False, repeat=True)

    return anim

    


## Main code
if __name__ == "__main__":
    if len(sys.argv) <= 1 :
        exit("No input file given to arguments")

    # Data file name from args
    data_file = sys.argv[1]
    # Example
    # data_file = "../data/simpleDistanceHistory.csv"

    # # Save animation if given annoter file name
    # save_file = ""
    # if len(sys.argv) >= 3 :
    #     save_file = sys.argv[2]

    # Read in data from given cvs file
    data = pd.read_csv(data_file, header=0, index_col=0)

    # Create animation with data table values
    anim = plot(data)

    # # If there is a save file name, save the animation
    # if (len(save_file) > 0):
    #     # Set up formatting for the movie files
    #     Writer = animation.writers['ffmpeg']
    #     writer = Writer(fps=15, metadata=dict(artist='TrafficJam'), bitrate=1800)
    #     anim.save(save_file, writer=writer)
    
    # Show animation plot
    plt.show()
    

    
    
    