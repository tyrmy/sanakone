#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
translate.py pitää yllä tietokantaa "eng_fi.db", josta se ottaa
sattumanvaraisesti sanoja kysyen niiden merkitystä. Tietokantaan
voi lisätä sanoja add_word() funtiolla.

Tietokanta on yksinkertainen .csv -tiedosto

Ohjelma toimii python2.7 -versiolla. Tarvitsee toimiakseen
googletrans paketin. (pip install googletrans)

Bash-ohjelma "order" lajittelee tietokannan aakkosjärjestykseen.
Tämä ei ole välttämätöntä ohjelman toimimisen kannalta.
'''

import os
import unicodecsv as csv
import time as t
import random as r
from googletrans import Translator

os.chdir('/home/lassi/Python/sanakone1.1/')
dictionary = set()

# Ilmoittaa csv-tiedoston sanojen määrän
def dict_size():
	word_count = 0
	with open('eng_fi.db') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			word_count = word_count+1
	return word_count

# Luo dictionary kohteen csv-tiedostosta.
def generate_dict(): # luo dictionary .csv tiedoston pohjalta
	dictionary = {}
	with open('eng_fi.db') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		next(csv_reader)
		for row in csv_reader:
			dictionary[row[0]] = row[1]
	return dictionary

'''	Kysyy satunnaisen sanan dictionaryn sisältä
	Voi ottaa vastaan joko:
		-arvauksen
		-"x" merkin, jolloin tietokantaan voi lisätä uuden sanan
		-"exit", jolloin ohjelma suljetaan
'''
def ask_random(): 
	#generate_csv()
	di = generate_dict()
	pick = r.choice(list(di.items()))
	print(u'Käännä "' + pick[0] + '"')
	vastaus = raw_input("Vastaus: ").decode('utf8')
	if vastaus == "x":
		fix = raw_input("Anna uusi sana: ")
		add_word(fix)
		print("Tietokannan koko = " + str(dict_size()) + " sanaa.")
	elif vastaus == "exit":
		exit()
	else:
		print('Ref: "' + pick[1] + '"')

def add_word(word):
	if word not in 
	with open("eng_fi.db", "a") as fd:
		tr = Translator()
		result = tr.translate(word, dest='fi')
		print(word + "," + result.text)
		output = word + "," + result.text
		fd.write(output.encode('utf-8') + "\n")

print("Nykyinen tietokannan koko = " + str(dict_size()) + " sanaa.")
while True:
	ask_random()
