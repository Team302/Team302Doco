==============================
Robot Hardware 
==============================

Robot Hardware overview can be found at https://docs.wpilib.org/en/stable/stubs/hardware-stub.html.

An overview presentation is found here:  https://docs.google.com/presentation/d/1Dhm7V9cdh9EMjhA33Lmx3TD4fkXS6uLIZx33OOgIuTM/edit#slide=id.g1f87997393_0_782

https://docs.google.com/presentation/d/1yIJ3jNkbtcEp67RDO22nGQyjTlIGVo6FmIXg52GUQuo/edit#slide=id.g1f87997393_0_782


Status Light Quick Reference
==============================

https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html

RoboRio
========

Configuration Tool
---------------------------

This is part of the FRC Game Tools that gets installed as part of installing the environment.  Some keys are the RoboRio 1 doesn't have an SD card and is configured completely using the tool.  RoboRio 2 has an SD card which is configured using the balenaEtcher (or other imaging tools listed on the main page).  Then the team number gets set using the RoboRio Imaging tool or the team number tool.

The team number can be set/reset without re-imaging the roboRio, so if we are taking multiple robots with the same team number to an event, we can change the number without having to re-deploy code.

See https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/index.html for details on imaging the particular roborio.

I2C Port
---------
RoboRio has issues with I2C bus (sometimes locks up the roboRio).   

PI Pico
^^^^^^^^^
There is a work around for I2C bug using a PI Pico board to interface.

Thad House has put together code to make this work.  See https://github.com/ThadHouse/picocolorsensor

Radio
======

Configuration Tool
------------------------

This tool is installed separately as part of the environment set up.

This one is filled with many ways to fail.  First make sure all of your virus protection and firewalls are turned off.  Then disable all of your network adapters except the ethernet adapter.  Then follow the steps found at https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/radio-programming.html.  Note: at one point there were Java version incompatability issues, but they've updated the tool to hopeully resolve this issue.

Lately, I've been pretty successful with this using just a power supply and my laptop.  Older laptops and some as well as some running the home edition of the operating system seem to have more issues.



CTRE Hardware
===============

Pheonix Tuner
-------------------

This gets installed as part of installing the CTRE 3rd party tools. It allows the firmware and CAN IDs to be set on the CTRE hardware. There are some really cool things that can be done as well such as running motors in both open loop and closed loop modes, plotting various property values, etc. Documentation can be found https://phoenix-documentation.readthedocs.io/en/latest/.

Lately we have been using Phoenix X which isn't installed this way rather it comes from the windows store.  This seems to work better.


REV Hardare
============

REV Hardware Client
----------------------

See https://docs.revrobotics.com/rev-hardware-client/ for setting up REV hardware.


Limelight
==========

Limelight Configuration Tool
------------------------------

Limelight (vision solution) has a series of tools found at https://limelightvision.io/pages/downloads.




Co-Processors
=======================



Raspberry PI
-------------

  TODO: pull doco

  

Orange PI
------------

TODO: pull doco



Rock PI
----------

TODO:  pull doco



Jetson Nano
------------
TODO:  pull doco


Arduino
----------
TODO: pull doco 


Hero
---------

TODO: pull doco


NUC
------

TODO: pull doco


Hardware Accelerators
=======================

Google Coral
--------------

Works with Limelight and Raspberry PI Machine Learning Solutions.
TODO: pull doco



