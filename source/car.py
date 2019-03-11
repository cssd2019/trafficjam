#!/usr/bin/env python

''' Container for the car. '''

class Car:
    ''' '''
    def __init__(self, starting_position, starting_velocity):
        self.position_history = []
        self.position = starting_position
        self.velocity = starting_velocity

        # Parameters of the cars "private", set these values to something sane
        self.max_accelration = 1
        self.desired_velocity = 1
        self.length = 2

    def update_position(self, distance_to_next_car):
        '''Get the new position of the car after a single time step, based on the
        position of the car in front.

        Update the position history of the car.

        Args:
            Distance_to_next_car: distance to the next car including 

        Returns:
            The position of the car after the next time step

        '''
        pass

    def return_position_array(self):
        ''' Give history of the array for plotting.

        Returns:
            Return an array of positions for each time point in the simulation.
        '''
        pass


