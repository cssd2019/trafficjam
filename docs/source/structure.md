## Structure of the program

The simulation is an agent based simulation based on the ```Car``` object 
controlled by the ```Road```. These are covered in more detail here:
```eval_rst
.. toctree::
  road
  car
```

The ```Road``` contains a list of ```car``` objects that it controls. This is 
initialised by calling ```Road.add_car``` with starting parameters for the car.

To advance a time-step in the simulation the ```Road``` calls ```Car.update_postion``` 
for each car in its list by providing it with the position of the car in-front,
starting with the one at the front of the queue.

The ```Car``` then decides how far it will advance and returns the new position to
the ```Road```.

At the end of the simulation, the ```Road``` polls all ```Car``` instances to get 
their ```history_postion_array```, and combines this into a data-frame to be used 
in plotting.
