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
