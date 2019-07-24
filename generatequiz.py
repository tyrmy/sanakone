#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
generatequiz.py tuottaa tulostettavan kyselyn eng_fi.db tietokannan pohjalta.
'''

import os
from datetime import datetime
import unicodecsv as csv
import time as t
import random as r

os.chdir('/home/lassi/Python/sanakone1.1/')

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

def generate_quiz(sanaa):
	source = generate_dict()

	quizfile = open('quiz.txt', 'w')
	quizfile.write('Kysely luotu ' + str(datetime.now()).split('.')[0] + '\n')
	quizfile.write('Tietokannan laajuus on ' + str(dict_size()) + ' sanaa.\n')
	quizfile.write('Kyselyn koko: ' + str(sanaa) + ' sanaa.\n')
	quizfile.write('==============================\n')
	
	for kysymys in range(sanaa):
		quizfile.write('\n Kysymys #' + str(kysymys+1) + ' \n')
		for i in range(4):
			quizfile.write('\t %s) jotain \n' % 'ABCD'[i])
	
	quizfile.write('\n==============================\n')
	quizfile.write('Kyselyn loppu')
	quizfile.write('\n==============================\n')
generate_quiz(3)

