#!/usr/bin/env python
import sys
import re
import os
import time



Total = 0
oldKey = None
oldKey1 = None
for line in sys.stdin:

    if (line[0].isalpha()):
            if (oldKey!= None and oldKey[0] == '$'):
                print oldKey,Total
                oldKey= None
                oldKey1 = None
                Total = 0
            values = line.split(" ")
            if oldKey==None and oldKey1==None:
                oldKey = values[0]
                oldKey1 = values[1]
            if oldKey==values[0] and oldKey1==values[1]:
                a = int(values[2])
                Total += a
            else:
                print oldKey,oldKey1,Total
                Total = int(values[2])
                oldKey = values[0]
                oldKey1 = values[1]

	

    elif ((line[0]=='$')and(line[1]=='$')):
            values = line.split(" ")
            if oldKey==None:
                oldKey = values[0]
            if oldKey==values[0]:
                a = int(values[1])
                Total += a
            else:
                print oldKey,Total
                Total = int(values[1])
                oldKey = values[0]


    elif ((line[0] == '$')and(line[1].isalpha())):
            if(oldKey[0]=='$' and oldKey[1] == '$'):
                print oldKey,Total
                oldKey = None
                Total = 0
            values = line.split(" ")
            if oldKey==None:
                oldKey = values[0]
            if oldKey==values[0]:
                Total += int(values[1])
            else:
                print oldKey,Total
                Total = int(values[1])
                oldKey = values[0]


if oldKey != None:
	print oldKey,oldKey1,Total


