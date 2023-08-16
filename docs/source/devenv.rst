
===================================
Development Enviornment
===================================

To set up the environment, first follow the instructions from https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/index.html for the C++ or common tasks.  

These steps will install:

* WPI Tools such as SmartDashboard, Shuffleboard and Glass (all dashboards), PathWeaver (autonomous path planning) and SysID (robot characterization).
* `VS Code <https://code.visualstudio.com/>`_ - A development environment to write robot code.
* The WPILib extension for VS Code which provides features for us to build and deploy robot code to the robot.

VSCode 
--------

TODO:  Add Details

Intellisense
^^^^^^^^^^^^^^^^

This is from this Chief Delphi topic (https://www.chiefdelphi.com/t/intelli-non-sense-help/375155/3)

It’s actually not a Gradle issue, it’s just that occasionally the vscode engine gets confused. Follow the following steps to try and reset everything.

* Make sure you’re not getting any popups saying you’re in the wrong folder when opening vscode, or any other popups.

* Make sure you didn’t accidentally create a c_cpp_properties.json file in the .vscode folder. It breaks everything. If it’s there, delete it.

* Close all files in vscode. Leave vscode open.

* Run the refresh c++ intellisense command in vscode.

* Once that finishes, in the bottom right you should see something that looks like a platform (linuxathena or windowsx86-64 etc). If it’s not linuxathena click it and set it to one of the linuxathena one.

* Wait one minute (yes one whole minute don’t skip this)

* Open your main cpp file (not a header file). Intellisense should now be working.

* Not closing vscode while doing this is key, closing it will reset the process. You just have to close all the tabs.

Gradle
--------

TODO:  Add Details


3rd Party Tools
----------------

3rd Party tools (CTRE and REV are the ones we use)  See https://team302doco.readthedocs.io/en/latest/hardware.html#ctre-pheonix-tuner and https://team302doco.readthedocs.io/en/latest/hardware.html#rev-hardware-client for details on running the tools.


In addition to the WPILib/FIRST provided tools, we use other 3rd party tools to develop, test, and run our robot code.  These include:

* Cross The Road Electronics Phoenix 6/Pro Library - an API to control the Falcon 500 motors we mainly use and read data from our sensors like CANCoders and the Pigeon IMU. (link to phoenix lib install)
* Cross The Road Electronics Phoenix Tuner X - a tool to test and configure CTRE products (Falcon motors, CANCoders, CANivores, etc.). (link to phoenix lib install)
* REV Hardware Client - a tool to configure and read data from REV Robotics hardware (PDH, PCM, etc.).  (link to rev hw install)
* Filezilla - a tool to transfer files from our computers to the RoboRIO. (link to filezilla)




Software Configuration Management Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


GitHub / Github Desktop 
--------------------------

This is a website where our code is stored using a Git Configuration Management Tool. Additionally, we create project(s) and use the Kanban board to manage activities. Visit Our main github page at https://github.com/orgs/Team302/repositories.  Github Desktop can interact with the projects locally.


GitKraken
---------

This is a desktop interface to Git -- specifically GitHub -- where our code and projects reside. This makes it easier to interact with the remote repository using a GUI instead of the command line. We use the free version that can be downloaded from here.




VS Code Plugin
---------------

TODO:  Add details



NI Game Tools 
===================================


RoboRio Imaging Tools
-----------------------

TODO:  Add Details


Driver's Station
------------------

TODO:  Add Details



Radio
===================================


Radio Configuration Tools (see https://team302doco.readthedocs.io/en/latest/hardware.html#radio-configuration-tool for details on running the tool)

TODO:  Add Details


