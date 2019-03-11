#!/usr/bin/env python
from car import Car

'''  '''

class Road:
    ''' '''
    def __init__(self):
        car_list = []

    def run_simulation(total_timesteps):
        ''' Step through all the time steps in simulation.

        Returns:
            history_position_array: To be used for plotting.
        '''
        for timestep in total_timesteps:
            # Run simulation
            update_car_positions()
        

    def add_car(self, starting_position, starting_velocity, **car_kwargs):
        ''' Add a car to the car list.

        Args:
            starting_velocity and starting_position of the car
            **car_kwargs: extra keywords to give to cars
        '''
        newCar = Car(starting_position, starting_velocity, **car_kwargs)
        car_list.append(newCar)

    def update_car_positions(self):
        ''' Move all the cars at the given time step. '''
        for car in car_list:
            distance_to_next_car = get_distance_to_next_car()
            position = car.update_position(distance_to_next_car)
            # Position can be reused to help calculate the distance to the next
            # car along

    def get_distance_to_next_car(self, car):
        ''' Get the distance to the car in front.

        Be careful about edge cases.
        '''
        return 0
    
    def get_history_position_array(self):
        ''' Create a history-position array for all the cars on the road

        Returns:
            distance_array: The value of x positions of the cars, each row
                represents a different car, each column is a time point in
                the simulation.

                Ideally a numpy array
        
        '''
        distance_array = []
        for car in self.car_list:
            pass

        return distance_array
