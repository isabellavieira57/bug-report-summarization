#!/usr/bin/python
# coding: utf-8

#-----------------------------------------------------------------------#
# Algoritmo:															#
# Desenvolvido por Isabella Vieira Ferreira								#
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

import nltk
import re
import operator
import numpy as np
import cairo
from sys import argv, exit
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from scipy import spatial
from operator import itemgetter
from igraph import *

#-----------------------------------------------------------------------#
# Função que lê o arquivo. 												#
#-----------------------------------------------------------------------#
def leArquivo():	
	try:
	    if(argv[1] == "-c"):
	        arquivo = open(argv[2], 'r')
	    else:
	        print "O padrao a ser seguido deve ser:\n"
	        print "python linksGrafo.py -c <nome_arquivo_entrada>"
	        exit(0)
	except:
	    print "O padrao a ser seguido deve ser:\n"
	    print "python linksGrafo.py -c <nome_arquivo_entrada>"
	    exit(0)
	
	conteudo = arquivo.readlines()		# conteudo armazena os itens de cada linha
	comentarios = []
	titulo = []
	texto = []
	string = ""
	tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')		# Expressao regular que quebra a string em substrings
	flag = 1

	# Verifica se é uma linha vazia
	# Se não for, contatena toda a string (comentario), coloca tudo em letra maiuscula, separa os tokens e coloca na lista de comentarios
	for item in conteudo:
		if (item != '\n'):
			string = string + str(item)
			string = re.sub(r'[\xc2\x99]'," ", string)	# expressao regular para remover bad caracteres (\xc2 - espaco)
		else:
			stringUpper = string.lower()
			tokens = tokenizer.tokenize(stringUpper)	
			if (flag == 1):
				titulo.append(tokens)
				flag = 0
			else:
				comentarios.append(tokens)
			texto = []
			string = ""

	return comentarios, titulo

#-----------------------------------------------------------------------#
# Uma referencia é explicita se ela possui @<nome_usuario>				#
# É salvo o id do comentario de @<nome_usuario> 						#
#-----------------------------------------------------------------------#
def salvaReferenciaExplicita(comentarios):	

	for i in (range(len(comentarios))):

		# Verifica se há uma referencia explicita em todo o comentario
		if (re.search('@+(\w)+', str(comentarios[i]))) is not None:

			referencia = re.search('@+(\w)+', str(comentarios[i]));

			# Percorro do 0 ate onde estou para olhar a referencia anterior
			for j in range(i):

				autorReferenciado = (str(referencia.group())).replace("@","")

				# Se o nome do autor do bug for igual ao da referencia
				if (comentarios[j][0] == autorReferenciado):
					idReferenciado = comentarios.index(comentarios[j])
					comentarios[i].append(idReferenciado)
					break
		else:
			comentarios[i].append(-1) 	# Se o comentario nao possui referencia a outro comentario

#-----------------------------------------------------------------------#
# TODO: falta verificar qual comentario  o like esta referenciando		#
# No momento está verificando apenas se o comentario possui like ou nao #
#-----------------------------------------------------------------------#
def verificaLike(comentarios):	

	for i in (range(len(comentarios))):
		if ("+1") in comentarios[i]:
			comentarios[i].append(1)
		else:
			comentarios[i].append(0)

#-----------------------------------------------------------------------------#
# 							 												  #
#-----------------------------------------------------------------------------#
def removeStopWords (comentarios):

	comentariosPreProcessado = []
	listaIntermediaria = []

	stopwords = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}
	
	j = 0

	for i in range(len(comentarios)):
		j=0
		while (j < len(comentarios[i])):
			if comentarios[i][j] not in stopwords:
				listaIntermediaria.append(comentarios[i][j])
			j = j + 1
		comentariosPreProcessado.append(listaIntermediaria)
		listaIntermediaria = []

	return comentariosPreProcessado

