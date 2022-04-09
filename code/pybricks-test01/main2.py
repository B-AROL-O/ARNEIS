from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# We'll use two motors. One is a dial
# to set the speed of the other motor.
motor = Motor(Port.B)
dial = Motor(Port.A)

# Say hello :)

# First, we'll move the dial to zero.
dial.run_target(500,0,Stop.COAST)

while True:
    # Set the speed based on dial angle
    speed = dial.angle()*3
    if abs(speed) < 100:
        speed = 0

    # Run motor at desired speed
    motor.run(speed)

    # Wait briefly, then repeat
    wait(10)
