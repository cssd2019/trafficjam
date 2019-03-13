from trafficjam.car import Car
import pytest

@pytest.fixture
def new_car():
    new_car = Car(
        starting_position = 0,
        starting_velocity = 40,
        braking_rate      = 25,
        acceleration_rate = 10,
        max_velocity      = 60,
        desired_velocity  = 40,
        length            = 4,
        stop_space        = 8,
        safe_dist         = 100
    )
    return new_car

def test_all_necessary_attributes(new_car):
    assert(new_car.position is not None)
    assert(new_car.velocity is not None)
    assert(new_car.braking_rate is not None)
    assert(new_car.acceleration_rate is not None)
    assert(new_car.max_velocity is not None)
    assert(new_car.desired_velocity is not None)
    assert(new_car.length is not None)
    assert(new_car.stop_space is not None)
    assert(new_car.safe_dist is not None)

def test_increase_velocity(new_car):
    new_car.increase_speed(time_step = 1)
    assert(new_car.velocity == 50)

def test_decrease_velocity(new_car):
    new_car.decrease_speed(time_step = 1)
    assert(new_car.velocity == 15)

def test_update_position_too_close(new_car):
    new_car.update_position(10)
    assert(new_car.position == 0)

def test_update_position_too_far(new_car):
    new_car.update_position(250)
    assert(new_car.position == 50)

def test_update_position_regular(new_car):
    new_car.update_position(20)
    assert(new_car.position == 15)
