# HOWTO Getting started with Foundries.io

## Introduction

This document explains how to use Foundries.io [FoundriesFactory](https://foundries.io/) cloud service.

FoundriesFactory is a cloud service to build, test, deploy, and maintain secure, updatable IoT and Edge products. It is used to customize open source software projects including u-Boot, OP-TEE, OE/Yocto Project, the Linux microPlatform™ and Docker®.

## Reference documents

* <https://foundries.io/>
* <https://docs.foundries.io/>
* <https://foundries.io/insights/news/foundriesio-arduino-secure-embedded-solution/>

## Step-by-step instructions

Browse <https://app.foundries.io/factories>

> **No Factories**
>
> Create your first Factory, and start your next product.
>
> [New Factory...](https://app.foundries.io/factories) | [Learn more](https://docs.foundries.io/latest/getting-started/signup/index.html#create-a-factory)

Click on "New Factory..."

> **Create Factory**
>
> **Choose a name for your factory**
>
> Fields marked with \* are required
>
> * **Platform** \*: Default (RaspberryPi 64-bit)
>
> * **Factory name** \*: (empty)
>   - 2 to 26 lowercase alphanumeric characters, must start with an alphanumeric character, can contain also - and _
>
> Cancel | Prev | Next

Fill in the required information

* Platform: `Default (RaspberryPi 4 64-bit)`
* Factory name: `test-fio-raspi4`

then click "Next".

> **Select a subscription plan for your factory**
>
> Pay Monthly | Pay Yearly
>
> **Free / $0 / 30-day trial**
> - No credit card required
> - For personal use
> - 3 builds a day
> - 10 managed devices
> - community support
>
> **Commercial / $5,000 / product / month**
> - For commercial use
> - Unlimited builds
> - Unlimited managed devices
> - Priority support
>
> Prices do not include taxes: we might have to collect taxes based on your billing country.
>
> Cancel | Prev | Next

Select "Free", then click "Next"

<!-- (2022-04-30 09:04 CEST) -->

<!-- markdown-link-check-disable -->
> **Almost there, review & create your factory**
>
> Fields marked with \* are required
>
> * Factory name: test-fio-raspi4
> * Factory platform: Default (RaspberryPi 4 64-bit)
> * Selected plan: Free Factory
> * Plan fee: $ 0
> * Taxes: $ 0
> * Total before taxes: $ 0
> * Total due on **Apr 30, 2022**: $ 0
>
> * [ ] I agree to the [FoundriesFactory Subscription](https://foundries.io/terms/) terms \*
>
> Cancel | Prev | Create Factory
<!-- markdown-link-check-enable -->

Review the displayed information, check "I agree", then click "Create Factory".

![2022-04-30-0911-fio-factories-test-fio-raspi4.png](../images/2022-04-30-0911-fio-factories-test-fio-raspi4.png)

If you click on tab "Targets" you will find the list of completed runs

![2022-05-11-1159-fio-targets.png](../images/2022-05-11-1159-fio-targets.png)

As an example, click on version "2" to display details

![2022-05-11-1202-fio-target-details.png](../images/2022-05-11-1202-fio-target-details.png)

If you expand the "Runs" panel

![2022-05-11-1205-fio-target-run-details.png](../images/2022-05-11-1205-fio-target-run-details.png)

You may also click on each artifact to display its contents.

Click on tab "Devices" to display the list of registered devices.

Install the `fioctl` tool following the instructions at <https://docs.foundries.io/latest/getting-started/install-fioctl/index.html> - for instance, on Linux

```bash
export FIOCTL_VERSION=v0.25
sudo curl -o /usr/local/bin/fioctl -LO https://github.com/foundriesio/fioctl/releases/download/$FIOCTL_VERSION/fioctl-linux-amd64
sudo chmod +x /usr/local/bin/fioctl
```

Verify the correct installation of `fioctl`

```text
gmacario@hw2228:~ $ fioctl
Manage Foundries Factories

Usage:
  fioctl [command]

Available Commands:
  completion       Generate completion script
  config           Manage configuration common to all devices in a factory
  configure-docker Configure a hub.foundries.io Docker credential helper
  devices          Manage devices registered to a factory
  event-queues     Manage event queues configured for a Factory
  help             Help about any command
  keys             Manage keys in use by your factory fleet
  login            Access Foundries.io services with your client credentials
  logout           Remove Foundries.io client credentials from system
  secrets          Manage secret crendentials configured in a factory
  status           Get dashboard view of a factory and its devices
  targets          Manage factory's TUF targets
  teams            List teams belonging to a FoundriesFactory
  users            List users with access to a FoundriesFactory
  version          Show version information of this tool.
  waves            Manage factory's waves

Flags:
  -c, --config string   config file (default is $HOME/.config/fioctl.yaml)
  -h, --help            help for fioctl
  -v, --verbose         Print verbose logging

Use "fioctl [command] --help" for more information about a command.
gmacario@hw2228:~ $
```

<!-- EOF -->
