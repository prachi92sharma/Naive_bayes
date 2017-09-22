#!/usr/bin/env python
import sys
import re
import os

stopwords = ['what','who','and','the','why','for','was','about','from','where','with','which','were']
#fpath = os.path.join("/user/ds222/assignment-1/DBPedia.verysmall", "verysmall_train.txt")
#with open(fpath, "r") as script:
#	filelines =script.readlines()[3:]
	#filelines = [filelines[0]]
for line in sys.stdin:
    	line = line.strip()
    	#data = line.split("\t")
   	values = line.split("\t")
    	labels=values[0].rstrip().split(",")
    	words = re.sub("\d+", "", values[1].rsplit('"',1)[0].split('"',1)[1])
    	regex = r'(\w*)'
    	list1=re.findall(regex,words)
    	while '' in list1:
		list1.remove('')
	list1  = [word for word in list1 if word.lower() not in stopwords]
    	list1 = map(str.lower,list1)
	for label in labels:
		print "$"+label,1
    		for word in list1:
			if(len(word)>2):
				print "$$"+label, 1
    				print word,label,1

