# Results

In order to create a traffic jam we create a number of cars on the road and
allow the simulation to advance for a given number of steps, before slowing one
of the cars near the front of the grid for several steps and the allowing it to
resume normal behaviour.

This is implemented by:
```eval_rst
.. autofunction:: traffic_jam.peturb_traffic
```

Once this has produces a ```history_postion_array``` this is then passed on to
the plotting code for visualisation

## Benchmark run
In order to test the plotting, and show that all parts run together we can show
cars simply drive after with no disturbance. This shows that a tightly grouped
set of cars will spread out into a diffuse group

```eval_rst
.. autofunction:: traffic_jam.simple_run
```

## Changing the starting distance

We run the simulation, changing the distance between the cars in each run, this is done by using the following function

```eval_rst
.. autofunction:: traffic_jam.start_space_sweep
```

This allows us to see two distinct behaviours, when the ```car_spacing``` is
above a critical distance the cars recover from the jam with only a small decrease 
in velocity.

[[embed figure]]

However, below this distance, when the first car slows it leads to a much larger
delays in the cars behind. Some cars even stop fully, as shown below,


