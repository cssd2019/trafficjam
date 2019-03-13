# Project: Traffic Jam with Python

The project tries to simulate a traffic jam. The simulation starts cars with certain speed and based on the distance between them the accleration changes to maintain a safe distance. This should creates a simulation of traffic jam. Following are some basic planning on the different objects and their relationships.

## Getting Started

To run the simulation `cd` into `trafficjam/source/` directory and then run

    python ./traffic_jam.py

- `source/traffic_jam.py` contains code to initialise the program, including the initial positions of the cars and their velocity.
- `source/car.py` contains the logic of the cars; how they accelerate or slow down in reaction to the cars surrounding them.
- `source/road.py` controls the flow of the simulation.

To then analyse the data and show the animation, run

    python ./plotting.py

## Configure the simulation

### Simulation parameters
- `n_cars`: number of cars in the simulation
- `n_timesteps`: number of timesteps to take in simulation
- `car_spread`: the distance between the first and last car in the starting grid

### Car parameters
- `max_velocity`: the desired velocity of the car
- `safe_distance`: the distance that the car will try and maintain from the car in front.
