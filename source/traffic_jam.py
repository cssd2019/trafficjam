#!/usr/bin/env python
from road import Road
import pandas as pd

''' Main script to run the traffic jam simulation. '''

n_cars = 4
n_timesteps = 30
starting_positions = range(0, n_cars)
starting_velocity = 3

road = Road()

# Populate the road with cars
road.add_multiple_cars(starting_positions, starting_velocity)

road.run_simulation(n_timesteps)
history_position_array = road.get_history_position_array()

# Save the history array to file
distance_dataframe = pd.DataFrame(history_position_array)
# distance_dataframe.to_csv(save_location)

print(distance_dataframe)
