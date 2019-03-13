# Project: Traffic Jam with Python

![](planning/planning.png)
The project tries to simulate the traffic jam. The simulation starts cars with certain speed and based on the distance between them the accleration changes to maintain a safe distance. This should creates a simulation of traffic jam. Following are some basic planning on the different objects and their relationships.

## Introduction

To run the simulation `cd` into `trafficjam` directory and then run

    python ./traffic_jam.py

- `trafficjam/traffic_jam.py` contains code to initialise the program, including the initial positions of the cars and their velocity.
- `trafficjam/car.py` contains the logic of the cars; how they accelerate or slow down in reaction to the cars surrounding them.
- `trafficjam/road.py` controls the flow of the simulation.

## Analysis of results

`traffic_jam.py` produces a `.csv` containing the historical postitions of all the cars, to show an animation of all the cars run 

    python ./plotting.py [history_array.csv]
       

## Making documentation

The results and summary of the project is contained with the docs. To view these, run 

    make html
    
or 

    make latex
    
from within docs. 
