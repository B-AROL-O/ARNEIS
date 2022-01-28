# Controlling LEGO Powered Up Hub from a Raspberry Pi

TODO: Create PR and link it to <https://github.com/B-AROL-O/ARNEIS/issues/50>

Add to links:

* <https://magpi.raspberrypi.com/articles/hack-lego-boost-with-raspberry-pi>

<hr>

<!-- (2022-01-27 16:45 CET) -->

Logged in as pi@rpi4gm45

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
