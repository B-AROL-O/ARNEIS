# ARNEIS - Software Architecture

This document details the planned Software Architecture that will be developed for the ARNEIS project.

The software architecture of the ARNEIS project will be based on microservices running on the ARNEIS Kubernetes cluster.

<!-- TODO: Add reference documents -->

<!-- TODO: Add links to definitions and acronyms -->

## Architecture of the ARNEIS cluster

<!-- TODO: Add diagram -->

The ARNEIS cluster is based on [Kubernetes](https://kubernetes.io/).

For simplicity we chose to deploy the ARNEIS cluster using [K3s](https://k3s.io/).

K3s (or “Lightweight Kubernetes”) is a simplified installation of the Kubernetes distribution built for IoT and Edge computing.

K3s is an Open Source project started and maintained by Rancher.com.

* Servers
  - VM arneis-vm01
  - (optional) 2x additional VM to provide High Availability?
* Agents:
  - Same hosts acting as main K3s server (primary agent)
  - (optional) VM arneis-vm02 on the cloud
  - RPI4 on each instance of ARNEIS edge system

## Services deployed on the ARNEIS cluster

* Terminate HTTPS (Traefik instance built into K3s)
* Web server for ARNEIS documentation (replica of <https://arneis.readthedocs.io>)
* Database for ARNEIS backend service (alternative: MongoDB instance at <https://www.mongodb.com/cloud/atlas/>)
* ARNEIS backend service (Node.js + Koa - based on some public boilerplate)
* ARNEIS customer frontend (static site developed in Next.js)
* Service running on the RPI4 for controlling the OAK-D-Lite (Python3?)
* Service running on the RPI3 for controlling the LEGO&reg; Technics Bluetooth Hub (Python3?)

<!-- EOF -->
