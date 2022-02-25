from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorDistanceSensor, Motor
from pybricks.tools import wait

# Say hello :)
print("Hello, Pybricks!")

motor = Motor(Port.A)
# dial = Motor(Port.A)
sensor = ColorDistanceSensor(Port.B)
# Sensor light will be set to Color.GREEN when measuring distance
sensor.light.off()

# First, we'll move the dial to zero.
# dial.run_target(500, 0, Stop.COAST)

while True:
    # Set the speed based on sensor distance
    dist = sensor.distance()
    # sensor.light.on(Color.RED)
    speed = dist * 5
    if abs(speed) < 100:
        speed = 0
    print("dist=", dist, ", speed=", speed)
    # speed = dial.angle() * 3

    # Run motor at desired speed
    motor.run(speed)

    # Wait briefly, then repeat
    wait(100)

# EOF
