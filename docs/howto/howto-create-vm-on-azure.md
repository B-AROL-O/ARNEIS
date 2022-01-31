# HOWTO Create a VM on Azure for the ARNEIS project

## Introduction

This document details how to create a Virtual Machine on [Microsoft Azure](https://azure.microsoft.com/) cloud that will be used for the [ARNEIS](https://github.com/b-arol-o/arneis) project.

## Step-by-step instructions

### Create a VM using the web interface

- Login to <http://portal.azure.com> using your Azure credentials

- Click on **Virtual Machines**.\

- Click on **+ Create**

- You will have 2 options: **Virtual Machine** or **Start with a preset configuration**

- We started with _Virtual Machine_

  ![image](https://user-images.githubusercontent.com/51110452/151772083-4b618e60-7141-4503-8560-4ecc4fc3b214.png)

- Set Subscription to **Azure Pass - Sponsorship** and Group to **Arneis-rg** as Arneis Resource Group.

  ![image](https://user-images.githubusercontent.com/51110452/151772456-3480cbc5-a8c4-4e4a-a692-0f8c3973d095.png)

- Choose the **Virtual machine name** as arneis-vm01

- Select **Region**

- No **Redundancy**

- Choose **Security type**

- Add your public SSH key if you have one, otherwise let Azure automatically generate one for you.

  Result:

  ![image](https://user-images.githubusercontent.com/51110452/151773952-0e301a1b-f51b-472c-9836-8d4760c69efc.png)

- Review and accept the default values in the following pages: **Disks**, **Networking**, **Management** and **Advanced**.

Now you just have to wait for the deployment to complete:

![image](https://user-images.githubusercontent.com/51110452/151774378-89350506-a4d9-4a03-9efb-e0cd6747f604.png)

### Test the VM

After the machine is deployed, and you got the correct IP address, you can connect to it through SSH and run:

```bash
htop
```

![image](https://user-images.githubusercontent.com/51110452/151774694-89f4b84d-ce23-4d19-ab25-b5ba9854838e.png)

### (Recommmended) Create a public DNS entry

If you have administrative rights to a DNS zone you may choose to access your VM using a symbolic name rather than an IP address.

If so, access your DNS administrative page (in my case, <https://register.it/>) and create an A record to map the name to the IP address assigned to your Raspberry Pi.

In my case

```text
A arneis01 20.124.132.35
```

Wait until the DNS zone is propagated, then verify that the device can be accessed by another host (in our case, our laptop) using the assigned name rather than its IP address:

```text
gmaca@alpha MINGW64 ~
$ ssh -i ~/.ssh/gmacario-gmail-com azureuser@arneis-vm01.gmacario.it
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.11.0-1027-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Jan 31 17:52:17 UTC 2022

  System load:  0.0               Processes:             155
  Usage of /:   9.8% of 28.90GB   Users logged in:       1
  Memory usage: 7%                IPv4 address for cni0: 10.42.0.1
  Swap usage:   0%                IPv4 address for eth0: 10.0.0.4

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


*** System restart required ***
Last login: Mon Jan 31 17:51:47 2022 from 93.43.242.87
azureuser@arneis-vm01:~$
```

<!-- EOF -->
