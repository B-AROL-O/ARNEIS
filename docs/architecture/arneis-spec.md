# ARNEIS - Specification

## Introduction

This document contains the Functional and Non-Functional requirements for the [ARNEIS](https://github.com/B-AROL-O/ARNEIS) project.

### Copyright and License

This document is Copyright (c) 2021-2022 by the [B-AROL-O Team](https://github.com/B-AROL-O).

### Reference documents

* [ARNEIS: Automated Recognizer, Network-Enabled, Items Sorter](https://github.com/B-AROL-O/opencv-spatial-ai-contest/blob/main/phase1/arneis-proposal-2021-11-20.pdf) - Project Proposal submitted to the OpenCV Spatial AI Contest, 2021-11-20 (PDF, 5 pages)

### Definitions, acronyms and abbreviations

* **AI**: Artificial Intelligence
* **ARNEIS**: Automated Recognizer, Network-Enabled, Items Sorter. See <https://github.com/B-AROL-O/ARNEIS>
* **B-AROL-O**: See <https://github.com/B-AROL-O/>
* **BLE**: Bluetooth Low Energy. See <https://en.wikipedia.org/wiki/Bluetooth_Low_Energy>
* **Bluetooth&reg;**. See <https://www.bluetooth.com/> 
* **BT**: See Bluetooth
* **LEGO&reg;**: See <https://www.lego.com/>
* **MOC**: My Own Creation
* **NFR**: Non-Functional Requirement
* **OAK**: OpenCV AI Kit
* **OpenCV**: See <https://opencv.org/>
* **PDF**: Portable Document Format. See <https://en.wikipedia.org/wiki/PDF>
* **SysML**: Systems Modeling Language. See <http://www.sysml.org/>
* **UC**: Use case. See <https://en.wikipedia.org/wiki/Use_case>
* **UML**: Unified Modeling Language. See <http://uml.org/>
* **USB**: Universal Serial Bus. See <https://en.wikipedia.org/wiki/USB>

## Open questions

* Q1: How many types of bottles should be recognized?
  - A1: First hypothesis: At least 5 different types

## Use cases

* UC1: End users should login to an internet site where they can submit an order (i.e. a case with 1xA, 2xB)
  - Result: the case is assembled taking bottles from the warehouse

## Objectives
- Minimize the number of motors
- (NFR) Create a fun and "brand-izeable" installation making high help of sounds, videos, lights, etc

## Design options (to be investigated)
- Rotating table
- Option for the container: something like the mignon 3x container

## Design constraints

* The whole installation should fit on a 200 x 90 cm table
* The installation should be easy to unassemble and reassemble (to make it easy to transport it in the carry-on luggage)
* The installation should be powered up from one single phase 100-240Vac power supply, max 400W
* The installation should only use radio frequencies in the ISM band (i.e. 2.54 GHz)
* The mechanical design should be based of only official LEGO parts
* If no suitable LEGO parts can be identified from the official LEGO catalog, a limited number of 3D-printed parts are allowed. Do not use non-official LEGO products (this may hamper the possibility to feature the MOC in official LEGO fests in the future)
* Additionally, beyond the OAK-D-LITE device provided by the organizers, only widely available, off-the shelf electronic devices (such as smart phones, tablets, Raspberry Pi, USB cables etc) should be required
* The site for submitting orders should be usable from a mobile phone or tablet (should decide on minimum requirements, but ideally the site is responsive and renders beautifully on a phone)

<!-- EOF -->
