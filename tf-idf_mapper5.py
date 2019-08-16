#!/usr/bin/env python
#coding: utf-8

from __future__ import print_function
from __future__ import division
import sys
import re

words=[]
doc_id=0;
line_number=1
wordcount = 1
wordcount_per_doc = 0
df_t=1

for line in sys.stdin:
	'''
	0. ***INPUT DATA*** | récupère le contenu de chaque fichier texte sur la sortie stdin
	1. Associe un ID au document lu
	2. Tokénise en mots
	3. Formatte chaque mot extrait
	4. Ajoute les mots de la ligne à la liste complète de mots
	5. Calcule le nombre de mot dans le document analysé
	6. ***OUTPUT DATA*** | Chaque mot est retourné sur stdout sur la forme suivante :
	    - <key>\t<value>
	    - <key> : 'word',docid
	    - <value> : wordcount,wordcount_per_doc, df_t
	'''
	# Supprimer les espaces
	line = line.strip()


