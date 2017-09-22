#!/usr/bin/env python

import sys
import os
import random
import re

stopwords = ['what','who','and','the','why','for','was','about','from','where','with','which','were']
for line in sys.stdin:
	if ((line[0]=='$')and(line[1]=='$')):
		line = line.split("\t")
		print line[0]
	elif ((line[0]=='$')and(line[1].isalpha())):
		line = line.split("\t")
		print line[0]
	elif (line[0].isalpha()):
		line = line.split("\t")
		print line[0]
	else:
		line = line.split("\t")
		words = re.sub("\d+", "",line[1].rsplit('"',1)[0].split('"',1)[1])
		regex = r'(\w*)'
		list1 = re.findall(regex,words)
		while '' in list1:
			list1.remove('')
		list1  = [word for word in list1 if word.lower() not in stopwords]
		list1=map(str.lower,list1)
		lis = []
		for word in list1:
			if word not in lis and (len(word)>2):
				lis.append(word)
		for word in lis:
			print word+' ~' ,line[0]
			 			






