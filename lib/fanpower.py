#!/usr/bin/python3

import RPi.GPIO as GPIO
import sys

Port_Fan1 = 22
Port_Fan2 = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def fan_power_ctl(cooler,status):
 if cooler == 1:
  GPIO.setup(Port_Fan1, GPIO.OUT)
  if status == 'On':
   GPIO.output(Port_Fan1, True)
   print("Power for FAN1 is now ON")
  if status == 'Off':
   GPIO.output(Port_Fan1, False)
   GPIO.cleanup()
   print("Power for FAN1 is now OFF")
 elif cooler == 2:
  GPIO.setup(Port_Fan2, GPIO.OUT)
  if status == 'On':
   GPIO.output(Port_Fan2, True)
   print("Power for FAN2 is now ON")
  if status == 'Off':
   GPIO.output(Port_Fan2, False)
   GPIO.cleanup()
   print("Power for FAN2 is now OFF")
 return

