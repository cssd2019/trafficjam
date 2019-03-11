#!/usr/bin/env python
import pandas as pd
import numpy as np

''' Create sample data of cars driving at a constant velocity.

distance_array: The value of x positions of the cars, each row
represents a different car, each column is a time point in
the simulation.

To read the data again use
dataframe = pandas.read_csv([filepath])

we can also use this as a numpy array
data = np.array(dataframe.values)
'''

save_location = 'sampledata.csv'
n_cars = 7
n_time_points = 50

furthest_starting_pos = 12
starting_positions = np.linspace(0, furthest_starting_pos, n_cars)
velocity = 3

distance_array = np.zeros((n_cars, n_time_points))

# Populate the starting positions
distance_array[:,0] = starting_positions

for time_point in range(1,n_time_points):
    distance_array[:,time_point] = distance_array[:,time_point-1] + velocity

distance_array = pd.DataFrame(distance_array)
distance_array.to_csv(save_location, header=False, index=False)


