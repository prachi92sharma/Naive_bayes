#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division  # Python 2 users only
import re
from nltk import word_tokenize
import io
import numpy
import os,sys,re,string
import collections
import numpy as np
from collections import defaultdict
from nltk.corpus import stopwords
import time
 	
start = time.time()
#d = collections.defaultdict(dict)
tardict = defaultdict(int)
count = defaultdict(lambda: defaultdict(int))  #for making defaultdict callable
fpath = os.path.join("/scratch/ds222-2017/assignment-1/DBPedia.full", "full_train.txt")
with open(fpath, "r") as script:
	filelines =script.readlines()
	#filelines=[filelines[0]]
	for line in filelines:
		    values = line.split("\t")
		    labels=values[0].rstrip().split(",")
		    words = re.sub("\d+", "", values[1].rsplit('"',1)[0].split('"',1)[1])
		    regex = r'(\w*)'
		    list1=re.findall(regex,words)
		    while '' in list1:
		       list1.remove('')
		    list1=map(str.lower,list1)
		    for target in labels:
			tardict[target] += 1
			#d[target] += 1
			for word in list1:
				#count[target]={ }
				count[target][word] += 1  
				#print(count[target][word])

#testing
#print(tardict)
#print(count)
print("--- %s seconds ---" % (time.time() - start))
test_path = os.path.join("/scratch/ds222-2017/assignment-1/DBPedia.full", "full_test.txt")
max_prob_clas="a";
max_prob = float("-inf")
err = 0.0
total = 0.0
correct = 0.0
start1 = time.time()
with open(test_path, "r") as script:
		filelines = script.readlines()
		#print len(filelines)
		for line in filelines:
		    max_prob = float("-inf")
		    total += 1
		    values = line.split("\t")
		    labels=values[0].rstrip().split(",")
		    words = re.sub("\d+", "", values[1].rsplit('"',1)[0].split('"',1)[1])
		    regex = r'(\w*)'
		    list1=re.findall(regex,words)
		    while '' in list1:
		    	list1.remove('')
		    list1=map(str.lower,list1)
		    #print list1
		    for clas in tardict.keys():
			prob = 0
			for word in list1:
				#if word in count[clas].keys():
				
					prob = prob + np.log((count[clas][word]+1.0/len(list1))/(sum(count[clas].values())+1.0))
				#else:
					#prob = prob + np.log((1/len(data))/(sum(count[clas].values())+1))
			#print(sum(tardict.values()))
			#print(tardict[clas])
			prob = prob + np.log((tardict[clas]+1.0/len(tardict))/(sum(tardict.values())+1.0))
			#print(prob)
                        if(max_prob<prob):
				max_prob = prob
				max_prob_clas = clas
		    #print(max_prob)
		    #print(max_prob_clas)
      
		    if max_prob_clas in labels:
			print "correct"
			correct = correct+1
		    else:
			print "error"

err = ((total-correct)/total)*100.00
print err
print("--- %s seconds ---" % (time.time() - start1))
			











				
		




