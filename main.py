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
	

oraculo = [0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 28, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32]

#-----------------------------------------------------------------------#
# MAIN																	#
#-----------------------------------------------------------------------#
def main():

	matriztfxidf = []
	matriztfxidfTitulo = []
	vetorIntermerdiario = []
	vetorSimilaridadeCossenoTitulo = []
	
	# "\n#################################### PRE-PROCESSAMENTO ###########################################\n"
	
	#comentarios, titulo = leArquivo()
	comentarios = leArquivo()	
	salvaReferenciaExplicita(comentarios)
	verificaLike(comentarios)
	comentariosSemStopWords = removeStopWords(comentarios)
	comentariosSemNumeros = removeNumeros(comentariosSemStopWords)
	comentariosSemCaracteresEspeciais = removeCaracteresEspeciais(comentariosSemNumeros)
	comentariosPreProcessado = stemming(comentariosSemCaracteresEspeciais)
	
	# matriz de ordem N, onde N é o número de comentários (Com descricao, sem titulo)
	matrizSimilaridadeCosseno = inicializaMatriz(comentarios)		
	matrizDistanciaEuclidiana = inicializaMatriz(comentarios)		
	#vetorSimilaridadeCossenoTitulo = inicializaVetor(comentariosPreProcessado)
	#vetorDistanciaEuclidianaTitulo = inicializaVetor(comentariosPreProcessado)
	vetorSimilaridadeCossenoTituloNMF = inicializaVetor(comentariosPreProcessado)
	vetorDistanciaEuclidianaTituloNMF = inicializaVetor(comentariosPreProcessado)

	# Calculo TFXIDF para cada token (incluindo titulo e descricao)
	for i in range(len(comentariosPreProcessado)):
		j = 0
		while (j < len(comentariosPreProcessado[i])):
			tfxidf(comentariosPreProcessado[i][j], i, j, comentariosPreProcessado, vetorIntermerdiario)
			j = j + 1
		matriztfxidf.append(vetorIntermerdiario)
		vetorIntermerdiario = []
		
    # "\n#################################### MATRIZ ORIGINAL ###########################################\n"
    
	# Para cada comentario calcula a similaridade de cosseno e a distancia euclidiana daquele comentario para todos (incluindo titulo e descricao)
	for i in range(len(comentariosPreProcessado)):
		for j in range(len(comentariosPreProcessado)):
			listaTokensDistintos = getTokensDistintos(comentariosPreProcessado[i], comentariosPreProcessado[j])
			frequenciaComentario1 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[i], listaTokensDistintos, i, matriztfxidf)
			frequenciaComentario2 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[j], listaTokensDistintos, j, matriztfxidf)
			calculaSimilaridadeCosseno(matrizSimilaridadeCosseno, i, j, frequenciaComentario1, frequenciaComentario2)
			calculaDistanciaEuclidiana(matrizDistanciaEuclidiana, i, j, frequenciaComentario1, frequenciaComentario2)
		
	# Calculo TFXIDF para titulo (olhando tokens em todos os comentarios)
	#for i in range(len(titulo)):
    #		j = 0
	#	while (j < len(titulo[i])):
	#		tfxidf(titulo[i][j], i, j, comentariosPreProcessado, vetorIntermerdiario)
	#		j = j + 1
	#	matriztfxidfTitulo.append(vetorIntermerdiario)
	#	vetorIntermerdiario = []

	# Para cada comentario calcula a frequencia (TFXIDF) e a similaridade de cosseno e a distancia euclidiana daquele comentario com o titulo
	#for i in range(len(comentariosPreProcessado)):
	#	listaTokensDistintos = getTokensDistintosTitulo(comentariosPreProcessado[i], titulo[0])
	#	frequenciaComentario1 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[i], listaTokensDistintos, i, matriztfxidf)
	#	frequenciaComentario2 = calculaFrequenciaSimilaridadeCossenoTitulo(titulo[0], listaTokensDistintos, 0, matriztfxidfTitulo)
	#	calculaSimilaridadeCossenoTitulo (vetorSimilaridadeCossenoTitulo, i, frequenciaComentario1, frequenciaComentario2)
	#	calculaDistanciaEuclidianaTitulo (vetorDistanciaEuclidianaTitulo, i, frequenciaComentario1, frequenciaComentario2)

	# Tenho a similaridade de cosseno média de cada comentário com o título e a descrição do bug
	mediaSimilaridadeCossenoDescricaoTitulo = calculaMediaSimilaridadeComentarioTituloDescricao (matrizSimilaridadeCosseno)
	# Ordena a média da similaridade do comentário com o título e a descrição
	rankingSimilaridadeCossenoMediaTituloDescricao = ordenaRanking (mediaSimilaridadeCossenoDescricaoTitulo)
	
	# Tenho a distancia euclidiana média de cada comentário com o título e a descrição do bug
	mediaDistanciaEuclidianaTituloDescricao = calculaMediaSimilaridadeComentarioTituloDescricao (matrizDistanciaEuclidiana)
	# Ordena a média da distancia euclidiana do comentário com o título e a descrição
	rankingMediaDistanciaEuclidianaTituloDescricao = ordenaRanking (mediaDistanciaEuclidianaTituloDescricao)
	
	# "\n#################################### MATRIZ TRANSFORMADA ###########################################\n"
	
	# NMF
	matrizReduzidaNMF = nmf(matriztfxidf)
		
	# Inicializa matrizes de Similaridade para NMF
	matrizSimilaridadeCossenoNMF = [[0 for x in range(len(matrizReduzidaNMF))] for x in range(len(matrizReduzidaNMF))]
	matrizDistanciaEuclidianaNMF = [[0 for x in range(len(matrizReduzidaNMF))] for x in range(len(matrizReduzidaNMF))]
	
	# Calculo a similaridade de cosseno e a distancia euclidiana na matriz reduzida (com titulo e descricao)
	for i in range(len(matrizReduzidaNMF)):
		for j in range(len(matrizReduzidaNMF)):
			calculaSimilaridadeCosseno(matrizSimilaridadeCossenoNMF, i, j, matrizReduzidaNMF[i], matrizReduzidaNMF[j])
			calculaDistanciaEuclidiana(matrizDistanciaEuclidianaNMF, i, j, matrizReduzidaNMF[i], matrizReduzidaNMF[j])
		
	# Tenho a similaridade de cosseno média de cada comentário com o título e a descrição do bug
	mediaSimilaridadeCossenoDescricaoTituloNMF = calculaMediaSimilaridadeComentarioTituloDescricao (matrizSimilaridadeCossenoNMF)
	# Ordena a média da similaridade do comentário com o título e a descrição
	rankingSimilaridadeCossenoMediaTituloDescricaoNMF = ordenaRanking (mediaSimilaridadeCossenoDescricaoTituloNMF)
	
	# Tenho a distancia euclidiana média de cada comentário com o título e a descrição do bug
	mediaDistanciaEuclidianaTituloDescricaoNMF = calculaMediaSimilaridadeComentarioTituloDescricao (matrizDistanciaEuclidianaNMF)
	# Ordena a média da distancia euclidiana do comentário com o título e a descrição
	rankingMediaDistanciaEuclidianaTituloDescricaoNMF = ordenaRanking (mediaDistanciaEuclidianaTituloDescricaoNMF)
			
	# PCA
	#matrizReduzidaPCA = pca (matriztfxidf)
	
	# "\n######################################### GRAFO ################################################\n"
			
	# Fazer massey antes de fazer esparcidade da matriz de similaridade de cosseno
	resultadoMassey = massey(len(comentarios), matrizSimilaridadeCosseno)
	resultadoMasseyNMF = massey(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)
	
	# Fazer colley antes de fazer esparcidade da matriz de similaridade de cosseno
	resultadoColley = colley(len(comentarios), matrizSimilaridadeCosseno)
	resultadoColleyNMF = colley(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)
		
	"""vetorMassey = []
	for i in range(len(resultadoMassey)):
		vetorMassey.append(resultadoMassey[i][1])
		
	vetorColley = []
	for i in range(len(resultadoColley)):
		vetorColley.append(resultadoColley[i][1])
	
	spearman = spearmanCorrelation(vetorMassey, vetorColley)
	print "SPEARMAN", spearman
	
	kendall = kendallCorrelation(vetorMassey,vetorColley)
	print "KENDALL", kendall"""
	
	#thresholdIdeal = thresholdModularidade (matrizSimilaridadeCosseno, len(comentariosPreProcessado))
	#contaIntervalosSimilaridade (matrizSimilaridadeCosseno)
	
	aumentaEsparcidadeMatriz (matrizSimilaridadeCosseno)
	aumentaEsparcidadeMatriz (matrizSimilaridadeCossenoNMF)
	
	salvaMatrizSimilaridadeCossenoEsparsa (matrizSimilaridadeCosseno, len(comentarios), "grafo.txt")
	salvaMatrizSimilaridadeCossenoEsparsa (matrizSimilaridadeCossenoNMF, len(matrizReduzidaNMF), "grafoNMF.txt")

	rede = inicializaGrafo ("grafo.txt")
	redeNMF = inicializaGrafo ("grafoNMF.txt")
	
	resultadoPageRank = pageRank(rede)
	resultadoPageRankNMF = pageRank(redeNMF)
	
	resultLouvain = louvain(rede)
	resultLouvainNMF = louvain(redeNMF)
	
	clusterPossuiDescricao = verificaClusterPossuiDescricao(resultLouvain)
	clusterPossuiDescricaoNMF = verificaClusterPossuiDescricao(resultLouvainNMF)

	ordenacaoPageRank = pageRankIntraCluster (resultLouvain, rede)
	ordenacaoPageRankNMF = pageRankIntraCluster (resultLouvainNMF, redeNMF)
	
	centrality_eigenvector = centralidade_autovetor (rede)
	centrality_eigenvectorNMF = centralidade_autovetor (redeNMF)
	
	rankingComunidade = rankingIntraComunidade (centrality_eigenvector, resultLouvain)
	rankingComunidadeNMF = rankingIntraComunidade (centrality_eigenvectorNMF, resultLouvainNMF)
	
	rankingClusters = clusterImportante (mediaSimilaridadeCossenoDescricaoTitulo, resultLouvain)
	rankingClustersNMF = clusterImportante (mediaSimilaridadeCossenoDescricaoTituloNMF, resultLouvainNMF)
	
	# "\n######################################### K-MEANS ################################################\n"
	
	#Kmeans
	kmeansResultSimilaridadeCosseno = kmeans (matrizSimilaridadeCosseno)
	kmeansResultNMF = kmeans (matrizSimilaridadeCossenoNMF)

	"""
	print "\n#################### RESULTADOS ####################\n"

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
	
	#print comentariosPreProcessado[4]
	
	#media = 0
	
	#for i in range(len(comentariosPreProcessado)):
	#	media = media + len(comentariosPreProcessado[i])
	#	print "Numero de termos comentário", i, ":", len(comentariosPreProcessado[i])
	
	#media1 = media/len(comentariosPreProcessado)
	#print "MEDIA TERMOS",media1

	print "\n#######################################################\n"	
	print ":: RESULTADO ALGORITMO COMUNIDADE ::\n", resultLouvain
	print "\n\n:: MODULARIDADE :: ", resultLouvain.modularity

	print "\n#######################################################\n"
	print "\n:: RANKING CLUSTERS ::\n"
	for i in range(len(rankingClusters)):
		print rankingClusters[i], "\n"
		
	print "\n:: RANKING INTRA CLUSTER ::\n"
	for i in range(len(rankingComunidade)):
		print "--> Cluster: ", i
		for j in range(len(rankingComunidade[i])):
			print rankingComunidade[i][j][0]
		print "\n"
 
	print "\n#######################################################\n"
	print "\n:: PAGERANK ::\n", resultadoPageRank
	
	print "\n#######################################################\n"
	print "\n:: MASSEY ::\n", resultadoMassey
	
	print "\n#######################################################\n"
	print "\n:: COLLEY ::\n", resultadoColley
	
	print "\n#######################################################\n"
	print "\n:: RESULTADOS PARA EXPERIMENTOS::\n"
	print "Oráculo desenvolvedores: \n", oraculo
	print "\n\n"
	
	acertos = 0
	oraculo_algoritmo = []
	
	# LOUVAIN
	# percorro os top10 da comunidade mais importante
	
	if (len(rankingComunidade[rankingClusters[0][0]]) < 10):
		print "Tamanho cluster Louvain: ", len(rankingComunidade[rankingClusters[0][0]])
		
		for i in range(len(rankingComunidade[rankingClusters[0][0]])):	
			oraculo_algoritmo.append(rankingComunidade[rankingClusters[0][0]][i][0]) 
			if (rankingComunidade[rankingClusters[0][0]][i][0] in oraculo):
				acertos = acertos + 1
				
		print "Oráculo algoritmo Louvain: \n", oraculo_algoritmo
		print "Acertos algoritmo Louvain: \n", acertos
		print "\n\n"
	else: 			
		for i in range(10):	
			print "Tamanho cluster Louvain: 10", 
			oraculo_algoritmo.append(rankingComunidade[rankingClusters[0][0]][i][0]) 
			if (rankingComunidade[rankingClusters[0][0]][i][0] in oraculo):
				acertos = acertos + 1
		print "Oráculo algoritmo Louvain: \n", oraculo_algoritmo
		print "Acertos algoritmo Louvain: \n", acertos
		print "\n\n"
		
	acertos = 0
	oraculo_algoritmo = []
	
	# PAGERANK
	for i in range(10):	
		oraculo_algoritmo.append(resultadoPageRank[i][0]) 
		if (resultadoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	print "Oráculo PageRank: \n", oraculo_algoritmo
	print "Acertos PageRank: \n", acertos
	print "\n\n"

	acertos = 0
	oraculo_algoritmo = []
	
	# MASSEY
	for i in range(10):	
		oraculo_algoritmo.append(resultadoMassey[i][0]) 
		if (resultadoMassey[i][0] in oraculo):
			acertos = acertos + 1
	print "Oráculo Massey: \n", oraculo_algoritmo
	print "Acertos Massey: \n", acertos
	print "\n\n"
	
	acertos = 0
	oraculo_algoritmo = []
	
	# COLLEY
	for i in range(10):	
		oraculo_algoritmo.append(resultadoColley[i][0]) 
		if (resultadoColley[i][0] in oraculo):
			acertos = acertos + 1
	print "Oráculo Colley: \n", oraculo_algoritmo
	print "Acertos Colley: \n", acertos
	print "\n\n"
	"""
		
	print "\n###################################### RESULTADOS #########################################\n"
	
	ranking = ""
	print "\n###################################### ESTUDO 1 ###########################################\n"
	print "### RANKING ORACULO X RANKING DE SIMILARIDADE DA DESCRIÇÃO E DO TÍTULO COM CADA COMENTÁRIO ###\n"
	print "\n :: ESPAÇO ORIGINAL: SIMILARIDADE DE COSSENO ::\n"
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricao)):
		ranking = ranking+" "+str(rankingSimilaridadeCossenoMediaTituloDescricao[i][0])
	print ranking
		
	ranking = ""
	print "\n :: ESPAÇO ORIGINAL: EUCLIDIANA ::\n"
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricao)):
		ranking = ranking+" "+str(rankingMediaDistanciaEuclidianaTituloDescricao[i][0])
	print ranking

	ranking = ""
	print "\n :: ESPAÇO TRANSFORMADO: SIMILARIDADE DE COSSENO ::\n"
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricaoNMF)):
		ranking = ranking+" "+str(rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][0])
	print ranking
	
	ranking = ""
	print "\n :: ESPAÇO TRANSFORMADO: DISTÂNCIA EUCLIDIANA ::\n"
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricaoNMF)):
		ranking = ranking+" "+str(rankingMediaDistanciaEuclidianaTituloDescricaoNMF[i][0])
	print ranking
	
	print "\n###################################### ESTUDO 2 ###########################################\n"
	print "### RANKING ORACULO X RANKING REDES ###\n"
	
	ranking = ""
	print "\n :: ESPAÇO ORIGINAL: PAGERANK ::\n"
	for i in range(len(resultadoPageRank)):
		ranking = ranking+" "+str(resultadoPageRank[i][0])
	print ranking
	
	ranking = ""
	print "\n :: ESPAÇO ORIGINAL: MASSEY ::\n"
	for i in range(len(resultadoMassey)):
		ranking = ranking+" "+str(resultadoMassey[i][0])
	print ranking
	
	ranking = ""
	print "\n :: ESPAÇO ORIGINAL: COLLEY ::\n"
	for i in range(len(resultadoColley)):
		ranking = ranking+" "+str(resultadoColley[i][0])
	print ranking
	
	ranking = ""
	print "\n :: ESPAÇO TRANSFORMADO: PAGERANK ::\n"
	for i in range(len(resultadoPageRankNMF)):
		ranking = ranking+" "+str(resultadoPageRankNMF[i][0])
	print ranking
		
	ranking = ""
	print "\n :: ESPAÇO TRANSFORMADO: MASSEY ::\n"
	for i in range(len(resultadoMasseyNMF)):
		ranking = ranking+" "+str(resultadoMasseyNMF[i][0])
	print ranking
	
	ranking = ""
	print "\n :: ESPAÇO TRANSFORMADO: COLLEY ::\n"
	for i in range(len(resultadoColleyNMF)):
		ranking = ranking+" "+str(resultadoColleyNMF[i][0])
	print ranking
	
	print "\n###################################### ESTUDO 3 ###########################################\n"
	print "### RANKING ORACULO X RANKING GRUPO ONDE ESTÁ A DESCRIÇÃO ###\n"
	
	print "\n :: ESPAÇO ORIGINAL: LOUVAIN ::\n"
	print resultLouvain
	#print "\nCluster que possui descricao: ", clusterPossuiDescricao
	#print "\n"	
	#print "Ranking clusters: ", rankingClusters
	#print "\n"
	print "\n"
	
	ranking = ""
	for i in range(len(ordenacaoPageRank[clusterPossuiDescricao])):
		ranking = ranking+" "+str(ordenacaoPageRank[clusterPossuiDescricao][i][0])
	print "PAGERANK: ",ranking
	print "\n"
	
	ranking = ""
	for i in range(len(rankingComunidade[clusterPossuiDescricao])):
		ranking = ranking+" "+str(rankingComunidade[clusterPossuiDescricao][i][0])
	print "CENTRALIDADE POR AUTOVETOR: ", ranking
	print "\n"
	
	print "\n :: ESPAÇO ORIGINAL: K-MEANS ::\n"
	print kmeansResultSimilaridadeCosseno
	print "\n"
	
	print "\n :: ESPAÇO TRANSFORMADO: LOUVAIN ::\n"
	print resultLouvainNMF
	#print "\nCluster que possui descricao: ", clusterPossuiDescricao
	#print "\n"	
	#print "Ranking clusters: ", rankingClusters
	#print "\n"
	print "\n"
	
	ranking = ""
	for i in range(len(ordenacaoPageRankNMF[clusterPossuiDescricaoNMF])):
		ranking = ranking+" "+str(ordenacaoPageRankNMF[clusterPossuiDescricaoNMF][i][0])
	print "PAGERANK: ",ranking
	print "\n"
	
	ranking = ""
	for i in range(len(rankingComunidadeNMF[clusterPossuiDescricaoNMF])):
		ranking = ranking+" "+str(rankingComunidadeNMF[clusterPossuiDescricaoNMF][i][0])
	print "CENTRALIDADE POR AUTOVETOR: ", ranking
	print "\n"
	
		
	print "\n :: ESPAÇO TRANSFORMADO: K-MEANS ::\n"
	print kmeansResultNMF
	print "\n"
	
	
	
	print ":: KENDALL ::"
	
	print ":: ESTUDO 1::"
	vetor1 = []
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricao)):
		vetor1.append(rankingMediaDistanciaEuclidianaTituloDescricao[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	vetor1 = []
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricao)):
		vetor1.append(rankingSimilaridadeCossenoMediaTituloDescricao[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	vetor1 = []
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricaoNMF)):
		vetor1.append(rankingMediaDistanciaEuclidianaTituloDescricaoNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	vetor1 = []
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricaoNMF)):
		vetor1.append(rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
		
	
	print ":: ESTUDO 2::"
	vetor1 = []
	for i in range(len(resultadoPageRank)):
		vetor1.append(resultadoPageRank[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	vetor1 = []
	for i in range(len(resultadoMassey)):
		vetor1.append(resultadoMassey[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	vetor1 = []
	for i in range(len(resultadoColley)):
		vetor1.append(resultadoColley[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	
	vetor1 = []
	for i in range(len(resultadoPageRankNMF)):
		vetor1.append(resultadoPageRankNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	
	vetor1 = []
	for i in range(len(resultadoMasseyNMF)):
		vetor1.append(resultadoMasseyNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	vetor1 = []
	for i in range(len(resultadoColleyNMF)):
		vetor1.append(resultadoColleyNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	"""
	print ":: ESTUDO 3::"
	vetor1 = []
	for i in range(len(ordenacaoPageRank[clusterPossuiDescricao])):
		vetor1.append(ordenacaoPageRank[clusterPossuiDescricao][i][0])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall
	
	vetor1 = []
	for i in range(len(rankingComunidade[clusterPossuiDescricao])):
		vetor1.append(rankingComunidade[clusterPossuiDescricao][i][0])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall"""
	
	print ":: SPEARMAN ::"
	
	print ":: ESTUDO 1::"
	vetor1 = []
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricao)):
		vetor1.append(rankingMediaDistanciaEuclidianaTituloDescricao[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	vetor1 = []
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricao)):
		vetor1.append(rankingSimilaridadeCossenoMediaTituloDescricao[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	vetor1 = []
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricaoNMF)):
		vetor1.append(rankingMediaDistanciaEuclidianaTituloDescricaoNMF[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	vetor1 = []
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricaoNMF)):
		vetor1.append(rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
		
	
	print ":: ESTUDO 2::"
	vetor1 = []
	for i in range(len(resultadoPageRank)):
		vetor1.append(resultadoPageRank[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	vetor1 = []
	for i in range(len(resultadoMassey)):
		vetor1.append(resultadoMassey[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	vetor1 = []
	for i in range(len(resultadoColley)):
		vetor1.append(resultadoColley[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	
	vetor1 = []
	for i in range(len(resultadoPageRankNMF)):
		vetor1.append(resultadoPageRankNMF[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	
	vetor1 = []
	for i in range(len(resultadoMasseyNMF)):
		vetor1.append(resultadoMasseyNMF[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	vetor1 = []
	for i in range(len(resultadoColleyNMF)):
		vetor1.append(resultadoColleyNMF[i][1])
	spearman = spearmanCorrelation(vetor1, oraculo)
	print spearman
	
	return 0

if __name__ == '__main__':
	main()	
