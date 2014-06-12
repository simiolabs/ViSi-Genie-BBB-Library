#!/usr/bin/python

import serial, operator

ser = serial.Serial()

class vgCmd:
  ReadObject = 0
  WriteObject = 1
  WriteString = 2
  WriteStringUnicode = 3
  WriteContrast = 4
  ReportObject = 5
  ReportEvent = 6
  ACK = 0x06
  NAK = 0x15
 
class vgObject:
  DipSwitch = 0
  Knob = 1
  RockerSwitch = 2
  RotarySwitch = 3
  Slider = 4
  TrackBar = 5
  WinButton = 6
  Meter = 7
  CoolGauge = 8
  CustomDigits = 9
  Form = 10
  Guage = 11
  Image = 12
  Keyboard = 13
  LED = 14
  LEDdigits = 15
  Meter = 16
  Strings = 17
  Thermomter = 18
  UserLED = 19
  Video = 20
  StaticText = 21
  Sound = 22
  Timer = 23
 
def vgWriteObject(id, index, value):
  global ser
  cmd = chr(vgCmd.WriteObject) + chr(id) + chr(index) + chr(int(value/256)) + chr(value%256)
  cks = reduce(operator.xor, (ord(s) for s in cmd), 0)
  cmd = cmd + chr(cks)
#  print "vg write"
#  print ":".join("{:02x}".format(ord(c)) for c in cmd)
  ser.write(cmd)
#  print "rsp"
  rsp = ord(ser.read(1))
#  print "{:02x}".format(rsp)
  return rsp
  
def vgWriteString(index, text):
  global ser
  cmd = chr(vgCmd.WriteString) + chr(index) + chr(len(text)) + text
  cks = reduce(operator.xor, (ord(s) for s in cmd), 0)
  cmd = cmd + chr(cks)
#  print "vg write"
#  print ":".join("{:02x}".format(ord(c)) for c in cmd)
  ser.write(cmd)
#  print "rsp"
  rsp = ord(ser.read(1))
#  print "{:02x}".format(rsp)
  return rsp    
  
def vgInitDisplay(display_port):
    global ser
    
    # Open the serial port, close, & re-open again
    ser = serial.Serial(port=display_port, baudrate=115200, timeout=5, parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
    ser.close()
    ser.open()
    
    # send dummy characters until we get a NAK back, hopefully
    # then the display sequencer will be in a stable state.
    #time.sleep(1)
    for i in range(1,10):
      rsp = vgWriteObject(vgObject.Form, 0, 0) # load Form 0
      if (rsp != vgCmd.NAK):
        break
      time.sleep(1)
    if (i > 9):
      print "unable to open serial port, exiting"
