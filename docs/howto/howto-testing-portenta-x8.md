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

Logged in as `root@portenta-x8` from the shell accessible from the web interface

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

Result: TODO

### Inspect the host OS on the Portenta X8

From a laptop connected on the same network (172.30.48.0/24)

```text
gpmacario@HW2457 MINGW64 ~
$ ssh fio@172.30.48.28
fio@172.30.48.28's password:
fio@portenta-x8-a13b209dab6fad9:~$
```

Now logged as `fio@portenta-x8-xxxx`, inspect the host OS

```bash
uname -a
cat /etc/os-release
cat /proc/cpuinfo
free -h
```

Result:

```text
fio@portenta-x8-a13b209dab6fad9:~$ uname -a
Linux portenta-x8-a13b209dab6fad9 5.4.134-lmp-standard #1 SMP PREEMPT Tue Jul 20 21:09:28 UTC 2021 aarch64 aarch64 aarch64 GNU/Linux
fio@portenta-x8-a13b209dab6fad9:~$ cat /etc/os-release
ID=lmp-xwayland
NAME="Linux-microPlatform XWayland"
VERSION="3.3.2-391-83-21-g3ad61e0"
VERSION_ID=3.3.2-391-83-21-g3ad61e0
PRETTY_NAME="Linux-microPlatform XWayland 3.3.2-391-83-21-g3ad61e0"
HOME_URL="https://foundries.io/"
SUPPORT_URL="https://support.foundries.io/"
LMP_MACHINE="portenta-x8"
LMP_FACTORY="arduino"
LMP_FACTORY_TAG="devel"
fio@portenta-x8-a13b209dab6fad9:~$ cat /proc/cpuinfo
processor       : 0
BogoMIPS        : 16.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 4

processor       : 1
BogoMIPS        : 16.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 4

processor       : 2
BogoMIPS        : 16.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 4

processor       : 3
BogoMIPS        : 16.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 4

fio@portenta-x8-a13b209dab6fad9:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           1.9Gi       308Mi       1.3Gi        26Mi       343Mi       1.6Gi
Swap:          1.9Gi          0B       1.9Gi
fio@portenta-x8-a13b209dab6fad9:~$
```

Inspect disk utilization

```bash
df -h
```

Result:

```text
fio@portenta-x8-a13b209dab6fad9:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           976M   26M  950M   3% /run
devtmpfs        651M     0  651M   0% /dev
/dev/mmcblk2p2   14G  2.1G   11G  16% /sysroot
tmpfs           976M     0  976M   0% /dev/shm
tmpfs           4.0M     0  4.0M   0% /sys/fs/cgroup
tmpfs           976M     0  976M   0% /tmp
tmpfs           976M   12K  976M   1% /var/volatile
/dev/mmcblk2p1   84M   28K   83M   1% /var/rootdirs/mnt/boot
tmpfs           196M     0  196M   0% /run/user/63
overlay          14G  2.1G   11G  16% /var/lib/docker/overlay2/71bfdab5583038b5068957a0ac6808c843636759bd1e8e23610686a294748ec5/merged
overlay          14G  2.1G   11G  16% /var/lib/docker/overlay2/ebf99a4712b01bd0d3e6a27f6c4f7b1dda3c1018f4abe2598b083240d29b9875/merged
fio@portenta-x8-a13b209dab6fad9:~$
```

Inspect the network interfaces

```bash
ip addr
```

Result:

