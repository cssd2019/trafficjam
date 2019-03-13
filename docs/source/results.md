# Results

In order to create a traffic jam we create a number of cars on the road and
allow the simulation to advance for a given number of steps, before slowing one
of the cars near the front of the grid for several steps and the allowing it to
resume normal behaviour.

This is implemented by 

```eval_rst
.. autofunction:: traffic_jam.peturb_traffic
```

Once this has produces a ```history_postion_array``` this is then passed on to
the plotting code for visualisation

## Changing the starting distance

We run the simulation, changing the distance between the cars in each run, this is done by using the following function

```eval_rst
.. autofunction:: traffic_jam.start_space_sweep
```
