# HOWTO Prepare a Raspberry Pi 4B for the ARNEIS project

<!-- (2022-01-12 07:44 CET) -->

## Introduction

The following document explains how to prepare and configure a Raspberry Pi for the [ARNEIS project](https://github.com/B-AROL-O/ARNEIS).

## Prerequisites

* One [Raspberry Pi](https://www.raspberrypi.org/).
  - Tested on rpi4gm35 ([Raspberry Pi 4B 4GB](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X))
* One MicroSD card of at least 4GB.
  - **IMPORTANT**: The card should be blank, or at least should not contain any important data since it will be completely erased.
  - Tested with a [SanDisk Ultra 256 GB MicroSDXC](https://www.amazon.it/SanDisk-microSDXC-adattatore-prestazioni-Rosso-Grigio/dp/B08GY8NHF2)
* One desktop PC or laptop for formatting the SD card and controlling the RPi
  - OS: A recent version of Windows or Linux or macOS
  - The PC should have a MicroSDHC card reader.
    Alternatively, an additional USB MicroSD card reader is required
* Fast internet connection

## Step-by-step instructions

### Prepare the MicroSD card with Raspberry Pi OS

Launch a browser on your laptop and open <https://www.raspberrypi.com/software/>

Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and install it on your laptop.

Insert a MicroSD card into one slot of your laptop.
Alternatively, insert the MicroSD into the USB card reader, then plug the USB card reader into one empty USB port of your laptop.

Launch the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and select the following options

* Sistema operativo: Raspberry Pi OS (32-bit)
* Scheda SD: MXT-USB Storage Device USB Device - 255.9 GB

then click "SCRIVI".

> **Attenzione**
>
> Tutti i dati esistenti in 'MXT-USB Storage Device USB Device' verranno eliminati.
> Sei sicuro di voler continuare?
>
> [NO](https://github.com/) | [SI](https://github.com/)

Click "SI".

...

> **Scrittura completata senza errori**
>
> Scrittura di **Raspberry Pi OS (32-bit)** in **MXT-USB Storage Device USB Device** completata.
>
> Ora puoi rimuovere la scheda SD dal lettore
>
> [CONTINUA](https://github.com/)

Remove the MicroSD from your laptop

### First boot of the RPi with the new MicroSD card

(2022-01-12 08:35 CET)

* Insert the MicroSD card into your Raspberry Pi.
* Connect a display using a MicroHDMI-to-HDMI cable
* Connect a USB keyboard to the first USB 2.0 port of the RPi4
* Connect a USB mouse to the second USB 2.0 port of the RPi4
* Connect a 5Vdc, 3A power supply to the USB-C port of the RPi4

Turn on the power supply and wait for Raspberry Pi OS to boot.

> **Welcome to Raspberry Pi**
>
> Welcome to the Raspberry Pi Desktop!
>
> Before you start usin it, there are a few things to set up.
>
> Press 'Next' to get started.
>
> [Cancel](https://github.com/) | [Next](https://github.com/)

Click "Next".

> **Set Country**
>
> Enter the details of your location.
> This is used to set the language, time zone, keyboard and other international settings.
>
> * Country: Italy
> * Language: Italian
> * Timezone: Rome
>
> * [x] Use English language
> * [ ] Use US keyboard
>
> Press 'Next' when you have made your selection.
>
> [Back](https://github.com/) | [Next](https://github.com/)

Fill in the form as shown above, then click "Next"

...

> **Change Password**
>
> The default 'pi' user account currently has the password 'raspberry'.
> It is strongly recommended that you change this to a different
> password that only you know
>
> * Enter new password: xxxx
> * Confirm new password: xxx
>
> * [x] Hide characters
>
> Press 'Next' to activate your new passowrd.
>
> [Back](https://github.com/) | [Next](https://github.com/)

Fill in the form as instructed, then click "Next"

> **Set Up Screen**
>
> You should be able to set the taskbar along the top of the screen.
> Tick the box if some or all of it does not fit on the screen.
>
> [ ] The taskbar does not fit one the screen
>
> The change will take effect when the Pi is restarted.
>
> Press 'Next' to save your setting.
>
> [Back](https://github.com/) | [Next](https://github.com/)

Verify and update if needed, then click "Next".

> **Select WiFi Network**
>
> Select your WiFi network from the list.
>
> ...
>
> Press 'Next' to connect, or 'Skip' to continue without connecting.
>
> [Back](https://github.com/) | [Skip](https://github.com/) | [Next](https://github.com/)

Select the desired WiFi network, then click "Next".
If the select network is protected you will be requested the password

> **Enter WiFi Network**
>
> Enter the password for the WiFi network 'xxxx'.
>
> * Password: yyyy
>
> [x] Hide characters
>
> Press 'Next' to connect, or 'Skip' to continue without connecting.
>
> [Back](https://github.com/) | [Skip](https://github.com/) | [Next](https://github.com/)

Click "Next".

> **Update Software**
>
> The operating system and applications will now be checked and
> updated if necessary. This may involve a large download.
>
> Press 'Next' ...
>
> [Back](https://github.com/) | [Skip](https://github.com/) | [Next](https://github.com/)

Click "Next".

> Download updates - please wait.

When the update is complete the following popup should be displayed

> System is up to date
>
> [OK](https://github.com/)

Click "OK" to continue.

> **Setup Complete**
>
> Your Raspberry Pi is now set up and ready to go.
>
> To run applications, click the raspberry icon
> in the top left corner of the screen to open the menu.
>
> Press 'Restart' to restart your Pi so the new settings will take effect.
>
> [Back](https://github.com/) | [Later](https://github.com/) | [Restart](https://github.com/)

Click "Restart".

Verify that the RPi reboots correctly.

![2022-01-12-1037-raspian-os-rpi4b.jpg](../images/2022-01-12-1037-raspian-os-rpi4b.jpg)


### Display assigned IP addresses

To know the IP addresses assigned to the Raspberry Pi just move the mouse over the network icon at the top right of the desktop

![2022-01-21-2123-rpios-desktop-ipaddr.png](../images/2022-01-21-2123-rpios-desktop-ipaddr.png)


### Configure hostname, SSH and VNC

<!-- (2022-01-12 10:10 CET) -->

Open a terminal and type the following command

```bash
sudo raspi-config
```

* Select "1" (System Options), then "S4" (Hostname)
* Enter hostname: `rpi4gm35` (will replace default hostname `raspberrypi`)
* Select "3" (Interface Options), then "I2" (SSH)
* Select "Yes" to enable SSH
* Select "3" (Interface Options), then "I3" (VNC)
* Select "Yes" to enable VNC
* Select "Finish" to exit `raspi-config`. Reboot if requested

Verify that the RPi is accessible from the laptop via SSH and VNC
(you may need to scan the local Wi-Fi network to get the IPv4 address assigned by the router)

HINT: To scan the network and identify the open services you can use one of those tools

- The [Fing app](https://www.fing.com/) on a mobile phone or on your laptop.
- [nmap](https://nmap.org/)

It this works disconnect the USB keyboard, mouse and display

![2022-01-12-1038-rpi4b-boxed](../images/2022-01-12-1038-rpi4b-boxed.jpg)

Reboot your RPi4 and verify that the device is still accessible from SSH:

```text
gpmacario@HW2457 MINGW64 ~
$ ssh pi@172.30.48.18
pi@172.30.48.18's password:
Linux rpi4gm35 5.10.63-v7l+ #1488 SMP Thu Nov 18 16:15:28 GMT 2021 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Jan 12 16:36:38 2022
pi@rpi4gm35:~ $
```

Do the same using a VNC client (in my case I used the free to use [VNC&reg; Viewer](https://www.realvnc.com/en/connect/download/viewer/))

![2022-01-13-1731-vnc-connect.png](../images/2022-01-13-1731-vnc-connect.png)

Double click on the selected profile to connect to the remote desktop of the Raspberry Pi:

![2022-01-13-1731-vnc-connect-rpi4gm35.png](../images/2022-01-13-1736-vnc-connect-rpi4gm35.png)

### (Recommended) Create a public DNS entry

If you have administrative rights to a DNS zone you may choose to access your Raspberry Pi using a symbolic name rather than an IP address.

If so, access your DNS administrative page (in my case, <https://register.it/>) and create an A record to map the name to the IP address assigned to your Raspberry Pi.

In my case

> `A rpi4gm35 172.30.48.18`

Wait until the DNS zone is propagated, then verify that the device can be accessed by another host (in our case, our laptop) using the assigned name rather than its IP address:

```bash
gpmacario@HW2457 MINGW64 ~
$ ping rpi4gm35.gmacario.it

Esecuzione di Ping rpi4gm35.gmacario.it [172.30.48.18] con 32 byte di dati:
Risposta da 172.30.48.18: byte=32 durata=8ms TTL=64
Risposta da 172.30.48.18: byte=32 durata=7ms TTL=64
Risposta da 172.30.48.18: byte=32 durata=6ms TTL=64
Risposta da 172.30.48.18: byte=32 durata=6ms TTL=64

Statistiche Ping per 172.30.48.18:
    Pacchetti: Trasmessi = 4, Ricevuti = 4,
    Persi = 0 (0% persi),
Tempo approssimativo percorsi andata/ritorno in millisecondi:
    Minimo = 6ms, Massimo =  8ms, Medio =  6ms

gpmacario@HW2457 MINGW64 ~
$
```

### Configure public SSH keypair

Logged in as pi@rpi4gm35, create a public/private SSH keypair:

```bash
ssh-keygen
```

Type the following commands to be able to login to your Raspberry Pi through your public SSH key - for instance:

```bash
cat <<END >>~/.ssh/authorized_keys
ssh-rsa AAAAB3Nza....W1cG35r8= gpmacario@HW2457
END
```

Test


```bash
gpmacario@HW2457 MINGW64 ~
$ ssh pi@rpi4gm35.gmacario.it
Linux rpi4gm35 5.10.92-v7l+ #1514 SMP Mon Jan 17 17:38:03 GMT 2022 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Jan 20 09:12:23 2022
pi@rpi4gm35:~ $
```


### Install Virtual Keyboard

Reference: <https://pimylifeup.com/raspberry-pi-on-screen-keyboard/>

Logged in as pi@rpi4gm35, type the following commands to setup the On-Screen Keyboard:

```bash
sudo apt update
sudo apt upgrade
sudo apt install -y matchbox-keyboard
```

Test: On the Raspberry Pi OS dashboard run

Accessories > Keyboard

![2022-01-21-1701-virtual-keyboard1.jpg](../images/2022-01-21-1701-virtual-keyboard1.jpg)

Result:

![2022-01-21-1701-virtual-keyboard2.jpg](../images/2022-01-21-1701-virtual-keyboard2.jpg)


### Install byobu

```bash
sudo apt -y install byobu
```


#### Install git and tig

```bash
sudo apt update
sudo apt -y install git tig
```

#### Install git-aware-prompt
  
<!-- (2022-01-22 17:15 CET) -->

Reference: <https://github.com/jimeh/git-aware-prompt>

Clone git-aware-prompt sources from GitHub

```bash
mkdir ~/.bash
cd ~/.bash
git clone https://github.com/jimeh/git-aware-prompt.git
```

then append the following lines to `~/.bashrc` to customize the default shell prompt:

```bash
# Configure git-aware-prompt
export GITAWAREPROMPT=~/.bash/git-aware-prompt
source "\${GITAWAREPROMPT}/main.sh"
export PS1="\${debian_chroot:+(\$debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\] \[$txtcyn\]\$git_branch\[$txtred\]\$git_dirty\[$txtrst\]\$ "
```

Logout and login for applying the changes.

Now when inside a directory versioned with git your prompt should show the branch where you are in, as in the following example

```text
pi@rpi4gm35:~/.bash/git-aware-prompt (master)$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
pi@rpi4gm35:~/.bash/git-aware-prompt (master)$
```

Notice that the `(master)` branch is part the prompt.

<!--
#### Install Github CLI

Reference: <https://lindevs.com/install-github-cli-on-raspberry-pi/>

```bash
TODO
```
-->

<!--
### Configure remote access through Visual Studio Code

TODO
-->

### Clone ARNEIS sources from GitHub

<!-- (2022-01-20 09:50 CET) -->

Logged in as pi@rpi4gm35

```bash
mkdir -p ~/github/B-AROL-O
cd ~/github/B-AROL-O
git clone https://github.com/B-AROL-O/ARNEIS.git
```

<!-- EOF -->
