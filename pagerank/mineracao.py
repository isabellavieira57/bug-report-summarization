#!/usr/bin/python
# coding: utf-8

#-----------------------------------------------------------------------#
# Sumarização Automática de Relatórios de Bug							#
# Desenvolvido por Isabella Vieira Ferreira								#
# POC II - Ciência da Computação - UFSJ									#
#-----------------------------------------------------------------------#

import numpy as np
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from scipy import spatial

#-----------------------------------------------------------------------#
# Coloca os tokens distintos dos dois comentarios a serem analisados em #
# uma lista						 										#
#-----------------------------------------------------------------------#
def getTokensDistintos (comentarios):

	listaTokensDistintos = []

	for i in range(len(comentarios)):
		for j in range(len(comentarios[i])):
			if comentarios[i][j] not in listaTokensDistintos:
				listaTokensDistintos.append(comentarios[i][j])

	return listaTokensDistintos

#-----------------------------------------------------------------------#
# Conta quantas vezes o token aparece no documento						#
#-----------------------------------------------------------------------#
def frequenciaToken (token, comentariosPreProcessado):

	contador = 0

	for comentario in comentariosPreProcessado:
		contador = contador + comentario.count(token)

	return contador

#-----------------------------------------------------------------------#
# Numero de comentarios que tem o token 								#
#-----------------------------------------------------------------------#
def contaTokenDocumento (token, comentariosPreProcessado):

	count = 0

	for comentario in comentariosPreProcessado:
		if token in comentario:
			count = count + 1

	return count
#-----------------------------------------------------------------------#
# 						 												#
#-----------------------------------------------------------------------#
def tfxidf(comentariosPreProcessado, listaTokensDistintos, matriztfxidf):

	numeroComentarios = len(comentariosPreProcessado)

	for i in range(len(comentariosPreProcessado)):
		for j in range(len(listaTokensDistintos)):
			# numero de comentarios que tem o token
			totalComentariosTemToken = contaTokenDocumento(listaTokensDistintos[j], comentariosPreProcessado)		
			# quantas vezes o token aparece no documento
			frequenciaTokenDocumento = frequenciaToken(listaTokensDistintos[j],comentariosPreProcessado[i]) 		
			# calculo tfxidf	
			resultadoTFXIDF = (frequenciaTokenDocumento * (np.log(numeroComentarios/totalComentariosTemToken)))
			#matriztfxidf[i][j] = { 'token' : listaTokensDistintos[j], 'freq' : resultadoTFXIDF }
			matriztfxidf[i][j] = resultadoTFXIDF
	
#-----------------------------------------------------------------------#
# spatial.distance.cosine calcula a distância e não a similaridade.     # 
# Para avaliar a similaridade, deve-se subtrair 1.                      #
#-----------------------------------------------------------------------#
def calculaSimilaridadeCosseno (matrizSimilaridadeCosseno, comentariosPreProcessado, matriztfxidf):

	for i in range(len(matriztfxidf)):
		for j in range(len(matriztfxidf)):
			similaridade = 1 - spatial.distance.cosine(matriztfxidf[i], matriztfxidf[j])
			matrizSimilaridadeCosseno[i][j] = similaridade
			
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def salvaMatrizSimilaridadeCossenoEsparsa (matriz, nomeArquivo):

	arquivoGrafoPonderado = open(nomeArquivo, 'wr+')
	
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			arquivoGrafoPonderado.write("%d %d %f\n" % (i,j,matriz[i][j]))
				
	arquivoGrafoPonderado.close()
			
#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def calculaDistanciaEuclidiana	(matrizDistanciaEuclidiana, comentariosPreProcessado, matriztfxidf):

	for i in range(len(comentariosPreProcessado)):
		for j in range(len(comentariosPreProcessado)):
			distanciaEuclidiana = spatial.distance.euclidean(matriztfxidf[i], matriztfxidf[j])
			matrizDistanciaEuclidiana[i][j] = distanciaEuclidiana
	
