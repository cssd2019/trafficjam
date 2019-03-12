# Project: Traffic Jam with Python

The project tries to simulate the traffic jam. The simulation starts cars with certain speed and based on the distance between them the accleration changes to maintain a safe distance. This should creates a simulation of traffic jam. Following are some basic planning on the different objects and their relationships.

## Introduction

To run the simulation `cd` into `trafficjam` directory and then run

    python source/traffic_jam.py

- `source/trafficjam.py` contains code to initialise the program, including the initial positions of the cars and their velocity.
- `source/car.py` contains the logic of the cars; how they accelerate or slow down in reaction to the cars surrounding them.
- `source/road.py` controls the flow of the simulation.