#-----------------------------------------------------------------------------#
# TODO: remover numeros		 												  #
#-----------------------------------------------------------------------------#
def removeCaracteresEspeciais (comentarios):

	comentariosPreProcessado = []
	listaIntermediaria = []

	caracteresEspeciais = {",",".",";","-","_","?","!",":", "(", ")", "/", "|", "=", "[","]", "'", '"', "$", "#","/", "...", "{", "}", "[];", "();", "()", "'s", "..", "->"}

	j = 0

	for i in range(len(comentarios)):
		j=0
		while (j < len(comentarios[i])):
			if comentarios[i][j] not in caracteresEspeciais:
				#re.match("[1-9]"," ", comentarios[i][j])
				listaIntermediaria.append(comentarios[i][j])
			j = j + 1
		comentariosPreProcessado.append(listaIntermediaria)
		listaIntermediaria = []

	return comentariosPreProcessado

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
def getTokensDistintosTitulo (comentario1, titulo):

	listaTokensDistintos = []

	# -2 para nao verificar a referencia explicita e o like
	for i in range(len(comentario1)-2):
		if comentario1[i] not in listaTokensDistintos:
			listaTokensDistintos.append(comentario1[i])

	for i in range(len(titulo)):
		if titulo[i] not in listaTokensDistintos:
			listaTokensDistintos.append(titulo[i])

	return listaTokensDistintos

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
def calculaFrequenciaSimilaridadeCossenoTitulo (titulo, listaTokensDistintos, indexComentario, matriztfxidfTitulo):

	frequenciaComentario = []

	for i in range(len(listaTokensDistintos)):
		if (listaTokensDistintos[i] in titulo):						# Se o token distinto esta no comentario
			index = titulo.index(listaTokensDistintos[i])
			frequenciaComentario.append(matriztfxidfTitulo[indexComentario][index])
		else:
			frequenciaComentario.append(0)

	return frequenciaComentario

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

	resultadoTFXIDF = (frequenciaTokenDocumento * (np.log(numeroComentarios/totalComentariosTemToken)))

	vetorIntermerdiario.append(resultadoTFXIDF)

#-----------------------------------------------------------------------#
# 						 												#
#-----------------------------------------------------------------------#
def inicializaMatriz (comentarios):

	matrizSimilaridadeCosseno = [[0 for x in range(len(comentarios))] for x in range(len(comentarios))]

	return matrizSimilaridadeCosseno

#-----------------------------------------------------------------------#
# spatial.distance.cosine calcula a distância e não a similaridade.     # 
# Para avaliar a similaridade, deve-se subtrair 1.                      #
#-----------------------------------------------------------------------#
def calculaSimilaridadeCosseno (matrizSimilaridadeCosseno, indexComentario1, indexComentario2, frequenciaComentario1, frequenciaComentario2):

	similaridade = 1 - spatial.distance.cosine(frequenciaComentario1, frequenciaComentario2)
	matrizSimilaridadeCosseno[indexComentario1][indexComentario2] = similaridade
	matrizSimilaridadeCosseno[indexComentario2][indexComentario1] = similaridade

#-----------------------------------------------------------------------#
# spatial.distance.cosine calcula a distância e não a similaridade.     # 
# Para avaliar a similaridade, deve-se subtrair 1.                      #
#-----------------------------------------------------------------------#
def calculaSimilaridadeCossenoTitulo (vetorSimilaridadeCossenoTitulo, indexComentario, frequenciaComentario1, frequenciaComentario2):

	similaridade = 1 - spatial.distance.cosine(frequenciaComentario1, frequenciaComentario2)
	vetorSimilaridadeCossenoTitulo[indexComentario] = similaridade

#-----------------------------------------------------------------------------#
# average(cosine_similarities)+alpha*standard_deviation(cosine_similarities)  #
#-----------------------------------------------------------------------------#
def calculaThresholdSimilaridadeCosseno (matrizSimilaridadeCosseno):

	alpha = 0.75

	threshold = np.mean(matrizSimilaridadeCosseno) + alpha * np.std(matrizSimilaridadeCosseno)

	return threshold

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def agrupaComentarios (comentarios, matrizSimilaridadeCosseno, threshold):

	# comentariosAgrupados possui a linha e coluna dos comentarios que possuem simlaridade >= threshold
	comentariosAgrupados = []
	linhaColuna = []

	for i in range(len(matrizSimilaridadeCosseno)):		
		j = i + 1
		while (j < (len(matrizSimilaridadeCosseno))):
			if (matrizSimilaridadeCosseno[i][j] >= threshold):
				linhaColuna.append(i)
				linhaColuna.append(j)
				comentariosAgrupados.append(linhaColuna)
			linhaColuna = []
			j = j + 1

	return comentariosAgrupados

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def salvaMatrizSimilaridadeCosseno (matriz, tamanhoMatriz):

	arquivoGrafoPonderado = open("grafo.txt", 'wr+')
	
	for i in range(tamanhoMatriz):
		for j in range(i+1,tamanhoMatriz):
			arquivoGrafoPonderado.write("%d %d %0.1f\n" % (i,j,matriz[i][j]))
	
	arquivoGrafoPonderado.close()
	