#-----------------------------------------------------------------------------#
# Método de Fatoração de Matrizes: NMF									  	  #
#-----------------------------------------------------------------------------#
def nmf (matriztfxidf):
	
	nmf = NMF(n_components = 50, init='random', random_state=0)
	matrizReduzida = nmf.fit_transform(matriztfxidf)			# w
	#h = nmf.components_										# h
	#resultado = np.dot(matrizReduzida, h)						# w.h -> volta na matriz original aproximada

	return matrizReduzida
	
#-----------------------------------------------------------------------------#
# Método de Fatorização de Matrizes: PCA									  #
#-----------------------------------------------------------------------------#
def pca (matriztfxidf):

	normalizaTFXIDF (matriztfxidf)
	
	vetor = []
	
	# testa qual o melhor numero de componentes	que representa 95% dos dados
	for i in range(len(matriztfxidf[0])):
		num_pca_components = i
		pca = PCA(num_pca_components)
		pca.fit(matriztfxidf)
		PCA(copy=True, whiten=False)

		# guardo em um vetor para montar graficos
		# vetor.append(sum(pca.explained_variance_ratio_))
		
		if(sum(pca.explained_variance_ratio_) >= 0.95):
			#print "Numero de colunas: ", len(np.transpose(matriztfxidf))
			#print "Numero de linhas: ", len(matriztfxidf)
			#print "Numero de PCA componentes (95%): ",num_pca_components
			#print "Componentes"
			#print pca.explained_variance_ratio_

			pca.n_components = num_pca_components
			pca.fit(matriztfxidf)
			matrizReduzida = pca.fit_transform(matriztfxidf)
			#print "Tamanho da matriz redimensionada: ", matrizReduzida.shape
			#print "Nova matriz reduzida: ", matrizReduzida			
			break

	#inverso = pca.inverse_transform(matrizReduzida)
	
	#print "INVERSO"
	#print inverso
	
	#return matrizReduzida
	return num_pca_components
	#print "VETOR\n"
	#print vetor

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def kmeans (matriz):
	
	kmeans = KMeans(init='k-means++', n_clusters=2, n_init=10, copy_x=True)
	kmeans.fit_transform(matriz)

	return kmeans.cluster_centers_
	#return kmeans.labels_
	
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def calculaPrecision (acertos, tamanhoSumario):

	# no caso de nao ter ninguem na comunidade
	if (tamanhoSumario==0):
		return 0.0
	else: 
		return (float(acertos)/float(tamanhoSumario))

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def calculaAveragePrecision (acertos, tamanhoSumario, numeroComentarios):
	
	#return (calculaPrecision(acertos,tamanhoSumario) / numeroComentarios)
	return (calculaPrecision(acertos,tamanhoSumario))
	
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def calculaRecall (acertos, tamanhoOraculo):
	
	return (float(acertos)/float(tamanhoOraculo))
	
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def calculaFscore (precision, recall):
	
	if ((precision==0) and (recall==0)): 
		return 0
	else:
		return (2*((float(precision)*float(recall))/(float(precision)+float(recall))))
	

#-----------------------------------------------------------------------------#
# Calcula Mean Average Precision (MAP)										  #
#-----------------------------------------------------------------------------#
def calculaMAP (acertos, tamanhoSumario, numeroComentarios, totalRelatoriosBugProjeto):

	averagePrecision = calculaAveragePrecision (acertos, tamanhoSumario, numeroComentarios)
	
	return (averagePrecision/totalRelatoriosBugProjeto)
		
#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#	
def leArquivoMAPIndividual (arquivo):
	
	linha = arquivo.readlines()	# possui todas as linhas do arquivo em um vetor
	
	MAP = []
	
	for conteudo in linha:
		tokens = conteudo.split("		")
		MAP.append(float(tokens[1]))
			
	somatorioMAPAngular = 0
	i=0
	while (i<5):
		somatorioMAPAngular = somatorioMAPAngular + MAP[i]
		i = i + 1
	
	somatorioMAPJquery = 0
	i = 5
	while (i<10):
		somatorioMAPJquery = somatorioMAPJquery + MAP[i]
		i = i + 1
	
	somatorioMAPBootstrap = 0
	i = 10
	while (i<15):
		somatorioMAPBootstrap = somatorioMAPBootstrap + MAP[i]
		i = i + 1

	return somatorioMAPAngular, somatorioMAPJquery, somatorioMAPBootstrap
	
