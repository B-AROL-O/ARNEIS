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

## Installing `rclone`

The page at <https://rclone.org/install/> provide detailed instructions for installing `rclone` under many Operating Systems and HW architectures.

The following sections detail the results performing the installation on some relevant hosts.

### Install rclone on Ubuntu 22.04.3 LTS

(Tested on host HW2228)

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

A more recent version of `rclone` (1.64.0 as of 2023-11-05) is available via [snap](https://snapcraft.io/docs/installing-snap-on-ubuntu), therefore let us install `rclone` with the following command:

```text
sudo snap install rclone
```

Verify that the installation was performed correctly:

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

### Installing rclone on Windows 10 Pro

(Tested on host ALPHA)

Download the installation file for the Windows OS from <https://rclone.org/downloads/> (as of 2023-11-05 this is `rclone-v1.64.2-windows-amd64.zip`),
then uncompress the `.zip` archive and copy the `rclone.exe` file into a directory listed in the `PATH` environment variable.

You may verify that the installation was performed successfully by typing `rclone --version` from the command-line prompt.

Example (from Git bash)

```text
gmaca@alpha MINGW64 ~
$ which rclone
/c/Users/gmaca/bin/rclone

gmaca@alpha MINGW64 ~
$ rclone --version
rclone v1.64.2
- os/version: Microsoft Windows 10 Pro 22H2 (64 bit)
- os/kernel: 10.0.19045.3636 (x86_64)
- os/type: windows
- os/arch: amd64
- go/version: go1.21.3
- go/linking: static
- go/tags: cmount

gmaca@alpha MINGW64 ~
$
```

## Configuring rclone for Cubbit DS3

After the `rclone` tool has been installed it must be configured in order to access the data stored on Cubbit DS3.

**NOTE**: A similar procedure can be used to configure rclone for other object storage backends, for instance [Amazon Simple Storage Service (Amazon S3)](https://aws.com/s3) or [Azure Blob Storage](https://azure.microsoft.com/products/storage/blobs/).

### Create Access Key ID and Secret for Cubbit DS3

Login to Cubbit DS3 Object Storage from <https://www.cubbit.io/it/log-in>

From your Workspace click "Settings > API keys", then click "+ Generate new client API key"

![2023-11-05-cubbit-ds-create-access-key.png](../images/2023-11-05-cubbit-ds-create-access-key.png)

Accept the proposed key name, or change it if you prefer, then click "Download .csv".
This file contains the Access key ID and Secret access key which will be used to configure a S3 client application such as [S3 Browser](https://s3browser.com/).

### Run `rclone config`

Prerequisite: `snap` installed as detailed in the previous chapter.

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

## Some useful `rclone` commands

### List files in a bucket

```bash
rclone ls cubbit:${BUCKET_NAME}
```

Example result:

```text
gmacario@hw2228:~$ rclone ls cubbit:baroloteam
  4985990 IMG_20230826_124002_1.jpg
  4421972 IMG_20230826_124009_1.jpg
    64546 newplot.png
gmacario@hw2228:~$
```

An error is returned if the bucket does not exist or we have no access:

```text
gmacario@hw2228:~$ rclone ls cubbit:newbucket
2023/11/05 11:05:33 Failed to ls: LambdaRuntimeError: Forbidden
        status code: 403, request id: , host id:
gmacario@hw2228:~$
```

**NOTE**: The `rclone ls` command has a number of useful options which may be discovered with the `rclone ls --help` command:

```text
gmacario@hw2228:~$ rclone ls --help

Lists the objects in the source path to standard output in a human
readable format with size and path. Recurses by default.

Eg

    $ rclone ls swift:bucket
        60295 bevajer5jef
        90613 canole
        94467 diwogej7
        37600 fubuwic


Any of the filtering options can be applied to this command.

There are several related list commands

  * `ls` to list size and path of objects only
  * `lsl` to list modification time, size and path of objects only
  * `lsd` to list directories only
  * `lsf` to list objects and directories in easy to parse format
  * `lsjson` to list objects and directories in JSON format

`ls`,`lsl`,`lsd` are designed to be human-readable.
`lsf` is designed to be human and machine-readable.
`lsjson` is designed to be machine-readable.

Note that `ls` and `lsl` recurse by default - use `--max-depth 1` to stop the recursion.

The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default - use `-R` to make them recurse.

Listing a nonexistent directory will produce an error except for
remotes which can't have empty directories (e.g. s3, swift, or gcs -
the bucket-based remotes).

Usage:
  rclone ls remote:path [flags]

Flags:
  -h, --help   help for ls


# Filter Flags

Flags for filtering directory listings.

      --delete-excluded                     Delete files on dest excluded from sync
      --exclude stringArray                 Exclude files matching pattern
      --exclude-from stringArray            Read file exclude patterns from file (use - to read from stdin)
      --exclude-if-present stringArray      Exclude directories if filename is present
      --files-from stringArray              Read list of source-file names from file (use - to read from stdin)
      --files-from-raw stringArray          Read list of source-file names from file without any processing of lines (use - to read from stdin)
  -f, --filter stringArray                  Add a file filtering rule
      --filter-from stringArray             Read file filtering patterns from a file (use - to read from stdin)
      --ignore-case                         Ignore case in filters (case insensitive)
      --include stringArray                 Include files matching pattern
      --include-from stringArray            Read file include patterns from file (use - to read from stdin)
      --max-age Duration                    Only transfer files younger than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --max-depth int                       If set limits the recursion depth to this (default -1)
      --max-size SizeSuffix                 Only transfer files smaller than this in KiB or suffix B|K|M|G|T|P (default off)
      --metadata-exclude stringArray        Exclude metadatas matching pattern
      --metadata-exclude-from stringArray   Read metadata exclude patterns from file (use - to read from stdin)
      --metadata-filter stringArray         Add a metadata filtering rule
      --metadata-filter-from stringArray    Read metadata filtering patterns from a file (use - to read from stdin)
      --metadata-include stringArray        Include metadatas matching pattern
      --metadata-include-from stringArray   Read metadata include patterns from file (use - to read from stdin)
      --min-age Duration                    Only transfer files older than this in s or suffix ms|s|m|h|d|w|M|y (default off)
      --min-size SizeSuffix                 Only transfer files bigger than this in KiB or suffix B|K|M|G|T|P (default off)

# Listing Flags

Flags for listing directories.

      --default-time Time   Time to show if modtime is unknown for files and directories (default 2000-01-01T00:00:00Z)
      --fast-list           Use recursive list if available; uses more memory but fewer transactions


Additional help topics:

Use "rclone [command] --help" for more information about a command.
Use "rclone help flags" for to see the global flags.
Use "rclone help backends" for a list of supported services.
gmacario@hw2228:~$
```

### Sync a local folder to a bucket on Cubbit DS3

```bash
rclone sync -P ./backup-folder cubbit:${BUCKET_NAME}
```

Note that `BUCKET_NAME` must exist otherwise the command will fail (it may be created from <https://console.cubbit.eu/>)

On the other hand, if you sync files to a subfolder of a bucket, the subfolder will be created automatically if it does not exist.

#### Example 1

```text
gmacario@gmpowerhorse:~ $ rclone sync -P ~/Downloads cubbit:bk-gmpowerhorse/test02
Transferred:      146.829M / 146.829 MBytes, 100%, 7.582 MBytes/s, ETA 0s
Errors:                 0
Checks:                 0 / 0, -
Transferred:           17 / 17, 100%
Elapsed time:       19.3s
gmacario@gmpowerhorse:~ $
```

#### Example 2

<!-- (2023-11-07 22:52 CET) -->

```bash
cd ~/Dropbox/Cubbit_MIRROR/CUBBIT_SHARED/SHARED_WITH_BAROLOTEAM
rclone sync -P . cubbit:baroloteam-from-dropbox
```

Result:

```text
gmaca@alpha MINGW64 ~/Dropbox/Cubbit_MIRROR/CUBBIT_SHARED/SHARED_WITH_BAROLOTEAM
$ rclone sync -P . cubbit:baroloteam-from-dropbox
Transferred:        4.945 GiB / 4.945 GiB, 100%, 117.173 KiB/s, ETA 0s
Transferred:          724 / 724, 100%
Elapsed time:      33m8.1s

gmaca@alpha MINGW64 ~/Dropbox/Cubbit_MIRROR/CUBBIT_SHARED/SHARED_WITH_BAROLOTEAM
$
```

#### Example 3

<!-- (2023-11-09 20:23 CET) -->

```bash
cd ~/Dropbox/Cubbit_MIRROR
rclone sync -P . cubbit:mirror-from-dropbox
```

Result:

```text
gmaca@alpha MINGW64 ~/Dropbox/Cubbit_MIRROR
$ rclone sync -P . cubbit:mirror-from-dropbox
...
2023/11/09 22:21:17 ERROR : Win10-images/Win10_21H1_Italian_x64.iso: Failed to copy:
multi-thread copy: failed to open source: The file cannot be accessed by the system.
2023/11/09 22:21:18 ERROR : ARCHIVE/2023-07-15-google-takeout/Tutti i messaggi compre
si Spam e Cestino-005.mbox: Failed to copy: multi-thread copy: failed to open source:
 The file cannot be accessed by the system.
Transferred:        3.285 GiB / 211.470 GiB, 2%, 241.274 KiB/s, ETA 1w3d11h
Errors:                 4 (retrying may help)
Checks:              3292 / 5125, 64%
Transferred:          295 / 2853, 10%
Elapsed time:    2h2m18.9s
Checking:
 * CUBBIT_SHARED/SHARED_W…30830_17_02_10_Pro.jpg: checking
 * CUBBIT_SHARED/SHARED_W…30830_17_02_11_Pro.jpg: checking
 * CUBBIT_SHARED/SHARED_W…30830_17_02_12_Pro.jpg: checking
 * CUBBIT_SHARED/SHARED_W…30830_17_20_12_Pro.jpg: checking
 * CUBBIT_SHARED/SHARED_W…30830_17_20_13_Pro.jpg: checking
 * CUBBIT_SHARED/SHARED_W…30830_17_20_16_Pro.jpg: checking
 * CUBBIT_SHARED/SHARED_W…30830_17_20_22_Pro.jpg: checking
 * CUBBIT_SHARED/SHARED_W…30830_17_20_23_Pro.jpg: checking
Transferring:
 * ARCHIVE/2023-07-15-goo…230715T062408Z-003.zip:  0% /1.984Gi, 9.408Ki/s, 60h48m14
 * ARCHIVE/2023-07-15-goo…230715T062408Z-004.zip:  1% /1.611Gi, 46.785Ki/s, 9h54m17
 * warez/2019-09-04-solid…dWorks 2018.part01.rar:  3% /1Gi, 45.942Ki/s, 6h5m31s
 * warez/2019-09-04-solid…dWorks 2018.part02.rar:  1% /1Gi, 87.172Ki/s, 3h16m33s


gmaca@alpha MINGW64 ~/Dropbox/Cubbit_MIRROR
$
```

TODO

### Backup files from gmpowerhorse (Ubuntu 20.04.6 LTS)

Prerequisites:

* Bucket already created from <https://console.cubbit.eu/>
  * Bucket name: `bk-gmpowerhorse`
  * Bucket versioning: Versioning disabled
  Object Lock: Object Lock disable
  * Ownership Control: Object writer
* Cubbit DS3 API key saved in a `.csv` file

Install rclone using apt

```bash
sudo apt install rclone
```

Check installed version

```text
gmacario@gmpowerhorse:~ $ rclone --version
rclone v1.50.2
- os/arch: linux/amd64
- go version: go1.13.8
gmacario@gmpowerhorse:~ $
```

Type the following command to make sure you can access bucket `bk-gmpowerhorse`:

```bash
rclone ls cubbit:bk-gmpowerhorse
```

Result:

```text
gmacario@gmpowerhorse:~ $ rclone ls cubbit:bk-gmpowerhorse
gmacario@gmpowerhorse:~ $
```

Now use rclone to synchronize contents of folder `~/Downloads` to bucket `bk-gmpowerhorse` on Cubbit DS3:

```bash
rclone sync -P ~/Downloads cubbit:bk-gmpowerhorse
```

Result:

```text
gmacario@gmpowerhorse:~ $ rclone sync -P ~/Downloads cubbit:bk-gmpowerhorse
Transferred:      146.829M / 146.829 MBytes, 100%, 7.824 MBytes/s, ETA 0s
Errors:                 0
Checks:                 0 / 0, -
Transferred:           17 / 17, 100%
Elapsed time:       18.7s
gmacario@gmpowerhorse:~ $
```

Now check from `gmacario@hw2228` that all the files have been transferred:

```text
gmacario@hw2228:~$ rclone ls cubbit:bk-gmpowerhorse
gmacario@hw2228:~$ rclone ls cubbit:bk-gmpowerhorse
 80609819 CLI_Linux_Debian_5.5.2.zip
 53237226 FingKit_CLI_Linux_Debian.zip
  1572864 bios-gmpowerhorse/BIOS_CD/7F5_0146.iso
  1048576 bios-gmpowerhorse/DOS_Flash/7F5_0146.bin
    27660 bios-gmpowerhorse/DOS_Flash/ASSIGNPW.EXE
     2841 bios-gmpowerhorse/DOS_Flash/DOSFM.txt
    54441 bios-gmpowerhorse/DOS_Flash/FLASHBIN.EXE
     3102 bios-gmpowerhorse/DOS_Flash/Flashbin.txt
     1003 bios-gmpowerhorse/DOS_Flash/README.TXT
     3388 bios-gmpowerhorse/DOS_Flash/flsh.cpu
     2957 bios-gmpowerhorse/README
    18746 bios-gmpowerhorse/hp-lxbios-1.5-1.i386.rpm
    13894 bios-gmpowerhorse/hp-lxbios-mod-1.5-1_2.6.9.67.ELsmp.src.rpm
    48836 bios-gmpowerhorse/lxbios_readme.pdf
      411 iottly-device-agent.service
 16079382 iottlyagent_1.6.4_linux_AMD64.tar.gz
  1235710 sp59252.tgz
gmacario@hw2228:~$
```

<!-- (2023-11-09 20:25 CET) -->

Command:

```bash
cd
rclone sync -P ~/Downloads cubbit:bk-gmpowerhorse
```

Result>

```text
gmacario@gmpowerhorse:~ $ rclone sync -P . cubbit:bk-gmpowerhorse/home_gmacario
...
2023-11-09 23:34:43 ERROR : S3 bucket bk-gmpowerhorse path home_gmacario: not deleting files as there were IO errors
2023-11-09 23:34:43 ERROR : S3 bucket bk-gmpowerhorse path home_gmacario: not deleting directories as there were IO errors
2023-11-09 23:34:43 ERROR : Attempt 3/3 failed with 17 errors and: failed to open source object: open /home/gmacario/github/gmacario/hassio-gmpowerhorse/config/.storage/core.uuid: permission denied
Transferred:      414.161M / 414.161 MBytes, 100%, 81.090 kBytes/s, ETA 0s
Errors:                17 (retrying may help)
Checks:             99165 / 99165, 100%
Transferred:        13571 / 13571, 100%
Elapsed time:   1h27m9.9s
2023/11/09 23:34:43 Failed to sync with 17 errors: last error was: failed to open source object: open /home/gmacario/github/gmacario/hassio-gmpowerhorse/config/.storage/core.uuid: permission denied
gmacario@gmpowerhorse:~ $
```

TODO

<!-- EOF -->