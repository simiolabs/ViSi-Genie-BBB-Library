ViSi-Genie-BBB-Library
======================

Beaglebone Black Python Library for Visi-Genie

Python library for the Beaglebone Black to allow easy communication between 4D Intelligent Display modules running ViSi-Genie programmed from Workshop 4, and the Beaglebone Black.

This work was based on original code from William Phelps posted on the 4D Systems' forum.

# Installation #

Simply copy the file uLCD.py to your directory and import the library adding "import uLCD" to top of the file.

# Working example #
Once you added the library, go ahead and control your GUI. Here's an example of how to use it:

```
#!/usr/bin/python

import uLCD

# init. port
port = "/dev/ttyO1"
uLCD.vgInitDisplay(port)

# select form
uLCD.vgWriteObject(uLCD.vgObject.Form, 2, 0) # load Form 2

# update LED digits
uLCD.vgWriteObject(uLCD.vgObject.LEDdigits, 11, 100) # update LED digits 11

# turn on LED
uLCD.vgWriteObject(uLCD.vgObject.LED, 0, 1) # turn on LED 0
```
