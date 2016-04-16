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
	vetorIntermerdiario = []
	retorno = []
	
	# "\n#################################### PRE-PROCESSAMENTO ###########################################\n"
	
	retorno = leArquivo()			# leitura arquivo retorna comentarios, nome arquivo, oraculo

	# Comentarios
	comentarios = retorno[0]

	# Nome arquivo .txt
	nomeArquivo = retorno[1]
	nomeArquivo = nomeArquivo.split("/")
	nomeArquivo = nomeArquivo[1].split(".")
	nomeArquivo = nomeArquivo[0].split("_")
	nomeArquivo = nomeArquivo[0]+nomeArquivo[1]
		
	# Oraculo
	oraculoParametro = retorno[2]
	oraculoParametro = oraculoParametro.split(',')
	oraculo = []
	for i in range(len(oraculoParametro)):
		oraculo.append(int(oraculoParametro[i]))
	
	#salvaReferenciaExplicita(comentarios)
	#verificaLike(comentarios)
	comentariosSemStopWords = removeStopWords(comentarios)
	comentariosSemNumeros = removeNumeros(comentariosSemStopWords)
	comentariosSemCaracteresEspeciais = removeCaracteresEspeciais(comentariosSemNumeros)
	comentariosPreProcessado = stemming(comentariosSemCaracteresEspeciais)

	print ">>> Numero comentarios com titulo e descricao separados: ", len(comentariosPreProcessado)


	# Concateno titulo e descricao para um unico comentario
	tituloEDescricao = comentariosPreProcessado[0]+comentariosPreProcessado[1]
	del (comentariosPreProcessado[0])		# remove titulo
	del (comentariosPreProcessado[0])		# remove descricao
	comentariosPreProcessado.insert(0, tituloEDescricao)		# insere titulo + descricao na posicao 0 da matriz

	print ">>> Numero comentarios com titulo e descricao juntos: ", len(comentariosPreProcessado)

	print "comentario 0: ", len(comentariosPreProcessado[0])

	# matriz de ordem N, onde N é o número de comentários (primeiro comentario e titulo+descricao)
	matrizSimilaridadeCosseno = inicializaMatriz(comentariosPreProcessado)		
	matrizDistanciaEuclidiana = inicializaMatriz(comentariosPreProcessado)		
	vetorSimilaridadeCossenoTituloNMF = inicializaVetor(comentariosPreProcessado)
	vetorDistanciaEuclidianaTituloNMF = inicializaVetor(comentariosPreProcessado)

	# tenho uma lista com todos os tokens distintos desse relatorio
	listaTokensDistintos = getTokensDistintos(comentariosPreProcessado)

	# Matriz tfxidf -> linhas = numero comentarios, colunas = numero tokens distintos
	matriztfxidf = [[0.0 for x in range(len(listaTokensDistintos))] for x in range(len(comentariosPreProcessado))]

	print "Linhas matriztfxidf: ", len(matriztfxidf)
	print "Colunas matriztfxidf: ", len(matriztfxidf[0])

	# Calculo TFXIDF para cada token de cada comentario
	tfxidf(comentariosPreProcessado, listaTokensDistintos, matriztfxidf)

	"""for i in range(len(matriztfxidf)):
		for j in range(len(matriztfxidf[i])):
			print matriztfxidf[i][j] , "\n" """

		
    # "\n#################################### MATRIZ ORIGINAL ###########################################\n"
    
	# Para cada comentario calcula a similaridade de cosseno e a distancia euclidiana daquele comentario para todos
	# linha 0 da matriz possui a distancia de todos os comentarios para o titulo+descricao
	calculaSimilaridadeCosseno(matrizSimilaridadeCosseno, comentariosPreProcessado, matriztfxidf)
	calculaDistanciaEuclidiana(matrizDistanciaEuclidiana, comentariosPreProcessado, matriztfxidf)
			
	#print "Sim Cosseno original: descricao com todos os coments", matrizSimilaridadeCosseno[0], "\n\n"
	#print "Euclidiana original: descricao com todos os coments", matrizDistanciaEuclidiana[0], "\n\n"

	# Ordena a similaridade de todos os comentarios com o titulo+descricao
	rankingSimilaridadeCossenoMediaTituloDescricao = ordenaRanking (matrizSimilaridadeCosseno[0])
	removeTituloDescricaoRanking(rankingSimilaridadeCossenoMediaTituloDescricao)
	salvaDadosArquivoTXT (rankingSimilaridadeCossenoMediaTituloDescricao, "rankingSimCosseno_original", nomeArquivo)

	acertos = 0
	tamanhoSumario = 10
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricao[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)

	print "Precision sim cosseno: ", precision
	
	# Ordena a similaridade de todos os comentarios com o titulo+descricao
	rankingMediaDistanciaEuclidianaTituloDescricao = ordenaRanking (matrizDistanciaEuclidiana[0])
	removeTituloDescricaoRanking(rankingMediaDistanciaEuclidianaTituloDescricao)
	salvaDadosArquivoTXT (rankingMediaDistanciaEuclidianaTituloDescricao, "rankingEuclidiana_original", nomeArquivo)
	
	# "\n#################################### MATRIZ TRANSFORMADA ###########################################\n"
	
	# NMF
	matrizReduzidaNMF = nmf(matriztfxidf)

	#print matrizReduzidaNMFNotacaoCientifica

	# Conversao de notacao cientifica (resultado nmf) para float
	#vetor = []
	#matrizReduzidaNMF = []
	#for i in range(len(matrizReduzidaNMF)):
	#	for j in range(len(matrizReduzidaNMF[i])):
	#		matrizReduzidaNMF[i][j] = float(matrizReduzidaNMF[i][j])

