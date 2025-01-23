=================
Base Robot Classes
=================


The Robot class subclasses the timed robot (similar concep to the previous iterative robot).   It has a series of Init methods that run when that particular state of the robot is starts and then runs the corresonding periodic method every 20 milliseconds.

The different states  and their methods are:
* Robot (general stuff that is common regardless of state): RobotInit (runs when robot starts up) and RobotPeriodic (runs after the periodic method for the particular state) 
* Disabled: DisabledInit and DisabledPeriodic
* Autonomous:  AutonomousInit (typically where the auton routine is selected) and AutonomousPeriodic
* Teleop: TeleopInit and TeleopPeriodic
* Test: TestInit and TestPeriodic
* Simulation: SimulationInit and SimulationPeriodic


As a general rule, there are not loops in the periodic routines as this code is called in a loop.  If the periodic routine take longer than 20 milliseconds you will see loop overruns in the log.   This can lead to watchdog not fed errors and ultimately the robot stopping if this becomes too prevailent.


Presentations
====================

https://docs.google.com/presentation/d/1QZVJoTMAku7hOwZAs1tNAO83_mChDXLXYg4HWHvv3PM/edit#slide=id.g3c87b495af_0_0

https://docs.google.com/presentation/d/1Dhm7V9cdh9EMjhA33Lmx3TD4fkXS6uLIZx33OOgIuTM/edit#slide=id.g1f87997393_0_782

https://docs.google.com/presentation/d/19RoP2f6UMAKUeeprYdJLxGrGX3dBWLX5gTrPWNBichk/edit#slide=id.g405015a370_0_26

https://docs.google.com/presentation/d/184iOF7HFaPfpPfC1JpWVNIyWscpaO2jDgGzur1je3Hk/edit#slide=id.g1f87997393_0_782


Overview
====================

https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-4/creating-test-drivetrain-program-cpp-java.html






