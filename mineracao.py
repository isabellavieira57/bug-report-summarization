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
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from scipy import spatial
#np.seterr(divide='ignore', invalid='ignore')

#-----------------------------------------------------------------------#
# Coloca os tokens distintos dos dois comentarios a serem analisados em #
# uma lista						 										#
#-----------------------------------------------------------------------#
def getTokensDistintos (comentario1, comentario2):

	listaTokensDistintos = []

	# -2 para nao verificar a referencia explicita e o like
	for i in range(len(comentario1)-2):
		if comentario1[i] not in listaTokensDistintos:
			listaTokensDistintos.append(comentario1[i])
	
	for i in range(len(comentario2)-2):
		if comentario2[i] not in listaTokensDistintos:
			listaTokensDistintos.append(comentario2[i])

	return listaTokensDistintos

#-----------------------------------------------------------------------#
# Coloca os tokens distintos dos dois comentarios a serem analisados em #
# uma lista						 										#
#-----------------------------------------------------------------------#
"""def getTokensDistintosTitulo (comentario1, titulo):

	listaTokensDistintos = []

	# -2 para nao verificar a referencia explicita e o like
	for i in range(len(comentario1)-2):
		if comentario1[i] not in listaTokensDistintos:
			listaTokensDistintos.append(comentario1[i])

	for i in range(len(titulo)):
		if titulo[i] not in listaTokensDistintos:
			listaTokensDistintos.append(titulo[i])

	return listaTokensDistintos"""

#-----------------------------------------------------------------------#
# Calcula a frequencia de um termo em uma lista de tokens distintos 	#
#-----------------------------------------------------------------------#
def calculaFrequenciaSimilaridadeCosseno (comentario, listaTokensDistintos, indexComentario, matriztfxidf):

	frequenciaComentario = []

	for i in range(len(listaTokensDistintos)):
		if (listaTokensDistintos[i] in comentario):						# Se o token distinto esta no comentario
			index = comentario.index(listaTokensDistintos[i])
			frequenciaComentario.append(matriztfxidf[indexComentario][index])
		else:
			frequenciaComentario.append(0)

	return frequenciaComentario

#-----------------------------------------------------------------------#
# Calcula a frequencia de um termo em uma lista de tokens distintos 	#
#-----------------------------------------------------------------------#
"""def calculaFrequenciaSimilaridadeCossenoTitulo (titulo, listaTokensDistintos, indexComentario, matriztfxidfTitulo):

	frequenciaComentario = []

	for i in range(len(listaTokensDistintos)):
		if (listaTokensDistintos[i] in titulo):						# Se o token distinto esta no comentario
			index = titulo.index(listaTokensDistintos[i])
			frequenciaComentario.append(matriztfxidfTitulo[indexComentario][index])
		else:
			frequenciaComentario.append(0)

	return frequenciaComentario"""

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
def tfxidf (token, i, j, comentariosPreProcessado, vetorIntermerdiario):

	totalComentariosTemToken = contaTokenDocumento(token,comentariosPreProcessado)
	frequenciaTokenDocumento = frequenciaToken(token,comentariosPreProcessado) 
	numeroComentarios = len(comentariosPreProcessado)

	if (totalComentariosTemToken != 0):
		resultadoTFXIDF = (frequenciaTokenDocumento * (np.log(numeroComentarios/totalComentariosTemToken)))
	else:
		resultadoTFXIDF = (frequenciaTokenDocumento * (np.log(numeroComentarios)))

	vetorIntermerdiario.append(resultadoTFXIDF)
	
	
#-----------------------------------------------------------------------#
# Normaliza numero colunas na matriz tfxidf								#
# Todas as linhas passam a ter o mesmo numero de colunas preenchidas com #
# 0 (ou seja, nao possui aquele termo)									#
#-----------------------------------------------------------------------#
def normalizaTFXIDF (matriztfxidf):
	
	# Encontra qual a maior dimensao da matriz
	maiorDimensao = 0
	for i in (range(len(matriztfxidf))):
		if (len(matriztfxidf[i]) > maiorDimensao):
			maiorDimensao = len(matriztfxidf[i])
			#maiorIndice = i
	
	maiorDimensao = maiorDimensao
	#print "MAIOR DIMENSAO: ", maiorDimensao
	
	# Percorre a matriz toda e depois cada linha, concatenando ate atingir a maior dimensao
	for i in range(len(matriztfxidf)):
		j = len(matriztfxidf[i])
		quantidadeColunasFaltantes = maiorDimensao - len(matriztfxidf[i])
		for j in range(quantidadeColunasFaltantes):
			matriztfxidf[i].append(0)
		
