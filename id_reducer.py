#!/usr/bin/env python 

import sys
import re
import random
import os

lastword = " "
lastlist = ""

for line in sys.stdin:
	if line[0]=='$':
		print line.split("\n")[0]
	else:
		line = line.strip()
		#line = line.split("\t")[0]
		line = line.split("~")
		line[0] = line[0].strip()
		if lastword == " " or lastword == line[0]:
			lastword = line[0]
			lastlist = lastlist+ " " +"~"+line[1].split("\n")[0]
		else:
			print lastword,lastlist
			lastword = line[0]
			lastlist = "~"+line[1].split("\n")[0]
print lastword,lastlist

