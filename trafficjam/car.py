#!/usr/bin/env python

import numpy as np

''' Container for the car. '''

class Car:
    ''' '''
    def __init__(self, starting_position, starting_velocity, braking_rate = 25,
                 acceleration_rate = 10, max_velocity = 60, desired_velocity = 40,
                 length = 4, stop_space = 8, safe_dist = 100):
        self.position_history   = [starting_position]
        self.position           = starting_position
        self.velocity           = starting_velocity
        self.braking_rate       = braking_rate # m/s^2
        self.acceleration_rate  = acceleration_rate # m/s^2
        self.max_velocity       = max_velocity # m/s
        self.desired_velocity   = desired_velocity # m/s
        self.length             = length # meters
        self.stop_space         = stop_space # meters
        self.safe_dist          = safe_dist # meters

    def increase_speed(self, time_step):
        self.velocity += self.acceleration_rate * time_step
        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity

    def decrease_speed(self, time_step):
        self.velocity -= self.braking_rate * time_step
        if self.velocity < 0:
            self.velocity = 0

    def update_position(self, position_of_next_car):
        '''Get the new position of the car after a single time step, based on the
        position of the car in front.

        Update the position history of the car.

        Args:
            position_of_next_car: distance to the next car including

        Returns:
            The position of the car after the next time step

        '''
        dist = position_of_next_car - self.position - self.length - self.stop_space
        if dist < self.safe_dist:
            self.decrease_speed(time_step = 1) # We have not defined time step
        if dist > self.safe_dist:
            self.increase_speed(time_step = 1) # We have not defined time step

        self.position += self.velocity
        self.position_history.append(self.position)
        return self.position

    def return_position_array(self):
        ''' Give history of the array for plotting.

        Returns:
            Return an array of positions for each time point in the simulation.
        '''
        return self.position_history
