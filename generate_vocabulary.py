#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
generate_vocabulary luo sanaston tietokanna pohjalta
'''

import os
from datetime import datetime
import unicodecsv as csv
import time as t
import random as r

os.chdir('/home/lassi/Python/sanakone1.1/')
filename = './vocabularies/vocabulary_%s.txt' % str(datetime.now()).split('.')[0]

# Ilmoittaa csv-tiedoston sanojen määrän
def dict_size():
	word_count = 0
	with open('eng_fi.db') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			word_count = word_count+1
	return word_count

# Luo dictionary kohteen csv-tiedostosta.
def generate_dict(): 
	dictionary = {}
	with open('eng_fi.db') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		next(csv_reader)
		for row in csv_reader:
			dictionary[row[0]] = row[1]
	return dictionary

def generate_vocabulary():
	pass