```text
fio@portenta-x8-a13b209dab6fad9:~$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
3: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether 6e:4f:24:e2:aa:4b brd ff:ff:ff:ff:ff:ff
4: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 74:7a:90:ce:f3:94 brd ff:ff:ff:ff:ff:ff
    inet 172.30.48.28/24 brd 172.30.48.255 scope global dynamic noprefixroute wlan0
       valid_lft 598757sec preferred_lft 598757sec
    inet6 fe80::d422:768c:a623:311d/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
5: can0: <NOARP,ECHO> mtu 16 qdisc noop state DOWN group default qlen 10
    link/can
6: can1: <NOARP,ECHO> mtu 16 qdisc noop state DOWN group default qlen 10
    link/can
7: usb0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 46:f2:7f:29:29:18 brd ff:ff:ff:ff:ff:ff
    inet 192.168.7.1/24 brd 192.168.7.255 scope global noprefixroute usb0
       valid_lft forever preferred_lft forever
    inet6 fe80::67f4:afe1:2c7d:abe8/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
8: usb1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 32:f2:98:46:1b:c2 brd ff:ff:ff:ff:ff:ff
    inet 192.168.8.1/24 brd 192.168.8.255 scope global noprefixroute usb1
       valid_lft forever preferred_lft forever
    inet6 fe80::f0db:a7c1:d850:58d8/64 scope link tentative noprefixroute
       valid_lft forever preferred_lft forever
9: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:b0:7b:86:28 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
10: br-9a0e17781cd2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:59:99:dc:7b brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-9a0e17781cd2
       valid_lft forever preferred_lft forever
    inet6 fe80::42:59ff:fe99:dc7b/64 scope link
       valid_lft forever preferred_lft forever
12: veth7267f54@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-9a0e17781cd2 state UP group default
    link/ether 9a:a2:8f:91:28:58 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::98a2:8fff:fe91:2858/64 scope link
       valid_lft forever preferred_lft forever
14: veth68241db@if13: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-9a0e17781cd2 state UP group default
    link/ether 5a:a7:6c:72:19:e6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::58a7:6cff:fe72:19e6/64 scope link
       valid_lft forever preferred_lft forever
fio@portenta-x8-a13b209dab6fad9:~$
```

Inspect Docker

```bash
docker version
docker info
docker images
docker ps -a
```

Result:

```text
fio@portenta-x8-a13b209dab6fad9:~$ docker version
Client:
 Version:           20.10.7
 API version:       1.41
 Go version:        go1.16.7
 Git commit:        e9b8231d6a
 Built:             Tue Feb 15 18:02:50 2022
 OS/Arch:           linux/arm64
 Context:           default
 Experimental:      true

Server:
 Engine:
  Version:          20.10.7
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.7
  Git commit:       013d6655bb0f4c86bcd9d48372ef67afd0ded65e
  Built:            Tue Feb 15 18:01:38 2022
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          v1.5.4-12-g1c13c54ca.m
  GitCommit:        1c13c54cae4f53510a7a45ae3e4af49030a76193.m
 runc:
  Version:          1.0.0-rc95+dev
  GitCommit:        bfcbc947d5d11327f2680047e2e6e94f4ee93d2a-dirty
 docker-init:
  Version:          0.19.0
  GitCommit:        b9f42a0-dirty
fio@portenta-x8-a13b209dab6fad9:~$ docker info
Client:
 Context:    default
 Debug Mode: false

Server:
 Containers: 2
  Running: 2
  Paused: 0
  Stopped: 0
 Images: 2
 Server Version: 20.10.7
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: journald
 Cgroup Driver: cgroupfs
 Cgroup Version: 1
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: runc io.containerd.runc.v2 io.containerd.runtime.v1.linux
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c13c54cae4f53510a7a45ae3e4af49030a76193.m
 runc version: bfcbc947d5d11327f2680047e2e6e94f4ee93d2a-dirty
 init version: b9f42a0-dirty (expected: de40ad007797e)
 Security Options:
  seccomp
   Profile: default
 Kernel Version: 5.4.134-lmp-standard
 Operating System: Linux-microPlatform XWayland 3.3.2-391-83-21-g3ad61e0
 OSType: linux
 Architecture: aarch64
 CPUs: 4
 Total Memory: 1.905GiB
 Name: portenta-x8-a13b209dab6fad9
 ID: 6YE7:I5FE:OINP:4YR2:ZMSQ:CC24:GZVF:QRDX:PB3V:KDQO:XMDL:OQFJ
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false

fio@portenta-x8-a13b209dab6fad9:~$ docker images
REPOSITORY                                      TAG       IMAGE ID       CREATED       SIZE
hub.foundries.io/arduino/python-devel-arduino   <none>    60de54fcb301   2 weeks ago   268MB
hub.foundries.io/arduino/go-webapp-arduino      <none>    495e2e950a62   2 weeks ago   127MB
fio@portenta-x8-a13b209dab6fad9:~$ docker ps -a
CONTAINER ID   IMAGE                                           COMMAND            CREATED         STATUS      PORTS                                   NAMES
49c117163405   hub.foundries.io/arduino/go-webapp-arduino      "/entrypoint.sh"   13 months ago   Up 5 days   0.0.0.0:80->1323/tcp, :::80->1323/tcp   x8-setup
782933c5d575   hub.foundries.io/arduino/python-devel-arduino   "/entrypoint.sh"   13 months ago   Up 5 days                                           x8-devel
fio@portenta-x8-a13b209dab6fad9:~$
```

<!-- EOF -->