#			vetor.append())
#		matrizReduzidaNMF.append(vetor)
#		vetor = []

	#print "MATRIZ NMF SEM NOTACAO CIENTIFICA ", matrizReduzidaNMF, "\n\n"
			
	# Inicializa matrizes de Similaridade para NMF
	matrizSimilaridadeCossenoNMF = [[0 for x in range(len(matrizReduzidaNMF))] for x in range(len(matrizReduzidaNMF))]
	matrizDistanciaEuclidianaNMF = [[0 for x in range(len(matrizReduzidaNMF))] for x in range(len(matrizReduzidaNMF))]
	
	# Calculo a similaridade de cosseno e a distancia euclidiana na matriz reduzida
	#for i in range(len(matrizReduzidaNMF)):
	#	for j in range(len(matrizReduzidaNMF)):
	calculaSimilaridadeCosseno(matrizSimilaridadeCossenoNMF, matrizReduzidaNMF, matrizReduzidaNMF)
	calculaDistanciaEuclidiana(matrizDistanciaEuclidianaNMF, matrizReduzidaNMF, matrizReduzidaNMF)
	
	#print "Sim Cosseno transformada: descricao com todos os coments", matrizSimilaridadeCossenoNMF[0], "\n\n"
	#print "Euclidiana transformada: descricao com todos os coments", matrizDistanciaEuclidianaNMF[0], "\n\n"

	# Ordena a similaridade dos comentários com o título e a descrição
	rankingSimilaridadeCossenoMediaTituloDescricaoNMF = ordenaRanking (matrizSimilaridadeCossenoNMF[0])
	removeTituloDescricaoRanking(rankingSimilaridadeCossenoMediaTituloDescricaoNMF)
	salvaDadosArquivoTXT (rankingSimilaridadeCossenoMediaTituloDescricaoNMF, "rankingSimCosseno_transformada", nomeArquivo)

	print ""

	acertos = 0
	tamanhoSumario = 10
	for i in range(tamanhoSumario):
		if (rankingSimilaridadeCossenoMediaTituloDescricaoNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)

	print "Precision sim cosseno: ", precision

	# Ordena distancia euclidiana dos comentários com o título e a descrição
	rankingMediaDistanciaEuclidianaTituloDescricaoNMF = ordenaRanking (matrizDistanciaEuclidianaNMF[0])	
	removeTituloDescricaoRanking(rankingMediaDistanciaEuclidianaTituloDescricaoNMF)
	salvaDadosArquivoTXT (rankingMediaDistanciaEuclidianaTituloDescricaoNMF, "rankingEuclidiana_transformada", nomeArquivo)
	
			
	# "\n######################################### GRAFO ################################################\n"
			
	# Fazer massey antes de fazer esparcidade da matriz de similaridade de cosseno
	#resultadoMassey = massey(len(comentarios), matrizSimilaridadeCosseno)
	#resultadoMasseyNMF = massey(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)
	
	#print "Resultado Massey: ", resultadoMassey
	
	#salvaDadosArquivoTXT (resultadoMassey, "rankingMassey_original", nomeArquivo)
	#salvaDadosArquivoTXT (resultadoMassey, "rankingMassey_transformada", nomeArquivo)
	
	# Fazer colley antes de fazer esparcidade da matriz de similaridade de cosseno
	#resultadoColley = colley(len(comentarios), matrizSimilaridadeCosseno)
	#resultadoColleyNMF = colley(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)
	
	#salvaDadosArquivoTXT (resultadoColley, "rankingColley_original", nomeArquivo)
	#salvaDadosArquivoTXT (resultadoColleyNMF, "rankingColley_transformada", nomeArquivo)	
	
	matrizPageRank = [[0 for x in range(len(matrizSimilaridadeCosseno))] for x in range(len(matrizSimilaridadeCosseno))]	
	matrizPageRankNMF = [[0 for x in range(len(matrizSimilaridadeCossenoNMF))] for x in range(len(matrizSimilaridadeCossenoNMF))]	
	
	calculaPesoMatrizPageRank(matrizPageRank, matrizSimilaridadeCosseno)
	calculaPesoMatrizPageRank(matrizPageRankNMF, matrizSimilaridadeCossenoNMF)
			
	aumentaEsparcidadeMatriz (matrizPageRank)
	aumentaEsparcidadeMatriz (matrizPageRankNMF)
	
	salvaMatrizSimilaridadeCossenoEsparsa (matrizPageRank, "grafo.txt")
	salvaMatrizSimilaridadeCossenoEsparsa (matrizPageRankNMF, "grafoNMF.txt")

	rede = inicializaGrafo ("grafo.txt")
	redeNMF = inicializaGrafo ("grafoNMF.txt")
	
	#os.remove("grafo.txt")
	#os.remove("grafoNMF.txt")
	
	# Pagerank
	resultadoPageRank = pageRank(rede)
	
	acertos = 0
	tamanhoSumario = 10
	for i in range(tamanhoSumario):
		if (resultadoPageRank[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	print "Precision pagerank original: ", precision
	
	resultadoPageRankNMF = pageRank(redeNMF)
	
	acertos = 0
	tamanhoSumario = 10
	for i in range(tamanhoSumario):
		if (resultadoPageRankNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, tamanhoSumario)
	print "Precision pagerank TRans: ", precision
	
	salvaDadosArquivoTXT (resultadoPageRank, "rankingPageRank_original", nomeArquivo)
	salvaDadosArquivoTXT (resultadoPageRankNMF, "rankingPageRank_transformada", nomeArquivo)
	
	salvaMatrizSimilaridadeCossenoEsparsa (matrizSimilaridadeCosseno, "grafoL.txt")
	salvaMatrizSimilaridadeCossenoEsparsa (matrizSimilaridadeCossenoNMF, "grafoNMFL.txt")

	rede = inicializaGrafo ("grafoL.txt")
	redeNMF = inicializaGrafo ("grafoNMFL.txt")
	
	# Acho os clusters na rede
	resultLouvain = louvain(rede)
	resultLouvainNMF = louvain(redeNMF)
	
	print "result louvain ", resultLouvain
	
	# Verifico qual cluster possui a descrição (id=0)
	clusterPossuiDescricao = verificaClusterPossuiDescricao(resultLouvain)
	clusterPossuiDescricaoNMF = verificaClusterPossuiDescricao(resultLouvainNMF)
	
	# Calculo o pagerank dentro do cluster que possui descricao
	#ordenacaoPageRank = pageRankIntraCluster (clusterPossuiDescricao, resultLouvain, rede)
	#ordenacaoPageRankNMF = pageRankIntraCluster (clusterPossuiDescricaoNMF, resultLouvainNMF, redeNMF)
	
	#salvaDadosArquivoTXT (ordenacaoPageRank, "rankingLouvain+PageRank_original", nomeArquivo)
	#salvaDadosArquivoTXT (ordenacaoPageRank, "rankingLouvain+PageRank_transformada", nomeArquivo)
	
	# Calculo a centralidade por autovetor da rede
	centrality_eigenvector = centralidade_autovetor (rede)
	centrality_eigenvectorNMF = centralidade_autovetor (redeNMF)
	
	#print 'Centralidade autovetor: ', centrality_eigenvector, "\n"
	#print 'Centralidade autovetor NMF: ', centrality_eigenvectorNMF, "\n"
	
	# Pego a centralidade por autovetor dentro do cluster que possui a descricao e ordeno
	rankingComunidade = rankingIntraComunidade (clusterPossuiDescricao, centrality_eigenvector, resultLouvain)
	rankingComunidadeNMF = rankingIntraComunidade (clusterPossuiDescricaoNMF, centrality_eigenvectorNMF, resultLouvainNMF)
	
	salvaDadosArquivoTXT (rankingComunidade, "rankingLouvain+Centralidade_original", nomeArquivo)
	salvaDadosArquivoTXT (rankingComunidadeNMF, "rankingLouvain+Centralidade_transformada", nomeArquivo)
	
	acertos = 0
	tamanhoSumario = 10
	for i in range(len(rankingComunidade)):
		if (rankingComunidade[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, len(rankingComunidade))
	print "Precision centralidade: ", precision
	
	
	acertos = 0
	tamanhoSumario = 10
	for i in range(len(rankingComunidadeNMF)):
		if (rankingComunidadeNMF[i][0] in oraculo):
			acertos = acertos + 1
	precision = calculaPrecision(acertos, len(rankingComunidadeNMF))
	print "Precision centralidade trans: ", precision
	
	#print "ranking: ", rankingComunidade
	#print "ranking NMF: ", rankingComunidadeNMF
	
	# Cluster importante 
	#rankingClusters = clusterImportante (mediaSimilaridadeCossenoDescricaoTitulo, resultLouvain)
	#rankingClustersNMF = clusterImportante (mediaSimilaridadeCossenoDescricaoTituloNMF, resultLouvainNMF)
	
	# "\n######################################### K-MEANS ################################################\n"
	
	#Kmeans
	#kmeansResultSimilaridadeCosseno = kmeans (matrizSimilaridadeCosseno)
	
	#print "Kmeans: ", kmeansResultSimilaridadeCosseno
	#print "len ", len(comentariosPreProcessado)
	#kmeansResultNMF = kmeans (matrizSimilaridadeCossenoNMF)
	
	# "\n######################################### RESULTADO ################################################\n"
	
	#resultadosPrecisionRecallFscore(oraculo, nomeArquivo, len(comentariosPreProcessado), rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF)
	
	#resultadosMAPIndividual(oraculo, nomeArquivo, len(comentariosPreProcessado), rankingSimilaridadeCossenoMediaTituloDescricao, rankingSimilaridadeCossenoMediaTituloDescricaoNMF, rankingMediaDistanciaEuclidianaTituloDescricao, rankingMediaDistanciaEuclidianaTituloDescricaoNMF, resultadoPageRank, resultadoPageRankNMF, resultadoColley, resultadoColleyNMF, resultadoMassey, resultadoMasseyNMF, ordenacaoPageRank, ordenacaoPageRankNMF, rankingComunidade, rankingComunidadeNMF)
	
	# Comentar os dois resultados acima e executar experimentosMAP.sh, pois e necessario que tenha feito todos os testes para executar o MAP geral
	#resultadosMAPGeral ()
	
	return 0

if __name__ == '__main__':
	main()	
