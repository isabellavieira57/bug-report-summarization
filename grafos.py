#!/usr/bin/python
# coding: utf-8

#-----------------------------------------------------------------------#
# Sumarização Automática de Relatórios de Bug							#
# Desenvolvido por Isabella Vieira Ferreira								#
# POC II - Ciência da Computação - UFSJ									#
#-----------------------------------------------------------------------#

#-----------------------------------------------------------------------#
# Estrutura de dados:													#
#      [[tokens_comentarios, referencia_explicita, like]]				#
# Onde:																	#
#	- tokens_comentarios = tokens do comentario							#
#	- referencia_explicita = index do comentario referenciado ou -1 se  #
# nao possui referencia													#
#	- like = 1 se possui like e 0 se nao possui like                    #
#-----------------------------------------------------------------------#

import numpy as np
import cairo
from igraph import *
	
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def inicializaGrafo ():

	rede = Graph.Read_Ncol('grafo.txt', names=True, weights=True, directed=False)

	return rede

#-----------------------------------------------------------------------------#
# Community_multilevel retorna uma lista de VertexClustering				  #
#-----------------------------------------------------------------------------#
def louvain (rede):

	louvain = rede.community_multilevel(weights=rede.es["weight"], return_levels=False)

	return louvain

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
"""def drawingGraph (rede):

	layout=rede.layout("lgl")
	plot (rede, "graph.pdf", layout=layout)"""

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def thresholdModularidade (matrizSimilaridadeCosseno, tamanhoComentarios):

	arquivoResultadosModularidadeVsThreshold = open("modularidadeVsThreshold", 'w')

	modularidade = 0
	thresholdIdeal = 0.00000

	copiaMatrizSimilaridadeCosseno = []
	copiaMatrizSimilaridadeCosseno = inicializaMatriz (matrizSimilaridadeCosseno)
	fazCopiaMatrizSimilaridadeCosseno(matrizSimilaridadeCosseno, copiaMatrizSimilaridadeCosseno)

	threshold = 0.0	# nao eliminando nada

	while (threshold <= 1.0):
		for i in range(len(matrizSimilaridadeCosseno)):
			for j in range(len(matrizSimilaridadeCosseno)):
				if (matrizSimilaridadeCosseno[i][j] < threshold):
					copiaMatrizSimilaridadeCosseno[i][j] = 0

		salvaMatrizSimilaridadeCosseno (copiaMatrizSimilaridadeCosseno, tamanhoComentarios)
		rede = inicializaGrafo ()
		resultLouvain = louvain(rede)

		arquivoResultadosModularidadeVsThreshold.write("%0.1f %f\n" % (threshold, resultLouvain.modularity))

		if (resultLouvain.modularity > modularidade):
			thresholdIdeal = threshold
			modularidade = resultLouvain.modularity

		threshold = threshold + 0.1
		
	arquivoResultadosModularidadeVsThreshold.close()

	return thresholdIdeal

#-----------------------------------------------------------------------------#
# O threshold é calculado por outra função									  #
#-----------------------------------------------------------------------------#
"""def aumentaEsparcidadeMatriz (matrizSimilaridadeCosseno, threshold):

	for i in range(len(matrizSimilaridadeCosseno)):
		for j in range(len(matrizSimilaridadeCosseno)):
			if (matrizSimilaridadeCosseno[i][j] < threshold):
				matrizSimilaridadeCosseno[i][j] = 0
			if (matrizSimilaridadeCosseno[i][j] >= threshold):
				matrizSimilaridadeCosseno[i][j] = 1 """

#-----------------------------------------------------------------------------#
# evcent: Calculates the eigenvector centralities of the vertices in a graph. #	    					 				
#-----------------------------------------------------------------------------#
def centralidade_autovetor (rede):

	centrality_eigenvector = rede.evcent(directed=False, scale=True, weights=rede.es["weight"], return_eigenvalue=False)

	#print "peso", rede.es["weight"]
	
	return centrality_eigenvector

#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def rankingIntraComunidade (centrality_eigenvector, resultLouvain):

	ranking = []
	vetorIntermerdiario = []
	vetor = []

	for i in range(len(resultLouvain)):			# percorre cada comunidade
		for j in range(len(resultLouvain[i])):	# percorre cada elemento da comunidade
			vetor.append(resultLouvain[i][j])	# id do comentario
			vetor.append(centrality_eigenvector[resultLouvain[i][j]])	# autovetor de centralidade
			vetorIntermerdiario.append(vetor)
			vetor = []
 		ranking.append(sorted(vetorIntermerdiario, key=operator.itemgetter(1), reverse=True))# ordena pelo autovetor em ordem descrescente
 		vetorIntermerdiario = []

 	return ranking
 	
