#!/usr/bin/python3

import os
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
else:
 parser.print_usage()
 print(" ")
 print("Nothing to do!")
 print("Try:",os.path.basename(__file__),"-h")
 print(" ")
