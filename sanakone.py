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
import sys
from googletrans import Translator

info = """
Käyttö:
-r	satunnainen kysely
-k	ohjelman sisäinen kysely
-s	tulosta sanasto terminaaliin
-a      lisää sana tietokantaan
"""
# Tulosta ohjeet jossei parametreja
if ( len(sys.argv) == 1 ):
	print('Parametri puuttuu!')
	#print sys.argv[0]
	print info
	exit()

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
	#print("Nykyinen tietokannan koko = " + str(dict_size()) + " sanaa.")

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
		print('Suljetaan sanakone...')
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
			ehdotus = u'Ehdotus: "%s"? (k/e/v)' % result.text
			vastaus = raw_input(ehdotus.encode(sys.stdout.encoding)).decode('utf-8')
			if vastaus == 'k':
				print(u'Lisättiin "%s,%s"' % ( word, result.text ))
				output = word + ',' + result.text
				fd.write(output.encode('utf-8') + "\n")
			elif vastaus == 'v':
				korvike = raw_input(u'Korvaava: ').decode('utf-8')
				print(u'Lisättiin "%s,%s"' % ( word, korvike))
				output = word + ',' + korvike
				fd.write(output.encode('utf-8') + "\n")
			elif vastaus == 'e':
				print('Keskeytettiin lisääminen...')
			else:
				print('Kelvoton vastaus. Perutaan...')
	else:
		print('Sana ei kelpaa tai se on jo tietokannassa...')

# Tulosta ohje jos enemmän kuin yksi argumentti
if ( len(sys.argv) > 3 ):
        print("Liikaa argumentteja! Suljetaan...")
	print(info)
	exit()
else:
	dict_from_csv()
	if ( sys.argv[1] == '-r' ):
		while True:
			ask_random()
	elif ( sys.argv[1] == '-s' ):
		for letter in list(string.ascii_lowercase):
			print_by_letter(letter)
		exit()
	elif ( sys.argv[1] == '-k' ):
		ask_randoms(20)		
		exit()

        elif ( sys.argv[1] == '-a' ):
                if ( len(sys.argv) == 3 ):
                    add_word(sys.argv[2])
                    print("Tietokannan koko:" + str(dict_size()))
                else:
                    print("Argumenttivirhe! Anna uusi sana parametrin jälkeen.")
		exit()

	else:
		print('Tuntematon parametri!')
		print(info)
		exit()
