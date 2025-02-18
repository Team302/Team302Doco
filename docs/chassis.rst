============================
Chassis
============================


Swerve
============

Follow the steps to define the motors, CANCoders, Pigeon, Swerve Modules, Swerve Chassis as defined: https://v6.docs.ctr-electronics.com/en/2024/docs/tuner/tuner-swerve/index.html.

- Export the TunerConstants File from the CTRE Swerve Project.
- Create a folder in the chassis/definitions for a particular robot (e.g. chassis9998)
- Put the generated TunerConstants.h  file into this folder
- Rename file from TunerConstants.h to TunerConstantsXXXX.h where XXXX is the robot number
- Rename class to match file name
- Comment out (or delete) the TunerSwerveDrivetrain class (carefule there are block end comments in this block)
- Comment out (or delete) forward declaration of CommandSwerveDrivetrain
- Comment out (or delete) static subsystems::CommandSwerveDrivetrain CreateDrivetrain();
- Comment out (or delete) static constexpr swerve::SwerveDrivetrainConstants lines
- Comment out (or delete) the private: after this previous block
- Comment out (or delete) static constexpr swerve::SwerveModuleConstantsFactory ConstantCreator = lines
- Comment out (or delete) the 4 static constexpr swerve::SwerveModuleConstants definitions
- Comment out (or delete) private before inversion constants
- Add public at beginnning of TunerConstansXXXX class
- Copy a ChassisConfigXXXX.cpp and ChassisConfigXXXX.h file into this definitions file
- Change TunerConstantsXXXX to TunerConstantsYYYY where XXXX is the robot id where the ChassisConfig was copied from and YYYY is the robot that is being defined (change all instances).
- build 
- test



Swerve Math
------------

.. todo::
Add information


Architecture of our Swerve Code
---------------------------------

.. todo::
Add information



Differential Drive
=======================

.. todo::
Add information


Mecanum Drive
=================

.. todo::
Add information


Kiwi Drive
=============

.. todo::
Add information
