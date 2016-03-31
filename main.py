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
	
# Angular 1412
#oraculo = [0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 28, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32]
#oraculo = [0, 1, 3, 4, 7, 15, 29, 6]	# top 25% = 8
#oraculo = [0, 1, 3, 4, 7, 15, 29, 6, 10, 12]			# tamanho_cluster_matriz_normal = 10
#oraculo_matriz_reduzida = [0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 28, 19, 20, 21, 9]			# tamanho_cluster_matriz_reduzida = 27 componentes = 2
#oraculo_matriz_reduzida = [0, 1, 3, 4, 7, 15, 29, 6]			#  tamanho_cluster_matriz_reduzida = 8 componentes = 10 e 14
#oraculo_matriz_reduzida = [0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22]			#  tamanho_cluster_matriz_reduzida = 14 componentes = 8 e 53
#oraculo_matriz_reduzida = [0, 1, 3, 4, 7, 15, 29]			#  tamanho_cluster_matriz_reduzida = 7 componentes = 20


# Angular 5160
oraculo = [0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30]
#oraculo = [0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11]	 # 19 itens
#oraculo_matriz_reduzida = [0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22] # 2 componentes = 24 itens
#oraculo = [0, 1, 5, 6, 2, 3, 7, 9]		# top 25% = 8
#oraculo_matriz_reduzida = [0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12] # 14 itens
#oraculo_matriz_reduzida = [0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8] # 12 itens
#oraculo_matriz_reduzida = [0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10] # 13 itens
#oraculo_matriz_reduzida = [0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21]	 # 17 itens

# jQuery 2199
#oraculo = [0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14]
#oraculo = [0, 1, 7, 9, 12] 		# top 25% = 5

# Bootstrap 341
#oraculo = [0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 3, 38, 14, 27, 39]
#oraculo = [0, 1, 3, 21, 29, 31, 35, 5, 6, 9]		# top 25% = 10

