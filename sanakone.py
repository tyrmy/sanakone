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

import string
from prettytable import PrettyTable
import os
import unicodecsv as csv
import time as t
import random as r
from googletrans import Translator

os.chdir('/home/lassi/Python/sanakone1.1/')
dictionary = {}

# Ilmoittaa csv-tiedoston sanojen määrän
def dict_size():
	global dictionary
	return len(dictionary)

# Luo dictionary kohteen csv-tiedostosta.
def dict_from_csv(): # luo dictionary .csv tiedoston pohjalta
	global dictionary
	with open('eng_fi.db') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		next(csv_reader)
		for row in csv_reader:
			dictionary[row[0]] = row[1]
	print("Nykyinen tietokannan koko = " + str(dict_size()) + " sanaa.")

'''	Kysyy satunnaisen sanan dictionaryn sisältä
	Voi ottaa vastaan joko:
		-arvauksen
		-"x" merkin, jolloin tietokantaan voi lisätä uuden sanan
		-"exit", jolloin ohjelma suljetaan
'''
def ask_randoms(amount): 
	global dictionary
	print(u'Kysytään %i sanaa...' % amount)
	picks = r.sample(list(dictionary.items()), amount)
	vastaukset = []
	index = 0
	montakoOikein = 0
	for i in picks:
		index += 1
		print(u'%i. %s' % (index, i[0]))
		vastaus = raw_input("Vastaus: ").decode('utf8')
		if vastaus == i[1].lower():
			vastaukset.append('Oikein! (%s : %s)' % (i[0],i[1]))
			montakoOikein += 1
		else:
			vastaukset.append(u'Väärin! (%s : %s)' % (i[0],i[1]))
	print('\n')
	print('========Tulokset========')
	for i in vastaukset:
		print i
	print('========================')
	print(u'Yhteensä %i/%i oikein!' % (montakoOikein, len(vastaukset)))
	print('========================')

def ask_random(): 
	global dictionary
	pick = r.choice(list(dictionary.items()))
	print(u'Käännä "' + pick[0] + '"')
	vastaus = raw_input("Vastaus: ").decode('utf8')
	if vastaus == "x":
		fix = raw_input("Anna uusi sana: ")
		add_word(fix)
		dict_from_csv()
	elif vastaus == "exit":
		exit()
	else:
		print('Ref: "' + pick[1] + '"')

def print_by_letter(key):
	print('Taulukko %s-kirjaimen mukaan:' % key)
	global dictionary
	word_count = 0
	t = PrettyTable()
	t.field_names = ['Eng','Fi']
	for eng, fi in sorted(dictionary.items()):
		if eng[0] == key:
			t.add_row([eng, fi])
			word_count += 1
	print(t)
	print(u'Yhteensä %s sanaa' % word_count)

def add_word(word):
	global dictionary
	if word not in dictionary:
		with open("eng_fi.db", "a") as fd:
			tr = Translator()
			result = tr.translate(word, dest='fi')
			print(word + "," + result.text)
			output = word + "," + result.text
			fd.write(output.encode('utf-8') + "\n")
	else:
		print('Sana ei kelpaa tai se on jo tietokannassa...')

dict_from_csv()
#for letter in list(string.ascii_lowercase):
#	print_by_letter(letter)
while True:
	ask_random()

#ask_randoms(20)