#-----------------------------------------------------------------------------#
# Verifica se cluster possui a descrição									  #
#-----------------------------------------------------------------------------#
def verificaClusterPossuiDescricao (resultLouvain):
	
	for i in range(len(resultLouvain)):			# percorre cada comunidade
			if 0 in resultLouvain[i]:
				return i
	
#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def clusterImportante (mediaDescricaoTitulo, resultLouvain):

	similaridadeElementosCluster = []
	vetorIntermerdiario = []
	mediaSimilaridadesPorCluster = []

	# Vetor similaridadeCluster possui a media da similaridade do titulo e descricao dos comentarios daquele cluster
	for i in range(len(resultLouvain)):			# percorre cada comunidade
		for j in range(len(resultLouvain[i])):	# percorre cada elemento da comunidade
			vetorIntermerdiario.append(mediaDescricaoTitulo[resultLouvain[i][j]])
		similaridadeElementosCluster.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	for i in range(len(similaridadeElementosCluster)):
		vetorIntermerdiario.append(i)
		vetorIntermerdiario.append(np.mean(similaridadeElementosCluster[i]))	
		mediaSimilaridadesPorCluster.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	# ordena pelas similaridades em ordem descrescente
	ranking = sorted(mediaSimilaridadesPorCluster, key=operator.itemgetter(1), reverse=True) 

	return ranking
	
#-----------------------------------------------------------------------------#
# Conta quantos valores possuem os intervalos de similaridade				  #
#-----------------------------------------------------------------------------#
def contaIntervalosSimilaridade (matrizSimilaridadeCosseno):
	
	contaIntervalos = open("intervalosSimilaridade.txt", 'w')
	
	intervalos = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5,	0.6, 0.7, 0.8, 0.9, 1.0]
	
	contador = 0
	for i in range(len(intervalos)):
		for j in range(len(matrizSimilaridadeCosseno)):
			contador = contador + matrizSimilaridadeCosseno[j].count(intervalos[i])
		contaIntervalos.write("%0.1f %d \n" % (intervalos[i], contador))
		contador = 0
		
#-----------------------------------------------------------------------------#
# Já tenho o threshold ideal para deixar a matriz mais esparsa calculado pela #
# funcao thresholdModularidade												  #
#-----------------------------------------------------------------------------#
def aumentaEsparcidadeMatriz (matrizSimilaridadeCosseno):

	threshold = 0.2

	for i in range(len(matrizSimilaridadeCosseno)):
		for j in range(len(matrizSimilaridadeCosseno)):
			if (matrizSimilaridadeCosseno[i][j] < threshold):
				matrizSimilaridadeCosseno[i][j] = 0
			if (matrizSimilaridadeCosseno[i][j] >= threshold):
				matrizSimilaridadeCosseno[i][j] = 1
				
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def agrupaComentarios (comentarios, matrizSimilaridadeCosseno, threshold):

	# comentariosAgrupados possui a linha e coluna dos comentarios que possuem simlaridade >= threshold
	comentariosAgrupados = []
	linhaColuna = []

	for i in range(len(matrizSimilaridadeCosseno)):		
		j = i + 1
		while (j < (len(matrizSimilaridadeCosseno))):
			if (matrizSimilaridadeCosseno[i][j] >= threshold):
				linhaColuna.append(i)
				linhaColuna.append(j)
				comentariosAgrupados.append(linhaColuna)
			linhaColuna = []
			j = j + 1

	return comentariosAgrupados
	
#-----------------------------------------------------------------------------#
# Retorna a ordenacao dos autovalores										  #
# Estrutura: [indice_comentario, autovalor_daquele_comentario]				  #
#-----------------------------------------------------------------------------#
def ordenaRanking (resultadoParaOrdenar):
	
	listaIntermediaria = []
	matriz = []
	
	for i in range(len(resultadoParaOrdenar)):
		listaIntermediaria.append(i)
		listaIntermediaria.append(resultadoParaOrdenar[i])
		matriz.append(listaIntermediaria)
		listaIntermediaria = []

	# ordena pelas similaridades em ordem descrescente
	ranking = sorted(matriz, key=operator.itemgetter(1), reverse=True) 
	
	return ranking
	
#-----------------------------------------------------------------------------#
# Ordena a similaridade média entre titulo e descricao de todos os comentarios# 
# para comparar com oráculo													  #
#-----------------------------------------------------------------------------#
def rankingSimilaridadeMediaComentarioTituloDescricao (mediaDescricaoTitulo):
	
	ranking = ordenaRanking(mediaDescricaoTitulo)
	
	return ranking
	
	
#-----------------------------------------------------------------------------#
# PageRank: retorna o autovalor de cada comentario 							  #
#-----------------------------------------------------------------------------#
def pageRank (rede):
	
	# Resultado == o autovalor de cada comentario (indice resultado == indice comentario)
	resultado = rede.pagerank(vertices=None, directed=False, weights=rede.es["weight"])
	
	rankingPageRank = ordenaRanking(resultado)
	
	return rankingPageRank	

