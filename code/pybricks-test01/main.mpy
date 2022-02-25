from pybricks.parameters import Port
from pybricks.pupdevices import ColorDistanceSensor, Motor
from pybricks.tools import wait

motor = Motor(Port.A)
# dial = Motor(Port.A)
sensor = ColorDistanceSensor(Port.B)

# Say hello :)
print("Hello, Pybricks!")

# First, we'll move the dial to zero.
# dial.run_target(500, 0, Stop.COAST)

while True:
    # Set the speed based on sensor distance
    dist = sensor.distance()
    speed = dist * 5
    if abs(speed) < 100:
        speed = 0
    print("dist=", dist, ", speed=", speed)
    # speed = dial.angle() * 3

    # Run motor at desired speed
    motor.run(speed)

    # Wait briefly, then repeat
    wait(10)

# EOF