#-----------------------------------------------------------------------#
# MAIN																	#
#-----------------------------------------------------------------------#
def main():

	matriztfxidf = []
	matriztfxidfTitulo = []
	vetorIntermerdiario = []
	vetorSimilaridadeCossenoTitulo = []
	
	# "\n#################################### PRE-PROCESSAMENTO ###########################################\n"
	
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
	
	#PCA
	numeroComponentesIdeal = pca(matriztfxidf)
	
	print "Numero de componentes ideal PCA: ", numeroComponentesIdeal
		
	# Inicializa matrizes de Similaridade para NMF
	matrizSimilaridadeCossenoNMF = [[0 for x in range(len(comentariosPreProcessado))] for x in range(len(comentariosPreProcessado))]
	matrizDistanciaEuclidianaNMF = [[0 for x in range(len(comentariosPreProcessado))] for x in range(len(comentariosPreProcessado))]
	
	#matrizSimilaridadeCossenoNMF = [[0 for x in range(len(matrizReduzidaNMF))] for x in range(len(matrizReduzidaNMF))]
	#matrizDistanciaEuclidianaNMF = [[0 for x in range(len(matrizReduzidaNMF))] for x in range(len(matrizReduzidaNMF))]	
	
	# Calculo a similaridade de cosseno e a distancia euclidiana na matriz reduzida (com titulo e descricao)
	for i in range(len(comentariosPreProcessado)):
		for j in range(len(comentariosPreProcessado)):
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
			
	# "\n######################################### GRAFO ################################################\n"
			
	# Fazer massey antes de fazer esparcidade da matriz de similaridade de cosseno
	resultadoMassey = massey(len(comentarios), matrizSimilaridadeCosseno)
	resultadoMasseyNMF = massey(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)
	
	# Fazer colley antes de fazer esparcidade da matriz de similaridade de cosseno
	resultadoColley = colley(len(comentarios), matrizSimilaridadeCosseno)
	resultadoColleyNMF = colley(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)
			
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
	
	"""print ":: ESTUDO 1::\n"
	
	print ">>>> Distancia euclidiana matriz normal"
	vetor1 = []
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricao)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(rankingMediaDistanciaEuclidianaTituloDescricao[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> Distancia euclidiana matriz reduzida"
	vetor1 = []
	for i in range(len(rankingMediaDistanciaEuclidianaTituloDescricaoNMF)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(rankingMediaDistanciaEuclidianaTituloDescricaoNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> Similaridade de cosseno matriz normal"
	vetor1 = []
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricao)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(rankingSimilaridadeCossenoMediaTituloDescricao[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> Similaridade de cosseno matriz reduzida"
	vetor1 = []
	for i in range(len(rankingSimilaridadeCossenoMediaTituloDescricaoNMF)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"""
		
	
	"""print ":: ESTUDO 2::"
	
	print ">>>> PageRank matriz normal"
	vetor1 = []
	for i in range(len(resultadoPageRank)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(resultadoPageRank[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> PageRank matriz reduzida"
	vetor1 = []
	for i in range(len(resultadoPageRankNMF)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(resultadoPageRankNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> Massey matriz normal"
	vetor1 = []
	for i in range(len(resultadoMassey)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(resultadoMassey[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> Massey matriz reduzida"
	vetor1 = []
	for i in range(len(resultadoMasseyNMF)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(resultadoMasseyNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> Colley matriz normal"
	vetor1 = []
	for i in range(len(resultadoColley)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(resultadoColley[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"
	
	print ">>>> Massey matriz reduzida"
	vetor1 = []
	for i in range(len(resultadoColleyNMF)):
	#for i in range(8):
	#for i in range(5):
	#for i in range(10):
		vetor1.append(resultadoColleyNMF[i][1])
	kendall = kendallCorrelation(vetor1, oraculo)
	print kendall, "\n"""
	
	
	print ":: ESTUDO 3::\n"
	
	#print "TAMANHO CLUSTER LOUVAIN + PAGERANK normal: ", len(ordenacaoPageRank[clusterPossuiDescricao])
	#print "TAMANHO CLUSTER LOUVAIN + PAGERANK reduzida: ", len(ordenacaoPageRankNMF[clusterPossuiDescricaoNMF])
	#print "TAMANHO CLUSTER LOUVAIN + CENTRALIDADE AUTOVETOR normal: ", len(rankingComunidade[clusterPossuiDescricao])
	#print "TAMANHO CLUSTER LOUVAIN + CENTRALIDADE AUTOVETOR reduzida: ", len(rankingComunidadeNMF[clusterPossuiDescricaoNMF])
	#print "\n"
	
	oraculoClusterMatrizOriginal = oraculo[:len(ordenacaoPageRank[clusterPossuiDescricao])]
	
	oraculoClusterMatrizReduzida = oraculo[:len(ordenacaoPageRankNMF[clusterPossuiDescricaoNMF])]
	
	#print "TAMANHOOO ", tamanhoClusterMatrizOriginal
	#print "TAMANHOOO ", tamanhoClusterMatrizReduzida
	
	print ">>>> Louvain + PageRank - matriz normal"
	vetor1 = []
	for i in range(len(ordenacaoPageRank[clusterPossuiDescricao])):
		vetor1.append(ordenacaoPageRank[clusterPossuiDescricao][i][0])
	kendall = kendallCorrelation(vetor1, oraculoClusterMatrizOriginal)
	print kendall, "\n"
	
	print ">>>> Louvain + PageRank - matriz reduzida"
	vetor1 = []
	for i in range(len(ordenacaoPageRankNMF[clusterPossuiDescricaoNMF])):
		vetor1.append(ordenacaoPageRankNMF[clusterPossuiDescricaoNMF][i][0])
	kendall = kendallCorrelation(vetor1, oraculoClusterMatrizReduzida)
	print kendall, "\n"
	
	print ">>>> Louvain + Centralidade por Autovetor - matriz normal"
	vetor1 = []
	for i in range(len(rankingComunidade[clusterPossuiDescricao])):
		vetor1.append(rankingComunidade[clusterPossuiDescricao][i][0])
	kendall = kendallCorrelation(vetor1, oraculoClusterMatrizOriginal)
	print kendall, "\n"
	
	print ">>>> Louvain + Centralidade por Autovetor - matriz reduzida"
	vetor1 = []
	for i in range(len(rankingComunidadeNMF[clusterPossuiDescricaoNMF])):
		vetor1.append(rankingComunidadeNMF[clusterPossuiDescricaoNMF][i][0])
	kendall = kendallCorrelation(vetor1, oraculoClusterMatrizReduzida)
	print kendall, "\n"
	

	
	"""print ":: SPEARMAN ::"
	
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
	print spearman"""
	
	return 0

if __name__ == '__main__':
	main()	
