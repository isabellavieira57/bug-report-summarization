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
