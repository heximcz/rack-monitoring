"""Derived from https://github.com/simonmonk/raspberrypi_cookbook"""

import glob

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
 f = open(device_file, 'r')
 lines = f.readlines()
 f.close()
 return lines

def read_temp():
 lines = read_temp_raw()
 while lines[0].strip()[-3:] != 'YES':
  time.sleep(0.2)
  lines = read_temp_raw()
 equals_pos = lines[1].find('t=')
 if equals_pos != -1:
  temp_string = lines[1][equals_pos+2:]
  temp_c = float(temp_string)
  return temp_c

def print_temp(sx):
 if sx == 1:
  print( round ( read_temp(), -2) / 1000 )
#TODO: get more then one sensor value ...
 elif sx == 2:
  print( round ( read_temp(), -2) / 1000 )
 return