#-----------------------------------------------------------------------------#
# 												 							  #
#-----------------------------------------------------------------------------#
def pageRankIntraCluster (resultLouvain, rede):
	
	resultadoPageRank = []
	listaIntermediaria = []
	matriz = []
	matrizIDPageRank = []
	ranking = []
	
	# calculo o page rank dos elementos de cada comunidade
	for i in range(len(resultLouvain)):			# percorre cada comunidade
		resultadoPageRank.append(rede.pagerank(vertices=resultLouvain[i], directed=False, weights=rede.es["weight"]))
		
	#print "PAGERANK INTRACLUSTER\n", resultadoPageRank
	
	# crio uma lista com o id do comentario e o respectivo pagerank
	for i in range(len(resultadoPageRank)):
		for j in range(len(resultadoPageRank[i])):
			listaIntermediaria.append(resultLouvain[i][j])
			listaIntermediaria.append(resultadoPageRank[i][j])
			matriz.append(listaIntermediaria)
			listaIntermediaria = []
		matrizIDPageRank.append(matriz)
		matriz = []
		
	#print "PAGE RANK INTRACLUSTER COM ID\n", matrizIDPageRank
		
	# ordena os resultados do pagerank de cada cluster
	for i in range(len(matrizIDPageRank)):
		ranking.append(sorted(matrizIDPageRank[i], key=operator.itemgetter(1), reverse=True))
	
	#print "RESULTADOS ORDENADOS \n", ranking
	
	return ranking
	
#-----------------------------------------------------------------------------#
# Massey										 							  #
# Conferir valores na matriz de ranking e soma sucessiva... ESTÁ CERTO?		  #
#-----------------------------------------------------------------------------#
def massey (numeroComentarios, matrizSimilaridadeCosseno):
	
	massey = [[0.0 for x in range(numeroComentarios)] for x in range(numeroComentarios)] 
	
	for i in range(len(matrizSimilaridadeCosseno)):
		for j in range(len(matrizSimilaridadeCosseno)):
			if (i > j):
				 # na matriz similaridade de cosseno a diagonal superior e igual a diagonal inferior
				massey[i][j] = -matrizSimilaridadeCosseno[i][j]
			elif (i == j): # diagonal principal: colocar 0 ou o numero de comentarios? (Comentario nao e avaliado com ele mesmo)
				massey[i][j] = numeroComentarios
			elif (i < j):
				massey[i][j] = -1
				
			if ((i == (numeroComentarios-1))):	# Pelo método de Massey, ultima linha da matriz de ranking deve ser = 1
				massey[i][j] = 1
								
	ranking = []
	
	# Faz somas sucessivas ate o ranking convergir
	for i in range(len(matrizSimilaridadeCosseno)):
		if (i != len(matrizSimilaridadeCosseno)-1):	# se nao for a ultima linha da matriz
			ranking.append(np.sum(matrizSimilaridadeCosseno[i]))
		else:	# se for a ultima linha da matriz
			ranking.append(0)
	
	a = np.array(massey)
	b = np.array(ranking)
	x = np.linalg.solve(a, b)
		
	rankingOrdenado = ordenaRanking(x)
	
	return rankingOrdenado
	
#-----------------------------------------------------------------------------#
# Colley										 							  #
# Conferir valores na matriz de ranking e soma sucessiva... ESTÁ CERTO?		  #
#-----------------------------------------------------------------------------#
def colley (numeroComentarios, matrizSimilaridadeCosseno):
	
	ranking = [[0 for x in range(numeroComentarios)] for x in range(numeroComentarios)] 
	colley = [[0 for x in range(numeroComentarios)] for x in range(numeroComentarios)] 
	
	for i in range(len(matrizSimilaridadeCosseno)):
		for j in range(len(matrizSimilaridadeCosseno)):
			if (matrizSimilaridadeCosseno[i][j] > 0):
				colley[i][j] = 1
			elif (matrizSimilaridadeCosseno[i][j] < 0):
				colley[i][j] = -1			
			else:
				colley[i][j] = 0
				
			if (i > j):
				ranking[i][j] = -matrizSimilaridadeCosseno[j][i]
			if (i == j):
				ranking[i][j] = numeroComentarios
			else:
				ranking[i][j] = -1	
	
	soma = []
	for i in range(len(matrizSimilaridadeCosseno)):
		aux = np.sum(colley[i])
		soma.append(1 + 0.5 * aux)   # ?
	
	a = np.array(ranking)
	b = np.array(soma)
	x = np.linalg.solve(a, b)
	
	rankingOrdenado = ordenaRanking(x)
	
	return rankingOrdenado
