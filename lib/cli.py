#!/usr/bin/python3

import argparse

# cli parser
parser = argparse.ArgumentParser(description='Rack Monitoring Add-on driver')
parser.add_argument('-t', help='Get temperature value from sensor', required=False, type=int, choices=[1,2])
parser.add_argument('-r', help='Get actual speed of fan1 or fan2', required=False, type=int, choices=[1,2])
parser.add_argument('-f1', help='Fan1 power On/Off', required=False, choices=['On','Off'])
parser.add_argument('-f2', help='Fan2 power On/Off', required=False, choices=['On','Off'])
args = parser.parse_args()
