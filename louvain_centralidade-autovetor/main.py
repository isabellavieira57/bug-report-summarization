#!/usr/bin/python
# coding: utf-8

#-----------------------------------------------------------------------#
# Sumarização Automática de Relatórios de Bug							#
# Desenvolvido por Isabella Vieira Ferreira								#
# POC II - Ciência da Computação - UFSJ									#
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
	
	comentariosSemStopWords = removeStopWords(comentarios)
	comentariosSemNumeros = removeNumeros(comentariosSemStopWords)
	comentariosSemCaracteresEspeciais = removeCaracteresEspeciais(comentariosSemNumeros)
	comentariosPreProcessado = stemming(comentariosSemCaracteresEspeciais)

	# Concateno titulo e descricao para um unico comentario
	tituloEDescricao = comentariosPreProcessado[0]+comentariosPreProcessado[1]
	del (comentariosPreProcessado[0])		# remove titulo dos comentarios pre processados
	del (comentariosPreProcessado[0])		# remove descricao dos comentarios pre processados
	comentariosPreProcessado.insert(0, tituloEDescricao)		# insere titulo + descricao na posicao 0 da matriz

	# matriz de ordem N, onde N é o número de comentários (primeiro comentario é titulo+descricao)
	matrizSimilaridadeCosseno = inicializaMatriz(comentariosPreProcessado)		
	matrizDistanciaEuclidiana = inicializaMatriz(comentariosPreProcessado)		
	
	# tenho uma lista com todos os tokens distintos desse relatorio
	listaTokensDistintos = getTokensDistintos(comentariosPreProcessado)

	# Matriz tfxidf -> linhas = numero comentarios, colunas = numero tokens distintos
	matriztfxidf = [[0.0 for x in range(len(listaTokensDistintos))] for x in range(len(comentariosPreProcessado))]
	
	# Calculo TFXIDF para cada token de cada comentario
	tfxidf(comentariosPreProcessado, listaTokensDistintos, matriztfxidf)
		
    # "\n#################################### MATRIZ ORIGINAL ###########################################\n"
    
	# Para cada comentario calcula a similaridade de cosseno e a distancia euclidiana daquele comentario para todos
	# linha 0 da matriz possui a distancia de todos os comentarios para o titulo+descricao
	calculaSimilaridadeCosseno(matrizSimilaridadeCosseno, comentariosPreProcessado, matriztfxidf)
			
	# "\n#################################### MATRIZ TRANSFORMADA ###########################################\n"
	
	# NMF
	matrizReduzidaNMF = nmf(matriztfxidf)

	# Inicializa matrizes para NMF
	matrizSimilaridadeCossenoNMF = inicializaMatriz(matrizReduzidaNMF)		
	
	# Calculo a similaridade de cosseno e a distancia euclidiana na matriz reduzida
	calculaSimilaridadeCosseno(matrizSimilaridadeCossenoNMF, matrizReduzidaNMF, matrizReduzidaNMF)
			
	# "\n######################################### GRAFO ################################################\n"
			
	matrizPageRank = inicializaMatriz(matrizSimilaridadeCosseno)		
	matrizPageRankNMF = inicializaMatriz(matrizSimilaridadeCossenoNMF)
			
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
		
	# Acho os clusters na rede
	resultLouvain = louvain(rede)
	resultLouvainNMF = louvain(redeNMF)
		
	# Calculo a centralidade por autovetor da rede
	centrality_eigenvector = centralidade_autovetor (rede)
	centrality_eigenvectorNMF = centralidade_autovetor (redeNMF)
	
	# Verifico qual cluster possui a descrição (id=0)
	clusterPossuiDescricao = verificaClusterPossuiDescricao(resultLouvain)
	clusterPossuiDescricaoNMF = verificaClusterPossuiDescricao(resultLouvainNMF)
	
	# Pego a centralidade por autovetor dentro do cluster que possui a descricao e ordeno
	rankingComunidade = rankingIntraComunidade (clusterPossuiDescricao, centrality_eigenvector, resultLouvain)
	rankingComunidadeNMF = rankingIntraComunidade (clusterPossuiDescricaoNMF, centrality_eigenvectorNMF, resultLouvainNMF)
	
	removeTituloDescricaoRanking(rankingComunidade)
	removeTituloDescricaoRanking(rankingComunidadeNMF)
	
	salvaDadosArquivoTXT (rankingComunidade, "rankingLouvain+Centralidade_original", nomeArquivo)
	salvaDadosArquivoTXT (rankingComunidadeNMF, "rankingLouvain+Centralidade_transformada", nomeArquivo)
	
	# "\n######################################### RESULTADO ################################################\n"
	
	resultadosPrecisionRecallFscore(oraculo, nomeArquivo, len(comentariosPreProcessado), rankingComunidade, rankingComunidadeNMF)
	
	return 0

if __name__ == '__main__':
	main()	
