#!/usr/bin/env python

''' Container for the car. '''

class Car:
    ''' '''
    def __init__(self, starting_position, starting_velocity):
        self.position_history = []
        self.position = starting_position
        self.velocity = starting_velocity

        # Parameters of the cars "private", set these values to something sane
        self.retardation_rate = 25
        self.acceleration_rate = 30

        self.max_velocity = 250
        self.length = 5
        self.stop_space = 10

    def increase_speed(self):
        self.position += self.acceleration_rate

    def decrease_speed(self):
        self.position -= self.retardation_rate

    def isin_safe_distance(self, distance_to_next_car):
        return distance_to_next_car - self.length - self.stop_space

    def critical_distance(self):
        return ((self.velocity**2) / self.retardation_rate)

    def update_position(self, distance_to_next_car):
        '''Get the new position of the car after a single time step, based on the
        position of the car in front.

        Update the position history of the car.

        Args:
            Distance_to_next_car: distance to the next car including 

        Returns:
            The position of the car after the next time step

        '''

        # safe_distance = self.safe_distance(distance_to_next_car)
        # need_brake = safe_distance > self.critical_distance()
        # # too_fast = self.velocity >= self.max_velocity
        # # keep_up = (safe_distance < ((self.velocity**2) / self.acceleration_rate))
        # can_accelerate = keep_up and not too_fast
        # if need_brake:
        #     self.decrease_speed(self)
        # elif can_accelerate:
        #     new_velocity = self.increase_speed(self)
        #     if new_velocity > self.max_velocity:
        #         self.velocity = self.max_velocity
        #     else:
        #         self.velocity = new_velocity

        ## Update the position
        self.position += self.velocity
        return self

    def return_position_array(self):
        ''' Give history of the array for plotting.

        Returns:
            Return an array of positions for each time point in the simulation.
        '''
        pass


