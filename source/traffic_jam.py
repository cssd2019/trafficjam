#!/usr/bin/env python
from road import Road

''' Main script to run the traffic jam simulation. '''

n_cars = 4
n_timesteps = 100
starting_positions = range(0, n_cars)
starting_velocity = 1

road = Road()

# Populate the road with cars
road.add_multiple_cars(starting_positions, starting_velocity)

road.run_simulation(n_timesteps)
history_array = road.get_history_position_array()

print(history_array)
