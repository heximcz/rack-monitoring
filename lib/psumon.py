#!/usr/bin/python3

# get status of redundancy PSU for Zabbix:
# Mean Well DR-RDN20

import RPi.GPIO as GPIO
import time
import sys

Port_PDU1 = 24
Port_PDU2 = 25

GPIO.setmode(GPIO.BCM)

def get_psu_status(n):
 if n == 1:
  Port = Port_PDU1
 elif n == 2:
  Port = Port_PDU2
 else:
  print('error')
  return
 GPIO.setup(Port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 input_state = GPIO.input(Port)
 if input_state == True:
  print('0')
 else:
  print('1')
 GPIO.cleanup()
 return
