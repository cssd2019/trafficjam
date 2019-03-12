#!/usr/bin/env python
from road import Road
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

''' Main script to run the traffic jam simulation. '''

n_cars = 5
n_timesteps = 30
starting_positions = np.linspace(0, 9, n_cars)
starting_velocity = 2

road = Road()

# Populate the road with cars
road.add_multiple_cars(starting_positions, starting_velocity)

road.run_simulation(n_timesteps)
history_position_array = road.get_history_position_array()

# Save the history array to file
distance_dataframe = pd.DataFrame(history_position_array)

save_location = 'simpleDistanceHistory.csv'
distance_values = distance_dataframe[0:n_timesteps]
distance_dataframe.to_csv(save_location)

