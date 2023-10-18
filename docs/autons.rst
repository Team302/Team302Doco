============================
Auton Structure
============================


Drive Primitives
=================

Currently there are the following Drive Primitives:
-    Stop: Don't send anything to the wheels; just let brake mode stop the robot
-    Hold Position: Need to be exact, lock the weeks so the robot cannot be moved
-    Drive PathWeaver Path:  Create a trajectory (from a PathWeaver json file) and follow it
-    Drive Path Planner Path: Create a trajectory (from a Path Planner json file) and follow it
-    Auto Balance:  Get the robot to a level position
-    Vision Drive:  Utilize vision to drive to a target (game piece, April Tag, etc.)

For the 2023 season we should be eliminating one of the Path option.  Additionally there were some other options such as drive distance, drive time, turn to angle, etc. that we haven't used since we went to swerve drive and these should be removed as well.

`See Path Generation <https://team302doco.readthedocs.io/en/latest/paths.html>`_ for details on how paths are created.

TODO:  Add information


Transitions between Drive Primitives
=====================================

TODO:  Add information



Events along the Path
=======================

TODO:  Add information




Mechanism State Control
=======================

TODO:  Add information