#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def inicializaGrafo ():

	rede = Graph.Read_Ncol('grafo.txt', names=True, weights=True, directed=False)

	return rede

#-----------------------------------------------------------------------------#
# Community_multilevel retorna uma lista de VertexClustering				  #
#-----------------------------------------------------------------------------#
def louvain (rede):

	louvain = rede.community_multilevel(weights=rede.es["weight"], return_levels=False)

	return louvain

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
#def drawingGraph (rede):

#	layout=rede.layout("lgl")
#	plot (rede, "graph.pdf", layout=layout)

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def fazCopiaMatrizSimilaridadeCosseno (matrizSimilaridadeCosseno, copiaMatrizSimilaridadeCosseno):

	for i in range(len(matrizSimilaridadeCosseno)):
		for j in range(len(matrizSimilaridadeCosseno)):
			copiaMatrizSimilaridadeCosseno[i][j] = matrizSimilaridadeCosseno[i][j]

#-----------------------------------------------------------------------------#
# 	    					 												  #
#-----------------------------------------------------------------------------#
def thresholdModularidade (matrizSimilaridadeCosseno, tamanhoComentarios):

	arquivoResultadosModularidadeVsThreshold = open("modularidadeVsThreshold", 'w')

	modularidade = 0

	copiaMatrizSimilaridadeCosseno = []
	copiaMatrizSimilaridadeCosseno = inicializaMatriz (matrizSimilaridadeCosseno)
	fazCopiaMatrizSimilaridadeCosseno(matrizSimilaridadeCosseno, copiaMatrizSimilaridadeCosseno)

	threshold = 0.0	# nao eliminando nada

	while (threshold <= 1.0):
		for i in range(len(matrizSimilaridadeCosseno)):
			for j in range(len(matrizSimilaridadeCosseno)):
				if (matrizSimilaridadeCosseno[i][j] < threshold):
					copiaMatrizSimilaridadeCosseno[i][j] = 0

		salvaMatrizSimilaridadeCosseno (copiaMatrizSimilaridadeCosseno, tamanhoComentarios)
		rede = inicializaGrafo ()
		resultLouvain = louvain(rede)

		arquivoResultadosModularidadeVsThreshold.write("%0.1f %f\n" % (threshold, resultLouvain.modularity))

		if (resultLouvain.modularity > modularidade):
			thresholdIdeal = threshold
			modularidade = resultLouvain.modularity

		threshold = threshold + 0.1
		
	arquivoResultadosModularidadeVsThreshold.close()

	return thresholdIdeal

#-----------------------------------------------------------------------------#
# Já tenho o threshold ideal para deixar a matriz mais esparsa calculado pela #
# funcao thresholdModularidade												  #
#-----------------------------------------------------------------------------#
def aumentaEsparcidadeMatriz (matrizSimilaridadeCosseno, threshold):

	for i in range(len(matrizSimilaridadeCosseno)):
		for j in range(len(matrizSimilaridadeCosseno)):
			if (matrizSimilaridadeCosseno[i][j] < threshold):
				matrizSimilaridadeCosseno[i][j] = 0
			if (matrizSimilaridadeCosseno[i][j] >= threshold):
				matrizSimilaridadeCosseno[i][j] = 1

#-----------------------------------------------------------------------------#
# evcent: Calculates the eigenvector centralities of the vertices in a graph. #	    					 				
#-----------------------------------------------------------------------------#
def centralidade_autovetor (rede):

	centrality_eigenvector = rede.evcent(directed=False, scale=True, weights=rede.es["weight"], return_eigenvalue=False)
	
	return centrality_eigenvector


#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def rankingIntraComunidade (centrality_eigenvector, resultLouvain):

	ranking = []
	vetorIntermerdiario = []
	vetor = []

	for i in range(len(resultLouvain)):			# percorre cada comunidade
		for j in range(len(resultLouvain[i])):	# percorre cada elemento da comunidade
			vetor.append(resultLouvain[i][j])	# id do comentario
			vetor.append(centrality_eigenvector[resultLouvain[i][j]])	# autovetor de centralidade
			vetorIntermerdiario.append(vetor)
			vetor = []
 		ranking.append(sorted(vetorIntermerdiario, key=operator.itemgetter(1), reverse=True))# ordena pelo autovetor em ordem descrescente
 		vetorIntermerdiario = []

 	return ranking

