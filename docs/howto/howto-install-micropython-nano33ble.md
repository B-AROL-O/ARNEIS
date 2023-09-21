# HOWTO: Install MicroPython on an Arduino Nano 33 BLE

(2023-09-19 16:00 CEST)

## Introduction

This document explains how to install [MicroPython](https://micropython.org/) on an [Arduino Nano 33 BLE](https://store.arduino.cc/products/arduino-nano-33-ble) embedded board, then run a sample MicroPython program.

The [Nano 33 BLE](https://store.arduino.cc/products/arduino-nano-33-ble) is Arduino’s 3.3V compatible board in the smallest available form factor: 45x18mm!

The Arduino Nano 33 BLE is a completely new board on a well-known form factor. It comes with an embedded 9 axis inertial sensor what makes this board ideal for wearable devices, but also for a large range of scientific experiments in the need of short-distance wireless communication.

## Reference Documents

* [MicroPython Home Page](https://micropython.org/)
* [Arduino Nano 33 BLE](https://store.arduino.cc/products/arduino-nano-33-ble) product page on the Arduino Store
* [MicroPython with Arduino Boards](https://docs.arduino.cc/learn/programming/arduino-and-python)
* [Install MicroPython on your Nano BLE](https://docs.arduino.cc/tutorials/nano-33-ble-sense/micropython-installation#arduino-nano-33-ble)
* [Getting started with OpenMV and Nano 33 BLE](https://docs.arduino.cc/tutorials/nano-33-ble/getting-started-omv)
* [Nano 33 BLE Python® API guide](https://docs.arduino.cc/tutorials/nano-33-ble/ble-python-api) (a collection of useful scripts)]
* <https://github.com/micropython/micropython>
* [MicroPython 101](https://docs.arduino.cc/micropython-course/) - A course for learning MicroPython with the Arduino Nano ESP32

## Step-by-step instructions

<!-- Reference: <https://micropython.org/download/ARDUINO_NANO_33_BLE_SENSE/> -->

Reference: <https://docs.arduino.cc/tutorials/nano-33-ble-sense/micropython-installation#arduino-nano-33-ble>

### Install Arduino IDE

Download latest release of the Arduino IDE (2.2.1 as of 2023-09-19) from <https://www.arduino.cc/en/software>.

```bash
# Download Arduino IDE
mkdir -p ~/Downloads && cd ~/Downloads
curl -fsSL -O https://downloads.arduino.cc/arduino-ide/arduino-ide_2.2.1_Linux_64bit.AppImage
chmod a+x arduino-ide_2.2.1_Linux_64bit.AppImage

# Run Arduino IDE
~/Downloads/arduino-ide_2.2.1_Linux_64bit.AppImage
```

Follow the on-screen instructions to install the Arduino IDE on your PC.

### Run a sample sketch on the Arduino Nano 33 BLE

Arduino: File > Examples > 01.Basics > Blink

Arduino: Select Board: Arduino Nano 33 BLE on `/dev/ttyACM0`

> The "Arduino Mbed OS Nano Boards [v4.0.6]" core has to be installed for
> the currently selected "Arduino Nano 33 BLE" board.
> Do you want to install it now?

Click **YES**.

Arduino IDE: Sketch > Upload

Wait until the sketch has been successfully uploaded to the Arduino Nano 33 BLE.
The LED on the board should blink every second.

Try modifiying the sketch changing the value in the `delay(...)` statements, then upload the new sketch and make sure the blink frequency changes accordingly.

### Installing the Core

Arduino IDE: Tools > Board > Board Manager

* Make sure that the latest version of "Arduino Mbed OS Nano Boards" (4.0.6 as of 2023-09-20) is installed.

### Update Bootloader

Arduino IDE: File > Examples > Nano33BLE_System > Nano33_updateBLandSoftDevice

and open the sketch.

Arduino IDE: Sketch > Upload

Arduino IDE: Tools > Serial Monitor

```text

Flashing bootloader...
Flash Address = E0000
Flashed 11%
Flash Address = E1000
Flashed 22%
Flash Address = E2000
Flashed 34%
Flash Address = E3000
Flashed 45%
Flash Address = E4000
Flashed 56%
Flash Address = E5000
Flashed 68%
Flash Address = E6000
Flashed 79%
Flash Address = E7000
Flashed 91%
Flash Address = E8000
Flashed 100%

Bootloader 32bit CRC is: CB51658F
Writing in UICR memory the address of the new bootloader...

Bootloader update successfully completed!

Would you like to install the Soft Device (required for OpenMV)? Y/N
Storing SoftDevice length info at 0xFF000...
Flashing SoftDevice...
Flash Address = A0000
Flashed 2%
Flash Address = A1000
Flashed 5%
...
Flash Address = C3000
Flashed 97%
Flash Address = C4000
Flashed 100%


SoftDevice update complete! The board is restarting...
```

Now close the serial monitor, we will need to use the serial port for other things very soon.

### Downloading firmware

Now you will need to find the specific firmware that you need to flash to your board. You can find the available firmware on the [MicroPython page](https://docs.arduino.cc/micropython).

Download the .bin file that corresponds to the board you have.

Latest stable Nano BLE Sense Firmware (as of 2023-09-20):

* (stable)  [20230426-v1.20.0.bin](https://downloads.arduino.cc/micropython/ARDUINO_NANO_33_BLE_SENSE-20230426-v1.20.0.bin)

Result:

```text
gmacario@hw2228:~ $ ls -la Downloads/ARDUINO*
-rw-rw-r-- 1 gmacario gmacario 274216 set 20 13:40 Downloads/ARDUINO_NANO_33_BLE_SENSE-20230426-v1.20.0.bin
gmacario@hw2228:~ $ sha256sum Downloads/ARDUINO*
fbe9740fdaf7d341387424c46dd43cbe64abf9a8daaea453c268dab740938a36  Downloads/ARDUINO_NANO_33_BLE_SENSE-20230426-v1.20.0.bin
gmacario@hw2228:~ $
```

### Board Installation

Reference: <https://docs.arduino.cc/micropython/basics/board-installation>

~~Download [Arduino MicroPython Installer here](https://labs.arduino.cc/en/labs/micropython-installer)~~ ==> NO, THIS ONLY APPLIES TO Nano ESP32!

#### Finding BOSSAC

Extract `bossac` from the installation package within Arduino IDE plugins.

In our example we have installed Arduino IDE on hw2228 which is running Ubuntu 22.04 desktop:

```bash
mkdir -p ~/bin && cd ~/bin
cd ~/.arduino15/staging/packages
ls -la bossac*
tar tvzf bossac*
cd ~
tar xvzf ~/.arduino15/staging/packages/bossac*.tar.gz
ls -la ~/bin/bossac
```

Now add the installation directory to `PATH` and print `bossac` help:

```bash
PATH=~/bin:$PATH

bossac --help
```

Result:

```text
gmacario@hw2228:~ $ PATH=~/bin:$PATH
gmacario@hw2228:~ $ bossac --help
Usage: bossac [OPTION...] [FILE]
Basic Open Source SAM-BA Application (BOSSA) Version 1.9.1-17-g89f3556
Flash programmer for Atmel SAM devices.
Copyright (c) 2011-2018 ShumaTech (http://www.shumatech.com)

Examples:
  bossac -e -w -v -b image.bin   # Erase flash, write flash with image.bin,
                                 # verify the write, and set boot from flash
  bossac -r0x10000 image.bin     # Read 64KB from flash and store in image.bin

Options:
  -e, --erase           erase the entire flash starting at the offset
  -w, --write           write FILE to the flash; accelerated when
                        combined with erase option
  -r, --read[=SIZE]     read SIZE from flash and store in FILE;
                        read entire flash if SIZE not specified
  -v, --verify          verify FILE matches flash contents
  -o, --offset=OFFSET   start erase/write/read/verify operation at flash OFFSET;
                        OFFSET must be aligned to a flash page boundary
  -p, --port=PORT       use serial PORT to communicate to device;
                        default behavior is to use first serial port
  -b, --boot[=BOOL]     boot from ROM if BOOL is 0;
                        boot from FLASH if BOOL is 1 [default];
                        option is ignored on unsupported devices
  -c, --bod[=BOOL]      no brownout detection if BOOL is 0;
                        brownout detection is on if BOOL is 1 [default]
  -t, --bor[=BOOL]      no brownout reset if BOOL is 0;
                        brownout reset is on if BOOL is 1 [default]
  -l, --lock[=REGION]   lock the flash REGION as a comma-separated list;
                        lock all if not given [default]
  -u, --unlock[=REGION] unlock the flash REGION as a comma-separated list;
                        unlock all if not given [default]
  -s, --security        set the flash security flag
  -i, --info            display device information
  -d, --debug           print debug messages
  -U, --usb-port[=BOOL] force serial port detection to USB if BOOL is 1 [default]
                        or to RS-232 if BOOL is 0
  -R, --reset           reset CPU (if supported)
  -a, --arduino-erase   erase and reset via Arduino 1200 baud hack
  -h, --help            display this help text
  -V, --version         display version info

Report bugs to <bugs@shumatech.com>
gmacario@hw2228:~ $
```

Flash the firmware using the `bossac` command as shown

```bash
bossac -e -w --offset=0x16000 --port={port} -i -d -U -R {firmware}
```

In our example we have

* port: `/dev/ttyACM0`
* firmware: `~/Downloads/ARDUINO_NANO_33_BLE_SENSE-20230426-v1.20.0.bin`

(2023-09-21 08:51 CEST)

Result:

```text
macario@hw2228:~ $ bossac -e -w --offset=0x16000 --port=/dev/ttyACM0 -i -d -U -R ~/Downloads/ARDUINO_NANO_33_BLE_SENSE-20230426-v1.20.0.bin
Set binary mode
version()=Arduino Bootloader (SAM-BA extended) 2.0 [Arduino:IKXYZ]
Connected at 921600 baud
identifyChip()=nRF52840-QIAA
write(addr=0,size=0x34)
writeWord(addr=0x30,value=0x400)
writeWord(addr=0x20,value=0)
version()=Arduino Bootloader (SAM-BA extended) 2.0 [Arduino:IKXYZ]
Device       : nRF52840-QIAA
Version      : Arduino Bootloader (SAM-BA extended) 2.0 [Arduino:IKXYZ]
Address      : 0x0
Pages        : 256
Page Size    : 4096 bytes
Total Size   : 1024KB
Planes       : 1
Lock Regions : 0
Locked       : none
Security     : false
Erase flash
chipErase(addr=0x16000)

Done in 0.001 seconds
Write 274216 bytes to flash (67 pages)
[                              ] 0% (0/67 pages)write(addr=0x34,size=0x1000)
writeBuffer(scr_addr=0x34, dst_addr=0x16000, size=0x1000)
write(addr=0x34,size=0x1000)
writeBuffer(scr_addr=0x34, dst_addr=0x17000, size=0x1000)
write(addr=0x34,size=0x1000)
writeBuffer(scr_addr=0x34, dst_addr=0x18000, size=0x1000)
[=                             ] 4% (3/67 pages)write(addr=0x34,size=0x1000)
writeBuffer(scr_addr=0x34, dst_addr=0x19000, size=0x1000)
...
[============================= ] 98% (66/67 pages)write(addr=0x34,size=0x1000)
writeBuffer(scr_addr=0x34, dst_addr=0x58000, size=0x1000)
[==============================] 100% (67/67 pages)
Done in 10.430 seconds
reset()
gmacario@hw2228:~ $
```

### Run MicroPython

Launch a terminal emulator and connect to the serial port

```text
MicroPython v1.20.0 on 2023-04-26; Arduino Nano 33 BLE Sense with NRF52840
Type "help()" for more information.
>>>
```

#### Display help

```text
>>> help()
Welcome to MicroPython!

For online help please visit http://micropython.org/help/.

Quick overview of commands for the board:
  board.LED(n)    -- create an LED object for LED n (n=1,2,3,4)

If compiled with SD=<softdevice> the additional commands are
available:
  ble.enable()    -- enable bluetooth stack
  ble.disable()   -- disable bluetooth stack
  ble.enabled()   -- check whether bluetooth stack is enabled
  ble.address()   -- return device address as text string

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)
>>>
```

#### NOTE: MicroPython is a subset of Python

```text
MicroPython v1.20.0 on 2023-04-26; Arduino Nano 33 BLE Sense with NRF52840
Type "help()" for more information.
>>> foo = "Giovanni"
>>> foo
'Giovanni'
>>> foo[1:-1]
'iovann'
>>> foo[::2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: only slices with step=1 (aka None) are supported
>>>
```

<!-- EOF -->
