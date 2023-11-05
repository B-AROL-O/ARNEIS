# HOWTO Use rclone with Cubbit DS3

## Executive Summary

This guide explains how to use the [rclone](https://rclone.org/) tool to access contents and backup data inside a bucket on [Cubbit DS3 Object Storage](https://www.cubbit.io/).

## Reference Documents

* [Rclone landing page](https://rclone.org/)
* [GitHub: rclone/rclone](https://github.com/rclone/rclone)
* [Cubbit docs > Integrations > Rclone](https://docs.cubbit.io/integrations/rclone)

## Introduction to `rclone`

Rclone ("_rsync for cloud storage_") is a command-line program to sync files and directories to and from different cloud storage providers.

From <https://rclone.org/>:

> Rclone is a command-line program to manage files on cloud storage. It is a feature-rich alternative to cloud vendors' web storage interfaces.
> [Over 70 cloud storage products](https://rclone.org/#providers) support rclone including S3 object stores, business & consumer file storage services, as well as standard transfer protocols.

Official instructions for using rclone with Cubbit DS3 are available at <https://docs.cubbit.io/integrations/rclone>

## Installing rclone

Follow the instructions at <https://rclone.org/install/>.
The following sections detail the results performing the installation on some relevant hosts.

### Install `rclone` on hw2228 (Ubuntu 22.04.3 LTS)

Check if rclone is already installed:

```text
gmacario@hw2228:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
gmacario@hw2228:~$ rclone
Command 'rclone' not found, but can be installed with:
sudo snap install rclone  # version 1.64.0, or
sudo apt  install rclone  # version 1.53.3-4ubuntu1.22.04.2
See 'snap info rclone' for additional versions.
gmacario@hw2228:~$
```

Let us install rclone 1.64.0 via snap

```text
sudo snap install rclone
```

Check:

```text
gmacario@hw2228:~$ rclone version
rclone v1.64.0
- os/version: ubuntu 22.04 (64 bit)
- os/kernel: 6.2.0-36-generic (x86_64)
- os/type: linux
- os/arch: amd64
- go/version: go1.21.1
- go/linking: static
- go/tags: snap
gmacario@hw2228:~$
```

### Configure rclone for Cubbit DS3

Run the `rclone config` command and type the following options
(you must replace `************` with the values from the `.csv` file)

```bash
n                     # e/n/d/r/c/s/q> (New remote)
cubbit                # name> (Enter name for new remote.)
5                     # Storage> (Amazon S3 Compliant Storage Provider)
29                    # provider> (Any other S3 compatible provider)
1                     # env_auth> (Enter AWS credentials in the next step)
************          # access_key_id>
************          # secret_access_key>
eu-west-1             # region>
https://s3.cubbit.eu  # endpoint> (Required when using an S3 clone.)
                      # location_constraint> (Press Enter to leave empty)
1                     # acl> (Owner gets FULL_CONTROL.No one else has access rights (default).(private))
n                     # Edit advanced config?
y                     # y/e/d> (Yes this is OK)
q                     # e/n/d/r/c/s/q> (Quit config)
```

Once the `rclone config` command is complete the following command dumps the config file as JSON:

```bash
rclone config dump
```

TODO

<!-- EOF -->