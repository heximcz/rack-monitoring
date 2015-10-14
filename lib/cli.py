import argparse

# cli parser
parser = argparse.ArgumentParser(description='Rack Monitoring Add-on driver')
parser.add_argument('-t', help='Get temperature value from sensor', required=False, type=int, choices=[1,2])
parser.add_argument('-f1', help='Fan1 power On/Off', required=False, choices=['On','Off'])
parser.add_argument('-f2', help='Fan2 power On/Off', required=False, choices=['On','Off'])
parser.add_argument('-r', help='Get actual speed of fan1 or fan2', required=False, type=int, choices=[1,2])
parser.add_argument('-p', help='Get actual status of PSU1 or PSU2', required=False, type=int, choices=[1,2])
parser.add_argument('-sht', help='Get temperature/humidity value from SHT21 sensor. (v = verbose)', required=False, choices=['t','h','tv','hv'])
args = parser.parse_args()
