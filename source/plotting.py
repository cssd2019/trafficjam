#!/usr/bin/env python

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
