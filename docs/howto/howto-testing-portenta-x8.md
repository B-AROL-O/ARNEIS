# HOWTO Testing Arduino Portenta X8

## Press coverage

* <https://www.electronicsweekly.com/news/sponsored-content-report-highlights-demand-industry-led-iot-security-guidelines-2022-04/>

## Documentation

* [Portenta X8 Getting Started (Beta)](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box)
  - Sources: <https://github.com/arduino/docs-content/commits/main/content/hardware/04.pro/boards/portenta-x8/tutorials/out-of-the-box/content.md>
  - docs-content/pull/159: [Portenta X8: Getting Started update [PC-889]](https://github.com/arduino/docs-content/pull/159)
* [foundries.io](https://foundries.io/)
  - <https://foundries.io/company/partners/arduino/>
* [docs.foundries.io](https://docs.foundries.io/latest/index.html)
  - [Supported Boards](https://docs.foundries.io/latest/reference-manual/boards/boards.html)

## First experiences with Portenta X8

- Connect the patch antenna to the Portenta X8 uFL connector
- Connect the Portenta X8 to a laptop using a USB-A to USB-C cable
- Wait until the upper LED turns green

<!-- markdown-link-check-disable-next-line -->
Browse <http://192.168.7.1/>

<!-- markdown-link-check-disable -->
> Welcome to the **Arduino Portenta X8**
>
> Setup your board to get started
>
> * Configure Wi-Fi
> * Register Factory name
>
> [GO TO DOCUMENTATION](https://docs.arduino.cc/hardware/portenta-x8)
>
> [BOARD INFO](http://192.168.7.1/)
<!-- markdown-link-check-enable -->

Click on "BOARD INFO"

<!-- markdown-link-check-disable -->
> **BOARD INFO**
>
> * Hostname: `PORTENTA-X8-A13B209DAB6FAD9`
> * Wi-Fi: `AROLIOT`
> * Ethernet: `USBRNDIS`
> * Factory: [->](https://www.arduino.cc/x8-registerarolred)
>
> [LAUNCH SHELL](http://192.168.7.1/#/shell)
>
> [GO TO ARDUINO CLOUD](https://cloud.arduino.cc/)
<!-- markdown-link-check-enable -->

Expand "AROLIOT"

> * Hostname: `portenta-x8-a13b209dab6fad9`
> * IPv4: `172.30.48.28/24`
> * MAC: `74:7A:90:CE:F3:94`

Expand "USBRNDIS"

> * Hostname: `portenta-x8-a13b209dab6fad9`
> * IPv4: `192.168.7.1/24`
> * MAC: `32:2E:E3:05:3D:31`

Click on "LAUNCH SHELL"

```text
To list installed python packages
pip3 list

To add a package
apk add <packagename>

To explore list of available packages
https://pkgs.alpinelinux.org/packages

Arduino Portenta-X8 documentation under
https://docs.arduino.cc/hardware/portenta-x8


portenta-x8:~#
```

### Clone ARNEIS sources from GitHub

Logged in as `root@portenta-x8`

```bash
apk add git
git clone https://github.com/B-AROL-O/ARNEIS
```

### Build ARNEIS documentation

Build ARNEIS documentation from sources in `docs/`:

```bash
cd ~/ARNEIS/docs
pip install -r requirements.txt
apk add make
make html
```

TODO

<!-- EOF -->
