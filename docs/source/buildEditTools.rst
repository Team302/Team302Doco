
Build/Edit Tools
=========================

To set up the environment, first follow the instructions from here. This will get many of the tools installed. Then look through the following list to add missing tools.

VSCode / Gradle / 3rd Party Tools
----------------------------------

This is from this Chief Delphi topic (https://www.chiefdelphi.com/t/intelli-non-sense-help/375155/3)

It’s actually not a Gradle issue, it’s just that occasionally the vscode engine gets confused. Follow the following steps to try and reset everything.

- Make sure you’re not getting any popups saying you’re in the wrong folder when opening vscode, or any other popups.

- Make sure you didn’t accidentally create a c_cpp_properties.json file in the .vscode folder. It breaks everything. If it’s there, delete it.

- Close all files in vscode. Leave vscode open.

- Run the refresh c++ intellisense command in vscode.

- Once that finishes, in the bottom right you should see something that looks like a platform (linuxathena or windowsx86-64 etc). If it’s not linuxathena click it and set it to one of the linuxathena one.

- Wait one minute (yes one whole minute don’t skip this)

- Open your main cpp file (not a header file). Intellisense should now be working.

- Not closing vscode while doing this is key, closing it will reset the process. You just have to close all the tabs.
