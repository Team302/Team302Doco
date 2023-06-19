Robot Hardware Configuration
=============================

Robot Hardware overview can be found at https://docs.wpilib.org/en/stable/stubs/hardware-stub.html.

Status Light Quick Reference
----------------------------------

https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html

RoboRio Configuration Tool
----------------------------------

This is part of the FRC Game Tools that gets installed as part of installing the environment.  Some keys are the RoboRio 1 doesn't have an SD card and is configured completely using the tool.  RoboRio 2 has an SD card which is configured using the balenaEtcher (or other imaging tools listed on the main page).  Then the team number gets set using the RoboRio Imaging tool or the team number tool.

The team number can be set/reset without re-imaging the roboRio, so if we are taking multiple robots with the same team number to an event, we can change the number without having to re-deploy code.

See https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/index.html for details on imaging the particular roborio.


Radio Configuration Tool
----------------------------------

This tool is installed separately as part of the environment set up.

This one is filled with many ways to fail.  First make sure all of your virus protection and firewalls are turned off.  Then disable all of your network adapters except the ethernet adapter.  Then follow the steps found at https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/radio-programming.html.  Note: at one point there were Java version incompatability issues, but they've updated the tool to hopeully resolve this issue.

Lately, I've been pretty successful with this using just a power supply and my laptop.  Older laptops and some as well as some running the home edition of the operating system seem to have more issues.



CTRE Pheonix Tuner
---------------------

This gets installed as part of installing the CTRE 3rd party tools. It allows the firmware and CAN IDs to be set on the CTRE hardware. There are some really cool things that can be done as well such as running motors in both open loop and closed loop modes, plotting various property values, etc. Documentation can be found https://phoenix-documentation.readthedocs.io/en/latest/.

Lately we have been using Phoenix X which isn't installed this way rather it comes from the windows store.  This seems to work better.

REV Hardware Client
-----------------------------

See https://docs.revrobotics.com/rev-hardware-client/ for setting up REV hardware.

Limelight Configuration Tool
-----------------------------

Limelight (vision solution) has a series of tools found at https://limelightvision.io/pages/downloads.






