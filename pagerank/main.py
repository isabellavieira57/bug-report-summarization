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
	eventos = leArquivoEventos(retorno[1])

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

	#comentariosSemURL = removeURL(comentarios)
	#comentariosSemStopWords = removeStopWords(comentariosSemURL)
	#comentariosSemNumeros = removeNumeros(comentariosSemStopWords)
	#comentariosSemCaracteresEspeciais = removeCaracteresEspeciais(comentariosSemNumeros)
	#comentariosSemMeses = removeMeses(comentariosSemCaracteresEspeciais)	
	#comentariosPreProcessado = stemming(comentariosSemCaracteresEspeciais)

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
	calculaSimilaridadeCosseno(matrizSimilaridadeCosseno, matriztfxidf)
			
	# "\n#################################### MATRIZ TRANSFORMADA ###########################################\n"
	
	# NMF
	matrizReduzidaNMF = nmf(matriztfxidf)

	# Inicializa matrizes para NMF
	matrizSimilaridadeCossenoNMF = inicializaMatriz(matrizReduzidaNMF)		
	
	# Calculo a similaridade de cosseno e a distancia euclidiana na matriz reduzida
	calculaSimilaridadeCosseno(matrizSimilaridadeCossenoNMF, matrizReduzidaNMF)
			
	# "\n######################################### GRAFO ################################################\n"
			
	# Fazer massey antes de fazer esparcidade da matriz de similaridade de cosseno
	#resultadoMassey = massey(len(comentarios), matrizSimilaridadeCosseno)
	#resultadoMasseyNMF = massey(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)	
	#salvaDadosArquivoTXT (resultadoMassey, "rankingMassey_original", nomeArquivo)
	#salvaDadosArquivoTXT (resultadoMassey, "rankingMassey_transformada", nomeArquivo)
	
	# Fazer colley antes de fazer esparcidade da matriz de similaridade de cosseno
	#resultadoColley = colley(len(comentarios), matrizSimilaridadeCosseno)
	#resultadoColleyNMF = colley(len(matrizReduzidaNMF), matrizSimilaridadeCossenoNMF)
	#salvaDadosArquivoTXT (resultadoColley, "rankingColley_original", nomeArquivo)
	#salvaDadosArquivoTXT (resultadoColleyNMF, "rankingColley_transformada", nomeArquivo)
	
	matrizPageRank = inicializaMatriz(matrizSimilaridadeCosseno)		
	matrizPageRankNMF = inicializaMatriz(matrizSimilaridadeCossenoNMF)
			
	calculaPesoMatrizPageRank(matrizPageRank, matrizSimilaridadeCosseno, eventos)
	calculaPesoMatrizPageRank(matrizPageRankNMF, matrizSimilaridadeCossenoNMF, eventos)
				
	aumentaEsparcidadeMatriz (matrizPageRank)
	aumentaEsparcidadeMatrizNMF (matrizPageRankNMF)	

	matrizEstocasticaPageRank(matrizPageRank)
	matrizEstocasticaPageRank(matrizPageRankNMF)
	
	salvaMatrizSimilaridadeCossenoEsparsa (matrizPageRank, "grafo.txt")
	salvaMatrizSimilaridadeCossenoEsparsa (matrizPageRankNMF, "grafoNMF.txt")

	rede = inicializaGrafo ("grafo.txt")
	redeNMF = inicializaGrafo ("grafoNMF.txt")
	
	#os.remove("grafo.txt")
	#os.remove("grafoNMF.txt")
	
	# Pagerank
	resultadoPageRank = pageRank(rede)
	resultadoPageRankNMF = pageRank(redeNMF)
	
	removeTituloDescricaoRanking(resultadoPageRank)	
	removeTituloDescricaoRanking(resultadoPageRankNMF)	

	rankingSemUm = removeMaisUm(resultadoPageRank, comentariosPreProcessado)
	rankingSemUmNMF = removeMaisUm(resultadoPageRankNMF, comentariosPreProcessado)

	for i in range(len(rankingSemUm)):
		rankingSemUm[i][0] = rankingSemUm[i][0] + 1

	for i in range(len(rankingSemUmNMF)):
		rankingSemUmNMF[i][0] = rankingSemUmNMF[i][0] + 1	
	
	salvaDadosArquivoTXT (rankingSemUm, comentarios, "rankingPageRank_original", nomeArquivo)
	salvaDadosArquivoTXT (rankingSemUmNMF, comentarios, "rankingPageRank_transformada", nomeArquivo)

	arquivo = open("resultados/resultadosRanking/sumario_PageRank" + nomeArquivo + ".txt", 'w')
	sep = " "

	for i in range(10):
		comentario =  sep.join(comentarios[rankingSemUm[i][0]])    
		arquivo.write(comentario)
		arquivo.write ("\n\n")

	arquivo.close()
	
	# "\n######################################### RESULTADO ################################################\n"
	
	resultadosPrecisionRecallFscore(oraculo, nomeArquivo, len(comentariosPreProcessado), rankingSemUm, rankingSemUmNMF)
		
	return 0

if __name__ == '__main__':
	main()	