#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def calculaMediaSimilaridadeTituloDescricao (matrizSimilaridadeCosseno, vetorSimilaridadeCossenoTitulo):

	mediaDescricaoTitulo = []
	vetorParaMedia = []
	vetorIntermerdiario = []

	for i in range(len(matrizSimilaridadeCosseno)):
		vetorIntermerdiario.append(matrizSimilaridadeCosseno[0][i])
		vetorIntermerdiario.append(vetorSimilaridadeCossenoTitulo[i])
		vetorParaMedia.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	for i in range(len(matrizSimilaridadeCosseno)):
		mediaDescricaoTitulo.append(np.mean(vetorParaMedia[i]))		# contem a media da similaridade do titulo e da descricao

	return mediaDescricaoTitulo

#-----------------------------------------------------------------------------#
# 																			  #
#-----------------------------------------------------------------------------#
def clusterImportante (mediaDescricaoTitulo, resultLouvain):

	similaridadeElementosCluster = []
	vetorIntermerdiario = []
	mediaSimilaridadesPorCluster = []

	# Vetor similaridadeCluster possui a media da similaridade do titulo e descricao dos comentarios daquele cluster
	for i in range(len(resultLouvain)):			# percorre cada comunidade
		for j in range(len(resultLouvain[i])):	# percorre cada elemento da comunidade
			vetorIntermerdiario.append(mediaDescricaoTitulo[resultLouvain[i][j]])
		similaridadeElementosCluster.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	for i in range(len(similaridadeElementosCluster)):
		vetorIntermerdiario.append(i)
		vetorIntermerdiario.append(np.mean(similaridadeElementosCluster[i]))	
		mediaSimilaridadesPorCluster.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	# ordena pelas similaridades em ordem descrescente
	ranking = sorted(mediaSimilaridadesPorCluster, key=operator.itemgetter(1), reverse=True) 

	return ranking

#-----------------------------------------------------------------------#
# Main																	#
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
	comentariosPreProcessado = removeCaracteresEspeciais(comentariosSemStopWords)

	matrizSimilaridadeCosseno = inicializaMatriz(comentarios)
	vetorSimilaridadeCossenoTitulo = [0 for x in range(len(comentariosPreProcessado))]

	# Calculo TFXIDF para cada token (incluindo descricao)
	for i in range(len(comentariosPreProcessado)):
		j = 0
		while (j < len(comentariosPreProcessado[i])):
			tfxidf(comentariosPreProcessado[i][j], i, j, comentariosPreProcessado, vetorIntermerdiario)
			j = j + 1
		matriztfxidf.append(vetorIntermerdiario)
		vetorIntermerdiario = []

	# Para cada comentario calcula a frequencia (TFXIDF) e a similaridade daquele comentario para todos (incluindo descricao)
	for i in range(len(comentariosPreProcessado)):
		for j in range(i+1,len(comentariosPreProcessado)):
			listaTokensDistintos = getTokensDistintos(comentariosPreProcessado[i], comentariosPreProcessado[j])
			frequenciaComentario1 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[i], listaTokensDistintos, i, matriztfxidf)
			frequenciaComentario2 = calculaFrequenciaSimilaridadeCosseno(comentariosPreProcessado[j], listaTokensDistintos, j, matriztfxidf)
			calculaSimilaridadeCosseno(matrizSimilaridadeCosseno, i, j, frequenciaComentario1, frequenciaComentario2)

	# Calculo TFXIDF para titulo
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
	thresholdIdeal = thresholdModularidade (matrizSimilaridadeCosseno, len(comentariosPreProcessado))
	aumentaEsparcidadeMatriz (matrizSimilaridadeCosseno, thresholdIdeal)
	salvaMatrizSimilaridadeCosseno (matrizSimilaridadeCosseno, len(comentarios))
	rede = inicializaGrafo ()
	resultLouvain = louvain(rede)
	centrality_eigenvector = centralidade_autovetor (rede)
	rankingComunidade = rankingIntraComunidade (centrality_eigenvector, resultLouvain)
	rankingClusters = clusterImportante (mediaDescricaoTitulo, resultLouvain)

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
		print rankingClusters[i], "\n"

	return 0

if __name__ == '__main__':
	main()	
