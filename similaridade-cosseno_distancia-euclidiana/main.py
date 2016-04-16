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
	calculaDistanciaEuclidiana(matrizDistanciaEuclidiana, comentariosPreProcessado, matriztfxidf)
			
	# Ordena a similaridade de todos os comentarios com o titulo+descricao
	rankingSimilaridadeCossenoTituloDescricao = ordenaRanking (matrizSimilaridadeCosseno[0])
	removeTituloDescricaoRanking(rankingSimilaridadeCossenoTituloDescricao)
	salvaDadosArquivoTXT (rankingSimilaridadeCossenoTituloDescricao, "rankingSimCosseno_original", nomeArquivo)
	
	# Ordena a distancia euclidiana de todos os comentarios com o titulo+descricao
	rankingDistanciaEuclidianaTituloDescricao = ordenaRanking (matrizDistanciaEuclidiana[0])
	removeTituloDescricaoRanking(rankingDistanciaEuclidianaTituloDescricao)
	salvaDadosArquivoTXT (rankingDistanciaEuclidianaTituloDescricao, "rankingEuclidiana_original", nomeArquivo)
	
	# "\n#################################### MATRIZ TRANSFORMADA ###########################################\n"
	
	# NMF
	matrizReduzidaNMF = nmf(matriztfxidf)

	# Inicializa matrizes para NMF
	matrizSimilaridadeCossenoNMF = inicializaMatriz(matrizReduzidaNMF)		
	matrizDistanciaEuclidianaNMF = inicializaMatriz(matrizReduzidaNMF)	
	
	# Calculo a similaridade de cosseno e a distancia euclidiana na matriz reduzida
	calculaSimilaridadeCosseno(matrizSimilaridadeCossenoNMF, matrizReduzidaNMF, matrizReduzidaNMF)
	calculaDistanciaEuclidiana(matrizDistanciaEuclidianaNMF, matrizReduzidaNMF, matrizReduzidaNMF)

	# Ordena a similaridade dos comentários com o título e a descrição
	rankingSimilaridadeCossenoTituloDescricaoNMF = ordenaRanking (matrizSimilaridadeCossenoNMF[0])
	removeTituloDescricaoRanking(rankingSimilaridadeCossenoTituloDescricaoNMF)
	salvaDadosArquivoTXT (rankingSimilaridadeCossenoTituloDescricaoNMF, "rankingSimCosseno_transformada", nomeArquivo)

	# Ordena distancia euclidiana dos comentários com o título e a descrição
	rankingDistanciaEuclidianaTituloDescricaoNMF = ordenaRanking (matrizDistanciaEuclidianaNMF[0])	
	removeTituloDescricaoRanking(rankingDistanciaEuclidianaTituloDescricaoNMF)
	salvaDadosArquivoTXT (rankingDistanciaEuclidianaTituloDescricaoNMF, "rankingEuclidiana_transformada", nomeArquivo)
	
	# "\n######################################### RESULTADO ################################################\n"
	
	resultadosPrecisionRecallFscore(oraculo, nomeArquivo, len(comentariosPreProcessado), rankingSimilaridadeCossenoTituloDescricao, rankingSimilaridadeCossenoTituloDescricaoNMF, rankingDistanciaEuclidianaTituloDescricao, rankingDistanciaEuclidianaTituloDescricaoNMF)

	return 0

if __name__ == '__main__':
	main()	