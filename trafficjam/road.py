#!/usr/bin/env python
from car import Car
import numpy as np

'''  '''

class Road:
    ''' Handler for the running of the code. '''
    def __init__(self):
        self.car_list = []

    def run_simulation(self, total_timesteps):
        ''' Step through all the time steps in simulation.

        At the start of the simulation we sort the cars by position to ensure
        that the car at the start of the list is at the front of the road.

        Returns:
            (``n_cars`` x ``n_time_steps+1``) array : History of the positions
            of the cars.
        '''

        # Sort the cars by position
        getPosition = lambda x: x.position
        self.car_list.sort(key=getPosition, reverse=True)

        for timestep in range(total_timesteps):
            self.update_car_positions()

    def add_multiple_cars(self, starting_positions, starting_velocity,
                          car_class=None, **car_kwargs):
        ''' Add several cars to the list.

        Args:
            starting_positions: may be a list or float (for a single car)
            starting_velocity: constant starting velocity for all cars
            car_class: Car like object to use, default to the simple Car class
            **car_kwargs: extra keywords to give to cars
        '''
        if car_class is None:
            car_class = Car

        # Treat a integer as a single length list so we can iterate
        if type(starting_positions) is int:
            starting_positions = [starting_positions,]

        for starting_position in starting_positions:
            self.add_car(
                starting_position=starting_position,
                starting_velocity=starting_velocity,
                car_class=car_class,
                **car_kwargs,
            )

    def add_car(self, starting_position, starting_velocity, car_class=None,
                **car_kwargs):
        ''' Add a car to the car list.

        Args:
            starting_velocity
            starting_position 
            car_class: Car like object to use, default to the simple Car class
            **car_kwargs: extra keywords to give to cars
        '''
        if car_class is None:
            car_class = Car

        newCar = car_class(starting_position, starting_velocity, **car_kwargs)
        self.car_list.append(newCar)

    def update_car_positions(self):
        ''' Move all the cars at the given time step. '''
        for num_car, car in enumerate(self.car_list):

            if num_car == 0:
                prev_position = car.update_position(1e6)
            else:
                prev_position = car.update_position(prev_position)

    def get_distance_to_next_car(self, car, prev_position):
        ''' Get the distance to the car in front.

        Args:
            car: Car object of the car of interest.
            prev_position: x value of the car in front.

        Returns:
            The distance between the car between the rears of the two cars.
        '''
        # The length of the car is handled by the Car's methods
        distance = prev_position - car.position

        # Sanity checks
        if distance < 0:
            error_string = (f'Distance {distance} to next'
                            'car should always be positive')
            raise ValueError(error_string)

        return distance

    def get_history_position_array(self):
        ''' Create a history-position array for all the cars on the road

        Returns:
            The value of x positions of the cars, each row
            represents a different car, each column is a time point in
            the simulation.
        '''
        distance_array = []
        for car in self.car_list:
            distance_array.append(car.return_position_array())

        distance_array = np.vstack(distance_array)
        return distance_array
