#!/usr/bin/env pytest
# import pytest
import sys; sys.path.append('../trafficjam/')
import numpy as np
from car import Car
from road import Road
from numpy.testing import assert_allclose

class SimpleCar(Car):
    ''' Create a car that moves at constant velocity. '''
    def update_position(self, distance_to_next_car):
        ''' Move the car at a constant velocity. '''
        self.position += self.velocity
        self.position_history.append(self.position)
        return self.position

    def return_position_array(self):
        ''' Return the history-position array. '''
        return self.position_history


def run_simulation(n_time_steps, starting_velocity, starting_positions=0):
    ''' Run the simulation with a number of cars.

    starting_positions can either be a list or integer (for a single car).
    '''
    r = Road()

    if type(starting_positions) is int:
        starting_positions = [starting_positions,]

    for starting_position in starting_positions:
        r.add_car(
            starting_velocity=starting_velocity,
            starting_position=starting_position,
            car_class=SimpleCar,
        )

    r.run_simulation(total_timesteps=n_time_steps)
    return r

def test_final_position_single_car():
    ''' Car ends up at the right position. '''
    n_time_steps = 100
    starting_velocity = 1
    r = run_simulation(n_time_steps, starting_velocity)

    history_array = r.get_history_position_array()
    final_position = history_array[0,-1]

    expected_final_position = n_time_steps*starting_velocity
    assert expected_final_position == final_position

def test_all_positions():
    ''' History of the car should be [starting_pos,
    starting_pos+velocity, ..., starting_pos+n_time_steps*velocity] .
    '''
    n_time_steps = 100
    starting_velocity = 1
    starting_pos = 2
    r = run_simulation(n_time_steps, starting_velocity, starting_pos)

    history_array = r.get_history_position_array()[0]
    expected_history = np.arange(
        starting_pos,
        starting_pos+starting_velocity*(n_time_steps+0.5),
        starting_velocity,
    )

    np.testing.assert_allclose(expected_history, history_array)

def test_history_array_shape():
    ''' History array should be of shape (n_cars)*(n_timesteps + 1). '''
    n_time_steps = 100
    starting_velocity = 1

    n_cars = 3
    starting_positions = range(n_cars)

    r = run_simulation(n_time_steps, starting_velocity, starting_positions)
    history_array = r.get_history_position_array()

    expected_shape = (n_cars, n_time_steps+1)
    assert expected_shape == history_array.shape

def test_correct_starting_positions():
    ''' '''
    starting_range = 100
    n_cars = 5
    starting_positions = np.linspace(0, starting_range, n_cars)
    starting_velocity = 2

    road = Road()
    road.add_multiple_cars(starting_positions, starting_velocity,
                           car_class=Car)

    history_array = road.get_history_position_array()
    actual_starting_pos = history_array.flatten()
    assert_allclose(actual_starting_pos, starting_positions)
