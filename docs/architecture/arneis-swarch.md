# ARNEIS - Software Architecture

This document details the planned Software Architecture that will be developed for the ARNEIS project.

The software architecture of the ARNEIS project will be based on microservices running on the [ARNEIS Kubernetes cluster](https://arneis.readthedocs.io/en/latest/howto/howto-install-k3s-for-arneis.html).

<!-- TODO: Add reference documents -->

<!-- TODO: Add links to definitions and acronyms -->

## Architecture of the ARNEIS cluster

<!-- TODO: Add diagram -->

The ARNEIS cluster is based on [Kubernetes](https://kubernetes.io/).

For simplicity we chose to deploy the ARNEIS cluster using [K3s](https://k3s.io/).

K3s (or “Lightweight Kubernetes”) is a simplified installation of the Kubernetes distribution built for IoT and Edge computing.

K3s is an Open Source project started and maintained by [Rancher.com](https://rancher.com/) (now part of [SUSE](https://www.suse.com/)).

### Planned topology of the ARNEIS K3s cluster

#### Server Node[s]

1. VM arneis-vm01
2. (optional) 2x additional VM to provide High Availability?

#### Agent Nodes

1. The same host acting as main K3s server (primary agent)
2. VM arneis-vm02 on the cloud
3. RPi4 on each instance of ARNEIS edge system

## Services to be deployed on the ARNEIS cluster

The following services are expected to be deployed on the ARNEIS cluster:

* Terminate HTTPS ([Traefik Proxy](https://traefik.io/) instance built into K3s)
* Web server for ARNEIS documentation (replica of <https://arneis.readthedocs.io>)
* Database for ARNEIS backend service (alternative: [MongoDB](https://www.mongodb.com/) instance at <https://www.mongodb.com/cloud/atlas/>)
* ARNEIS backend service ([Node.js](https://nodejs.org/) + [Koa](https://koajs.com/) - possibly based on some publicly available boilerplate)
* ARNEIS customer frontend (static site developed in [Next.js](https://nextjs.org/))
* Service running on the RPi4 for controlling the [OAK-D-Lite](https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9095.html) (Python3?)
* Service running on the RPi4 for controlling the [LEGO&reg; Technics Bluetooth Hub](https://www.bricklink.com/v2/catalog/catalogitem.page?P=bb0961c01&idColor=86#T=C&C=86) (Python3?)

<!-- EOF -->
