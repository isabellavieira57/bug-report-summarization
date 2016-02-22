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

import re

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
