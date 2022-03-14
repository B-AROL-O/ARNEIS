# LEGO&reg; ARNEIS Project

Here is the LEGO&reg; MOC (alias for _My Own Creation_) used for the ARNEIS project.

> **Resources**
>
> Various software applications and public resources have been used for the realization of this LEGO&reg; project:
>
> Resource | Description | Used For
> ----|----|-----
> [Bricklink Studio](https://www.bricklink.com/v3/studio/download.page) | Full featured CAD application| Project design, BOM creation, rendering, instruction manual editing, export to `ldr`
> [Bricklink PartDesigner](https://www.bricklink.com/v3/studio/partdesigner.page) | Single LEGO&reg; Part Editor | Creation of parts still not avalaible in _Bricklink Studio_. Correction of parts not working whern exported to `ldr`
> [LeoCAD](https://www.leocad.org) | Open Source CAD application | Check correctness of `ldr` files
> [LDraw](https://www.ldraw.org) | Centralized resources for LEGO&reg; CADs | Reference for getting last _parts_ used in _Bricklink PartDesigner_

## ARNEIS Conveyor (v.2022.03.12)

This conveyor is designed to move ["mignon" (miniature) bottles](https://en.wikipedia.org/wiki/Miniature_(alcohol)).
The main idea is to use a chain where some kind of _pushers_ are used to move bottles over a flat surface.

The chain is not used as a base surface for the bottles due to the difficulty of ensuring that it will stay horizontal during the movement.

A special support is designed to hold the [OAK-D-Lite](https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9095.html) AI Camera used in this project. It is possible to change the tilt of the camera by using the dedicated linear extender arm.

The white wall acts as a background for taking better snapshots of the bottles during their trip on the conveyor.

![bottles conveyor](arneis-conveyor-20220312.gif)

### Driving the conveyor

In order to verify the correct operation of the conveyor a small [MicroPython](https://micropython.org/) program has been developed.

Navigate to the [Pybricks](https://pybricks.com) home page and follow the instructions to activate the IDE for your browser and your operating system.

In this project two motors are used:
- 1x Technic Motor Powered Up XL (Item no. [bb0960c01](https://www.bricklink.com/v2/catalog/catalogitem.page?P=bb0960c01&idColor=85)): used to drive the conveyor
- 1x Technic Motor Power UP L (Item no. [bb0959c01](https://www.bricklink.com/v2/catalog/catalogitem.page?P=bb0959c01&idColor=85)): used as a _Speed Dial_

With the **XL** motor connected to the **Port B** of the Technic Hub and the **L** motor connected to the **Port A**, use the following source code to program the Hub:

```python
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# We'll use two motors. One is a dial
# to set the speed of the other motor.
motor = Motor(Port.B)
dial = Motor(Port.A)

# Say hello :)
print("Hello, Pybricks!")

# First, we'll move the dial to zero.
dial.run_target(500, 0, Stop.COAST)

while True:
    # Set the speed based on dial angle
    speed = dial.angle()*3
    if abs(speed) < 50:
        speed = 0

    # Run motor at desired speed
    motor.run(speed)

    angle = dial.angle()
    print("angle=" + str(angle) + "    ", end='\r')

    # Wait briefly, then repeat
    wait(10)
```

You may adjust the speed and direction of the conveyor by rotating the dial (clockwise or counterclockwise).

### Project resources

> **Files**
>
> [`arneis-conveyor-20220312.io`](arneis-conveyor-20220312.io) : the LEGO project in _Bricklink Studio_ CAD.<br/>
> [`arneis-conveyor-20220312.ldr`](arneis-conveyor-20220312.ldr) : the LEGO project exported in [LDraw file format](https://www.ldraw.org/article/218.html).<br/>
> [`arneis-conveyor-20220312.png`](arneis-conveyor-20220312.png) : a 3D rendered version image.<br/>
> [`arneis-conveyor-20220312.gif`](arneis-conveyor-20220312.gif) : a 3D rendered video of rotating MOC.<br/>
> [`arneis-conveyor-20220312.pdf`](https://arneis.blob.core.windows.net/public-folder/arneis-conveyor-20220312.pdf) : building instruction manual
