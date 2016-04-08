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
from resultados import *

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
	retorno = []
	
	# "\n#################################### PRE-PROCESSAMENTO ###########################################\n"
	
	retorno = leArquivo()
	comentarios = retorno[0]

	nomeArquivo = retorno[1]
	nomeArquivo = nomeArquivo.split("/")
	nomeArquivo = nomeArquivo[1]
	
	oraculoParametro = retorno[2]
	oraculoParametro = oraculoParametro.split(',')
	oraculo = []
	
	for i in range(len(oraculoParametro)):
		oraculo.append(int(oraculoParametro[i]))
	
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
			
	# Inicializa matrizes de Similaridade para NMF
	matrizSimilaridadeCossenoNMF = [[0 for x in range(len(comentariosPreProcessado))] for x in range(len(comentariosPreProcessado))]
	matrizDistanciaEuclidianaNMF = [[0 for x in range(len(comentariosPreProcessado))] for x in range(len(comentariosPreProcessado))]
	
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
	
	# Pagerank
	resultadoPageRank = pageRank(rede)
	resultadoPageRankNMF = pageRank(redeNMF)
	
	# Acho os clusters na rede
	resultLouvain = louvain(rede)
	resultLouvainNMF = louvain(redeNMF)
	
	# Verifico qual cluster possui a descrição
	clusterPossuiDescricao = verificaClusterPossuiDescricao(resultLouvain)
	clusterPossuiDescricaoNMF = verificaClusterPossuiDescricao(resultLouvainNMF)
	
	# Calculo o pagerank dentro do cluster que possui descricao
	ordenacaoPageRank = pageRankIntraCluster (clusterPossuiDescricao, resultLouvain, rede)
	ordenacaoPageRankNMF = pageRankIntraCluster (clusterPossuiDescricaoNMF, resultLouvainNMF, redeNMF)
	
	#print "Ordenacao page rank ", ordenacaoPageRank
	#print "Ordenacao page rankNMF ", ordenacaoPageRankNMF
	
	# Calculo a centralidade por autovetor da rede
	centrality_eigenvector = centralidade_autovetor (rede)
	centrality_eigenvectorNMF = centralidade_autovetor (redeNMF)
	
	# Calculo a centralidade por autovetor dentro de cada comunidade
	rankingComunidade = rankingIntraComunidade (centrality_eigenvector, resultLouvain)
	rankingComunidadeNMF = rankingIntraComunidade (centrality_eigenvectorNMF, resultLouvainNMF)
	
	# Cluster importante 
	rankingClusters = clusterImportante (mediaSimilaridadeCossenoDescricaoTitulo, resultLouvain)
	rankingClustersNMF = clusterImportante (mediaSimilaridadeCossenoDescricaoTituloNMF, resultLouvainNMF)
	
	# "\n######################################### K-MEANS ################################################\n"
	
	#Kmeans
	kmeansResultSimilaridadeCosseno = kmeans (matrizSimilaridadeCosseno)
	kmeansResultNMF = kmeans (matrizSimilaridadeCossenoNMF)
	
	# "\n######################################### RESULTADO ################################################\n"
	
	resultadosPrecisionRecallFscore(oraculo, nomeArquivo, len(comentariosPreProcessado), rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF)
	
	resultadosMAPIndividual(oraculo, nomeArquivo, len(comentariosPreProcessado), rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF)
	
	# Comentar os dois resultados acima e executar experimentosMAP.sh
	resultadosMAPGeral ()
	
	return 0

if __name__ == '__main__':
	main()	
