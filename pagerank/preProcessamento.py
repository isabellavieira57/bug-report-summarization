#!/usr/bin/python
# coding: utf-8

#-----------------------------------------------------------------------#
# Sumarização Automática de Relatórios de Bug							#
# Desenvolvido por Isabella Vieira Ferreira								#
# POC II - Ciência da Computação - UFSJ									#
#-----------------------------------------------------------------------#

import nltk
import re
from sys import argv, exit
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

#-----------------------------------------------------------------------#
# Função que lê o arquivo. 												#
#-----------------------------------------------------------------------#
def leArquivo():	
	try:
	    if(argv[1] == "-c"):
	        arquivo = open(argv[2], 'r')
	        oraculo = argv[3]
	    else:
	        print "O padrao a ser seguido deve ser:\n"
	        print "python main.py -c <nome_arquivo_entrada> <oraculo>"
	        exit(0)
	except:
	    print "O padrao a ser seguido deve ser:\n"
	    print "python main.py -c <nome_arquivo_entrada> <oraculo>"
	    exit(0)
	
	conteudo = arquivo.readlines()		# conteudo armazena os itens de cada linha
	comentarios = []
	texto = []
	string = ""
	tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')		# Expressao regular que quebra a string em substrings

	# Verifica se é uma linha vazia
	# Se não for, contatena toda a string (comentario), coloca tudo em letra maiuscula, separa os tokens e coloca na lista de comentarios
	for item in conteudo:
		if (item != '\n'):
			string = string + str(item)
			string = re.sub(r'[\xc2\x99]'," ", string)		# expressao regular para remover bad caracteres (\xc2 - espaco)
			string = re.sub(r'[\xe2\x80\x94]'," ", string)	# expressao regular para dash (\xe2\x80\x94 == -)
		else:
			stringUpper = string.lower()
			tokens = tokenizer.tokenize(stringUpper)
			comentarios.append(tokens)
			texto = []
			string = ""
	
	return comentarios, argv[2], oraculo
	
#-----------------------------------------------------------------------------#
# 							 												  #
#-----------------------------------------------------------------------------#
def removeStopWords (comentarios):

	comentariosPreProcessado = []
	listaIntermediaria = []

	stopwords = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'll', 't'}
	
	j = 0

	for i in range(len(comentarios)):
		j=0
		while (j < len(comentarios[i])):
			if comentarios[i][j] not in stopwords:
				listaIntermediaria.append(comentarios[i][j])
			j = j + 1
		comentariosPreProcessado.append(listaIntermediaria)
		listaIntermediaria = []

	return comentariosPreProcessado

#-----------------------------------------------------------------------------#
# 							 												  #
#-----------------------------------------------------------------------------#
def removeCaracteresEspeciais (comentarios):

	comentariosPreProcessado = []
	listaIntermediaria = []

	caracteresEspeciais = {",",".",";","-","_","?","!",":", "(", ")", "/", "|", "=", "[","]", "'", '"', "$", "#","/", "...", "{", "}", "[];", "();", "()", "'s", "..", "->", " ", "-", "'t", "#", "'ll", "<=.", ">=.", "(),", ").", "(."}

	j = 0

	for i in range(len(comentarios)):
		j=0
		while (j < len(comentarios[i])):
			if comentarios[i][j] not in caracteresEspeciais:
				listaIntermediaria.append(comentarios[i][j])
			j = j + 1
		comentariosPreProcessado.append(listaIntermediaria)
		listaIntermediaria = []

	return comentariosPreProcessado

#-----------------------------------------------------------------------------#
# 		 												  					  #
#-----------------------------------------------------------------------------#
def removeNumeros (comentarios):

	listaIntermediaria = []
	comentariosPreProcessado = []

	for i in range(len(comentarios)):		
		j = 1
		listaIntermediaria.append(comentarios[i][0])		#nao remove numeros do nome do usuario
	
		while (j < (len(comentarios[i])-2)):				#nao remove referencia explicita e like
			lista = str(comentarios[i][j])
			x = filter(lambda y: not str.isdigit(y), lista)	# x recebe true ou false se for digito ou nao
			if x != '':										# se x for digito, sera removido e sera uma string vazia
				listaIntermediaria.append(x)				# adiciona na lista se nao for digito
			j = j + 1
		listaIntermediaria.append(comentarios[i][len(comentarios[i])-2])	# adiciona na lista referencia explicita
		listaIntermediaria.append(comentarios[i][len(comentarios[i])-1])	# adiciona na lista like
		comentariosPreProcessado.append(listaIntermediaria)
		listaIntermediaria = []

	return comentariosPreProcessado

#-----------------------------------------------------------------------------#
#					 		 												  #
#-----------------------------------------------------------------------------#
def stemming (comentarios):

	comentariosPreProcessado = []
	listaIntermediaria = []

	#stemmer = PorterStemmer()
	stemmer = SnowballStemmer("english")

	for i in range(len(comentarios)):
		j = 1
		listaIntermediaria.append(comentarios[i][0])		#nao remove numeros do nome do usuario
		while (j < (len(comentarios[i]))):				#nao remove referencia explicita e like
			#comentarioStemmer = stemmer.stem(comentarios[i][j])
			comentarioStemmer = SnowballStemmer("english").stem(comentarios[i][j])
			listaIntermediaria.append(str(comentarioStemmer))
			j = j + 1
		comentariosPreProcessado.append(listaIntermediaria)
		listaIntermediaria = []

	return comentariosPreProcessado
