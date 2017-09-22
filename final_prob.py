#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division  # Python 2 users only
import re
from nltk import word_tokenize
import io
import numpy,math
import os,sys,string
import collections
import numpy as np
from collections import defaultdict
from nltk.corpus import stopwords


words = defaultdict(int)
classes = defaultdict(int)

data = open("dict",'r')
filelines = data.readlines()
for line in filelines:
	if line[0]=='$' and line[1]=='$':
		line = line.split("\t")[0]
		line = line.split("$$")[1]
		line = line.split()
		label = line[0]
		count_words = line[1]
		words[label] = int(count_words)

	elif line[0]=='$':
		line = line.split("\t")[0]
		line = line.split("$")[1]
		line = line.split()
		label = line[0]
		no_of_classes = line[1]
		classes[label] = int(no_of_classes)
#print classes
#print words
for lines in sys.stdin:
	if lines[0]!= '$':
		max_prob=0 
		max_prob_class=None
		final_prob = defaultdict(int)
		lines = lines.split("~")
		lines[0] = lines[0].strip()
		test_file_no = lines[0].split()[0]
		all_classes = lines[0].split()[1]
		all_classes = all_classes.split(",")
		words_class_count = lines[1:]
		for classes in classes.keys():
			final_prob[classes]=0
		no_of_words_td = len(lines[1:])
		for i in range(no_of_words_td):
			first_list = words_class_count[i].split()
			no_of_words_el = len(first_list)
			prob_word = defaultdict(int)
			vocab = len(words_class_count)
			for i in range(1,no_of_words_el,2):
				prob_word[first_list[i]] = first_list[i+1]
			for y in classes.key():
				if y in prob_word.keys():
					final_prob[y] = final_prob[y] + math.log((prob_word[y]+1.0/vocab)/words[y]+1.0)
				else:
					final_prob[y] = final_prob[y] + math.log((0+1.0/vocab)/words[y]+1.0)
			for y in classes.key():
				final_prob[y] = final_prob[y] + math.log((classes[y]+1.0/50)/(sum(classes.values())+1))
												
		for y in classes.key():
			if(max_prob < final_prob[y]):
				max_prob = final_prob[y]
				max_prob_class = y
		if max_prob_class in all_classes:
			print "yes"
		else:
			print "no"









