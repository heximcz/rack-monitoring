#!/usr/bin/python3

import os
import fcntl
import time
import unittest
from lib.cli import *

if args.t:
 from lib.temperature import *
 print_temp(args.t)
elif args.r:
 from lib.fanrpm import *
 get_fan_rpm(args.r)
elif args.f1:
 from lib.fanpower import *
 fan_power_ctl(1,args.f1)
elif args.f2:
 from lib.fanpower import *
 fan_power_ctl(2,args.f2)
elif args.p:
 from lib.psumon import *
 get_psu_status(args.p)
elif args.sht:
 """Class to read temperature and humidity from SHT21. Derived from http://python3-microstacknode.readthedocs.org/"""
 from lib.sht21 import SHT21
 with SHT21() as htsensor:
  if args.sht == 't':
   temperature = htsensor.get_temperature()
   print('{:.2f}'.format(temperature))
  elif args.sht == 'h':
   humidity = htsensor.get_humidity()
   print('{:.2f}'.format(humidity))
  elif args.sht == 'tv':
   temperature = htsensor.get_temperature()
   print('Temperature: {:.2f}°C'.format(temperature))
  elif args.sht == 'hv':
   humidity = htsensor.get_humidity()
   print('Humidity: {:.2f}%'.format(humidity))
else:
 parser.print_usage()
 print(" ")
 print("Nothing to do!")
 print("Try:",os.path.basename(__file__),"-h")
 print(" ")
