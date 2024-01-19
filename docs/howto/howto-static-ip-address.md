# HOWTO Configure a Static IP Address on Linux

## Introduction

This document explains how to configure a static IP address on the Ethernet interface of a Linux host.

With recent versions of Linux distributions, the network configuration is performed with [NetworkManager](https://wiki.debian.org/NetworkManager).

Ubuntu configures networking through a higher abstraction tool called [Netplan](https://netplan.io/) which internally invokes NetworkManager as a renderer.

## Reference documents

* <https://www.baeldung.com/linux/set-static-ip-address>
* [Netplan documentation](https://netplan.readthedocs.io/)
* [NetworkManager - Debian WIki](https://wiki.debian.org/NetworkManager)
* [Ubuntu Forum: Need advice: Redoing networking on an old server?](https://ubuntuforums.org/showthread.php?t=2478425)

<!--
TODO: Integrate @OrsoEric notes from section "4a) ETH0 Static IP" of
<https://arol.atlassian.net/l/cp/01AGbw4N>

TODO: Integrate @alv67 notes from <https://arol.atlassian.net/l/cp/PSbCAVjP>
-->

## Configuring Netplan

From <https://netplan.io>:

> Netplan is a utility for easily configuring networking on a linux system.
> You simply create a YAML description of the required network interfaces and what each should be configured to do.
> From this description Netplan will generate all the necessary configuration for your chosen renderer tool.

TODO

## Configuring NetworkManager

**NOTE**: Even though NetworkManager was designed for the Gnome desktop environment, it works "just-fine" also in server editions of those OSs. Checked on the following

Vendor       | OS Name                            | network-manager | version
-------------|------------------------------------|-----------------|------------------
Canonical    | Ubuntu 22.04                       | network-manager | 1.36.6-0ubuntu2
Raspberry Pi | Raspbian GNU/Linux 10 (buster)     | dhcpd5          | 1:8.1.2-1+rpt1
Raspberry Pi | Debian GNU/Linux 11 (bullseye)     | network-manager | 1.30.6-1+deb11u1
Raspberry Pi | Debian GNU/Linux 12 (bookworm)     | network-manager | 1.42.4-1+rpt1

<!-- textlint-disable -->
<!-- TODO: Check on Red Hat Enterprise Linux 8: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/index> -->
<!-- textlint-enable -->

<!-- (2023-11-24 14:30 CET) -->

Logged in to the host which will act as `raspinstall01` execute the following commands:

```bash
sudo cp /etc/network/interfaces /etc/network/interfaces.ORIG
sudo vi /etc/network/interfaces/eth0-static
```

and write the following contents to the config file:

```text
# file:/etc/network/interfaces.d/eth0-static

# Configure static IP address for eth0
auto eth0
iface eth0 inet static
    address 172.20.0.1
    netmask 255.255.0.0

# EOF
```

Reboot `raspinstall01` to allow the changes to take effect.

Login again and verify that `eth0` was assigned the desired IP address:

```text
gmacario@raspinstall01:~ $ ip address show eth0
2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether e4:5f:01:dd:4c:0e brd ff:ff:ff:ff:ff:ff
    inet 172.20.0.1/24 brd 172.20.0.255 scope global eth0
       valid_lft forever preferred_lft forever
gmacario@raspinstall01:~ $
```

<!-- EOF -->
