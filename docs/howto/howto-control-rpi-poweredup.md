# HOWTO Control a LEGO Powered Up Hub for the ARNEIS Project

## Introduction

This document illustrates the available options to control a LEGO&reg; Powered Up Hub (LEGO Item No [bb0961c01](https://www.bricklink.com/v2/catalog/catalogitem.page?P=bb0961c01&idColor=86)).

The LEGO Powered Up Hub is an embedded device based on a small microcontroller which can control up to four LEGO Powered Up devices such as motor, lights and sensors.
In addition to a button and a multicolor programmable LED, the Hub is provided with a Bluetooth Low Energy interface which allows the Hub to act as a BLE Peripheral device and communicate with a BLE Central device such as a mobile phone, a laptop or even a Raspberry Pi.

The LEGO Group has released a few official apps for the iOS&trade; and Android&trade; operating systems.
Those apps can be downloaded and installed from the respective app stores (App Store for iOS devices, Google Play for Android devices) and provide a seamless user experience for controlling official LEGO sets and MOCs.

Additionally, a few open source projects such as [Pybricks](https://pybricks.com/) have been developed to simplify programming of the LEGO Powered Up Hubs.

The following chapters of this document examine the possible options which may be used to program and control the Hubs.

## Using the "LEGO&reg; Powered Up" App

TODO

## Using the "LEGO&reg; TECHNIC&trade; CONTROL+" App

Install the "LEGO&reg; TECHNIC&trade; CONTROL+" app from

* Google Play Store: <https://play.google.com/store/apps/details?id=com.lego.technic.controlplus>
* Apple Store: TODO

Launch the app and select set "Liebherr 9800".

Connect 2x XL motor and 1x L motor to the Hub.

Follow the instructions displayed by the app and update the firmware if requested.

TODO

## Using Pybricks

### Install the Pybricks firmware

Instructions at <https://pybricks.com/install/technic-boost-city/>

Before you begin, turn the hub off. The update works best with fresh batteries.
If you use the City Hub, you must unplug all motors and sensors. Follow these steps:

1. Go to [Pybricks Code](https://code.pybricks.com/).
2. Press and hold the hub button. Wait for a blinking pink light.
3. While you hold it, click the _firmware update_ button.
4. Select the _LEGO Bootloader_ and click _Pair_.
5. Wait until the light turns off, and then blinks red/green/blue.
6. Release the button and wait for the installation to finish.

### Load some Python program

From the [Pybricks Code](https://code.pybricks.com/) web interface, create or open a MicroPython source file and upload it to the LEGO Technics BT Hub. You may find some examples under the `/code` folder of the [ARNEIS repository on GitHub](https://github.com/B-AROL-O/ARNEIS).

TODO

## Controlling from a Raspberry Pi

### Install undera/pylgbst on the Raspberry Pi

<!-- (2022-01-27 16:45 CET) -->

Logged in as pi@rpi4gm35

```bash
mkdir -p ~/github/undera
cd ~/github/undera
git clone https://github.com/undera/pylgbst
```

Create a Python virtual environment

```bash
cd ~/github/undera/pylgbst
python3 -m venv .venv
source .venv/bin/activate
```

TODO: Install prerequisites:

```bash
sudo apt -y install libbluetooth-dev
sudo apt -y install libboost-python-dev
sudo apt -y install libboost-thread-dev
sudo apt -y install libglib2.0-dev
# pip install -U boost
# pip install -U gattlib
pip install -U bluepy
pip install -U pylgbst
```

Launch pylgbst demo:

```bash
cd ~/github/undera/pylgbst
source .venv/bin/activate
cd examples
python3 demo.py
```

Result:

```text
(.venv) pi@rpird102:~/github/undera/pylgbst/examples $ python3 demo.py
42      INFO    root    Trying get_connection_bluepy
74      INFO    comms-bluepy    Discovering devices...
88      INFO    root    Trying get_connection_bluegiga
90      INFO    root    Trying get_connection_gatt
92      INFO    root    Trying get_connection_bleak
148     INFO    root    Trying get_connection_gattool
150     INFO    root    Trying get_connection_gattlib
165     INFO    comms-gattlib   Discovering devices using hci0...
Traceback (most recent call last):
  File "demo.py", line 259, in <module>
    hub = MoveHub(**parameters)
  File "/home/pi/github/undera/pylgbst/.venv/lib/python3.7/site-packages/pylgbst/hub.py", line 231, in __init__
    connection = get_connection_auto(hub_name=self.DEFAULT_NAME)
  File "/home/pi/github/undera/pylgbst/.venv/lib/python3.7/site-packages/pylgbst/__init__.py", line 75, in get_connection_auto
    raise Exception("Failed to autodetect connection, make sure you have installed prerequisites")
Exception: Failed to autodetect connection, make sure you have installed prerequisites
Exception ignored in: <function Hub.__del__ at 0xb64d15d0>
Traceback (most recent call last):
  File "/home/pi/github/undera/pylgbst/.venv/lib/python3.7/site-packages/pylgbst/hub.py", line 76, in __del__
    if self.connection and self.connection.is_alive():
AttributeError: 'MoveHub' object has no attribute 'connection'
(.venv) pi@rpird102:~/github/undera/pylgbst/examples $
```

Troubleshooting

```text
(.venv) pi@rpird102:~/github/undera/pylgbst/examples $ hciconfig
hci0:   Type: Primary  Bus: UART
        BD Address: E4:5F:01:35:8F:98  ACL MTU: 1021:8  SCO MTU: 64:1
        UP RUNNING
        RX bytes:1611 acl:0 sco:0 events:103 errors:0
        TX bytes:3575 acl:0 sco:0 commands:103 errors:0

(.venv) pi@rpird102:~/github/undera/pylgbst/examples $
```

## Interfacing an input sensor

This chapter discusses several alternatives we have in case we need to interface one or more input sensors to the Edge Controller of ARNEIS.
The alternatives presented here are the following:

- Direct GPIO input pin of the Raspberry Pi
- Input sensors connected to the LEGO Powered Up Hub
- Input sensors connected to the SBrick Plus
- etc.

### Direct GPIO input pin of the Raspberry Pi

This is probably the most flexible option in terms of sensor interfacing.

In the internet there is abundance of tutorials, videos and blog posts which explain how to interface an input sensor to the GPIO pins of the Raspberry Pi and write a program to check the sensor state. Google is your friend.

Some quick links:

- [#369 Definitive Guide to Attaching Sensors to the Raspberry Pi (Tutorial)](https://www.youtube.com/watch?v=gnE4v-PcYKQ) - YouTube video by Andreas Speiss, 2021-01-24

On the other hand, this option has the disadvantage that the feedback loop sensor/actuator will be slower since a longer path (Sensor --> Raspberry Pi --> BLE --> Technics Hub --> Actuator) should be followed.

### Input sensors connected to the LEGO&reg; Powered Up Hub

At the moment only few types of input sensors with Powered Up interface are available:

- [LEGO Powered Up Color &amp; Distance Sensor](https://www.lego.com/en-it/product/color-distance-sensor-88007) - Code 88007
- [LEGO WeDo Tilt Sensor](https://www.brickowl.com/catalog/lego-wedo-tilt-sensor-63522) - Code 63522
- Infrared Sensor - Code TODO

Those sensors are directly usable with LEGO&reg; Technics BT Hub using different languages, including [Pybricks](https://pybricks.com/):

- <https://docs.pybricks.com/en/stable/pupdevices/colordistancesensor.html>
- <https://docs.pybricks.com/en/stable/pupdevices/tiltsensor.html>
- <https://docs.pybricks.com/en/stable/pupdevices/infraredsensor.html>

As an added bonus, the [ColorDistanceSensor](https://docs.pybricks.com/en/stable/pupdevices/colordistancesensor.html#pybricks.pupdevices.ColorDistanceSensor) can send infrared signals to control Power Functions infrared receivers. You can use this technique to control medium, large, extra large, and train motors. You can find more details at <https://docs.pybricks.com/en/stable/pupdevices/pfmotor.html>.

Provided that the available sensors are good enough for the use case, this option is probably the one which guarantees the quickest feedback loop (Sensor --> Technics Hub --> Actuator)

### Input sensors connected to the SBrick Plus

Another possible option is to connect and interface LEGO&reg; Power Functions sensors.

The LEGO&reg; Power Functions family provides a richer set of input sensors with respect to the relatively newer Powered Up family:

- TODO

To interface Power Functions components including input sensors and control them from either a mobile app or a Python scripts running on a Raspberry Pi the [SBrick Plus](TODO) brick can be used.

Additionally, we may use the RXTX mode of the Powered Up Color Sensor which allows to communicate with a Power Functions infrared receiver and thus control motors of the Power Functions family. Unfortunately this solution only works for actuators, not for sensors.

You may find more details at the following links:

- [Using Power Functions with the Powered Up app](https://www.lego.com/en-in/service/help/apps_video_games_device_guides/using-power-functions-with-the-powered-up-app-kA009000001dckrCAA) - LEGO&reg; Customer Service
- [LEGO Powered Up app with Power Functions and remote support! Too good to be true?](https://www.youtube.com/watch?v=scvifoxEbWs) - RacingBrick, 2020-03-21

<!-- EOF -->