#-----------------------------------------------------------------------#
# spatial.distance.cosine calcula a distância e não a similaridade.     # 
# Para avaliar a similaridade, deve-se subtrair 1.                      #
#-----------------------------------------------------------------------#
def calculaSimilaridadeCosseno (matriz, indexComentario1, indexComentario2, frequenciaComentario1, frequenciaComentario2):

	similaridade = 1 - spatial.distance.cosine(frequenciaComentario1, frequenciaComentario2)
	
	#similaridadeTruncada = float(format(similaridade, ".1f"))	# 1 casa decimal depois da virgula
	#print "similaridade truncada ", similaridadeTruncada
	#matrizSimilaridadeCosseno[indexComentario1][indexComentario2] = similaridadeTruncada
	#matrizSimilaridadeCosseno[indexComentario2][indexComentario1] = similaridadeTruncada
	
	matriz[indexComentario1][indexComentario2] = similaridade
	matriz[indexComentario2][indexComentario1] = similaridade

#-----------------------------------------------------------------------#
# spatial.distance.cosine calcula a distância e não a similaridade.     # 
# Para avaliar a similaridade, deve-se subtrair 1.                      #
#-----------------------------------------------------------------------#
"""def calculaSimilaridadeCossenoTitulo (vetorSimilaridadeCossenoTitulo, indexComentario, frequenciaComentario1, frequenciaComentario2):

	similaridade = 1 - spatial.distance.cosine(frequenciaComentario1, frequenciaComentario2)
	#similaridadeTruncada = float(format(similaridade, ".1f"))	# 1 casa decimal depois da virgula
	#vetorSimilaridadeCossenoTitulo[indexComentario] = similaridadeTruncada
	vetorSimilaridadeCossenoTitulo[indexComentario] = similaridade"""

#-----------------------------------------------------------------------------#
# average(cosine_similarities)+alpha*standard_deviation(cosine_similarities)  #
#-----------------------------------------------------------------------------#
"""def calculaThresholdSimilaridadeCosseno (matrizSimilaridadeCosseno):

	alpha = 0.75

	threshold = np.mean(matrizSimilaridadeCosseno) + alpha * np.std(matrizSimilaridadeCosseno)

	return threshold"""
	
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
"""def salvaMatrizSimilaridadeCosseno (matriz, tamanhoMatriz):

	arquivoGrafoPonderado = open("similaridadeCosseno.txt", 'wr+')
	
	for i in range(tamanhoMatriz):
		for j in range(i+1,tamanhoMatriz):
			arquivoGrafoPonderado.write("%d %d %0.1f\n" % (i,j,matriz[i][j]))
	
	for i in range(tamanhoMatriz):
		for j in range(tamanhoMatriz):
			arquivoGrafoPonderado.write("%d %d %0.1f\n" % (i,j,matriz[i][j]))
	
	
	arquivoGrafoPonderado.close()"""

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def salvaMatrizSimilaridadeCossenoEsparsa (matriz, tamanhoMatriz, nomeArquivo):

	arquivoGrafoPonderado = open(nomeArquivo, 'wr+')
	
	for i in range(tamanhoMatriz):
		for j in range(i+1,tamanhoMatriz):
			arquivoGrafoPonderado.write("%d %d %0.1f\n" % (i,j,matriz[i][j]))
				
	arquivoGrafoPonderado.close()
	
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def fazCopiaMatrizSimilaridadeCosseno (matrizSimilaridadeCosseno, copiaMatrizSimilaridadeCosseno):

	for i in range(len(matrizSimilaridadeCosseno)):
		for j in range(len(matrizSimilaridadeCosseno)):
			copiaMatrizSimilaridadeCosseno[i][j] = matrizSimilaridadeCosseno[i][j]
			
