.. ARNEIS documentation master file, created by
   sphinx-quickstart on Wed Jan 19 05:33:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the ARNEIS Project!
==============================

.. image:: ./images/arneis-logo.png
    :width: 400px
    :align: center

The **ARNEIS** (short for ``A`` utomated ``R`` ecognizer,  ``N`` etwork - ``E`` nabled, ``I`` tems ``S`` orter)
is one of the 50 selected finalists of the `OpenCV Spatial AI Contest <https://opencv.org/opencv-spatial-ai-contest/>`_
sponsored by `Intel® <https://www.intel.com/>`_ and `Microsoft Azure <https://azure.microsoft.com/>`_.

ARNEIS in a nutshell
--------------------

ARNEIS aims at reproducing in scale a packaging machine for the `Industry-4.0 <https://en.wikipedia.org/wiki/Fourth_Industrial_Revolution>`_.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/7qxbT31U5dE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

This goal is achieved by means of a combination of:
* An [OAK-D-Lite](https://docs.luxonis.com/projects/hardware/en/latest/pages/DM9095.html) Spatial AI camera
* A lot of [LEGO&reg; Technic](https://www.lego.com/) parts
* ... and plenty of Open Source software

ARNEIS Project sources
----------------------

The source files for the software programs, the LEGO® MOC as well as the documentation site are maintained in the GitHub repository at `github.com/B-AROL-O/ARNEIS <https://github.com/B-AROL-O/ARNEIS>`_.

Whenever the ``main`` branch of the git repository is updated, `this site <https://arneis.readthedocs.io/>`_` will be updated accordingly.

How to stay in touch
-------------------

The ARNEIS project roadmap is `maintained on GitHub <https://github.com/B-AROL-O/ARNEIS/milestones?direction=asc&sort=due_date&state=open>`_.

`Gianpaolo Macario <https://github.com/gmacario/>`_ publishes regular updates of the ARNEIS project on `his personal blog <https://gmacario.github.io/posts>`_.

You may also follow `twitter.com/baroloteam <https://twitter.com/baroloteam>`_ to get notified about the progress of the project.

Please report bugs and feature requests on https://github.com/B-AROL-O/ARNEIS/issues,
or DM the `B-AROL-O Team on Twitter <https://twitter.com/baroloteam>`_ about security issues or other non-public topics.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`

.. comment
   * :ref:`modindex`

.. toctree::
   :caption: Home
   :maxdepth: 2
   :hidden:

   self

.. toctree::
   :caption: Documentation
   :maxdepth: 1
   :hidden:

   acronyms
   bibliography

.. toctree::
   :caption: Architecture
   :maxdepth: 1
   :hidden:

   architecture/arneis-spec
   architecture/arneis-sysarch
   architecture/arneis-swarch
   
.. toctree::
   :caption: HOWTOs
   :maxdepth: 1
   :glob:
   :hidden:

   howto/*

.. toctree::
   :caption: LEGO®
   :maxdepth: 1
   :hidden:
   
   lego-set-42100/README
   lego-set-42100/unboxing-lego-set-42100
   lego/studies
   lego/camera-support
   lego/conveyor-wip