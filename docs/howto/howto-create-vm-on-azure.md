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

<!-- EOF -->
