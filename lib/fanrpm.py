import RPi.GPIO as GPIO
import time
import sys

Port_Fan1 = 17
Port_Fan2 = 18

x = 0
interval = 1
rpm = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def count(channel):
  global x
  x = x + 1

def get_fan_rpm(cooler):
 if cooler == 1:
  GPIO.setup(Port_Fan1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.add_event_detect(Port_Fan1, GPIO.RISING, callback=count)
  time.sleep(interval)
  rpm = int((x / 2) * 60)
  print(int(rpm))
  GPIO.cleanup()
 elif cooler == 2:
  GPIO.setup(Port_Fan2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.add_event_detect(Port_Fan2, GPIO.RISING, callback=count)
  time.sleep(interval)
  rpm = int((x / 2) * 60)
  print(int(rpm))
  GPIO.cleanup()
 return
