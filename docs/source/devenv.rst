Development Enviornment
=========================

.. _installation:

To set up the environment, first follow the instructions from here. This will get many of the tools installed. Then look through the following list to add missing tools.


Build/Edit Tools
------------------------

To set up the environment, first follow the instructions from here. This will get many of the tools installed. Then look through the following list to add missing tools.

VSCode / Gradle / 3rd Party Tools
----------------------------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:
This is ths standard environment and is needed to create C++ code, build it and deploy it to the robot. Install using the instructions found here. Don't forget the 3rd party tools (we used CTRE and Rev Robotics tools most years.)

Controller Tools
------------------------

Game Controllers
-----------------
Run Joystick on your windows laptop.   You can check whether each axis/button is working and configure the axis if the 0 point is off.

Gamepad Configuration Tool
----------------------------------

When building custom gamepads, this tool is used to program the board to assign certain inputs to particular analog/digital input. This is installed as part of the NI game specific tools.

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:
This is ths standard environment and is needed to create C++ code, build it and deploy it to the robot. Install using the instructions found here. Don't forget the 3rd party tools (we used CTRE and Rev Robotics tools most years.)



>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
