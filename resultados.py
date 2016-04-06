#!/usr/bin/python
# coding: utf-8

#-----------------------------------------------------------------------#
# Sumarização Automática de Relatórios de Bug							#
# Desenvolvido por Isabella Vieira Ferreira								#
# POC II - Ciência da Computação - UFSJ									#
#-----------------------------------------------------------------------#

from mineracao import *


def resultados (oraculo, nomeArquivo, numeroComentarios, rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF):
	
	arquivoResultados = open("resultados.txt", 'a')
			
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
	arquivoResultados.write("\nRELATORIO DE BUG		PRECISION		RECALL			F-SCORE			ESTUDO\n")	
	arquivoResultados.write("%s		%f		%f		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE DE COSSENO\n" % (nomeArquivo, precision, recall, fscore))	
	
	"""print "Tamanho sumario: ", tamanhoSumario
	print "Tamanho oraculo: ", len(oraculo)
	print "Oraculo: ", oraculo
	print "Ranking: ", rankingMediaDistanciaEuclidianaTituloDescricao
	print "Acertos: ", acertos
	print "Precision ", precision
	print "Recall: ", recall
	print "Fscore: ", fscore"""
			
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
	
	acertos = 0
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
	arquivoResultados.write("%s		%f		%f		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN+CENTRALIDADE AUTOVETOR\n" % (nomeArquivo, precision, recall, fscore))
	
	arquivoResultados.close()
