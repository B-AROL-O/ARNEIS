# Installing DepthAI Demo v3.0.9 on Windows 10

<!-- (2022-01-14 18:33 CET) -->

**TODO**: Create a PR to add to https://github.com/B-AROL-O/ARNEIS/tree/main/docs/howto

## Introduction

The following document explains how to prepare and configure a Windows lapto to be used with the [ARNEIS project](https://github.com/B-AROL-O/ARNEIS/tree/fix/updates-to-howto-rpi4).

## References

* <https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/#use-windows-installer>

## Prerequisites

* One [OAK-D-Lite](https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9095.html)
* One desktop PC or laptop for controlling the OAK-D-Lite
  - OS: A recent version of Windows or Linux or macOS
  - Tested on alpha (HW: Dell Precision M4600, OS: Windows 10 version 21H2)
* Fast internet connection

## Step-by-step instructions

### Install DepthAI

Download `DepthAI-setup-v3.0.9.exe` from <https://github.com/luxonis/depthai/releases>

Double click `DepthAI-setup-v3.0.9.exe` to launch the install wizard

> **Windows protected your PC**
>
> Microsoft Defender SmartScreen prevented an unrecognized app from starting.
> Running this app might put your PC at risk.
>
> [More info](TODO)
>
> [Don't run](TODO)

Click "More info".

> **Windows protected your PC**
>
> Microsoft Defender SmartScreen prevented an unrecognized app from starting.
> Running this app might put your PC at risk.
>
> * App: DepthAI-setup-v3.0.9.exe
> * Autore: Luxonis Holding Corporation
>
> [Run anyway](TODO) | [Don't run](TODO)

Click "Run anyway".

> **Select Destination Location**
>
> Where should DepthAI be installed?
>
> Setup will install DeptyAI into the following folder.
>
> To continue, click Next.
> If you would like to select a different folder, click Browse.
>
> `C:\Users\gmaca\AppData\Local\Programs\DepthAI`
>
> At least 364,5 MB of free disk space is required.
>
> [Next](TODO) | [Cancel](TODO)

Click "Next".

> **Select Additional Tasks**
>
> Which additional tasks should be performed?
>
> Select the additional tasks you would like Setup to perform while installing DepthAI, then click Next.
>
> Additional shortcuts:
> * [x] Create a desktop shortcut
>
> [Back](TODO) | [Next](TODO) | [Cancel](TODO)

Accept proposed values, then click "Next".

> **Ready to Install**
>
> Setup is now ready to begin installing DepthAI on your computer.
>
> Click Install to continue with the installation, or click Back if you want to review or change any settings.
>
> ```text
> Destination location:
>     C:\Users\gmaca\AppData\Local\Programs\DepthAI
>
> Additional tasks:
>     Additional shortcuts:
>         Create a desktop shortcut
> ```
>
> [Back](TODO) | [Install](TODO) | [Cancel](TODO)

Click "Install".

<!-- (2022-01-14 19:46 CET) -->

> **Installing**
>
> Please wait while Setup installs DepthAI on your computer.

...

<!-- (2022-01-14 19:51 CET) -->

> **Completing the DepthAI Setup Wizard**
>
> Setup has finished installing DepthAI on your computer.
> The application may be launched by selecting the installed shortcuts.
>
> Click Finish to exit Setup.
>
> * [x] Launch DepthAI

Click "Finish".

TODO

> Installing Depthai Requirements

If no OAK-D-Lite is connected a dialog box like this one should be displayed:

> An error occurred
>
> File "C:\Users\gmaca\AppData\Local\ProgramsDepthAI\depthai\depthai_demo.py", line 625, in run<br>
>     self.instance.run_all(self.conf)<br>
>     ...<br>
>     No DepthAI device found!
>
> [OK](TODO)

Click "OK" to terminate the program.

### Connect the OAK-D-Lite

Now connect your OAK-D-Lite to your laptop using a proper USB 3.0 USB-A to USB-C connector,
then double click on the "DepthAI" icon on your desktop.

Result: the DepthAI demo main window is displayed with the augmented video captured by the OAK-D-Lite.

TODO: Figure out how DepthAI-demo works.

<!-- EOF -->