#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def calculaMediaSimilaridadeComentarioTituloDescricao (matriz):

	mediaDescricaoTitulo = []
	vetorParaMedia = []
	vetorIntermerdiario = []

	for i in range(len(matriz)):
		vetorIntermerdiario.append(matriz[0][i])	# titulo
		vetorIntermerdiario.append(matriz[1][i]) # descricao
		vetorParaMedia.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	for i in range(len(matriz)):
		mediaDescricaoTitulo.append(np.mean(vetorParaMedia[i]))		# contem a media da similaridade do titulo e da descricao, o index do vetor mediaDescricaoTitulo é o ID do comentário

	return mediaDescricaoTitulo

#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def calculaDistanciaEuclidiana	(matrizDistanciaEuclidiana, indexComentario1, indexComentario2, frequenciaComentario1, frequenciaComentario2):

	distanciaEuclidiana = spatial.distance.euclidean(frequenciaComentario1, frequenciaComentario2)
	matrizDistanciaEuclidiana[indexComentario1][indexComentario2] = distanciaEuclidiana
	matrizDistanciaEuclidiana[indexComentario2][indexComentario1] = distanciaEuclidiana
	
#-----------------------------------------------------------------------#
# spatial.distance.cosine calcula a distância e não a similaridade.     # 
# Para avaliar a similaridade, deve-se subtrair 1.                      #
#-----------------------------------------------------------------------#
"""def calculaDistanciaEuclidianaTitulo (vetorDistanciaEuclidianaTitulo, indexComentario, frequenciaComentario1, frequenciaComentario2):

	distanciaEuclidiana = spatial.distance.euclidean(frequenciaComentario1, frequenciaComentario2)
	vetorDistanciaEuclidianaTitulo[indexComentario] = distanciaEuclidiana"""
	
#-----------------------------------------------------------------------------#
# Método de Fatorização de Matrizes: NMF									  #
# Matriz tfxidf nao tem like e referencia explicita
#-----------------------------------------------------------------------------#
def nmf (matriztfxidf):
	
	"""normalizaTFXIDF(matriztfxidf)
	
	print "Numero de linhas Matriz TFXIDF: ", len(matriztfxidf)
	print "Numero de colunas Matriz TFXIDF: ", len(matriztfxidf[0])
	
	model = NMF(n_components=2, init='random', random_state=0)
	matrizReduzida = model.fit_transform(matriztfxidf)
	
	print "\n\nCOMPONENTES"
	print matrizReduzida
	print "\n\nMODEL RECONSTRUCTION"
	print model.reconstruction_err_"""
	
	normalizaTFXIDF (matriztfxidf)
	
	#print "Numero linhas normal: ", len(matriztfxidf)
	#print "Numero colunas normal: ", len(np.transpose(matriztfxidf))
	
	#num_nmf_components = 1
	#while (num_nmf_components <= len(np.transpose(matriztfxidf))):
	
		#nmf = NMF(n_components = num_nmf_components, init='random', random_state=0)
	nmf = NMF(n_components = 14, init='random', random_state=0)
	#nmf = NMF(n_components = 13, init='nndsvd')
	matrizReduzida = nmf.fit_transform(matriztfxidf)
	
	#	if(nmf.reconstruction_err_ < 1.0):
			#print "Numero de colunas: ", len(np.transpose(matriztfxidf))
			#print "Numero de linhas: ", len(matriztfxidf)
			#print "Erro NMF: ",nmf.reconstruction_err_
			#print "Numero de componentes: ", num_nmf_components
			#print "Componentes"
			#print "Numero de linhas matriz reduzida: ", len(matrizReduzida)
			#print "Numero de colunas matriz reduzida: ", len(np.transpose(matrizReduzida))
			#print matrizReduzida
		
	#		break
	
	#	num_nmf_components = num_nmf_components + 1
	
	#print "numero linhas reduzida: ", len(matrizReduzida)
	#print "numero colunas reduzida: ", len(np.transpose(matrizReduzida))
	#print "erro: ", nmf.reconstruction_err_
	return matrizReduzida
	
#-----------------------------------------------------------------------------#
# Método de Fatorização de Matrizes: PCA									  #
# Matriz tfxidf nao tem like e referencia explicita
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
	
	return (float(acertos)/float(tamanhoSumario))

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def calculaAveragePrecision (acertos, tamanhoSumario, numeroComentarios):
	
	return (calculaPrecision(acertos,tamanhoSumario) / numeroComentarios)
	
		
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
