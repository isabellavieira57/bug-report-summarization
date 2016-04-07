#!/usr/bin/python
# coding: utf-8

#-----------------------------------------------------------------------#
# Sumarização Automática de Relatórios de Bug							#
# Desenvolvido por Isabella Vieira Ferreira								#
# POC II - Ciência da Computação - UFSJ									#
#-----------------------------------------------------------------------#

from mineracao import *
import os


#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def resultadosPrecisionRecallFscore (oraculo, nomeArquivo, numeroComentarios, rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF):
	
	arquivoResultados = open("resultados/resultadosPrecisionRecallFscore.txt", 'a')
			
	# Sumario terá 25% do numero de comentarios
	tamanhoSumario = int(round(numeroComentarios*0.25))
	
	#arquivoResultados.write("\n###################################### RESULTADOS #########################################\n")
	
	#arquivoResultados.write("\nEstudo 1: Ranking Oráculo x Ranking de similaridade da descrição e do título com cada comentário\n")
	#arquivoResultados.write("Estudo 2: Ranking Oráculo x Ranking redes\n")
	#arquivoResultados.write("Estudo 2: Ranking Oráculo x Ranking grupo onde está a descrição\n\n")
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricao[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)
	arquivoResultados.write("\nRELATORIO DE BUG		PRECISION		RECALL			F-SCORE					ESTUDO\n")	
	arquivoResultados.write("%s		%f		%f		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE DE COSSENO\n" % (nomeArquivo, precision, recall, fscore))	
			
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)
	arquivoResultados.write("%s		%f		%f		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE DE COSSENO\n" % (nomeArquivo, precision, recall, fscore))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingMediaDistanciaEuclidianaTituloDescricao[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)
	arquivoResultados.write("%s		%f		%f		%f		(1) ESPAÇO ORIGINAL: DISTÂNCIA EUCLIDIANA\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingMediaDistanciaEuclidianaTituloDescricaoNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)
	arquivoResultados.write("%s		%f		%f		%f		(1) ESPAÇO TRANSFORMADO: DISTÂNCIA EUCLIDIANA\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMassey[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMasseyNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColley[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColleyNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(len(ordenacaoPageRank)):
		if (ordenacaoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, len(ordenacaoPageRank))
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(3) ESPAÇO ORIGINAL: LOUVAIN+PAGERANK\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(len(ordenacaoPageRankNMF)):
		if (ordenacaoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, len(ordenacaoPageRankNMF))
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN+PAGERANK\n" % (nomeArquivo, precision, recall, fscore))	
	
	"""acertos = 0
	for i in range(len(rankingComunidade)):
		if (rankingComunidade[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, len(rankingComunidade))
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(3) ESPAÇO ORIGINAL: LOUVAIN+CENTRALIDADE AUTOVETOR\n" % (nomeArquivo, precision, recall, fscore))
	
	acertos = 0
	for i in range(len(rankingComunidadeNMF)):
		if (rankingComunidadeNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, len(rankingComunidadeNMF))
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s		%f		%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN+CENTRALIDADE AUTOVETOR\n" % (nomeArquivo, precision, recall, fscore))"""
	
	arquivoResultados.close()
	

#-----------------------------------------------------------------------------#
# Resultados Mean Average Precsion											  #
#-----------------------------------------------------------------------------#
def resultadosMAPIndividual (oraculo, nomeArquivo, numeroComentarios, rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF):
		
	originalSimCosseno = open("resultados/resultadosMAP_original_simCosseno.txt", 'a')
	transformadoSimCosseno = open("resultados/resultadosMAP_transformado_simCosseno.txt", 'a')
	
	originalEuclidiana = open("resultados/resultadosMAP_original_euclidiana.txt", 'a')
	transformadoEuclidiana = open("resultados/resultadosMAP_transformado_euclidiana.txt", 'a')
	
	originalPageRank = open("resultados/resultadosMAP_original_pagerank.txt", 'a')
	transformadoPageRank = open("resultados/resultadosMAP_transformado_pagerank.txt", 'a')
	
	originalMassey = open("resultados/resultadosMAP_original_massey.txt", 'a')
	transformadoMassey = open("resultados/resultadosMAP_transformado_massey.txt", 'a')
	
	originalColley = open("resultados/resultadosMAP_original_colley.txt", 'a')
	transformadoColley = open("resultados/resultadosMAP_transformado_colley.txt", 'a')
	
	originalLouvainPageRank = open("resultados/resultadosMAP_original_louvainPageRank.txt", 'a')
	transformadoLouvainPageRank = open("resultados/resultadosMAP_transformado_louvainPageRank.txt", 'a')
	
	arquivo = nomeArquivo.split("_")
	nomeProjeto = arquivo[0]
	
	acuracia = 0.0
	totalRelatoriosBugProjeto = 5
			
	# Sumario terá 25% do numero de comentarios
	tamanhoSumario = int(round(numeroComentarios*0.25))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricao[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalSimCosseno.write("%s		%f		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE DE COSSENO\n" % (nomeArquivo, acuracia, MAP))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoSimCosseno.write("%s		%f		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE DE COSSENO\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingMediaDistanciaEuclidianaTituloDescricao[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalEuclidiana.write("%s		%f		%f		(1) ESPAÇO ORIGINAL: DISTÂNCIA EUCLIDIANA\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingMediaDistanciaEuclidianaTituloDescricaoNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoEuclidiana.write("%s		%f		%f		(1) ESPAÇO TRANSFORMADO: DISTÂNCIA EUCLIDIANA\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalPageRank.write("%s		%f		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoPageRank.write("%s		%f		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMassey[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalMassey.write("%s		%f		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMasseyNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoMassey.write("%s		%f		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColley[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalColley.write("%s		%f		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColleyNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoColley.write("%s		%f		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (nomeArquivo, acuracia, MAP))
	
	acertos = 0
	for i in range(len(ordenacaoPageRank)):
		if (ordenacaoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalLouvainPageRank.write("%s		%f		%f		(3) ESPAÇO ORIGINAL: LOUVAIN+PAGERANK\n" % (nomeProjeto, acuracia, MAP))
	
	acertos = 0
	for i in range(len(ordenacaoPageRankNMF)):
		if (ordenacaoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoLouvainPageRank.write("%s		%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN+PAGERANK\n" % (nomeProjeto, acuracia, MAP))
	
	"""acertos = 0
	for i in range(len(rankingComunidade)):
		if (rankingComunidade[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	arquivoResultados.write("%s		%f		%f		(3) ESPAÇO ORIGINAL: LOUVAIN+CENTRALIDADE AUTOVETOR\n" % (nomeProjeto, acuracia, MAP))
	
	acertos = 0
	for i in range(len(rankingComunidadeNMF)):
		if (rankingComunidadeNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	arquivoResultados.write("%s		%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN+CENTRALIDADE AUTOVETOR\n" % (nomeProjeto, acuracia, MAP))"""
	
	originalSimCosseno.close()
	transformadoSimCosseno.close()
	originalEuclidiana.close()
	transformadoEuclidiana.close()
	originalPageRank.close()
	transformadoPageRank.close()
	originalMassey.close()
	transformadoMassey.close()
	originalColley.close()
	transformadoColley.close()
	originalLouvainPageRank.close()
	transformadoLouvainPageRank.close()
	
#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#	
def leArquivoMAPIndividual (arquivo):
	
	linha = arquivo.readlines()	# possui todas as linhas do arquivo em um vetor
	
	MAP = []
	
	for conteudo in linha:
		tokens = conteudo.split("		")
		MAP.append(float(tokens[2]))
			
	somatorioMAPAngular = 0
	i=0
	while (i<5):
		somatorioMAPAngular = somatorioMAPAngular + MAP[i]
		i = i + 1
	
	somatorioMAPJquery = 0
	i = 5
	while (i<10):
		somatorioMAPJquery = somatorioMAPJquery + MAP[i]
		i = i + 1
	
	somatorioMAPBootstrap = 0
	i = 10
	while (i<15):
		somatorioMAPBootstrap = somatorioMAPBootstrap + MAP[i]
		i = i + 1

	
	return somatorioMAPAngular, somatorioMAPJquery, somatorioMAPBootstrap
	
	
#-----------------------------------------------------------------------------#
# Resultados Mean Average Precsion											  #
#-----------------------------------------------------------------------------#
def resultadosMAPGeral ():
	
	acuracia = 0.0
	
	arquivoResultados = open("resultados/resultadosMAP.txt", 'a')
	arquivoResultados.write("\nPROJETO		ACURACIA		MAP				ESTUDO\n\n")
	
	originalSimCosseno = open("resultados/resultadosMAP_original_simCosseno.txt", 'r')
	retorno = leArquivoMAPIndividual(originalSimCosseno)
	arquivoResultados.write("ANGULAR		%f		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE COSSENO\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE COSSENO\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE COSSENO\n\n\n" % (acuracia, retorno[2]))
	
	transformadoSimCosseno = open("resultados/resultadosMAP_transformado_simCosseno.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoSimCosseno)
	arquivoResultados.write("ANGULAR		%f		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE COSSENO\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE COSSENO\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE COSSENO\n\n\n" % (acuracia, retorno[2]))
	
	originalEuclidiana = open("resultados/resultadosMAP_original_euclidiana.txt", 'r')
	retorno = leArquivoMAPIndividual(originalEuclidiana)
	arquivoResultados.write("ANGULAR		%f		%f		(1) ESPAÇO ORIGINAL: DISTANCIA EUCLIDIANA\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(1) ESPAÇO ORIGINAL: DISTANCIA EUCLIDIANA\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(1) ESPAÇO ORIGINAL: DISTANCIA EUCLIDIANA\n\n\n" % (acuracia, retorno[2]))
	
	transformadoEuclidiana = open("resultados/resultadosMAP_transformado_euclidiana.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoEuclidiana)
	arquivoResultados.write("ANGULAR		%f		%f		(1) ESPAÇO TRANSFORMADO: DISTANCIA EUCLIDIANA\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(1) ESPAÇO TRANSFORMADO: DISTANCIA EUCLIDIANA\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(1) ESPAÇO TRANSFORMADO: DISTANCIA EUCLIDIANA\n\n\n" % (acuracia, retorno[2]))
	
	originalPageRank = open("resultados/resultadosMAP_original_pagerank.txt", 'r')
	retorno = leArquivoMAPIndividual(originalPageRank)
	arquivoResultados.write("ANGULAR		%f		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n\n\n" % (acuracia, retorno[2]))
	
	transformadoPageRank = open("resultados/resultadosMAP_transformado_pagerank.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoPageRank)
	arquivoResultados.write("ANGULAR		%f		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n\n\n" % (acuracia, retorno[2]))
	
	originalMassey = open("resultados/resultadosMAP_original_massey.txt", 'r')
	retorno = leArquivoMAPIndividual(originalMassey)
	arquivoResultados.write("ANGULAR		%f		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(2) ESPAÇO ORIGINAL: MASSEY\n\n\n" % (acuracia, retorno[2]))
	
	transformadoMassey = open("resultados/resultadosMAP_transformado_massey.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoMassey)
	arquivoResultados.write("ANGULAR		%f		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n\n\n" % (acuracia, retorno[2]))
	
	originalColley = open("resultados/resultadosMAP_original_colley.txt", 'r')
	retorno = leArquivoMAPIndividual(originalColley)
	arquivoResultados.write("ANGULAR		%f		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(2) ESPAÇO ORIGINAL: COLLEY\n\n\n" % (acuracia, retorno[2]))
	
	transformadoColley = open("resultados/resultadosMAP_transformado_colley.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoColley)
	arquivoResultados.write("ANGULAR		%f		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n\n\n" % (acuracia, retorno[2]))

	originalLouvainPageRank = open("resultados/resultadosMAP_original_louvainPageRank.txt", 'r')
	retorno = leArquivoMAPIndividual(originalLouvainPageRank)
	arquivoResultados.write("ANGULAR		%f		%f		(3) ESPAÇO ORIGINAL: LOUVAIN + PAGERANK\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(3) ESPAÇO ORIGINAL: LOUVAIN + PAGERANK\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(3) ESPAÇO ORIGINAL: LOUVAIN + PAGERANK\n\n\n" % (acuracia, retorno[2]))
	
	transformadoLouvainPageRank = open("resultados/resultadosMAP_transformado_louvainPageRank.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoLouvainPageRank)
	arquivoResultados.write("ANGULAR		%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + PAGERANK\n" % (acuracia, retorno[0]))
	arquivoResultados.write("JQUERY		%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + PAGERANK\n" % (acuracia, retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + PAGERANK\n\n\n" % (acuracia, retorno[2]))
	
	arquivoResultados.close()
	originalSimCosseno.close()
	transformadoSimCosseno.close()
	originalEuclidiana.close()
	transformadoEuclidiana.close()
	originalPageRank.close()
	transformadoPageRank.close()
	originalMassey.close()
	transformadoMassey.close()
	originalColley.close()
	transformadoColley.close()
	originalLouvainPageRank.close()
	transformadoLouvainPageRank.close()
	
	os.remove("resultados/resultadosMAP_original_simCosseno.txt")
	os.remove("resultados/resultadosMAP_transformado_simCosseno.txt")
	os.remove("resultados/resultadosMAP_original_euclidiana.txt")
	os.remove("resultados/resultadosMAP_transformado_euclidiana.txt")	
	os.remove("resultados/resultadosMAP_original_pagerank.txt")
	os.remove("resultados/resultadosMAP_transformado_pagerank.txt")
	os.remove("resultados/resultadosMAP_original_massey.txt")
	os.remove("resultados/resultadosMAP_transformado_massey.txt")
	os.remove("resultados/resultadosMAP_original_colley.txt")
	os.remove("resultados/resultadosMAP_transformado_colley.txt")
	os.remove("resultados/resultadosMAP_original_louvainPageRank.txt")
	os.remove("resultados/resultadosMAP_transformado_louvainPageRank.txt")
