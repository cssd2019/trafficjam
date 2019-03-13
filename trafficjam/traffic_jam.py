#!/usr/bin/env python
from road import Road
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Main script to run the traffic jam simulation. '''

n_cars = 70
n_timesteps = 100
# starting_space = 100
starting_velocity = 2

def simple_run(n_timesteps):
    ''' Run the simulation for a given number of timesteps.

    Args:
        n_timesteps: number of steps to take in the simulation

    Returns:
        history_position_array: An array containing the positions of all the
        cars with time.
    '''
    road = Road()

    # Populate the road with cars
    road.add_multiple_cars(starting_positions, starting_velocity)
    road.run_simulation(n_timesteps)
    history_position_array = road.get_history_position_array()
    return history_position_array

def peturb_traffic(starting_positions, n_timesteps_before, n_timesteps_slowed, n_timesteps_after):
    '''Allow the simulation to run for a given number of steps before suddenly
    slowing one car and resuming the simulation.

    Args:
        n_timestep: number of steps to take in the simulation

    Returns:
        history_position_array: An array containing the positions of all the
        cars with time.
    '''
    road = Road()

    # Add the cars and allow them to run for a while
    road.add_multiple_cars(starting_positions, starting_velocity)
    road.run_simulation(n_timesteps_before)

    # Slow a car in the middle of pack
    slowed_car_num = 3
    slowed_car = road.car_list[slowed_car_num]
    slowed_car.max_velocity = 20
    slowed_car.velocity = 20

    # Resume the simulation
    road.run_simulation(n_timesteps_slowed)

    # Allow the car to recover
    slowed_car.max_velocity = 60
    road.run_simulation(n_timesteps_after)

    history_position_array = road.get_history_position_array()
    return history_position_array

def save_dataframe(history_position_array,
                   save_location='../data/simpleDistanceHistory.csv'):
    ''' Write the position array to file as a csv. '''
    distance_dataframe = pd.DataFrame(history_position_array)
    distance_dataframe.to_csv(save_location)

def start_space_sweep():
    ''' Run the simulation for several different starting positions. '''
    for starting_space in range(80, 240+1, 20):
        starting_positions = np.arange(n_cars)*starting_space
        history_position_array = peturb_traffic(starting_positions, 50, 40, 250)
        save_name = f'../data/staring_space_{starting_space}.csv'
        save_dataframe(history_position_array, save_name)

if __name__ == '__main__':
    start_space_sweep()

