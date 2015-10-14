# get status of redundancy PSU for Zabbix:
# for two PSU Mean Well and redundancy module MW - DR-RDN20

import RPi.GPIO as GPIO
import time
import sys

Port_PSU1 = 24
Port_PSU2 = 25

GPIO.setmode(GPIO.BCM)

def get_psu_status(n):
 if n == 1:
  Port = Port_PSU1
 elif n == 2:
  Port = Port_PSU2
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
