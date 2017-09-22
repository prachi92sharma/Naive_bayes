#!/usr/bin/env python 

import sys
import os
import random
import re

lastword = None
lastlist = []

for line in sys.stdin:
	if line[0] =='$':
		line = line.split("\n")
		line = line[0]
		print line
	else:
		line = line.split("\t")[0]
		line = line.split()
		if '~' not in line:
			if line[0]==lastword or lastword ==None:
				lastword = line[0]
				lastlist = lastlist + line[1:]
			else:
				lastword = line[0]
				lastlist = line[1:]
		else:
			newword = line[0]
			if(newword==lastword):
				print " ".join(line[2:]),"~"+newword," ".join(lastlist)
			else:
				print " ".join(line[2:]),"~"+newword
		

