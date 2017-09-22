#!/usr/bin/env python
import sys
import re
import os

i=1
fpath = os.path.join("/home/prachi.sharma92/full_test1.txt")
with open(fpath, "r") as script:
	filelines =script.readlines()
	#filelines = [filelines[1]]
	for line in filelines:
		line = line.replace('\n', '')
		print i,line
		i = i+1
	
