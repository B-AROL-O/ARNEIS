from pybricks.pupdevices import Motor
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# We'll use two motors. One is a dial
# to set the speed of the other motor.
motor = Motor(Port.A)
# dial = Motor(Port.A)
sensor = ColorDistanceSensor(Port.B)

# Say hello :)
print("Hello, Pybricks!")

# First, we'll move the dial to zero.
# dial.run_target(500, 0, Stop.COAST)

while True:
    # Set the speed based on dial angle
    dist = sensor.distance()
    speed = dist * 5 # dial.angle()*3
    if abs(speed) < 100:
        speed = 0
    print("dist=", dist, ", speed=", speed)

    # Run motor at desired speed
    motor.run(speed)

    # Wait briefly, then repeat
    wait(10)

# EOF
