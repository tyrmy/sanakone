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
filename = './quizes/quiz_%s.txt' % str(datetime.now()).split('.')[0]

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
	picks = r.sample(list(source.items()), sanaa)

	quizfile = open(filename, 'w')
	quizfile.write('Kysely luotu ' + str(datetime.now()).split('.')[0] + '\n')
	quizfile.write('Tietokannan laajuus on ' + str(dict_size()) + ' sanaa.\n')
	quizfile.write('==============================\n')
	quizfile.write('Kyselyn koko: ' + str(sanaa) + ' sanaa.\n')
	quizfile.write('==============================\n')
	
	index = 1
	for kysymys in picks:
		quizfile.write('\n %d) %s \n' % (index, kysymys[0]))
		answers = []
		answers.append(kysymys[1])
		for i in range(3):
			pick = r.sample(list(source.items()), 1)
			fanswers = pick[0]
			answers.append(fanswers[1])
		r.shuffle(answers)	
		for i in range(4):
			answer = '\t %s) %s \n' % ('ABCD'[i], answers[i])
			quizfile.write(answer.encode('utf-8'))
		index += 1
	
	quizfile.write('\n==============================\n')
	quizfile.write('Kyselyn loppu')
	quizfile.write('\n==============================\n')
generate_quiz(40)
