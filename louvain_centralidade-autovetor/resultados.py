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
def resultadosPrecisionRecallFscore (oraculo, nomeArquivo, numeroComentarios, resultadoPageRank, resultadoPageRankNMF):
	
	arquivoResultados = open("resultados/resultadosMetricas/resultadosPrecisionRecallFscore.txt", 'a')
			
	# Sumario terá 25% do numero de comentarios
	#tamanhoSumario = int(round(numeroComentarios*0.25))
	tamanhoSumario = 0

	if ( len(resultadoPageRank) < 10 ):
		tamanhoSumario = len(resultadoPageRank)
	else:
		tamanhoSumario = 10
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("\nRELATORIO DE BUG		PRECISION		RECALL			F-SCORE			ESTUDO\n")
	arquivoResultados.write("%s				%f		%f		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (nomeArquivo, precision, recall, fscore))	
	
	tamanhoSumario = len(resultadoPageRankNMF)

	if ( len(resultadoPageRankNMF) < 10 ):
		tamanhoSumario = len(resultadoPageRankNMF)
	else:
		tamanhoSumario = 10

	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s				%f		%f		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n\n" % (nomeArquivo, precision, recall, fscore))	
	
	"""acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMassey[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s				%f		%f		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMasseyNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s				%f		%f		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColley[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s				%f		%f		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (nomeArquivo, precision, recall, fscore))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColleyNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	recall = calculaRecall (acertos, len(oraculo))
	fscore = calculaFscore(precision, recall)	
	arquivoResultados.write("%s				%f		%f		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (nomeArquivo, precision, recall, fscore))"""	
	
	
	arquivoResultados.close()
	

#-----------------------------------------------------------------------------#
# Resultados Mean Average Precsion											  #
#-----------------------------------------------------------------------------#
def resultadosMAPIndividual (oraculo, nomeArquivo, numeroComentarios, rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF):
		
	originalSimCosseno = open("resultados/resultadosMetricas/resultadosMAP_original_simCosseno.txt", 'a')
	transformadoSimCosseno = open("resultados/resultadosMetricas/resultadosMAP_transformado_simCosseno.txt", 'a')
	
	originalEuclidiana = open("resultados/resultadosMetricas/resultadosMAP_original_euclidiana.txt", 'a')
	transformadoEuclidiana = open("resultados/resultadosMetricas/resultadosMAP_transformado_euclidiana.txt", 'a')
	
	originalPageRank = open("resultados/resultadosMetricas/resultadosMAP_original_pagerank.txt", 'a')
	transformadoPageRank = open("resultados/resultadosMetricas/resultadosMAP_transformado_pagerank.txt", 'a')
	
	originalMassey = open("resultados/resultadosMetricas/resultadosMAP_original_massey.txt", 'a')
	transformadoMassey = open("resultados/resultadosMetricas/resultadosMAP_transformado_massey.txt", 'a')
	
	originalColley = open("resultados/resultadosMetricas/resultadosMAP_original_colley.txt", 'a')
	transformadoColley = open("resultados/resultadosMetricas/resultadosMAP_transformado_colley.txt", 'a')
	
	originalLouvainPageRank = open("resultados/resultadosMetricas/resultadosMAP_original_louvainPageRank.txt", 'a')
	transformadoLouvainPageRank = open("resultados/resultadosMetricas/resultadosMAP_transformado_louvainPageRank.txt", 'a')
	
	originalLouvainCentralidade = open("resultados/resultadosMetricas/resultadosMAP_original_louvainCentralidade.txt", 'a')
	transformadoLouvainCentralidade = open("resultados/resultadosMetricas/resultadosMAP_transformado_louvainCentralidade.txt", 'a')
	
	arquivo = nomeArquivo.split("_")
	nomeProjeto = arquivo[0]
	
	totalRelatoriosBugProjeto = 5
			
	# Sumario terá 25% do numero de comentarios
	#tamanhoSumario = int(round(numeroComentarios*0.25))
	tamanhoSumario = 10
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricao[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalSimCosseno.write("%s		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE DE COSSENO\n" % (nomeArquivo, MAP))	
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoSimCosseno.write("%s		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE DE COSSENO\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingMediaDistanciaEuclidianaTituloDescricao[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalEuclidiana.write("%s		%f		(1) ESPAÇO ORIGINAL: DISTÂNCIA EUCLIDIANA\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (rankingMediaDistanciaEuclidianaTituloDescricaoNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoEuclidiana.write("%s		%f		(1) ESPAÇO TRANSFORMADO: DISTÂNCIA EUCLIDIANA\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalPageRank.write("%s		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoPageRank.write("%s		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMassey[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalMassey.write("%s		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoMasseyNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoMassey.write("%s		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColley[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalColley.write("%s		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(tamanhoSumario):
		if (resultadoColleyNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoColley.write("%s		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(len(ordenacaoPageRank)):
		if (ordenacaoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalLouvainPageRank.write("%s		%f		(3) ESPAÇO ORIGINAL: LOUVAIN+PAGERANK\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(len(ordenacaoPageRankNMF)):
		if (ordenacaoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoLouvainPageRank.write("%s		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN+PAGERANK\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(len(rankingComunidade)):
		if (rankingComunidade[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	originalLouvainCentralidade.write("%s		%f		(3) ESPAÇO ORIGINAL: LOUVAIN+CENTRALIDADE AUTOVETOR\n" % (nomeArquivo, MAP))
	
	acertos = 0
	for i in range(len(rankingComunidadeNMF)):
		if (rankingComunidadeNMF[i][0] in oraculo):
			acertos = acertos + 1
	MAP = calculaMAP(acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto)
	transformadoLouvainCentralidade.write("%s		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN+CENTRALIDADE AUTOVETOR\n" % (nomeArquivo, MAP))
	
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
	originalLouvainCentralidade.close()
	transformadoLouvainCentralidade.close()
	
#-----------------------------------------------------------------------------#
# Resultados Mean Average Precsion											  #
#-----------------------------------------------------------------------------#
def resultadosMAPGeral ():
	

	arquivoResultados = open("resultados/resultadosMetricas/resultadosMAP.txt", 'a')
	arquivoResultados.write("\nPROJETO		MAP				ESTUDO\n\n")
	
	originalSimCosseno = open("resultados/resultadosMetricas/resultadosMAP_original_simCosseno.txt", 'r')
	retorno = leArquivoMAPIndividual(originalSimCosseno)
	arquivoResultados.write("ANGULAR		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE COSSENO\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE COSSENO\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(1) ESPAÇO ORIGINAL: SIMILARIDADE COSSENO\n\n\n" % (retorno[2]))
	
	transformadoSimCosseno = open("resultados/resultadosMetricas/resultadosMAP_transformado_simCosseno.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoSimCosseno)
	arquivoResultados.write("ANGULAR		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE COSSENO\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE COSSENO\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(1) ESPAÇO TRANSFORMADO: SIMILARIDADE COSSENO\n\n\n" % (retorno[2]))
	
	originalEuclidiana = open("resultados/resultadosMetricas/resultadosMAP_original_euclidiana.txt", 'r')
	retorno = leArquivoMAPIndividual(originalEuclidiana)
	arquivoResultados.write("ANGULAR		%f		(1) ESPAÇO ORIGINAL: DISTANCIA EUCLIDIANA\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(1) ESPAÇO ORIGINAL: DISTANCIA EUCLIDIANA\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(1) ESPAÇO ORIGINAL: DISTANCIA EUCLIDIANA\n\n\n" % (retorno[2]))
	
	transformadoEuclidiana = open("resultados/resultadosMetricas/resultadosMAP_transformado_euclidiana.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoEuclidiana)
	arquivoResultados.write("ANGULAR		%f		(1) ESPAÇO TRANSFORMADO: DISTANCIA EUCLIDIANA\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(1) ESPAÇO TRANSFORMADO: DISTANCIA EUCLIDIANA\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(1) ESPAÇO TRANSFORMADO: DISTANCIA EUCLIDIANA\n\n\n" % (retorno[2]))
	
	originalPageRank = open("resultados/resultadosMetricas/resultadosMAP_original_pagerank.txt", 'r')
	retorno = leArquivoMAPIndividual(originalPageRank)
	arquivoResultados.write("ANGULAR		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(2) ESPAÇO ORIGINAL: PAGERANK\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(2) ESPAÇO ORIGINAL: PAGERANK\n\n\n" % (retorno[2]))
	
	transformadoPageRank = open("resultados/resultadosMetricas/resultadosMAP_transformado_pagerank.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoPageRank)
	arquivoResultados.write("ANGULAR		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(2) ESPAÇO TRANSFORMADO: PAGERANK\n\n\n" % (retorno[2]))
	
	originalMassey = open("resultados/resultadosMetricas/resultadosMAP_original_massey.txt", 'r')
	retorno = leArquivoMAPIndividual(originalMassey)
	arquivoResultados.write("ANGULAR		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(2) ESPAÇO ORIGINAL: MASSEY\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(2) ESPAÇO ORIGINAL: MASSEY\n\n\n" % (retorno[2]))
	
	transformadoMassey = open("resultados/resultadosMetricas/resultadosMAP_transformado_massey.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoMassey)
	arquivoResultados.write("ANGULAR		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(2) ESPAÇO TRANSFORMADO: MASSEY\n\n\n" % (retorno[2]))
	
	originalColley = open("resultados/resultadosMetricas/resultadosMAP_original_colley.txt", 'r')
	retorno = leArquivoMAPIndividual(originalColley)
	arquivoResultados.write("ANGULAR		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(2) ESPAÇO ORIGINAL: COLLEY\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(2) ESPAÇO ORIGINAL: COLLEY\n\n\n" % (retorno[2]))
	
	transformadoColley = open("resultados/resultadosMetricas/resultadosMAP_transformado_colley.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoColley)
	arquivoResultados.write("ANGULAR		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(2) ESPAÇO TRANSFORMADO: COLLEY\n\n\n" % (retorno[2]))

	originalLouvainPageRank = open("resultados/resultadosMetricas/resultadosMAP_original_louvainPageRank.txt", 'r')
	retorno = leArquivoMAPIndividual(originalLouvainPageRank)
	arquivoResultados.write("ANGULAR		%f		(3) ESPAÇO ORIGINAL: LOUVAIN + PAGERANK\n" % ( retorno[0]))
	arquivoResultados.write("JQUERY		%f		(3) ESPAÇO ORIGINAL: LOUVAIN + PAGERANK\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(3) ESPAÇO ORIGINAL: LOUVAIN + PAGERANK\n\n\n" % (retorno[2]))
	
	transformadoLouvainPageRank = open("resultados/resultadosMetricas/resultadosMAP_transformado_louvainPageRank.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoLouvainPageRank)
	arquivoResultados.write("ANGULAR		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + PAGERANK\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + PAGERANK\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + PAGERANK\n\n\n" % (retorno[2]))
	
	originalLouvainCentralidade = open("resultados/resultadosMetricas/resultadosMAP_original_louvainCentralidade.txt", 'r')
	retorno = leArquivoMAPIndividual(originalLouvainCentralidade)
	arquivoResultados.write("ANGULAR		%f		(3) ESPAÇO ORIGINAL: LOUVAIN + CENTRALIDADE AUTOVETOR\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(3) ESPAÇO ORIGINAL: LOUVAIN + CENTRALIDADE AUTOVETOR\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(3) ESPAÇO ORIGINAL: LOUVAIN + CENTRALIDADE AUTOVETOR\n\n\n" % (retorno[2]))
	
	transformadoLouvainCentralidade = open("resultados/resultadosMetricas/resultadosMAP_transformado_louvainCentralidade.txt", 'r')
	retorno = leArquivoMAPIndividual(transformadoLouvainCentralidade)
	arquivoResultados.write("ANGULAR		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + CENTRALIDADE AUTOVETOR\n" % (retorno[0]))
	arquivoResultados.write("JQUERY		%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + CENTRALIDADE AUTOVETOR\n" % (retorno[1]))
	arquivoResultados.write("BOOTSTRAP	%f		(3) ESPAÇO TRANSFORMADO: LOUVAIN + CENTRALIDADE AUTOVETOR\n\n\n" % (retorno[2]))
	
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
	originalLouvainCentralidade.close()
	transformadoLouvainCentralidade.close()
	
	# Deleta os arquivos txt
	os.remove("resultados/resultadosMetricas/resultadosMAP_original_simCosseno.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_transformado_simCosseno.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_original_euclidiana.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_transformado_euclidiana.txt")	
	os.remove("resultados/resultadosMetricas/resultadosMAP_original_pagerank.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_transformado_pagerank.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_original_massey.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_transformado_massey.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_original_colley.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_transformado_colley.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_original_louvainPageRank.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_transformado_louvainPageRank.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_original_louvainCentralidade.txt")
	os.remove("resultados/resultadosMetricas/resultadosMAP_transformado_louvainCentralidade.txt")
	
#-----------------------------------------------------------------------------#
#					 		 												  #
#-----------------------------------------------------------------------------#
def salvaDadosArquivoTXT (dados, comentarios, nomeArquivo, nomeRelatorioBug):
	
	#print "NOME RELATORIO BUG ", nomeRelatorioBug
	
	arquivo = open("resultados/resultadosRanking/" + nomeArquivo + "_" + nomeRelatorioBug + ".txt", 'w')
	
	for i in range(len(dados)):
		#if ( dados[i][0] != 0 ):
		arquivo.write(str(dados[i][0])+"\n")

	arquivo = open("resultados/resultadosRanking/" + nomeArquivo + "_" + nomeRelatorioBug + "_comentarios.txt", 'w')

	for i in range(len(dados)):
		arquivo.write(str(dados[i][0]) + "\n" + str(comentarios[dados[i][0]])+"\n\n")
	
