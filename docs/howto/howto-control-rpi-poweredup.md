# HOWTO Control a LEGO Powered Up Hub for the ARNEIS Project

## Introduction

This document explains how to install a use a Python script to control a LEGO Powered Up Hub through BLE.

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

## Controlling from a Raspberrry Pi

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

TODO

<!-- EOF -->
