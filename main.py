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

from preProcessamento import *
from mineracao import *
from grafos import *
from sumarizacao import *

#-----------------------------------------------------------------------#
# INICIALIZAÇÕES		 												#
#-----------------------------------------------------------------------#
def inicializaMatriz (comentarios):

	matrizSimilaridadeCosseno = [[0 for x in range(len(comentarios))] for x in range(len(comentarios))]

	return matrizSimilaridadeCosseno
	

def inicializaVetor (comentarios):

	matrizSimilaridadeCosseno = [0 for x in range(len(comentarios))]

	return matrizSimilaridadeCosseno

#-----------------------------------------------------------------------#
# MAIN																	#
#-----------------------------------------------------------------------#
def main():

	matriztfxidf = []
	matriztfxidfTitulo = []
	vetorIntermerdiario = []
	vetorSimilaridadeCossenoTitulo = []
	
	comentarios, titulo = leArquivo()
	salvaReferenciaExplicita(comentarios)
	verificaLike(comentarios)
	comentariosSemStopWords = removeStopWords(comentarios)
	comentariosSemNumeros = removeNumeros(comentariosSemStopWords)
	comentariosSemCaracteresEspeciais = removeCaracteresEspeciais(comentariosSemNumeros)
	comentariosPreProcessado = stemming(comentariosSemCaracteresEspeciais)

	# matriz de ordem N, onde N é o número de comentários (Com descricao, sem titulo)
	matrizSimilaridadeCosseno = inicializaMatriz(comentarios)		
	vetorSimilaridadeCossenoTitulo = inicializaVetor(comentariosPreProcessado)

	# Calculo TFXIDF para cada token (incluindo descricao, sem titulo)
	for i in range(len(comentariosPreProcessado)):
		j = 0
		while (j < len(comentariosPreProcessado[i])):
			tfxidf(comentariosPreProcessado[i][j], i, j, comentariosPreProcessado, vetorIntermerdiario)
			j = j + 1
		matriztfxidf.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	# Para cada comentario calcula a similaridade daquele comentario para todos (incluindo descricao, sem titulo)
	for i in range(len(comentariosPreProcessado)):
		for j in range(i+1,len(comentariosPreProcessado)):
			listaTokensDistintos = getTokensDistintos(comentariosPreProcessado[i], comentariosPreProcessado[j])
			frequenciaComentario1 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[i], listaTokensDistintos, i, matriztfxidf)
			frequenciaComentario2 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[j], listaTokensDistintos, j, matriztfxidf)
			calculaSimilaridadeCosseno(matrizSimilaridadeCosseno, i, j, frequenciaComentario1, frequenciaComentario2)

	# Calculo TFXIDF para titulo (olhando tokens em todos os comentarios)
	for i in range(len(titulo)):
		j = 0
		while (j < len(titulo[i])):
			tfxidf(titulo[i][j], i, j, comentariosPreProcessado, vetorIntermerdiario)
			j = j + 1
		matriztfxidfTitulo.append(vetorIntermerdiario)
		vetorIntermerdiario = []


	# Para cada comentario calcula a frequencia (TFXIDF) e a similaridade daquele comentario com o titulo
	for i in range(len(comentariosPreProcessado)):
		listaTokensDistintos = getTokensDistintosTitulo(comentariosPreProcessado[i], titulo[0])
		frequenciaComentario1 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[i], listaTokensDistintos, i, matriztfxidf)
		frequenciaComentario2 = calculaFrequenciaSimilaridadeCossenoTitulo(titulo[0], listaTokensDistintos, 0, matriztfxidfTitulo)
		calculaSimilaridadeCossenoTitulo (vetorSimilaridadeCossenoTitulo, i, frequenciaComentario1, frequenciaComentario2)

	mediaDescricaoTitulo = calculaMediaSimilaridadeTituloDescricao (matrizSimilaridadeCosseno, vetorSimilaridadeCossenoTitulo)
	#thresholdIdeal = thresholdModularidade (matrizSimilaridadeCosseno, len(comentariosPreProcessado))
	contaIntervalosSimilaridade (matrizSimilaridadeCosseno)
	aumentaEsparcidadeMatriz (matrizSimilaridadeCosseno)
	salvaMatrizSimilaridadeCossenoEsparsa (matrizSimilaridadeCosseno, len(comentarios))

	rede = inicializaGrafo ()
	
	resultadoPageRank = pageRank(rede)
	rankingPageRank = ordenaPageRank(resultadoPageRank)
	
	print "PAGERANK\n", rankingPageRank
	
	resultLouvain = louvain(rede)
	centrality_eigenvector = centralidade_autovetor (rede)
	rankingComunidade = rankingIntraComunidade (centrality_eigenvector, resultLouvain)
	rankingClusters = clusterImportante (mediaDescricaoTitulo, resultLouvain)

	"""print "\n#################### RESULTADOS ####################\n"

	print ":: NUMERO COMENTARIOS ::", len(comentarios)	

	countOriginal = 0
	for i in range(len(comentarios)):
		j = 0
		while (j < len(comentarios[i])):
			countOriginal = countOriginal + 1
			j = j + 1

	print "\n\n:: NUMERO TOKENS DOCUMENTO ORIGINAL ::", countOriginal

	countPreProcessado = 0
	for i in range(len(comentariosPreProcessado)):
		j = 0
		while (j < len(comentariosPreProcessado[i])):
			countPreProcessado = countPreProcessado + 1
			j = j + 1

	print "\n\n:: NUMERO TOKENS APOS PRE-PROCESSAMENTO ::", countPreProcessado

	print "\n\n:: TOTAL TOKENS REMOVIDOS ::", (countOriginal-countPreProcessado)

	print "\n#######################################################\n"
	
	print ":: RESULTADO ALGORITMO COMUNIDADE ::\n", resultLouvain
	print "\n\n:: MODULARIDADE :: ", resultLouvain.modularity


	print "\n#######################################################\n"

	print "\n:: RANKING INTRA CLUSTER ::\n"

	for i in range(len(rankingComunidade)):
		print "--> Cluster: ", i
		for j in range(len(rankingComunidade[i])):
			print rankingComunidade[i][j][0]
		print "\n"

	print "\n:: RANKING CLUSTERS ::\n"

	for i in range(len(rankingClusters)):
		print rankingClusters[i], "\n" """

	return 0

if __name__ == '__main__':
	main()	
