# ARNEIS

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/B-AROL-O/ARNEIS)
[![GitHub Super-Linter](https://github.com/B-AROL-O/ARNEIS/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

[![ARNEIS logo](docs/images/arneis-logo.png)](https://arneis.readthedocs.io/)

The **ARNEIS** (short for `A`utomated `R`ecognizer, `N`etwork-`E`nabled, `I`tem Sorter) project is the winner of the Popular Vote of the [OpenCV Spatial AI Contest](https://opencv.org/opencv-spatial-ai-contest/) sponsored by [Intel&reg;](https://www.intel.com/) and [Microsoft Azure](https://azure.microsoft.com/).

[![2022-06-14-opencv-spatial-ai-contest-popular-vote-winner.jpg](docs/images/2022-06-14-opencv-spatial-ai-contest-popular-vote-winner.jpg)](https://opencv.org/announcing-the-opencv-spatial-ai-contest-popular-vote-winner/)

## ARNEIS in a nutshell

ARNEIS aims at reproducing in scale a packaging machine for the [Industry-4.0](https://en.wikipedia.org/wiki/Fourth_Industrial_Revolution), thanks to a combination of:

1. An [OAK-D-Lite](https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9095.html) Spatial AI camera
2. A lot of [LEGO&reg; Technic](https://www.lego.com/) parts
3. An intelligent combination of both existing and new Open Source software...
4. ... deployed to a hybrid [Kubernetes cluster](https://kubernetes.io/) made with resources
   - partly on [Azure cloud](https://azure.microsoft.com/) running on [Intel&reg;](https://www.intel.com/) hardware
   - partly on the edge using either a [Raspberry Pi](https://www.raspberrypi.org/) or other [Embedded Linux](https://linuxfoundation.org/) devices.

## ARNEIS Project documentation

Even though the machine is made of LEGO&reg;, we strived to develop the project in a professional way as we are used in our daily job.
With this in mind we have released at <https://arneis.readthedocs.io/> the complete documentation of the ARNEIS project, including:

- functional specifications
- system and software architecture documents
- design documents with detailed instructions for reproducing the machine
- system integration and validation documents

However, as the old adage says (and [we learned it the hard way](https://idioms.thefreedictionary.com/learned+the+hard+way))

> [One picture is worth a thousand words](https://en.wikipedia.org/wiki/A_picture_is_worth_a_thousand_words)

here is a 3-minute video which we submitted to the OpenCV Spatial AI Contest final on 2022-04-04:

<!--
[![ARNEIS submission Video draft - v0.4](https://img.youtube.com/vi/eBbF6LRGaUA/0.jpg)](https://www.youtube.com/watch?v=eBbF6LRGaUA "ARNEIS submission Video draft - v0.4")
-->

[![ARNEIS submission Video](https://img.youtube.com/vi/qHFRRHWtTqY/0.jpg)](https://www.youtube.com/watch?v=qHFRRHWtTqY "ARNEIS submission Video")

The source files for the software programs, the LEGO&reg; MOC as well as the documentation site are maintained in the GitHub repository at <https://github.com/B-AROL-O/ARNEIS>.
Whenever the `main` branch of the git repository is updated, <https://arneis.readthedocs.io/> will be updated accordingly.

### The ARNEIS MOC

We have designed a MOC (My Own Creation) using the parts from [LEGO&reg; Set 42100](https://arneis.readthedocs.io/en/latest/lego-set-42100/README.html) (Liebherr R 9800 Excavator).

![arneis-conveyor-20220312.gif](https://github.com/B-AROL-O/ARNEIS/raw/main/mocs/project/arneis-conveyor-20220312.gif)

### The ARNEIS Software Architecture

The software architecture is based on microservices running on a hybrid Kubernetes cluster.
Please refer to <https://arneis.readthedocs.io> for details.

### The Computer Vision and Machine Learning

The OAK-D-Lite captures photos of the bottles flowing through the conveyor and runs a Neural Network trained on a custom dataset to be able to classify and recognize the type (Part Number) of the bottle. This information is fed in real-time to the Raspberry Pi which - based on the job order - decides whether to eject the bottle to the final packaging unit, or putting it back to the parts warehouse.

### ARNEIS project roadmap and timeline

The ARNEIS project roadmap is [kept updated on GitHub](https://github.com/B-AROL-O/ARNEIS/milestones?direction=asc&sort=due_date&state=open).

[Gianpaolo Macario](https://github.com/gmacario/) publishes regular updates of the ARNEIS project on [his personal blog](https://gmacario.github.io/posts).

#### B-AROL-O team interview, 2022-03-17

 During [OpenCV Weekly Webinar Episode 49](https://twitter.com/opencvweekly/status/1504487889630945281) the B-AROL-O Team was asked to introduce the ARNEIS and explain the vision, the motivations and the achievements after the first three months of development:

<!-- TODO: <https://github.com/B-AROL-O/ARNEIS/issues/259> -->

[![image](https://user-images.githubusercontent.com/75182/159136335-12c6b155-d7be-4172-bf84-1a45ef91c181.png)](https://www.linkedin.com/video/event/urn:li:ugcPost:6909587011267891201/)

#### ARNEIS LEGO MOC History

A 5-min video with the initial design of the LEGO MOC is [available on YouTube](https://www.youtube.com/watch?v=S-DiK0UgNBY).

[![ARNEIS LEGO MOC History HD 1080p](https://img.youtube.com/vi/S-DiK0UgNBY/0.jpg)](https://www.youtube.com/watch?v=S-DiK0UgNBY "ARNEIS LEGO MOC History HD 1080p")

### How to stay in touch

You may follow [@baroloteam on Twitter](https://twitter.com/baroloteam) to get notified about the progress of the project.

Please report bugs and feature requests on <https://github.com/B-AROL-O/ARNEIS/issues>, or DM [B-AROL-O Team on Twitter](https://twitter.com/baroloteam) about security issues or other non-public topics.

## Copyright and license

Copyright (C) 2021-2023, [B-AROL-O Team](https://github.com/B-AROL-O), all rights reserved.

### Source code license

The source code contained in this repository and the executable distributions are licensed under the terms of the MIT license as detailed in the [LICENSE](LICENSE) file.

### Documentation license

![CC BY-SA 4.0](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

Please note that your contribution to the ARNEIS Documentation is licensed under a Creative Commons Attribution-Share Alike 4.0 License. see <https://creativecommons.org/licenses/by-sa/4.0/>

<!-- EOF -->
